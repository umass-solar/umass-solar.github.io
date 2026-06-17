#!/usr/bin/env python3
"""
fetch_sigmetrics.py

Downloads SIGMETRICS records from the dblp Search API and writes data/sigmetrics.json.

WHY THIS VERSION:
  The previous per-year approach issued ~2 requests per year across 50+ years. dblp
  rate-limits per IP, so it tripped HTTP 429 and — because a 429 after retries was
  swallowed as "no TOC key matched" — whole years silently came back empty.

  This version fetches the entire venue as ONE paginated "stream" query (the same
  "export records of this stream" feed dblp links from the SIGMETRICS page), so the
  whole 1974..present history arrives in ~4-5 requests instead of ~100. That avoids
  the rate limit. All of your filtering rules are unchanged:

    - exclude "Editorship" and clearly non-conference entries (permissive if type missing)
    - posters by page length: years 1974-2016 drop entries < 5 pages; 2017+ keep all
    - identity merged by dblp pid (id = "pid:<pid>" or "name:<name>")

  Output schema is identical to before (records / authorMeta / authors / notes), so the
  website and make_author_links_from_csrankings.py keep working unchanged.

  If you prefer the old per-year crawl, use:  --method toc   (now with proper 429 waits).
"""

import argparse
import json
import os
import random
import time
import urllib.parse
import urllib.request
from collections import defaultdict, Counter
from urllib.error import HTTPError, URLError

API = "https://dblp.org/search/publ/api"
STREAM = "stream:streams/conf/sigmetrics:"   # the official SIGMETRICS stream feed
PAGE_SIZE = 1000                              # dblp max hits per request
DEFAULT_START_YEAR = 1974
UA = "sigmetrics-dashboard/2.0 (offline builder; polite paginated fetch)"
MAX_RETRY_AFTER = 600                         # cap a single forced wait at 10 min


# ----------------------------------------------------------------------------- HTTP
def fetch_json_with_retries(url, timeout, retries, base_delay, jitter=0.25):
    """GET JSON, honouring Retry-After and backing off on 429 / transient errors.
    Raises on final failure (callers must NOT silently swallow that)."""
    headers = {"User-Agent": UA, "Accept": "application/json"}
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except HTTPError as e:
            if e.code in (429, 500, 502, 503) and attempt < retries:
                retry_after = e.headers.get("Retry-After") if e.headers else None
                if retry_after and str(retry_after).strip().isdigit():
                    wait_s = min(float(retry_after), MAX_RETRY_AFTER)
                else:
                    wait_s = base_delay * (2 ** attempt)
                wait_s = max(1.0, wait_s * (1.0 + random.uniform(-jitter, jitter)))
                print(f"    HTTP {e.code} -> waiting {wait_s:.1f}s, retry {attempt+1}/{retries}", flush=True)
                time.sleep(wait_s)
                continue
            raise
        except (URLError, TimeoutError) as e:
            if attempt < retries:
                wait_s = max(0.5, base_delay * (2 ** attempt) * (1.0 + random.uniform(-jitter, jitter)))
                print(f"    network error ({e}) -> waiting {wait_s:.1f}s, retry {attempt+1}/{retries}", flush=True)
                time.sleep(wait_s)
                continue
            raise


def hits_block(data):
    return (((data or {}).get("result") or {}).get("hits") or {})


def extract_hits(data):
    h = hits_block(data).get("hit")
    if not h:
        return []
    return [h] if isinstance(h, dict) else list(h)


# ------------------------------------------------------------------------- parsing
def to_author_obj(x):
    if isinstance(x, str):
        name = x.strip()
        return {"id": "name:" + name, "pid": None, "name": name}
    if isinstance(x, dict):
        name = (x.get("text") or "").strip() or str(x).strip()
        pid = (x.get("@pid") or x.get("pid") or "").strip() or None
        return {"id": ("pid:" + pid) if pid else ("name:" + name), "pid": pid, "name": name}
    name = str(x).strip()
    return {"id": "name:" + name, "pid": None, "name": name}


