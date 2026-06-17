#!/usr/bin/env python3
"""
make_pc.py - write data/pc.json: the Technical Program Committee (PC) members of every
ACM SIGMETRICS conference 2010-2026. Static transcribed data (from each year's
sigmetrics.org committee / program_committee page). The website overlays it onto the
author dataset by matching author NAMES (same exact+fuzzy matcher used for awards and
chairs), so it marks PC service in the author dashboard without any DBLP refetch.

Rosters live as one-name-per-line files in pc_raw/yYYYY.txt. Edit those (or this header)
when a year is corrected, then re-run.
"""
import json, os, time, re, unicodedata

# Host city per edition (for the PC page header), consistent with chairs.json.
LOCATION = {
    2010: "New York, New York, USA",
    2011: "San Jose, California, USA",
    2012: "London, United Kingdom",
    2013: "Pittsburgh, Pennsylvania, USA",
    2014: "Austin, Texas, USA",
    2015: "Portland, Oregon, USA",
    2016: "Antibes Juan-les-Pins, France",
    2017: "Urbana-Champaign, Illinois, USA",
    2018: "Irvine, California, USA",
    2019: "Phoenix, Arizona, USA",
    2020: "Boston, Massachusetts, USA",     # held virtually (conference cancelled)
    2021: "Beijing, China",                 # held virtually
    2022: "Mumbai, India",
    2023: "Orlando, Florida, USA",
    2024: "Venice, Italy",
    2025: "Stony Brook, New York, USA",
    2026: "Ann Arbor, Michigan, USA",
}

RAW_DIR = "pc_raw"

def norm_key(name):
    """Normalization key for de-duplication and matching:
    strip accents, lowercase, drop parenthetical nicknames and punctuation."""
    s = unicodedata.normalize("NFKD", name)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"\(.*?\)", " ", s)          # drop "(Kevin)" etc.
    s = s.replace(".", " ").replace("-", " ")
    s = re.sub(r"[^a-zA-Z ]", " ", s)
    s = re.sub(r"\s+", " ", s).strip().lower()
    return s

def clean_display(name):
    """Tidy display form: collapse whitespace, fix ALL-CAPS surnames."""
    name = re.sub(r"\s+", " ", name).strip()
    name = name.replace('"', "")            # drop nickname quotes for display
    name = re.sub(r"\(.*?\)", "", name).strip()
    # Fix names submitted in ALL CAPS (e.g. "PRANAY SHARMA") -> title case,
    # but leave normal mixed-case and single-token initialisms alone.
    parts = name.split(" ")
    fixed = []
    for p in parts:
        if len(p) > 1 and p.isupper() and p.isalpha():
            fixed.append(p.capitalize())
        else:
            fixed.append(p)
    return " ".join(fixed)

def main():
    years = []
    all_keys = set()
    for y in sorted(LOCATION):
        path = os.path.join(RAW_DIR, f"y{y}.txt")
        if not os.path.exists(path):
            print(f"  WARN missing {path}, skipping {y}")
            continue
        seen = set()
        members = []
        with open(path, encoding="utf-8") as f:
            for line in f:
                raw = line.strip()
                if not raw:
                    continue
                disp = clean_display(raw)
                k = norm_key(disp)
                if not k or k in seen:
                    continue
                seen.add(k)
                all_keys.add(k)
                members.append(disp)
        members.sort(key=lambda n: norm_key(n))
        years.append({"year": y, "location": LOCATION[y], "members": members})

    years.sort(key=lambda r: r["year"], reverse=True)   # newest first

    out = {
        "generatedAt": int(time.time() * 1000),
        "source": "https://sigmetrics.org/sigmetrics<YEAR>/ committee / program_committee pages (2010-2026)",
        "startYear": min(LOCATION),
        "endYear": max(LOCATION),
        "years": years,
    }
    os.makedirs("data", exist_ok=True)
    with open("data/pc.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    total = sum(len(r["members"]) for r in years)
    print(f"Wrote data/pc.json: {len(years)} conferences ({out['startYear']}-{out['endYear']}), "
          f"{total} PC listings, {len(all_keys)} distinct people")

if __name__ == "__main__":
    main()
