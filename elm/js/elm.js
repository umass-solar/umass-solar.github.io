'use strict';
// The full site and bibliography remain readable without JavaScript.
const filters = document.querySelector('.publication-filters');
if (filters) {
  filters.hidden = false;
  const search = document.querySelector('#publication-search');
  const year = document.querySelector('#publication-year');
  const type = document.querySelector('#publication-type');
  const publications = Array.from(document.querySelectorAll('.publication'));
  const normalize = value => value.normalize('NFKD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  const text = new Map(publications.map(publication => [publication, normalize(publication.textContent)]));
  const update = () => {
    const terms = normalize(search.value.trim()).split(/\s+/).filter(Boolean);
    let count = 0;
    for (const publication of publications) {
      const matches = (!year.value || publication.dataset.year === year.value)
        && (!type.value || publication.dataset.type === type.value)
        && terms.every(term => text.get(publication).includes(term));
      publication.hidden = !matches;
      if (matches) count++;
    }
    document.querySelectorAll('.publication-year').forEach(section => {
      section.hidden = !section.querySelector('.publication:not([hidden])');
    });
    document.querySelector('#publication-count').textContent = `${count} of ${publications.length} publications`;
    document.querySelector('#no-results').hidden = count !== 0;
  };
  filters.addEventListener('submit', event => event.preventDefault());
  filters.addEventListener('input', update);
  filters.addEventListener('change', update);
  filters.addEventListener('reset', () => { requestAnimationFrame(update); });
  update();
}
for (const button of document.querySelectorAll('.alignment-toggle')) {
  const image = document.getElementById(button.getAttribute('aria-controls'));
  const setAligned = aligned => {
    image.src = aligned ? image.dataset.aligned : image.dataset.original;
    button.setAttribute('aria-pressed', String(aligned));
    button.textContent = aligned ? 'Show original images' : 'Show aligned images';
  };
  button.addEventListener('click', () => setAligned(button.getAttribute('aria-pressed') !== 'true'));
  image.addEventListener('pointerenter', event => { if (event.pointerType === 'mouse') setAligned(true); });
  image.addEventListener('pointerleave', event => { if (event.pointerType === 'mouse') setAligned(false); });
}