def normalize_authors(auth_node):
    if not auth_node:
        return []
    a = auth_node.get("author")
    if not a:
        return []
    out = [to_author_obj(z) for z in (a if isinstance(a, list) else [a])]
    return [z for z in out if z.get("name")]


def choose_canonical_name(alias_counts):
    if not alias_counts:
        return None
    items = sorted(alias_counts.items(), key=lambda kv: (-kv[1], len(kv[0])))
    return items[0][0]


def is_conference_like(info_type):
    if not info_type:
        return True  # older records sometimes omit type
    t = info_type.strip().lower()
    if "editorship" in t:
        return False
    if "conference" in t or "workshop" in t:
        return True
    if "journal" in t or "book" in t or "thesis" in t or "informal" in t:
        return False
    return True


def parse_page_count(pages):
    if not pages:
        return None
    first = pages.strip().split(",")[0].strip()
    if "-" not in first:
        return None
    a, b = first.split("-", 1)
    a, b = a.strip(), b.strip()
    if not a.isdigit() or not b.isdigit():
        return None
    lo, hi = sorted((int(a), int(b)))
    if lo <= 0 or hi <= 0:
        return None
    return hi - lo + 1


def keep_by_page_rule(year, pages, page_filter_end_year, min_pages_pre):
    if year > page_filter_end_year:
        return True
    pc = parse_page_count(pages)
    if pc is None:
        return True
    return pc >= min_pages_pre


# ----------------------------------------------------------------- fetch strategies
def fetch_stream(timeout, retries, delay):
    """Page through the whole SIGMETRICS stream. Returns a flat list of dblp 'hit' dicts.

    dblp does NOT always return the requested page size (it often caps a response at ~100
    hits even when h=1000). So we advance the offset by however many hits actually arrived
    (via dblp's @first/@sent counters), and stop only on an empty page or once @total is
    reached — never on 'fewer than requested'."""
    all_hits, first = [], 0
    total = None
    guard = 0
    while True:
        guard += 1
        if guard > 100000:                       # absolute safety against an infinite loop
            print("  ! pagination guard tripped; stopping.")
            break
        params = {"q": STREAM, "format": "json", "h": str(PAGE_SIZE), "f": str(first)}
        url = API + "?" + urllib.parse.urlencode(params)
        data = fetch_json_with_retries(url, timeout, retries, max(1.0, delay))
        hb = hits_block(data)
        if total is None:
            try:
                total = int(hb.get("@total", 0))
            except (TypeError, ValueError):
                total = 0
            print(f"  dblp reports {total} records in the stream.")
        batch = extract_hits(data)
        got = len(batch)
        if got == 0:
            break
        all_hits.extend(batch)
        # advance by what dblp actually sent (it may be < PAGE_SIZE)
        try:
            sent = int(hb.get("@sent", got))
            sent_first = int(hb.get("@first", first))
            next_first = sent_first + (sent if sent > 0 else got)
        except (TypeError, ValueError):
            next_first = first + got
        first = next_first if next_first > first else first + got   # guarantee progress
        print(f"  fetched {len(all_hits)} / {total}", flush=True)
        if total and first >= total:
            break
        time.sleep(delay)
    if total and len(all_hits) < total:
        print(f"  ! retrieved {len(all_hits)} of {total} reported records "
              f"(dblp may cap deep paging for this query). Try --method toc to backfill.")
    return all_hits


def candidate_bht_keys(year):
    yy = f"{year % 100:02d}"
    return [f"db/conf/sigmetrics/sigmetrics{year}.bht",
            f"db/conf/sigmetrics/sigmetrics{yy}.bht"]


def fetch_toc(start, end, timeout, retries, delay):
    """Original per-year crawl, kept as a fallback. Now waits out 429s properly and
    does NOT mask a rate-limit error as an empty year."""
    all_hits = []
    for year in range(start, end + 1):
        print(f"  {year}: ", end="", flush=True)
        year_hits, used = [], None
        for bht in candidate_bht_keys(year):
            params = {"q": f"toc:{bht}:", "format": "json", "h": str(PAGE_SIZE)}
            url = API + "?" + urllib.parse.urlencode(params)
            try:
                data = fetch_json_with_retries(url, timeout, retries, max(1.0, delay))
            except Exception as e:
                print(f"[error: {e}] ", end="")
                continue
            h = extract_hits(data)
            if h:
                year_hits, used = h, bht
                break
            time.sleep(delay)
        print(f"{len(year_hits)} records" + (f" (bht={used})" if used else " (no TOC key matched)"))
        all_hits.extend(year_hits)
        time.sleep(delay)
    return all_hits


