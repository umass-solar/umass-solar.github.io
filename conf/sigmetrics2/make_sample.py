#!/usr/bin/env python3
"""
make_sample.py — generate a clearly-labelled SYNTHETIC dataset (1974-2026) in the SAME
schema produced by fetch_sigmetrics.py, so the dashboard renders before you fetch real
data. Also writes a small sample data/author_links.json to demonstrate homepage / Scholar
links. Run fetch_sigmetrics.py (+ make_author_links_from_csrankings.py) for real data.
"""
import json, random, os, time
random.seed(7)

OUT = os.path.join(os.path.dirname(__file__), "data", "sigmetrics.json")
LINKS = os.path.join(os.path.dirname(__file__), "data", "author_links.json")
START, END = 1974, 2026

FIRST = ["Anshul","Mor","Bianca","Adam","Niklas","Edith","Philippe","Longbo","Jia","Wei",
         "Li","Maria","Sofia","Lucas","Nina","Omar","Priya","Chen","Yuki","Diego","Hannah",
         "Ravi","Elena","Marco","Aisha","Tomas","Greta","Sanjay","Lena","Felix","Nadia",
         "Ibrahim","Yara","Kenji","Olga","Pedro","Mei","Arjun","Clara","Hugo","Ines","Kofi",
         "Mira","Noah","Petra","Quinn","Rosa","Samir","Tara","Leon","Ada","Bo","Ima","Raj"]
LAST = ["Gandhi","Harchol-Balter","Schroeder","Wierman","Carlsson","Cohen","Robert","Huang",
        "Wang","Zhang","Liu","Lopez","Rossi","Nguyen","Andersson","Khan","Patel","Mueller",
        "Tanaka","Silva","Kowalski","Bianchi","Novak","Haddad","Okonkwo","Park","Costa",
        "Ferrari","Reddy","Olsen","Vargas","Ibrahim","Sato","Petrov","Mensah","Almeida",
        "Chen","Sharma","Mendes","Schmidt","Ferreira","Acheampong","Ito","Dubois","Romano",
        "Jansen","Becker","Larsson","Yilmaz","Moreau","Abbas","Wong","Diaz","Klein","Roy"]

N = 200
people, used = [], set()
for i in range(N):
    while True:
        nm = f"{random.choice(FIRST)} {random.choice(LAST)}"
        if nm not in used:
            used.add(nm); break
    pid = f"{random.randint(10,99)}/{random.randint(1000,9999)}"
    start = random.randint(START, END-2)
    span = min(END-start, int(random.expovariate(1/8))+1)
    people.append({"pid": pid, "id": "pid:"+pid, "name": nm,
                   "start": start, "span": span, "w": random.paretovariate(1.6)})

def surname(n): return n.split()[-1].lower()

records, page = [], 1
for year in range(START, END+1):
    growth = 0.5 + (year-START)/(END-START)*1.8
    n_papers = max(4, int(random.gauss(22*growth, 5)))
    base_team = 1.8 + (year-START)/(END-START)*2.0
    active = [p for p in people if p["start"] <= year < p["start"]+p["span"]]
    if len(active) < 3: continue
    ws = [p["w"] for p in active]
    for _ in range(n_papers):
        size = max(1, min(8, int(round(random.gauss(base_team, 1.2)))))
        chosen, pool, pw = [], active[:], ws[:]
        for _k in range(min(size, len(pool))):
            tot = sum(pw); r = random.uniform(0, tot); acc = 0
            for idx, w in enumerate(pw):
                acc += w
                if acc >= r:
                    chosen.append(pool.pop(idx)); pw.pop(idx); break
        if len(chosen) > 1 and random.random() < 0.38:
            chosen.sort(key=lambda p: surname(p["name"]))
        start_pg = page; end_pg = page + random.randint(5, 16); page = end_pg + 1
        au = [{"id": p["id"], "pid": p["pid"], "name": p["name"]} for p in chosen]
        records.append({
            "year": year,
            "title": f"Sample paper {len(records)+1} on performance modeling",
            "authors": au,
            "authorIds": [p["id"] for p in chosen],
            "venue": "SIGMETRICS",
            "pages": f"{start_pg}-{end_pg}",
            "doi": "", "url": "", "key": f"conf/sigmetrics/s{year}-{len(records)}",
            "type": "Conference and Workshop Papers",
        })

random.shuffle(records)

# authorMeta keyed by id (same shape fetch_sigmetrics.py emits)
authorMeta = {}
for p in people:
    authorMeta[p["id"]] = {"id": p["id"], "pid": p["pid"], "name": p["name"],
                           "canonicalName": p["name"], "aliases": [p["name"]]}

