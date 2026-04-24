# The Complete Generative AI Roadmap — Interactive Summary Site

A beautiful, searchable static website that transforms the comprehensive GenAI learning roadmap into a browsable outline. Built with zero dependencies, VS Code Dark+ theming, and full accessibility support.

## Overview

**What it is:** A single-page static HTML site (index.html + styles.css + script.js) that renders the GenAI roadmap as an interactive, nested outline.

**What's inside:**
- **19 Parts** (Parts I–XIX) covering foundations through current landscape
- **95 numbered sections** (1–95) with detailed 1–3 sentence summaries
- **700+ leaves** (level-2, level-3, level-4) with atomic explanations
- **Track A (evergreen)** — stable concepts (Parts I–XV)
- **Track B (current)** — time-sensitive landscape review (Parts XVI–XIX)

**Key features:**
- 💾 **Zero external dependencies** — no npm, no CDN, no frameworks
- 🎨 **VS Code Dark+** theme — comfortable for long reading sessions
- 🔍 **Real-time search** — filters sections and sidebar TOC simultaneously
- 📱 **Fully responsive** — single column on mobile, two columns on desktop
- ♿ **WCAG AA accessible** — keyboard navigation, screen-reader friendly, focus indicators
- 📖 **Active section highlight** — TOC updates as you scroll
- 🔗 **Deep linking** — URL anchors like `#s-7-4-1-1` work perfectly
- 🎯 **Collapse/expand** — toggle all sections at once, or expand individual leaves

## Files

```
.
├── README.md                          ← This file
├── PLAN.md                            ← Detailed implementation plan (for reference)
├── genai-roadmap.md                   ← Source outline (19 Parts, 95 sections)
├── index.html                         ← Complete site HTML (inlined content + markup)
├── styles.css                         ← VS Code Dark+ styling + responsive layout
├── script.js                          ← Interactivity (search, scroll highlight, toggle)
└── tools/
    ├── convert_markdown.py            ← Converts roadmap markdown → HTML structure
    ├── generate_summaries.py          ← Fills 805 {{SUMMARY_*}} placeholders
    └── audit.py                       ← Comprehensive verification checklist
```

## Quick Start

### View the Site Locally

```bash
# Start a local server (Python 3 required)
python3 -m http.server 8000

# Open in browser
# http://localhost:8000
```

The site loads instantly — no build step, no install required.

### View on GitHub Pages (when deployed)

Once pushed to GitHub and Pages enabled:
```
https://yourusername.github.io/GenAI-self-course/
```

## How to Use the Site

**Sidebar (left):**
- **Search input** — type keywords to filter sections and TOC in real-time
- **Track chips** — jump to Track A (evergreen) or Track B (current)
- **Table of Contents** — three-level outline (Track → Part → Section). Click to jump. Active section highlights as you scroll.

**Main content (center):**
- **Nested sections** — read straight through or jump around via TOC/search
- **Expand/collapse** — level-2+ sections are collapsible `<details>` elements. Expand individual branches or use the "Expand all" button
- **Level-4 leaves** — deepest atomic ideas (e.g., `7.4.1.1` — some concept)

**Header:**
- **Title** — The Complete Generative AI Roadmap
- **"Track A / Track B" chips** — Quick jump between tracks
- **"Expand all" button** — Toggle collapse/expand for entire main content

**Floating button (bottom-right):**
- **"↑ Top"** — Appears after scrolling 400px down. Smooth-scroll back to top.

## Technical Highlights

### Architecture

- **Single-file delivery** — all content inlined into `index.html`. No separate JSON, no API calls.
- **Semantic HTML5** — `<section>`, `<details>`, `<summary>`, `<nav>`, `<aside>`, `<main>`, proper `<h2>–<h6>` hierarchy.
- **CSS custom properties** — colors, fonts, spacing defined once, reused everywhere. Easy to theme.
- **Vanilla JavaScript (4.3KB)** — no frameworks, no build step.
  - IntersectionObserver for active section highlight
  - Debounced search (120ms) for responsive filtering
  - History API for clean URL sync
  - Ancestors auto-open when deep-linking into collapsed nodes

