(() => {
  'use strict';
  const root = document.getElementById('publication-browser');
  if (!root) return;
  const form = document.getElementById('pub-filters');
  const search = document.getElementById('pub-search');
  const year = document.getElementById('pub-year');
  const venue = document.getElementById('pub-venue');
  const count = document.getElementById('pub-count');
  const reset = document.getElementById('pub-reset');
  const empty = document.getElementById('pub-empty');
  const normalize = text => text.normalize('NFKD').replace(/[\u0300-\u036f]/g, '').toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();
  const papers = Array.from(root.querySelectorAll('.pub-entry')).map(node => ({
    node, item: node.closest('li'), type: node.dataset.type,
    year: node.dataset.year, venue: node.dataset.venue,
    text: normalize((node.dataset.aliases || '') + ' ' + ['.pub-title', '.pub-authors', '.pub-citation', '.pub-meta'].map(selector => node.querySelector(selector)?.textContent || '').join(' '))
  }));
  const sections = Array.from(root.querySelectorAll('.pub-year-section'));
  function options(select, values) {
    values.forEach(value => select.add(new Option(value, value)));
  }
  options(year, [...new Set(papers.map(paper => paper.year))].sort((a, b) => Number(b) - Number(a)));
  options(venue, [...new Set(papers.map(paper => paper.venue))].sort((a, b) => a.localeCompare(b)));
  function readURL() {
    const params = new URLSearchParams(window.location.search);
    search.value = params.get('q') || '';
    year.value = params.get('year') || 'all';
    venue.value = params.get('venue') || 'all';
    if (!year.value) year.value = 'all';
    if (!venue.value) venue.value = 'all';
    const type = params.get('type') || 'all';
    const radios = Array.from(form.querySelectorAll('[name="type"]'));
    (radios.find(input => input.value === type) || radios[0]).checked = true;
  }
  function update(writeURL = true) {
    const type = form.querySelector('[name="type"]:checked').value;
    const terms = normalize(search.value).split(' ').filter(Boolean);
    let shown = 0;
    papers.forEach(paper => {
      const visible = (type === 'all' || paper.type === type) &&
        (year.value === 'all' || paper.year === year.value) &&
        (venue.value === 'all' || paper.venue === venue.value) &&
        terms.every(term => paper.text.includes(term));
      paper.item.hidden = !visible;
      if (visible) shown++;
    });
    sections.forEach(section => {
      const visible = section.querySelectorAll('ol.bibliography > li:not([hidden])').length;
      section.hidden = visible === 0;
      section.querySelector('.pub-year-count').textContent = `${visible} ${visible === 1 ? 'paper' : 'papers'}`;
    });
    count.textContent = `Showing ${shown} of ${papers.length} publications`;
    empty.hidden = shown !== 0;
    reset.disabled = !search.value && type === 'all' && year.value === 'all' && venue.value === 'all';
    if (writeURL) {
      const url = new URL(window.location.href);
      for (const [key, value] of Object.entries({q: search.value.trim(), type, year: year.value, venue: venue.value})) {
        if (value && value !== 'all') url.searchParams.set(key, value);
        else url.searchParams.delete(key);
      }
      window.history.replaceState(null, '', url);
    }
  }
  form.addEventListener('submit', event => event.preventDefault());
  form.addEventListener('input', () => update());
  form.addEventListener('change', () => update());
  form.addEventListener('reset', () => { window.setTimeout(() => { update(); search.focus(); }, 0); });
  document.getElementById('pub-empty-reset').addEventListener('click', () => form.reset());
  window.addEventListener('popstate', () => { readURL(); update(false); });
  readURL();
  update(false);
  form.hidden = false;
})();
