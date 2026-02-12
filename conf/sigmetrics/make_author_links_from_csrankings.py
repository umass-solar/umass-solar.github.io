#!/usr/bin/env python3
"""Build an offline author_links.json for the SIGMETRICS dashboard.

- Always includes DBLP link when a PID exists (from sigmetrics.json).
- Optionally enriches with homepage + Google Scholar from CSRankings (only if name matches).
- If no CSRankings entry exists for a name, it is skipped for those extra links.

CSRankings source (fetched once when you run this script):
  https://raw.githubusercontent.com/emeryberger/CSRankings/gh-pages/csrankings-<letter>.csv
"""

import argparse
import csv
import json
import os
import re
import unicodedata
import urllib.request
import time
from typing import Dict, Optional, List

CSRANKINGS_BASE = "https://raw.githubusercontent.com/emeryberger/CSRankings/gh-pages"
CSRANKINGS_FILES = [f"csrankings-{chr(c)}.csv" for c in range(ord("a"), ord("z")+1)]

DEFAULT_SIGMETRICS_JSON = "data/sigmetrics.json"
DEFAULT_OUT = "data/author_links.json"


def _strip_accents(s: str) -> str:
    return "".join(ch for ch in unicodedata.normalize("NFKD", s) if not unicodedata.combining(ch))


def norm_name(s: str) -> str:
    if not s:
        return ""
    s = _strip_accents(s)
    s = s.casefold().strip()
    # drop dblp disambiguation suffix like ' 0001'
    s = re.sub(r"\s+\d{4}$", "", s)
    # remove punctuation
    s = re.sub(r"[^\w\s]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def read_json(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def fetch_text(url: str, timeout: int = 30) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "sigmetrics-dashboard/author-links (offline builder)"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="replace")


def load_csrankings_map(timeout: int = 30) -> Dict[str, Dict[str, str]]:
    out: Dict[str, Dict[str, str]] = {}
    for fn in CSRANKINGS_FILES:
        url = f"{CSRANKINGS_BASE}/{fn}"
        try:
            txt = fetch_text(url, timeout=timeout)
        except Exception:
            continue

        reader = csv.DictReader(txt.splitlines())
        for row in reader:
            name = (row.get("name") or "").strip()
            if not name:
                continue
            key = norm_name(name)
            if not key:
                continue

            homepage = (row.get("homepage") or "").strip()
            scholarid = (row.get("scholarid") or "").strip()

            if key not in out:
                out[key] = {"name": name, "homepage": homepage, "scholarid": scholarid}
            else:
                if not out[key].get("homepage") and homepage:
                    out[key]["homepage"] = homepage
                if (out[key].get("scholarid") in ("", "NOSCHOLARPAGE")) and scholarid:
                    out[key]["scholarid"] = scholarid
    return out


def dblp_url_from_pid(pid: Optional[str]) -> Optional[str]:
    if not pid:
        return None
    return f"https://dblp.org/pid/{pid}.html"


def scholar_url_from_id(scholarid: str) -> Optional[str]:
    if not scholarid or scholarid.strip().upper() == "NOSCHOLARPAGE":
        return None
    sid = scholarid.strip()
    return f"https://scholar.google.com/citations?user={sid}&hl=en"


def choose_best_csr_entry(csr_map: Dict[str, Dict[str, str]], names_to_try: List[str]) -> Optional[Dict[str, str]]:
    for nm in names_to_try:
        key = norm_name(nm)
        if key and key in csr_map:
            return csr_map[key]
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sigmetrics", default=DEFAULT_SIGMETRICS_JSON, help="Path to sigmetrics.json (default: data/sigmetrics.json)")
    ap.add_argument("--out", default=DEFAULT_OUT, help="Output path (default: data/author_links.json)")
    ap.add_argument("--timeout", type=int, default=30, help="HTTP timeout seconds (default: 30)")
    args = ap.parse_args()

    data = read_json(args.sigmetrics)
    author_meta = data.get("authorMeta") or {}

    print("Loading CSRankings name map (one-time fetch)…")
    csr_map = load_csrankings_map(timeout=args.timeout)
    print(f"CSRankings entries loaded: {len(csr_map)}")

    byPid: Dict[str, Dict[str, str]] = {}
    byName: Dict[str, Dict[str, str]] = {}

    matched = 0
    with_pid = 0

    for aid, meta in author_meta.items():
        pid = meta.get("pid")
        canonical = meta.get("canonicalName") or meta.get("name") or ""
        aliases = meta.get("aliases") or []

        links: Dict[str, str] = {}

        dblp = dblp_url_from_pid(pid)
        if dblp:
            links["dblp"] = dblp
            with_pid += 1

        csr = choose_best_csr_entry(csr_map, [canonical] + aliases)
        if csr:
            homepage = (csr.get("homepage") or "").strip()
            scholar = scholar_url_from_id(csr.get("scholarid") or "")
            if homepage:
                links["homepage"] = homepage
            if scholar:
                links["googleScholar"] = scholar
            if ("homepage" in links) or ("googleScholar" in links):
                matched += 1

        if links:
            if pid:
                byPid[pid] = links
            elif canonical:
                byName[canonical] = links

    out = {
        "generatedAt": int(time.time() * 1000),
        "source": "CSRankings gh-pages/csrankings-*.csv (name→homepage+scholarid) + dblp pid from sigmetrics.json",
        "stats": {
            "sigmetricsAuthors": len(author_meta),
            "authorsWithPid": with_pid,
            "authorsMatchedInCSRankings": matched,
            "csrankingsEntries": len(csr_map),
        },
        "byPid": byPid,
        "byName": byName,
    }

    out_path = args.out
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print(f"Wrote {os.path.abspath(out_path)}")
    print(f"byPid entries: {len(byPid)}")
    print(f"byName entries: {len(byName)}")


if __name__ == "__main__":
    main()