# --- seed a few REAL award-winning papers/authors so the awards overlay visibly works
#     on sample data (titles & names match data/awards.json). Clearly part of sample data. ---
SEED_PAPERS = [
    (2011,"Greening Geographical Load Balancing",["Zhenhua Liu","Minghong Lin","Adam Wierman","Steven Low","Lachlan L.H. Andrew"]),
    (2021,"Nudge: Stochastically Improving upon FCFS",["Isaac Grosof","Kunhe Yang","Ziv Scully","Mor Harchol-Balter"]),
    (2008,"Counter Braids: A Novel Counter Architecture for Per-Flow Measurement",["Yi Lu","Andrea Montanari","Balaji Prabhakar","Sarang Dharmapurikar","Abdul Kabbani"]),
    (2015,"Spy vs. Spy: Rumor Source Obfuscation",["Giulia Fanti","Peter Kairouz","Sewoong Oh","Pramod Viswanath"]),
    (2013,"Queueing System Topologies with Limited Flexibility",["John N. Tsitsiklis","Kuang Xu"]),
    (2010,"Detecting Sources of Computer Viruses in Networks: Theory and Experiment",["Devavrat Shah","Tauhid Zaman"]),
    (1996,"Exploiting Process Lifetime Distributions for Dynamic Load Balancing",["Mor Harchol-Balter","Allen Downey"]),
    (2018,"A refined mean field approximation",["Nicolas Gast","Benny van Houdt"]),
    (1996,"Self-similarity in World Wide Web Traffic: Evidence and Possible Causes",["Mark E. Crovella","Azer Bestavros"]),
    (1976,"Fundamental Laws of Computer System Performance",["Jeffrey P. Buzen"]),
    (2014,"A Measurement Study of Google Play",["Nicolas Viennot","Edward Garcia","Jason Nieh"]),
    (2012,"Temperature Management in Data Centers: Why Some (Might) Like It Hot",["Nosayba El-Sayed","Ioan Stefanovici","George Amvrosiadis","Andy A. Hwang","Bianca Schroeder"]),
    (2019,"Anshul Gandhi sample contribution",["Anshul Gandhi"]),
    (2014,"Florian Simatos sample contribution",["Florian Simatos"]),
    (2025,"Adversarial Network Optimization under Bandit Feedback: Maximizing Utility in Non-Stationary Multi-Hop Networks",["Yan Dai","Longbo Huang"]),
    (2023,"Mean-field Analysis for Load Balancing on Spatial Graphs",["Daan Rutten","Debankur Mukherjee"]),
    (2015,"Learning to Rank: Regret Lower Bounds and Efficient Algorithms",["Richard Combes","Stefan Magureanu","Alexandre Proutiere","Cyrille Laroche"]),
    (2002,"Network Tomography on General Topologies",["Tian Bu","Nick Duffield","Francesco Lo Presti","Donald F. Towsley"]),
    (2009,"A decoy paper to test name disambiguation",["Daniel Towsley"]),
]
_seed_pid = {}
def _pid_for(nm):
    if nm not in _seed_pid:
        _seed_pid[nm] = f"sd/{len(_seed_pid)+1:04d}"
    return _seed_pid[nm]
for i, (yr, title, auths) in enumerate(SEED_PAPERS):
    au = [{"id": "pid:" + _pid_for(n), "pid": _pid_for(n), "name": n} for n in auths]
    records.append({
        "year": yr, "title": title, "authors": au, "authorIds": [a["id"] for a in au],
        "venue": "SIGMETRICS", "pages": f"{100+i*3}-{118+i*3}", "doi": "", "url": "",
        "key": f"conf/sigmetrics/seed-{i}", "type": "Conference and Workshop Papers",
    })
    for n in auths:
        idd = "pid:" + _pid_for(n)
        authorMeta[idd] = {"id": idd, "pid": _pid_for(n), "name": n,
                           "canonicalName": n, "aliases": [n]}

out = {
    "fetchedAt": int(time.time()*1000),
    "startYear": START, "endYear": END,
    "sample": True,
    "source": "synthetic — run fetch_sigmetrics.py for real DBLP data",
    "records": records,
    "authorMeta": authorMeta,
    "notes": {"sample": True, "maxHitsPerToc": 1000,
              "note": "Synthetic data for demonstration only."},
}
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, separators=(",", ":"))

# a small sample author_links.json (homepage + scholar for a subset) to show the UI
byPid = {}
for p in random.sample(people, k=28):
    slug = p["name"].lower().replace(" ", "")
    byPid[p["pid"]] = {
        "dblp": f"https://dblp.org/pid/{p['pid']}.html",
        "homepage": f"https://example.edu/~{slug}",
        "googleScholar": f"https://scholar.google.com/citations?user={slug[:10]}AAAAJ&hl=en",
    }
with open(LINKS, "w", encoding="utf-8") as f:
    json.dump({"generatedAt": int(time.time()*1000), "sample": True,
               "byPid": byPid, "byName": {}}, f, ensure_ascii=False, indent=2)

print(f"Wrote {len(records)} records, {len(people)} authors -> {OUT}")
print(f"Wrote {len(byPid)} sample author links -> {LINKS}")