# ------------------------------------------------------------------------- assembly
def build_dataset(hits, start_year, end_year, keep_nonconf,
                  page_filter_end_year, min_pages_pre):
    records = []
    author_meta_agg = {}
    seen_keys = set()
    skipped_type = skipped_pages = skipped_year = dupes = 0

    for h in hits:
        info = (h or {}).get("info") or {}
        title = (info.get("title") or "").strip()
        if not title:
            continue

        key = info.get("key") or ""
        if key and key in seen_keys:
            dupes += 1
            continue

        info_type = (info.get("type") or "").strip()
        if "editorship" in info_type.lower():
            skipped_type += 1
            continue
        if (not keep_nonconf) and (not is_conference_like(info_type)):
            skipped_type += 1
            continue

        try:
            y = int(info.get("year"))
        except (TypeError, ValueError):
            continue
        if y < start_year or y > end_year:
            skipped_year += 1
            continue

        pages = (info.get("pages") or "").strip()
        if not keep_by_page_rule(y, pages, page_filter_end_year, min_pages_pre):
            skipped_pages += 1
            continue

        if key:
            seen_keys.add(key)

        authors = normalize_authors(info.get("authors") or {})
        for a in authors:
            aid = a["id"]
            m = author_meta_agg.setdefault(aid, {"pid": a.get("pid"), "alias_counts": Counter()})
            if (not m["pid"]) and a.get("pid"):
                m["pid"] = a.get("pid")
            nm = (a.get("name") or "").strip()
            if nm:
                m["alias_counts"][nm] += 1

        records.append({
            "year": y, "title": title,
            "authors": authors, "authorIds": [a["id"] for a in authors],
            "venue": info.get("venue") or "", "pages": pages,
            "doi": info.get("doi") or "", "url": info.get("ee") or info.get("url") or "",
            "key": key, "type": info_type,
        })

    records.sort(key=lambda r: (r["year"], r["key"]))

    author_meta = {}
    for aid, m in author_meta_agg.items():
        canonical = choose_canonical_name(m["alias_counts"]) or aid
        author_meta[aid] = {"id": aid, "pid": m["pid"], "name": canonical,
                            "canonicalName": canonical,
                            "aliases": sorted(m["alias_counts"].keys(), key=str.lower)}

    stats = {}
    def gs(aid):
        return stats.setdefault(aid, {"pubs": 0, "firstAuth": 0, "lastAuth": 0, "solo": 0,
                                      "years": defaultdict(int), "coauthors": set(), "teamSizes": []})
    for r in records:
        team = len(r["authorIds"])
        for i, aid in enumerate(r["authorIds"]):
            s = gs(aid)
            s["pubs"] += 1
            s["years"][r["year"]] += 1
            s["teamSizes"].append(team)
            if team == 1: s["solo"] += 1
            if i == 0: s["firstAuth"] += 1
            if i == team - 1: s["lastAuth"] += 1
            for j, bid in enumerate(r["authorIds"]):
                if j != i: s["coauthors"].add(bid)

    authors = []
    for aid, s in stats.items():
        ya = sorted(s["years"].keys())
        meta = author_meta.get(aid, {})
        authors.append({
            "id": aid, "pid": meta.get("pid"),
            "name": meta.get("canonicalName") or aid, "aliases": meta.get("aliases") or [],
            "pubs": s["pubs"], "firstAuth": s["firstAuth"], "lastAuth": s["lastAuth"],
            "solo": s["solo"], "coauthors": len(s["coauthors"]),
            "avgTeam": (sum(s["teamSizes"]) / len(s["teamSizes"])) if s["teamSizes"] else 0.0,
            "activeYears": len(ya), "firstYear": ya[0] if ya else None,
            "lastYear": ya[-1] if ya else None,
        })

    notes = {"maxHitsPerToc": PAGE_SIZE, "pageFilterEndYear": page_filter_end_year,
             "minPagesPre2017": min_pages_pre, "skippedNonConfOrEditorship": skipped_type,
             "skippedByPageLength": skipped_pages, "skippedOutOfYearRange": skipped_year,
             "duplicateKeysDropped": dupes}
    return records, author_meta, authors, notes


