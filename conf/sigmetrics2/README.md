# SIGMETRICS Author Dashboard

A fully static, dependency-free website for exploring authorship and collaboration at
ACM **SIGMETRICS (1974–present)**, built from [DBLP](https://dblp.org/db/conf/sigmetrics/).

- **No backend, no build step, no libraries.** One HTML file + one JSON file.
- The page **never contacts DBLP** at runtime. Small Python scripts fetch the data once,
  offline; the site just reads the result.
- A **year-range selector** (default **1974 → present**) recomputes every metric for the
  window you pick.
- Productivity *and* collaboration-structure metrics, with honest caveats about what
  DBLP data can and can't tell you.

---

## Quick start

You need **Python 3** (preinstalled on macOS/Linux; on Windows get it from python.org).
**Nothing to `pip install`** — the scripts use only the standard library.

```bash
cd sigmetrics-dashboard

# 1) build the dataset (1974 → current year)
python3 fetch_sigmetrics.py            # real DBLP data  (recommended)
#   — or try the UI instantly with synthetic data —
python3 make_sample.py                 # demo data, clearly labelled "sample"

# 2) (optional) add homepage + Google Scholar links from CSRankings
python3 make_author_links_from_csrankings.py

# 2b) (optional) build the awards overlay (best paper, test of time, rising star, achievement)
python3 make_awards.py

# 2c) (optional) build the chairs overlay (general + program chairs, 1973–2027)
python3 make_chairs.py

# 3) serve the folder and open it
python3 -m http.server 8000
```

Open **http://localhost:8000/**.

> A server is needed only because browsers block `fetch()` of a `file://` path.
> `python3 -m http.server` ships with Python; any static host (GitHub Pages, Netlify…) works too.

A sample `data/sigmetrics.json` is included so the site renders immediately; running
`fetch_sigmetrics.py` replaces it with real records and the "sample data" banner disappears.

---

## The scripts

### `fetch_sigmetrics.py` — the data fetcher (admin refresh)
Downloads SIGMETRICS records from the DBLP Search API (1974 → current year) and writes
`data/sigmetrics.json`. Its rules:

- **Default `--method stream`**: pulls the whole venue as one paginated *stream* query
  (the "export records of this stream" feed DBLP links from the SIGMETRICS page). The
  entire history comes back in ~4–5 requests, which **stays well under DBLP's per-IP rate
  limit**. A `--method toc` per-year crawl is kept as a fallback.
- Honours DBLP's `Retry-After` and backs off with jitter on HTTP 429 / transient errors;
  a real rate-limit error is reported, never silently turned into an "empty year".
- Excludes **editorships** and clearly non-conference entries (permissive when the type
  field is missing, as in some older records).
- Drops **posters / short non-papers** by page length: for **1974–2016**, entries shorter
  than 5 pages are removed; for **2017+**, no page filtering.
- De-duplicates by DBLP key and writes atomically, so the site never reads a half-written file.

Common flags: `--start 1974 --end 2026 --delay 2.0 --retries 8 --method stream|toc
--min-pages-pre2017 5 --page-filter-end-year 2016 --out data/sigmetrics.json`.

> **If you hit HTTP 503 or 429:** DBLP is throttling your IP (usually after rapid retries).
> The fetcher now **checkpoints progress after every page** to `data/sigmetrics.json.partial.json`
> and **resumes automatically** — so if DBLP cuts you off part-way, just wait a few minutes and
> run the *same command again*; it picks up where it stopped and keeps going until complete.
> If 503s persist, slow down with `--delay 5`. Use `--no-resume` to start fresh.
> (The earlier per-year version tripped this constantly; the stream method + resume is the fix.)

### `make_author_links_from_csrankings.py` — optional link enrichment
Reads `data/sigmetrics.json`, fetches the CSRankings name→homepage/scholar tables once,
and writes `data/author_links.json` (DBLP + homepage + Google Scholar per author, matched
by name; DBLP always included when a `pid` exists). The dashboard shows these on each
author's page when present — it works fine without this file.

### `make_awards.py` — awards overlay
Writes `data/awards.json` from the SIGMETRICS awards page (Achievement, Rising Star,
Test of Time, Best Paper / Best Student Paper). It's static transcribed data — no fetch
needed. The website overlays it onto whatever dataset is loaded by **matching paper titles
and author names**, so it marks award papers and award authors without touching DBLP. Edit
the lists at the top of the script when the awards page adds new entries.

### `make_chairs.py` — conference chairs overlay
Writes `data/chairs.json`: the General Chairs and Program (TPC) Chairs of every SIGMETRICS
conference (1973–2027), transcribed from the conference history and recent organization
pages. Like awards, it's matched onto authors by name (same exact + fuzzy matcher) and needs
no refetch. Edit the `CONF` list when a new edition is announced.

### `make_sample.py` — synthetic demo data
Generates a clearly-labelled sample `data/sigmetrics.json` (+ a small `author_links.json`)
in the exact schema `fetch_sigmetrics.py` produces, so the UI is viewable out of the box.
It also seeds a handful of real award-winning papers/authors so the awards overlay is
visibly demonstrable on sample data.

---

## Refreshing on a schedule

Re-run the fetcher whenever you want fresh data. To automate monthly, e.g.:

```cron
0 4 1 * *  cd /path/to/sigmetrics-dashboard && /usr/bin/python3 fetch_sigmetrics.py
```

The **Overview** and **Data & method** tabs show the fetch date, and a banner appears if
the data is more than ~4 months old.

---

## The five views

- **Overview** — community growth, collaboration intensity, newcomer renewal, team-size
  distribution, and a Lorenz curve / Gini of how concentrated publishing is.
- **Authors** — searchable, sortable table; every row has a publication-trajectory
  sparkline. Click anyone for their dashboard.
- **Author detail** — trajectory, authorship-role breakdown (with an alphabetical-ordering
  caveat), an ego coauthor network, top collaborators, DBLP/homepage/Scholar links, and the
  full paper list.
- **Network** — community-level collaboration structure: ties, the largest connected
  component, and the most-connected hubs.
- **Awards** — every SIGMETRICS Achievement Award, Rising Star, Test of Time, Best Paper /
  Best Student Paper (plus runners-up), and Doctoral Dissertation Award winner, current
  through 2026. Award papers are also badged in author pages, and award authors get a 🏅 in
  the table and award chips on their dashboard.
- **Chairs** — the General Chairs and Program (TPC) Chairs of every SIGMETRICS conference,
  1973–2027, with locations. Chairs are marked on author pages (🎫 General Chair / 🪑 PC
  Chair chips) and get a 🪑 marker in the authors table.
- **Data & method** — provenance, integrity checks, the refresh commands, and a plain-English
  statement of what the numbers mean and don't.

Every view honours the **year-range selector** in the header (default 1974–present, with
All / 20y / 10y / 5y presets). Narrow it and all charts, tables, and the network recompute
for that window; "active in last 5 years" is measured relative to the window's end year.

## Reading the numbers (important)

This dashboard measures **participation and collaboration**, not impact — DBLP has no
citations or abstracts, so "prolific" means *frequent at SIGMETRICS*, never "influential".
Authors are merged by DBLP **id** (`pid:…`), first/last-author metrics are flagged where
ordering is largely alphabetical, and editorships/short non-papers are excluded by the fetcher.

```
sigmetrics-dashboard/
├── index.html                          the whole website (HTML + CSS + JS)
├── fetch_sigmetrics.py                 admin refresh — real DBLP data, 1974→present
├── make_author_links_from_csrankings.py  optional homepage/Scholar links
├── make_sample.py                      synthetic demo data
├── data/
│   ├── sigmetrics.json                 the dataset the website reads
│   └── author_links.json               optional extra links
└── README.md
```
