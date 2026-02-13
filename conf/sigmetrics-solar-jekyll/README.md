# SIGMETRICS (Solar-style) Jekyll Site

This is a Jekyll site using a SOLAR-lab inspired layout (top nav + hero + clean content sections),
populated with the SIGMETRICS pages linked from the SIGMETRICS home page.

## Prerequisites
- Ruby (recommended: 3.x)
- Bundler (`gem install bundler`)

## Run locally
```bash
bundle install
bundle exec jekyll serve
```

Then open: http://localhost:4000

## Build
```bash
bundle exec jekyll build
```
The static site will be in `_site/`.

## Structure
- `_layouts/` and `_includes/` hold the reusable template parts.
- `_data/navigation.yml` defines the top navigation items.
- `assets/` holds CSS, JS, and images.
- Each root page is a standalone `.html` file with Jekyll front-matter.

## Updating content
Each page has a content section in `pages/` (markdown) that is embedded into the page layout.
Replace or expand those markdown files as desired.
