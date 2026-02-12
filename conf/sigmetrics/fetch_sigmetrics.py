#!/usr/bin/env python3
import argparse
import json
import os
import random
import re
import time
import urllib.parse
import urllib.request
from collections import defaultdict, Counter
from urllib.error import HTTPError, URLError

MAX_HITS_PER_TOC = 1000
DEFAULT_START_YEAR = 1974

# Poster/full-paper heuristic defaults
DEFAULT_POSTER_FILTER_UNTIL = 2017  # apply filter for years <= this
DEFAULT_MIN_FULL_PAGES = 5          # drop items with < this many pages (inclusive count)


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
    dblp SIGMETRICS TOC keys vary:
      - many years use 2-digit suffix: sigmetrics96, sigmetrics14, sigmetrics00
      - some tooling/pages may use 4-digit: sigmetrics2014
    We try both.
    """
    yy = f"{year % 100:02d}"
    return [
        # Prefer the 2-digit key first (covers many older years like sigmetrics74)
        f"db/conf/sigmetrics/sigmetrics{yy}.bht",
        f"db/conf/sigmetrics/sigmetrics{year}.bht",
    ]


def fetch_json_with_retries(url: str, timeout: int, retries: int, base_delay: float, jitter: float = 0.25):
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
            if e.code == 429:
                retry_after = e.headers.get("Retry-After")
                if retry_after:
                    try:
                        wait_s = float(retry_after)
                    except ValueError:
                        wait_s = base_delay * (2 ** attempt)
                else:
                    wait_s = base_delay * (2 ** attempt)

                wait_s = wait_s * (1.0 + random.uniform(-jitter, jitter))
                wait_s = max(1.0, wait_s)

                if attempt < retries:
                    print(
                        f"    429 Too Many Requests → sleeping {wait_s:.1f}s then retrying "
                        f"(attempt {attempt+1}/{retries})"
                    )
                    time.sleep(wait_s)
                    continue
            raise

        except (URLError, TimeoutError) as e:
            wait_s = base_delay * (2 ** attempt)
            wait_s = wait_s * (1.0 + random.uniform(-jitter, jitter))
            wait_s = max(0.5, wait_s)

            if attempt < retries:
                print(f"    Network error → sleeping {wait_s:.1f}s then retrying (attempt {attempt+1}/{retries})")
                time.sleep(wait_s)
                continue
            raise


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
    if not alias_counts:
        return None
    items = list(alias_counts.items())
    items.sort(key=lambda kv: (-kv[1], len(kv[0])))
    return items[0][0]


def is_conference_like(info_type: str) -> bool:
    """
    The dblp Search API does NOT use 'c'/'e' letters.
    It uses strings like:
      - "Conference and Workshop Papers"
      - "Editorship"
    We keep conference/workshop papers, and drop editorship.
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

    # otherwise, conservative: exclude things that are clearly not papers
    if "journal" in t or "book" in t or "thesis" in t:
        return False

    # default: keep
    return True


def extract_hits(data):
    hits = (((data or {}).get("result") or {}).get("hits") or {}).get("hit")
    if not hits:
        return []
    return [hits] if isinstance(hits, dict) else list(hits)


def page_count(pages: str):
    """
    Return inclusive page count, or None if unknown/unparseable.

    Common dblp 'pages' formats:
      - "83-94" -> 12
      - "369-370" -> 2
      - "1:83-1:94" -> 12 (we take last two numbers)
      - "83" -> 1
    """
    if not pages:
        return None
    s = str(pages).strip()
    if not s:
        return None

    nums = [int(x) for x in re.findall(r"\d+", s)]
    if not nums:
        return None
    if len(nums) == 1:
        return 1

    start, end = nums[-2], nums[-1]
    if end < start:
        return None
    return (end - start) + 1


