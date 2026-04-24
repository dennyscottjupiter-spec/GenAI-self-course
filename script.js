// Loaded with defer, so DOM is ready when this runs.
(() => {
  const $ = (sel, root = document) => root.querySelector(sel);
  const $$ = (sel, root = document) => Array.from(root.querySelectorAll(sel));

  /* ── 1. Active section highlight via IntersectionObserver ────────────── */
  const tocLinks = new Map($$('#toc a[href^="#"]').map(a => [a.getAttribute('href').slice(1), a]));
  const observed = $$('section[id], details[id]');

  const setActive = (id) => {
    tocLinks.forEach((a, key) => {
      if (key === id) a.setAttribute('aria-current', 'location');
      else a.removeAttribute('aria-current');
    });
  };

  const io = new IntersectionObserver((entries) => {
    // Pick the entry nearest the top of the viewport that is intersecting.
    const visible = entries.filter(e => e.isIntersecting).sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
    if (visible[0]) setActive(visible[0].target.id);
  }, { rootMargin: '-20% 0px -70% 0px', threshold: 0 });

  observed.forEach(el => io.observe(el));

  /* ── 2. Search with debounce ─────────────────────────────────────────── */
  const searchInput = $('#search');
  const allSections = $$('main section[id], main details[id]');
  const allTocItems = $$('#toc li');

  const debounce = (fn, ms) => { let t; return (...args) => { clearTimeout(t); t = setTimeout(() => fn(...args), ms); }; };

  const runSearch = (q) => {
    q = q.trim().toLowerCase();
    if (!q) {
      allSections.forEach(s => s.hidden = false);
      allTocItems.forEach(li => li.hidden = false);
      return;
    }
    // Hide everything first
    allSections.forEach(s => s.hidden = true);
    allTocItems.forEach(li => li.hidden = true);
    // Show sections matching in their own title or summary
    allSections.forEach(sec => {
      const text = (sec.querySelector(':scope > h2, :scope > h3, :scope > summary, :scope > .summary')?.innerText || '') + ' ' +
                   (sec.querySelector(':scope > .summary')?.innerText || '');
      if (text.toLowerCase().includes(q)) {
        sec.hidden = false;
        // Unhide ancestors so the match is reachable
        let p = sec.parentElement;
        while (p && p !== document.body) { if (p.matches('section[id], details[id]')) p.hidden = false; p = p.parentElement; }
        // Unhide the matching TOC entry
        const link = tocLinks.get(sec.id);
        if (link) { let li = link.closest('li'); while (li) { li.hidden = false; li = li.parentElement?.closest('li'); } }
      }
    });
  };
  searchInput.addEventListener('input', debounce(e => runSearch(e.target.value), 120));

  /* ── 3. Collapse / Expand all ────────────────────────────────────────── */
  const toggleBtn = $('#toggle-all');
  toggleBtn.addEventListener('click', () => {
    const shouldOpen = toggleBtn.getAttribute('aria-pressed') !== 'true';
    $$('main details').forEach(d => d.open = shouldOpen);
    toggleBtn.setAttribute('aria-pressed', String(shouldOpen));
    toggleBtn.textContent = shouldOpen ? 'Collapse all' : 'Expand all';
  });

  /* ── 4. Back to top ──────────────────────────────────────────────────── */
  const fab = $('#back-to-top');
  const firstPartTop = () => $('section.part')?.getBoundingClientRect().top ?? 0;
  const onScroll = () => { fab.hidden = window.scrollY < 400; };
  window.addEventListener('scroll', onScroll, { passive: true });
  fab.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

  /* ── 5. Keep URL hash in sync when clicking TOC ──────────────────────── */
  tocLinks.forEach((a, id) => {
    a.addEventListener('click', () => history.replaceState(null, '', '#' + id));
  });

  /* ── 6. On load, if URL has a hash targeting a collapsed details, open it and its ancestors ── */
  const openAncestors = (el) => { let p = el; while (p) { if (p.tagName === 'DETAILS') p.open = true; p = p.parentElement; } };
  if (location.hash) {
    const target = document.getElementById(location.hash.slice(1));
    if (target) openAncestors(target);
  }
})();
