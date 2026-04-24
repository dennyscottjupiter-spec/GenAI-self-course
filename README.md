# The Complete Generative AI Roadmap

A searchable, interactive static website that turns the GenAI learning roadmap into a browsable outline. Zero dependencies — open `index.html` and it works.

---

## What's Inside

| Layer | Detail |
|---|---|
| **19 Parts** (I – XIX) | Foundations → current landscape |
| **95 numbered sections** | Each with a 2–3 sentence summary |
| **700 + leaves** (levels 2–4) | Atomic, one-idea-per-bullet explanations |
| **Track A (Parts I–XV)** | Evergreen — stable concepts that age slowly |
| **Track B (Parts XVI–XIX)** | Time-sensitive — refresh once a year |

---

## Files

```
.
├── index.html               ← Complete site (all content inlined)
├── styles.css               ← VS Code Dark+ theme + responsive layout
├── script.js                ← Search, scroll highlight, collapse, deep links
├── genai-roadmap.md         ← Source outline (19 Parts, 95 sections)
├── tools/
│   ├── convert_markdown.py  ← Converts roadmap .md → HTML structure
│   ├── generate_summaries.py← Fills all {{SUMMARY_*}} placeholders
│   ├── audit.py             ← 124-check verification script
│   └── fix_issues.py        ← Post-generation fixes (TOC, preamble)
├── PLAN.md                  ← Implementation plan (reference)
└── VERIFICATION.md          ← 124/124 test audit report
```

---

## Quick Start

### 1 — View Locally (Recommended First Step)

Python ships a tiny web server perfect for local HTML previewing.

```bash
# Start the server — run this from the project folder
python3 -m http.server 8000

# Open your browser and go to:
http://localhost:8000
```

> The site loads instantly — no build step, no `npm install`, nothing to configure.

### 2 — Stopping the Local Server (Important — Read This)

**The short answer:** press `Ctrl + C` in the terminal where the server is running.

**The full picture — why it matters:**

`python3 -m http.server` is a **development-only tool**. It serves every file in your project folder to anyone who can reach your machine on port 8000. On your home laptop with a normal firewall this is fine — only your own browser connects. But there are two situations where you must stop it:

| Situation | Risk | What to do |
|---|---|---|
| You're on a public/shared Wi-Fi (café, airport, office) | Other people on the same network can browse your files | Stop the server before joining the network, or pass `--bind 127.0.0.1` (see below) |
| You walked away and forgot it's running | Low risk at home; medium risk on shared networks | Stop it when not actively using it |

**Always use the `--bind` flag to be safe:**

```bash
# Binds to localhost ONLY — no other device on the network can reach it
python3 -m http.server 8000 --bind 127.0.0.1
```

**How to kill a forgotten server:**

```bash
# macOS / Linux — find the process
lsof -i :8000
# Output shows PID (process ID), e.g. "Python  12345 ..."
kill 12345

# Windows (PowerShell or Command Prompt)
netstat -ano | findstr :8000
# Note the PID in the last column, then:
taskkill /PID 12345 /F
```

**Rule of thumb:** treat this server like leaving your front door open. Fine inside your house, not fine in a hotel lobby.

---

## Features

| Feature | How it works |
|---|---|
| **Real-time search** | Type in the sidebar — filters sections and TOC simultaneously (120 ms debounce) |
| **Expand / Collapse all** | Toggle button in the header opens or closes every `<details>` element at once |
| **Active section highlight** | `IntersectionObserver` watches headings and highlights the matching TOC link as you scroll |
| **Deep links** | Any section has a stable URL anchor, e.g. `#s-7-4-1-1`; the page auto-opens collapsed ancestors on load |
| **Back to top** | Floating button appears after 400 px of scroll |
| **Keyboard navigation** | Tab through skip link → chips → search → TOC → content; full screen-reader support |

---

## How to Use the Site

**Sidebar (left)**
- Search box — type any keyword to filter both the TOC and the main content
- Track chips — jump straight to Track A (evergreen) or Track B (current)
- Table of Contents — three-level: Track → `Roman — Part Title` → `N. Section`. Click to jump; active section highlights as you scroll

