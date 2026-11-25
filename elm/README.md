# Erik G. Learned-Miller homepage

A self-contained static adaptation of this repository's SOLAR Bootstrap template, with its green link palette and UMass maroon footer. No build step or third-party JavaScript is required.

Open `index.html` directly, or run a static server from the repository root:

```sh
python3 -m http.server 8000
```

Then visit `http://localhost:8000/elm/`.

## Content and sources

- Profile, news, 38 research entries, students, 26 courses across 25 terms, six funding entries, code, and FAQ preserve the content of [the original homepage](https://people.cs.umass.edu/~elm/) and its linked section pages. Historical roles, news, affiliations, and course descriptions have deliberately not been updated.
- [Publications](publications.html) contains all 173 records from [DBLP](https://dblp.org/pid/l/ErikGLearnedMiller), retrieved November 24, 2026: 19 journal articles, 104 conference/workshop papers, 49 preprint/informal records, and one thesis. Conference, journal, and preprint versions remain distinct, following DBLP.
- `data/publications.json` retains the complete imported bibliography and source links. The publication list is also rendered into HTML, so it works without JavaScript. Update both when refreshing the bibliography.
- Images are local in `images/`. They come from the original site, except the UMass seal reused from the SOLAR template. `FRTCover.png` renders the original PDF cover for reliable browser display.
- Original paper, project, student, course, and code links remain external. Some historical destinations may no longer be maintained.
- `papers_by_*.html` preserves the legacy section filenames through redirects.

## Layout and behavior

- Shared styles: `css/bootstrap.min.css` and `css/elm.css`.
- Progressive enhancement: `js/elm.js` provides publication search/year/type filtering and accessible buttons for both original image alignment demonstrations.
- Navigation, content, and publication links remain usable without JavaScript.
- Local changes are confined to `elm/`; the lab website is unchanged.