def main():
    ap = argparse.ArgumentParser(description="Download SIGMETRICS dblp TOC records and build data/sigmetrics.json")
    ap.add_argument("--start", type=int, default=DEFAULT_START_YEAR, help="Start year (default: 1974)")
    ap.add_argument("--end", type=int, default=time.localtime().tm_year, help="End year (default: current year)")
    ap.add_argument("--delay", type=float, default=0.6, help="Delay between years in seconds (default: 0.6)")
    ap.add_argument("--timeout", type=int, default=30, help="HTTP timeout seconds (default: 30)")
    ap.add_argument("--retries", type=int, default=6, help="Retries on 429/transient errors (default: 6)")
    ap.add_argument("--out", type=str, default="data/sigmetrics.json", help="Output JSON path (default: data/sigmetrics.json)")
    ap.add_argument("--conf-only", action="store_true", help="Only keep conference/workshop papers; drop editorship (recommended)")

    # Poster filter options
    ap.add_argument(
        "--no-poster-filter",
        action="store_true",
        help="Disable poster filtering by pages (default is enabled for years <= 2017)",
    )
    ap.add_argument(
        "--poster-filter-until",
        type=int,
        default=DEFAULT_POSTER_FILTER_UNTIL,
        help=f"Apply poster filter for years <= this year (default: {DEFAULT_POSTER_FILTER_UNTIL})",
    )
    ap.add_argument(
        "--min-full-pages",
        type=int,
        default=DEFAULT_MIN_FULL_PAGES,
        help=f"Minimum pages to keep for years covered by poster filter (default: {DEFAULT_MIN_FULL_PAGES})",
    )

    args = ap.parse_args()

    start_year = args.start
    end_year = args.end
    delay_s = max(0.0, args.delay)

    use_poster_filter = not args.no_poster_filter
    poster_filter_until = args.poster_filter_until
    min_full_pages = max(1, int(args.min_full_pages))

    records = []
    author_meta_agg = {}  # id -> {"pid":..., "alias_counts": Counter()}

    print(f"Downloading SIGMETRICS TOC records from {start_year}..{end_year}")
    print(
        f"Using delay={delay_s:.2f}s, retries={args.retries}, conf_only={bool(args.conf_only)}, "
        f"poster_filter={'on' if use_poster_filter else 'off'} "
        f"(<= {poster_filter_until}, min_pages={min_full_pages})"
    )

    total_skipped_type = 0
    total_years_no_hits = 0
    total_skipped_posters = 0

    for year in range(start_year, end_year + 1):
        print(f"  {year}: ", end="", flush=True)

        year_hit_list = []
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
                # Try next candidate bht_key
                continue

            hits = extract_hits(data)
            if hits:
                year_hit_list = hits
                used_bht = bht_key
                break

        if not year_hit_list:
            total_years_no_hits += 1
            print("0 records (no TOC key matched)")
            if delay_s:
                time.sleep(delay_s)
            continue

        print(f"{len(year_hit_list)} records (bht={used_bht})")

        kept_this_year = 0
        skipped_non_conf_this_year = 0
        skipped_posters_this_year = 0

        for h in year_hit_list:
            info = (h or {}).get("info") or {}
            title = (info.get("title") or "").strip()
            if not title:
                continue

            info_type = (info.get("type") or "").strip()
            if args.conf_only and (not is_conference_like(info_type)):
                skipped_non_conf_this_year += 1
                total_skipped_type += 1
                continue

            y = int(info.get("year") or year)
            pages_str = (info.get("pages") or "").strip()

            # ✅ Poster filter: only apply up to poster_filter_until (default: 2017)
            if use_poster_filter and y <= poster_filter_until:
                pc = page_count(pages_str)
                if pc is not None and pc < min_full_pages:
                    skipped_posters_this_year += 1
                    total_skipped_posters += 1
                    continue

            authors = normalize_authors(info.get("authors") or {})
            for a in authors:
                aid = a["id"]
                if aid not in author_meta_agg:
                    author_meta_agg[aid] = {"pid": a.get("pid"), "alias_counts": Counter()}
                m = author_meta_agg[aid]
                if not m["pid"] and a.get("pid"):
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
                "pages": pages_str,
                "doi": info.get("doi") or "",
                "url": info.get("url") or "",
                "key": info.get("key") or "",
                "type": info_type
            })
            kept_this_year += 1

        if args.conf_only or (use_poster_filter and skipped_posters_this_year):
            suffix = []
            if args.conf_only and skipped_non_conf_this_year:
                suffix.append(f"skipped_non_conf={skipped_non_conf_this_year}")
            if use_poster_filter and skipped_posters_this_year:
                suffix.append(f"skipped_short_pages={skipped_posters_this_year}")
            if suffix:
                print(f"      kept={kept_this_year}, " + ", ".join(suffix))

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

    # Aggregate per-author metrics
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
        "confOnly": bool(args.conf_only),
        "posterFilter": {
            "enabled": bool(use_poster_filter),
            "untilYear": int(poster_filter_until),
            "minFullPages": int(min_full_pages),
        },
        "records": records,
        "authorMeta": author_meta,
        "authors": authors,
        "notes": {
            "skippedNonConf": total_skipped_type,
            "skippedShortPages": total_skipped_posters,
            "yearsWithNoHits": total_years_no_hits,
            "maxHitsPerToc": MAX_HITS_PER_TOC
        }
    }

    out_path = args.out
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False)

    print(f"\nWrote {out_path} ({len(records)} records, {len(authors)} authors)")
    if args.conf_only:
        print(f"Skipped non-conference-like entries: {total_skipped_type}")
    if use_poster_filter:
        print(f"Skipped short-page (poster-like) entries (<= {poster_filter_until}, < {min_full_pages} pages): {total_skipped_posters}")
    if total_years_no_hits:
        print(f"Years with no hits (no TOC key matched): {total_years_no_hits}")


if __name__ == "__main__":
    main()
