#!/usr/bin/env python3
"""
make_submissions.py - write data/submissions.json: SIGMETRICS conference submission
statistics (submitted / accepted / rejected / acceptance rate) per year, 2010-2026.

Method follows csconferences.org (Emery Berger) exactly: for each year, SUM Accepted and
Submitted across all submission rounds ("Sequence" rows), then
    rejected = submitted - accepted
    acceptance_rate = accepted / submitted

2010-2024 come from csconferences.csv (proceedings front matter + HotCRP, per that repo).
2025-2026 are summed from the three rolling HotCRP round sites (summer/fall/winter), whose
public landing pages report "<accepted> of <submitted> submissions accepted" (read-only,
no login).
"""
import csv, json, time, os
from collections import OrderedDict

CSV = "csconferences.csv"
CS_URL = "https://csconferences.org/"

# Public HotCRP landing-page counts for the rolling rounds feeding POMACS.
HOTCRP = {
    2025: [("summer", 20, 110), ("fall", 15, 113), ("winter", 32, 159)],
    2026: [("summer", 24, 112), ("fall", 25, 155), ("winter", 33, 212)],
}

def main():
    agg = OrderedDict()
    with open(CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if (row.get("Conference") or "").strip().upper() != "SIGMETRICS":
                continue
            y = int(row["Year"]); a = int(row["Accepted"] or 0); s = int(row["Submitted"] or 0)
            d = agg.setdefault(y, {"accepted": 0, "submitted": 0})
            d["accepted"] += a; d["submitted"] += s

    series = []
    for y in sorted(agg):
        a, s = agg[y]["accepted"], agg[y]["submitted"]
        series.append({"year": y, "submitted": s, "accepted": a, "rejected": s - a,
                       "rate": round(100 * a / s, 1) if s else 0.0, "source": "csconferences.org"})
    for y in sorted(HOTCRP):
        rounds = [{"round": r, "accepted": a, "submitted": s} for (r, a, s) in HOTCRP[y]]
        a = sum(x["accepted"] for x in rounds); s = sum(x["submitted"] for x in rounds)
        series.append({"year": y, "submitted": s, "accepted": a, "rejected": s - a,
                       "rate": round(100 * a / s, 1) if s else 0.0,
                       "source": "HotCRP rounds", "rounds": rounds})
    series.sort(key=lambda d: d["year"])

    out = {
        "generatedAt": int(time.time() * 1000),
        "note": ("Acceptance computed as csconferences.org does: sum accepted & submitted "
                 "across rounds per year; rejected = submitted - accepted; rate = accepted/submitted."),
        "sources": {"2010-2024": CS_URL, "2025-2026": "SIGMETRICS HotCRP round sites (summer/fall/winter)"},
        "startYear": series[0]["year"], "endYear": series[-1]["year"], "years": series,
    }
    os.makedirs("data", exist_ok=True)
    with open("data/submissions.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    tsub = sum(d["submitted"] for d in series); tacc = sum(d["accepted"] for d in series)
    mean = sum(d["rate"] for d in series) / len(series)
    print(f"Wrote data/submissions.json: {len(series)} years ({out['startYear']}-{out['endYear']}), "
          f"{tsub} submitted, {tacc} accepted, pooled {100*tacc/tsub:.1f}%, per-year mean {mean:.1f}%")

if __name__ == "__main__":
    main()
