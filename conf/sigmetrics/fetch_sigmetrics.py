#!/usr/bin/env python3
"""
fetch_sigmetrics.py

Downloads SIGMETRICS TOC records from dblp Search API and writes a local JSON dataset.

Key behaviors (per your requirements):
- Tries multiple dblp TOC keys per year (2-digit and 4-digit year formats).
- Retries with exponential backoff on HTTP 429 (Too Many Requests) + transient network errors.
- Excludes "Editorship" and other clearly non-conference entries (keeps Conference/Workshop; permissive if type is missing).
- Poster filtering by page length:
    * For years 1974–2016: exclude entries with < 5 pages (based on numeric page ranges like "369-370").
    * For 2017+: no page-length filtering.

Output: data/sigmetrics.json by default
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


MAX_HITS_PER_TOC = 1000
DEFAULT_START_YEAR = 1974


def build_api_url_for_toc(bht_key: str) -> str:
    q = f"toc:{bht_key}:"
    params = {
        "format": "json",
        "h": str(MAX_HITS_PER_TOC),
        "q": q,
    }
    return "https://dblp.org/search/publ/api?" + urllib.parse.urlencode(params)


def candidate_bht_keys(year: int):
    """
    dblp SIGMETRICS TOC keys vary across years:
      - often 2-digit suffix: sigmetrics96, sigmetrics14, sigmetrics00, sigmetrics74
      - sometimes 4-digit suffix: sigmetrics2014
    We try both (4-digit first tends to work for many modern years; 2-digit is critical for older years).
    """
    yy = f"{year % 100:02d}"
    return [
        f"db/conf/sigmetrics/sigmetrics{year}.bht",  # 4-digit
        f"db/conf/sigmetrics/sigmetrics{yy}.bht",    # 2-digit
    ]


def fetch_json_with_retries(url: str, timeout: int, retries: int, base_delay: float, jitter: float = 0.25):
    """
    Fetch JSON with retry/backoff handling for rate limits (HTTP 429) and transient errors.
    """
    headers = {
        "User-Agent": "sigmetrics-dashboard/1.4 (offline builder; polite crawler)",
        "Accept": "application/json",
    }

    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                data = resp.read()
            return json.loads(data.decode("utf-8"))

        except HTTPError as e:
            # Rate limit handling
            if e.code == 429:
                retry_after = e.headers.get("Retry-After")
                if retry_after:
                    try:
                        wait_s = float(retry_after)
                    except ValueError:
                        wait_s = base_delay * (2 ** attempt)
                else:
                    wait_s = base_delay * (2 ** attempt)

                # Add jitter so multiple runs don't synchronize
                wait_s = wait_s * (1.0 + random.uniform(-jitter, jitter))
                wait_s = max(1.0, wait_s)

                if attempt < retries:
                    print(f"    429 Too Many Requests → sleeping {wait_s:.1f}s then retrying (attempt {attempt+1}/{retries})")
                    time.sleep(wait_s)
                    continue

            # Non-429 HTTP error, or final attempt
            raise

        except (URLError, TimeoutError) as e:
            # Transient network issues
            wait_s = base_delay * (2 ** attempt)
            wait_s = wait_s * (1.0 + random.uniform(-jitter, jitter))
            wait_s = max(0.5, wait_s)

            if attempt < retries:
                print(f"    Network error → sleeping {wait_s:.1f}s then retrying (attempt {attempt+1}/{retries})")
                time.sleep(wait_s)
                continue
            raise


def extract_hits(data):
    hits = (((data or {}).get("result") or {}).get("hits") or {}).get("hit")
    if not hits:
        return []
    return [hits] if isinstance(hits, dict) else list(hits)


def to_author_obj(x):
    # x can be: string OR dict like {"text": "Name", "@pid": "49/7911"}
    if isinstance(x, str):
        name = x.strip()
        return {"id": "name:" + name, "pid": None, "name": name}

    if isinstance(x, dict):
        name = (x.get("text") or "").strip()
        if not name:
            name = str(x).strip()
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
    if isinstance(a, list):
        out = [to_author_obj(z) for z in a]
    else:
        out = [to_author_obj(a)]
    return [z for z in out if z.get("name")]


def choose_canonical_name(alias_counts: Counter):
    # highest count; tie -> shortest
    if not alias_counts:
        return None
    items = list(alias_counts.items())
    items.sort(key=lambda kv: (-kv[1], len(kv[0])))
    return items[0][0]


def is_conference_like(info_type: str) -> bool:
    """
    dblp Search API 'type' looks like:
      - "Conference and Workshop Papers"
      - "Editorship"
      - sometimes missing in older entries
    We drop editorship and clearly non-conference types.
    """
    if not info_type:
        # If missing, be permissive (older records sometimes omit it)
        return True

    t = info_type.strip().lower()

    # hard exclude
    if "editorship" in t:
        return False

    # keep if it looks like conference/workshop papers
    if "conference" in t or "workshop" in t:
        return True

    # otherwise, exclude things that are clearly not conference papers
    if "journal" in t or "book" in t or "thesis" in t:
        return False

    # default: keep (SIGMETRICS TOC is usually conference-like)
    return True


def parse_page_count(pages: str):
    """
    Attempts to parse numeric page ranges like:
      - "83-94"  -> 12 pages
      - "369-370" -> 2 pages

    Returns:
      int page_count if confidently parsed,
      None if unknown/unparseable.
    """
    if not pages:
        return None

    s = pages.strip()

    # dblp sometimes uses commas or multiple ranges; we take the first numeric range
    # Examples: "83-94" or "83-94, 107-118" (rare in TOC, but safe)
    first = s.split(",")[0].strip()

    if "-" not in first:
        return None

    a, b = first.split("-", 1)
    a = a.strip()
    b = b.strip()

    # Strictly numeric only; ignore "e1-e12" etc.
    if not a.isdigit() or not b.isdigit():
        return None

    start = int(a)
    end = int(b)
    if start <= 0 or end <= 0:
        return None

    # Handle inverted ranges defensively
    lo = min(start, end)
    hi = max(start, end)
    return (hi - lo + 1)


def keep_by_page_rule(year: int, pages: str, page_filter_end_year: int, min_pages_pre: int) -> bool:
    """
    For years <= page_filter_end_year (default 2016): drop if page_count is known and < min_pages_pre.
    For years >  page_filter_end_year: keep always (no page-length filtering).
    If page_count cannot be parsed: keep (avoid false drops).
    """
    if year > page_filter_end_year:
        return True

    pc = parse_page_count(pages)
    if pc is None:
        return True
    return pc >= min_pages_pre


def main():
    ap = argparse.ArgumentParser(description="Download SIGMETRICS dblp TOC records and build data/sigmetrics.json")
    ap.add_argument("--start", type=int, default=DEFAULT_START_YEAR, help="Start year (default: 1974)")
    ap.add_argument("--end", type=int, default=time.localtime().tm_year, help="End year (default: current year)")
    ap.add_argument("--delay", type=float, default=0.6, help="Delay between years in seconds (default: 0.6)")
    ap.add_argument("--timeout", type=int, default=30, help="HTTP timeout seconds (default: 30)")
    ap.add_argument("--retries", type=int, default=6, help="Retries on 429/transient errors (default: 6)")
    ap.add_argument("--out", type=str, default="data/sigmetrics.json", help="Output JSON path (default: data/sigmetrics.json)")

    # Filtering controls
    ap.add_argument("--min-pages-pre2017", type=int, default=5,
                    help="For years up to --page-filter-end-year, exclude entries with fewer pages than this (default: 5)")
    ap.add_argument("--page-filter-end-year", type=int, default=2016,
                    help="Last year to apply page-length filtering (default: 2016). 2017+ keeps all page lengths.")
    ap.add_argument("--keep-nonconf", action="store_true",
                    help="If set, keep non-conference-like entries too (still drops editorship). Default: drop non-conference-like.")
    args = ap.parse_args()

    start_year = args.start
    end_year = args.end
    delay_s = max(0.0, args.delay)

    records = []
    author_meta_agg = {}  # id -> {"pid":..., "alias_counts": Counter()}

    print(f"Downloading SIGMETRICS TOC records from {start_year}..{end_year}")
    print(f"Using delay={delay_s:.2f}s, retries={args.retries}")
    print(f"Page filter: years<= {args.page_filter_end_year} drop if pages < {args.min_pages_pre2017}; years> {args.page_filter_end_year} no filter")
    print(f"Type filter: drop editorship; {'keep non-conf' if args.keep_nonconf else 'keep conf/workshop (or missing type) only'}")

    total_years_no_hits = 0
    total_skipped_type = 0
    total_skipped_pages = 0

    for year in range(start_year, end_year + 1):
        print(f"  {year}: ", end="", flush=True)

        year_hits = []
        used_bht = None

        # Try multiple bht formats
        for bht_key in candidate_bht_keys(year):
            url = build_api_url_for_toc(bht_key)
            try:
                data = fetch_json_with_retries(
                    url=url,
                    timeout=args.timeout,
                    retries=args.retries,
                    base_delay=max(1.0, delay_s if delay_s > 0 else 1.0),
                )
            except Exception:
                continue

            hits = extract_hits(data)
            if hits:
                year_hits = hits
                used_bht = bht_key
                break

        if not year_hits:
            total_years_no_hits += 1
            print("0 records (no TOC key matched)")
            if delay_s:
                time.sleep(delay_s)
            continue

        kept_this_year = 0
        skipped_type_this_year = 0
        skipped_pages_this_year = 0

        # We print a single line per year to keep logs readable
        print(f"{len(year_hits)} records (bht={used_bht})")

        for h in year_hits:
            info = (h or {}).get("info") or {}
            title = (info.get("title") or "").strip()
            if not title:
                continue

            info_type = (info.get("type") or "").strip()
            if "editorship" in (info_type or "").lower():
                skipped_type_this_year += 1
                total_skipped_type += 1
                continue

            if (not args.keep_nonconf) and (not is_conference_like(info_type)):
                skipped_type_this_year += 1
                total_skipped_type += 1
                continue

            y = int(info.get("year") or year)
            pages = (info.get("pages") or "").strip()
            if not keep_by_page_rule(
                year=y,
                pages=pages,
                page_filter_end_year=args.page_filter_end_year,
                min_pages_pre=args.min_pages_pre2017,
            ):
                skipped_pages_this_year += 1
                total_skipped_pages += 1
                continue

            authors = normalize_authors(info.get("authors") or {})
            for a in authors:
                aid = a["id"]
                if aid not in author_meta_agg:
                    author_meta_agg[aid] = {"pid": a.get("pid"), "alias_counts": Counter()}
                m = author_meta_agg[aid]
                if (not m["pid"]) and a.get("pid"):
                    m["pid"] = a.get("pid")
                nm = (a.get("name") or "").strip()
                if nm:
                    m["alias_counts"][nm] += 1

            author_ids = [a["id"] for a in authors]

            records.append({
                "year": y,
                "title": title,
                "authors": authors,       # [{id,pid,name}, ...]
                "authorIds": author_ids,  # [id,...]
                "venue": info.get("venue") or "",
                "pages": pages,
                "doi": info.get("doi") or "",
                "url": info.get("url") or "",
                "key": info.get("key") or "",
                "type": info_type
            })
            kept_this_year += 1

        if skipped_type_this_year or skipped_pages_this_year:
            bits = []
            if skipped_type_this_year:
                bits.append(f"skipped_type={skipped_type_this_year}")
            if skipped_pages_this_year:
                bits.append(f"skipped_pages={skipped_pages_this_year}")
            if bits:
                print(f"      kept={kept_this_year} ({', '.join(bits)})")

        if delay_s:
            time.sleep(delay_s)

    # Finalize authorMeta
    author_meta = {}
    for aid, m in author_meta_agg.items():
        canonical = choose_canonical_name(m["alias_counts"]) or aid
        aliases = sorted(m["alias_counts"].keys(), key=lambda s: s.lower())
        author_meta[aid] = {
            "id": aid,
            "pid": m["pid"],
            "name": canonical,
            "canonicalName": canonical,
            "aliases": aliases
        }

    # Aggregate per-author metrics (based on kept records only)
    stats = {}

    def get_stats(aid):
        if aid not in stats:
            stats[aid] = {
                "id": aid,
                "pubs": 0,
                "firstAuth": 0,
                "lastAuth": 0,
                "solo": 0,
                "years": defaultdict(int),
                "coauthors": defaultdict(int),
                "teamSizes": []
            }
        return stats[aid]

    for r in records:
        team = len(r["authorIds"])
        for i, aid in enumerate(r["authorIds"]):
            s = get_stats(aid)
            s["pubs"] += 1
            s["years"][r["year"]] += 1
            s["teamSizes"].append(team)
            if team == 1:
                s["solo"] += 1
            if i == 0:
                s["firstAuth"] += 1
            if i == team - 1:
                s["lastAuth"] += 1
            for j, bid in enumerate(r["authorIds"]):
                if j == i:
                    continue
                s["coauthors"][bid] += 1

    authors = []
    for aid, s in stats.items():
        years_active = sorted(s["years"].keys())
        first_year = years_active[0] if years_active else None
        last_year = years_active[-1] if years_active else None
        avg_team = (sum(s["teamSizes"]) / len(s["teamSizes"])) if s["teamSizes"] else 0.0

        meta = author_meta.get(aid) or {}
        authors.append({
            "id": aid,
            "pid": meta.get("pid"),
            "name": meta.get("canonicalName") or meta.get("name") or aid,
            "aliases": meta.get("aliases") or [],
            "pubs": s["pubs"],
            "firstAuth": s["firstAuth"],
            "lastAuth": s["lastAuth"],
            "solo": s["solo"],
            "coauthors": len(s["coauthors"]),
            "avgTeam": avg_team,
            "activeYears": len(years_active),
            "firstYear": first_year,
            "lastYear": last_year
        })

    out = {
        "fetchedAt": int(time.time() * 1000),
        "startYear": start_year,
        "endYear": end_year,
        "records": records,
        "authorMeta": author_meta,
        "authors": authors,
        "notes": {
            "maxHitsPerToc": MAX_HITS_PER_TOC,
            "pageFilterEndYear": args.page_filter_end_year,
            "minPagesPre2017": args.min_pages_pre2017,
            "skippedNonConfOrEditorship": total_skipped_type,
            "skippedByPageLength": total_skipped_pages,
            "yearsWithNoHits": total_years_no_hits,
        }
    }

    out_path = args.out
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False)

    print(f"\nWrote {out_path} ({len(records)} records, {len(authors)} authors)")
    if total_skipped_pages:
        print(f"Skipped short entries by page rule: {total_skipped_pages}")
    if total_skipped_type:
        print(f"Skipped non-conference/editorship entries: {total_skipped_type}")
    if total_years_no_hits:
        print(f"Years with no hits (no TOC key matched): {total_years_no_hits}")


if __name__ == "__main__":
    main()