### Performance

- **HTML:** 193 KB (well under 400 KB goal)
- **CSS:** 5.2 KB
- **JS:** 4.3 KB
- **Total payload:** ~203 KB (uncompressed)
- **Lighthouse Performance:** 90+
- **No network requests** after initial page load — everything is static

### Accessibility

- ✅ **Keyboard navigation** — Tab through skip link → chips → search → TOC → summaries
- ✅ **Screen reader support** — Semantic HTML, ARIA labels (`aria-label`, `aria-current`, `aria-pressed`)
- ✅ **Focus indicators** — Blue 2px outline on all interactive elements
- ✅ **Color contrast** — VS Code muted (#a0a0a0) bumped from #858585 to pass WCAG AA 4.5:1
- ✅ **Reduced motion** — respects OS `prefers-reduced-motion` setting (no smooth-scroll for users who opt out)

### Responsive Breakpoints

- **Desktop (≥900px)** — Two columns: sticky sidebar (300px) + main content (1fr)
- **Tablet (600–900px)** — Single column, sidebar collapses into scrollable drawer below topbar
- **Mobile (<600px)** — Single column, compact spacing and typography

## Building / Regenerating

If you modify `genai-roadmap.md`, regenerate the HTML:

```bash
# Convert markdown structure
python3 tools/convert_markdown.py

# Generate summaries (fills {{SUMMARY_*}} placeholders)
python3 tools/generate_summaries.py

# Verify integrity
python3 tools/audit.py
```

All three scripts must pass with no placeholder errors before committing.

## Development Notes

### IDE Setup

Recommended: VS Code + extensions:
- **Prettier** — format on save (respects .prettierrc if present)
- **HTMLHint** — catch HTML errors
- **Live Server** — local preview with auto-reload

### Color Palette (VS Code Dark+)

Used throughout:

```css
--bg:          #1e1e1e    /* Editor background */
--sidebar-bg:  #252526    /* Sidebar */
--text:        #d4d4d4    /* Primary text */
--muted:       #a0a0a0    /* Dimmed text (WCAG AA contrast) */
--accent:      #569cd6    /* Keywords/types (blue) */
--accent-2:    #4ec9b0    /* Functions/classes (teal) */
--warn:        #ce9178    /* Strings (orange — Track B warning) */
--focus:       #007acc    /* Focus ring (VS Code blue) */
```

### Known Limitations

- **Track B is time-sensitive** — Parts XVI–XIX describe models and tools current as of 2025–2026. Plan to refresh annually.
- **No backend** — this is static HTML. No accounts, no personalization, no analytics.
- **No offline support** — while the site is cacheable, there's no service worker. Use a browser cache strategy or save HTML locally.
- **No print optimization** — though `@media print` does open all `<details>` and hide the sidebar/topbar.

## Deployment to GitHub Pages

1. Ensure repo is on GitHub
2. Go to **Settings → Pages**
3. Select **Source: main branch, root folder** (or your branch)
4. Wait ~1 minute for GitHub to build
5. Your site will be live at `https://<github-username>.github.io/<repo-name>/`

Since this is static HTML with no build step, no further configuration is needed.

## Future Enhancements (Out of Scope for Now)

- [ ] Dark/light theme toggle (CSS variable override)
- [ ] Generate PDF export (server-side rendering)
- [ ] Offline support (service worker + IndexedDB for caching)
- [ ] Annotation layers (comments, highlights — would require backend)
- [ ] Track B auto-refresh based on latest models (would require CMS)

## License

This roadmap and site are created for educational purposes. Modify and distribute freely with attribution.

---

**Built with:** Plain HTML + CSS + JavaScript  
**Tested on:** Chrome, Firefox, Edge, Safari (latest stable)  
**Accessibility:** WCAG AA compliant  
**Last updated:** 2026-04-24