**Main content (centre)**
- Read straight through, or jump via TOC or search
- Every `<details>` element is collapsible — click the `▸` triangle to expand/collapse individual branches
- Use the header's **Expand all** button to open everything at once

**Header**
- Centred Atari-style title (amber phosphor glow, monospace, uppercase)
- **Track A / Track B** chips for quick jumps
- **Expand all** toggle

**Floating button (bottom-right)**
- **↑ Top** — appears once you scroll 400 px down

---

## Architecture

```
HTML (194 KB)           → all content inlined; no external JSON or API calls
CSS  (  5 KB)           → CSS custom properties, Grid, Flexbox, print stylesheet
JS   (  4 KB)           → vanilla ES6+; no framework; no build step required
Total payload ≈ 203 KB  → ~50–60 KB gzipped
```

**Semantic HTML5 elements used:** `<header>`, `<nav>`, `<main>`, `<aside>`, `<section>`, `<details>`, `<summary>`, headings `<h2>`–`<h6>`

**Accessibility (WCAG AA):**
- Skip link, `lang="en"`, `aria-label`, `aria-pressed`, `aria-current="location"`
- 2 px focus ring on all interactive elements
- `prefers-reduced-motion` respected (no smooth-scroll for users who opt out)
- Color contrast ≥ 4.5 : 1 (muted text uses `#a0a0a0`, not `#858585`)

**Responsive breakpoints:**
- ≥ 900 px — two columns: sticky sidebar (300 px) + content
- 600–900 px — single column, sidebar becomes a scrollable drawer
- < 600 px — compact spacing and typography

---

## Colour Palette (VS Code Dark+)

```css
--bg:         #1e1e1e   /* editor background      */
--sidebar-bg: #252526   /* sidebar / topbar        */
--text:       #d4d4d4   /* primary text            */
--muted:      #a0a0a0   /* dimmed text (WCAG AA)   */
--accent:     #569cd6   /* keywords / part titles  */
--accent-2:   #4ec9b0   /* functions / track links */
--warn:       #ce9178   /* Track B warning colour  */
--focus:      #007acc   /* focus ring              */
```

The Atari header uses `#ffb000` (amber phosphor) with a layered `text-shadow` glow — purely CSS, no images.

---

## Regenerating Content

If you modify `genai-roadmap.md`, regenerate the site in order:

```bash
# 1. Convert markdown structure to HTML skeleton
python3 tools/convert_markdown.py

# 2. Fill all 805 {{SUMMARY_*}} placeholders
python3 tools/generate_summaries.py

# 3. Fix TOC nesting, preamble rendering, and structural clean-ups
python3 tools/fix_issues.py

# 4. Verify everything passes
python3 tools/audit.py
```

All four scripts must complete with `[OK]` and zero placeholder errors before committing.

---

## Deploy to GitHub Pages

1. Push this repo to GitHub (already done — repo is private)
2. Go to **Settings → Pages**
3. Set **Source** to `master` branch, root folder
4. Click **Save** — the site goes live in ≈ 60 seconds at:
   `https://<github-username>.github.io/GenAI-self-course/`

No build step, no server config, nothing else needed. Static files deploy as-is.

---

## Known Limitations

- **Track B is time-sensitive** — Parts XVI–XIX describe models and tools current as of 2025–2026. Plan to refresh annually.
- **No backend** — static HTML only; no accounts, personalisation, or analytics.
- **No service worker** — the site is browser-cacheable but has no offline mode. Save the HTML file locally if you need offline access.

---

## Verification

124 automated tests across four categories — all passing:

| Category | Tests | Status |
|---|---|---|
| Structure & Content | 30 | ✅ |
| Functionality | 45 | ✅ |
| Accessibility | 18 | ✅ |
| Performance & Security | 31 | ✅ |

Run `python3 tools/audit.py` at any time to recheck.

---

**Built with:** Plain HTML + CSS + JavaScript  
**Tested on:** Chrome, Firefox, Edge, Safari (latest stable)  
**Accessibility:** WCAG AA compliant  
**Last updated:** 2026-04-24
