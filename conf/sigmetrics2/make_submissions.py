#!/usr/bin/env python3
"""
make_submissions.py - write data/submissions.json: SIGMETRICS conference submission
statistics (submitted / accepted / rejected / acceptance rate) per year, 2010-2026.

Method follows csconferences.org (Emery Berger) exactly: for each year, SUM Accepted and
Submitted across all submission rounds ("Sequence" rows), then
    rejected = submitted - accepted
    acceptance_rate = accepted / submitted
(csconferences groupby(Year).agg(sum) -> Accepted/Submitted; see build.py lines 135,212,213.)

2010-2024 come from csconferences.csv (front matter of proceedings + HotCRP, per that repo).
2025-2026 are summed from the three rolling HotCRP round sites (summer/fall/winter), whose
public landing pages report "<accepted> of <submitted> submissions accepted".
"""
import csv, json, time
from collections import defaultdict

CSV = "csconferences.csv"
CS_URL = "https://csconferences.org/"

# 2025 & 2026 use three rolling deadlines feeding POMACS; counts from each HotCRP landing page.
ROUNDS = {
    2025: [
        ("Summer", 20, 110, "https://sigmetrics25summer.hotcrp.com/"),
        ("Fall",   15, 113, "https://sigmetrics25fall.hotcrp.com/"),
        ("Winter", 32, 159, "https://sigmetrics25winter.hotcrp.com/"),
    ],
    2026: [
        ("Summer", 24, 112, "https://sigmetrics26summer.hotcrp.com/"),
        ("Fall",   25, 155, "https://sigmetrics26fall.hotcrp.com/"),
        ("Winter", 33, 212, "https://sigmetrics26winter.hotcrp.com/"),
    ],
}

def main():
    years = {}

    # ---- 2010-2024 from csconferences.csv (sum across sequences) ----
    agg = defaultdict(lambda: [0, 0])   # year -> [accepted, submitted]
    with open(CSV, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["Conference"].strip().upper() == "SIGMETRICS":
                y = int(r["Year"])
                if 2010 <= y <= 2024:
                    agg[y][0] += int(r["Accepted"]); agg[y][1] += int(r["Submitted"])
    for y, (acc, sub) in agg.items():
        years[y] = {"year": y, "submitted": sub, "accepted": acc,
                    "rejected": sub - acc,
                    "rate": round(100 * acc / sub, 1) if sub else None,
                    "source": "csconferences.org", "rounds": None}

    # ---- 2025-2026 from HotCRP rolling rounds ----
    for y, rounds in ROUNDS.items():
        acc = sum(a for _, a, _, _ in rounds)
        sub = sum(s for _, _, s, _ in rounds)
        years[y] = {"year": y, "submitted": sub, "accepted": acc,
                    "rejected": sub - acc, "rate": round(100 * acc / sub, 1),
                    "source": "HotCRP (summer + fall + winter rounds)",
                    "rounds": [{"name": n, "accepted": a, "submitted": s, "url": u}
                               for n, a, s, u in rounds]}

    series = [years[y] for y in sorted(years)]
    out = {
        "generatedAt": int(time.time() * 1000),
        "method": ("Per year, accepted and submitted are summed across all submission "
                   "rounds; rejected = submitted - accepted; acceptance rate = "
                   "accepted / submitted. Matches csconferences.org."),
        "sources": {"2010-2024": CS_URL, "2025-2026": "https://sigmetrics.org/ HotCRP round sites"},
        "startYear": series[0]["year"], "endYear": series[-1]["year"],
        "years": series,
    }
    import os; os.makedirs("data", exist_ok=True)
    with open("data/submissions.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    tsub = sum(s["submitted"] for s in series); tacc = sum(s["accepted"] for s in series)
    print(f"Wrote data/submissions.json: {len(series)} years "
          f"({out['startYear']}-{out['endYear']}), {tsub} submitted, {tacc} accepted, "
          f"overall {100*tacc/tsub:.1f}%")

if __name__ == "__main__":
    main()
