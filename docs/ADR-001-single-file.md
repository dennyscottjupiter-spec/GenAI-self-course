# ADR-001: Keep the roadmap as a single HTML file

## Context

The roadmap site is currently 195 KB (approximately 58 KB gzipped). During architecture planning, it was proposed to split the content into 19 separate HTML files — one per Part (Part I through Part XIX) — in order to reduce the size of any single page load and improve perceived performance.

## Decision

Keep `index.html` as a single inlined document. Do not split into per-Part files.

## Consequences

### Pros

- **Client-side search remains simple and comprehensive.** The search feature (`script.js`, lines 32–56) scans `document.querySelectorAll('main section[id], main details[id]')` — the full inlined DOM. A single-page architecture guarantees all 95 sections are searchable in one pass. Splitting would require either:
  - An API backend to search across files (defeats the zero-backend goal), or
  - Lazy-loading and searching only the current Part (frustrating for users), or
  - Building an index at build-time and rewriting search logic entirely.

- **Deep links and auto-open work in one load.** URLs like `https://site.com/roadmap#s-7-4-1-1` (a specific nested bullet in Part VII, Section 7.4.1.1) are handled by `script.js` lines 80–85, which auto-opens ancestor `<details>` elements on page load. This works because all sections are present in the DOM. Splitting breaks this: users clicking a deep link from a bookmark would land on a different HTML file (Part VII) than originally intended, requiring URL rewrite logic and breaking the bookmark's portability.

- **No build-step complexity.** Single-file architecture avoids the need for URL rewriting, link remapping, or a routing layer during the static build pipeline. The current tool pipeline (`convert_markdown.py` → `generate_summaries.py` → `fix_issues.py` → `audit.py`) remains unchanged.

### Cons

- **Initial payload is larger.** At 60 KB gzipped, the full roadmap is heavier than any individual Part would be. For users on slow mobile connections (3G), initial page load is noticeably slower (~2–3 seconds) compared to splitting (which could deliver a single Part in <1 second). However:
  - The site is designed for focused, linear reading — users typically stay on the page for 10–30 minutes, so amortizing the initial load is acceptable.
  - The use case is a learning resource, not a frequently-bounced news site; raw throughput matters less than total session time.
  - Gzip + browser caching make repeat visits instant.

### Revisit if

- **Total size exceeds 500 KB gzipped.** At that scale, modern bundlers and lazy-loading become justified.
- **Mobile-first users report slow first-paint metrics** (Lighthouse CLS, FCP score drops below 50). Use real-world monitoring data, not speculation.
- **Analytics reveal users are landing on deep links much more often than linear reading.** This would indicate users are sharing and bookmarking specific bullets, making a multi-file architecture more valuable.

---

## Reference

- **Exploration report:** Codebase analysis confirmed search scans the full inlined DOM and deep-links rely on ancestor `<details>` elements being present on load.
- **Alternative rejected:** Lazy-loading per-Part via `fetch()` + DOM injection loses search and requires URL-rewrite logic; net complexity increase despite per-file size win.