def main():
    ap = argparse.ArgumentParser(description="Download SIGMETRICS dblp records -> data/sigmetrics.json")
    ap.add_argument("--start", type=int, default=DEFAULT_START_YEAR, help="Start year (default 1974)")
    ap.add_argument("--end", type=int, default=time.localtime().tm_year, help="End year (default current year)")
    ap.add_argument("--method", choices=["stream", "toc"], default="stream",
                    help="stream = one paginated venue query (default, avoids rate limits); "
                         "toc = old per-year crawl")
    ap.add_argument("--delay", type=float, default=2.0, help="Seconds between requests (default 2.0)")
    ap.add_argument("--timeout", type=int, default=60, help="HTTP timeout seconds (default 60)")
    ap.add_argument("--retries", type=int, default=8, help="Retries on 429/transient (default 8)")
    ap.add_argument("--out", default="data/sigmetrics.json", help="Output path")
    ap.add_argument("--min-pages-pre2017", type=int, default=5,
                    help="For years <= --page-filter-end-year, drop entries with fewer pages (default 5)")
    ap.add_argument("--page-filter-end-year", type=int, default=2016,
                    help="Last year to apply page-length filtering (default 2016)")
    ap.add_argument("--keep-nonconf", action="store_true",
                    help="Keep non-conference-like entries too (still drops editorship)")
    args = ap.parse_args()

    print(f"SIGMETRICS fetch: method={args.method}, years {args.start}..{args.end}, "
          f"delay={args.delay}s, retries={args.retries}")
    print(f"Filters: drop editorship{'' if args.keep_nonconf else ' + non-conference'}; "
          f"years <= {args.page_filter_end_year} drop < {args.min_pages_pre2017} pages; 2017+ keep all")

    t0 = time.time()
    try:
        if args.method == "stream":
            hits = fetch_stream(args.timeout, args.retries, args.delay)
        else:
            hits = fetch_toc(args.start, args.end, args.timeout, args.retries, args.delay)
    except Exception as e:
        print(f"\nFETCH FAILED: {e}")
        print("If this is a 429, dblp is rate-limiting your IP. Wait a few minutes and re-run; "
              "the script honours dblp's Retry-After. You can also raise --delay.")
        raise SystemExit(1)

    if not hits:
        print("\nNo records returned. dblp may be rate-limiting (try again later) or the stream "
              "feed changed. You can also try: python3 fetch_sigmetrics.py --method toc")
        raise SystemExit(1)

    records, author_meta, authors, notes = build_dataset(
        hits, args.start, args.end, args.keep_nonconf,
        args.page_filter_end_year, args.min_pages_pre2017)

    out = {"fetchedAt": int(time.time() * 1000), "startYear": args.start, "endYear": args.end,
           "source": "dblp stream:streams/conf/sigmetrics" if args.method == "stream"
                     else "dblp per-year TOC",
           "records": records, "authorMeta": author_meta, "authors": authors, "notes": notes}

    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
    tmp = args.out + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False)
    os.replace(tmp, args.out)  # atomic

    yrs = sorted({r["year"] for r in records})
    print(f"\nWrote {args.out}: {len(records)} records, {len(authors)} authors, "
          f"years {yrs[0] if yrs else '-'}..{yrs[-1] if yrs else '-'} in {time.time()-t0:.1f}s")
    if notes["skippedByPageLength"]:
        print(f"  dropped {notes['skippedByPageLength']} short entries (poster page rule)")
    if notes["skippedNonConfOrEditorship"]:
        print(f"  dropped {notes['skippedNonConfOrEditorship']} editorship/non-conference entries")
    print("Reload the dashboard to see the data.")


if __name__ == "__main__":
    main()
