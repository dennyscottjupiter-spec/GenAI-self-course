# Implementation Plan — GenAI Roadmap Summary Website

> **TL;DR** — Build a static website (plain `index.html` + `styles.css` + `script.js`) that renders a large GenAI learning roadmap as a browsable, searchable outline where every header and sub-header has a 1–3 sentence summary. VS Code Dark+ styling. No frameworks, no build step. Content is inlined into the HTML. Estimated effort: **3–5 focused days** for a junior developer.

---

## 0. How to use this document

This plan is written for a **junior front-end developer** who will implement the entire project solo. It is structured as **sequential phases** — each phase has:

1. **Goal** — one line on what you're producing.
2. **Steps** — numbered, specific, copy-paste-ready where possible.
3. **Pitfalls** — things that commonly go wrong. Read *before* starting the phase, not after debugging.
4. **✅ Acceptance check** — exact things to verify before moving on. Do **not** skip these.

**Rules of engagement:**
- Do not introduce any tool, library, or framework not listed here.
- Do not split files beyond the three named outputs (`index.html`, `styles.css`, `script.js`).
- Commit at the end of each phase (see §12 Git workflow).
- If a step seems ambiguous, pick the most obvious option, note your assumption as a one-line comment in the file, and keep moving.

---

## 1. Glossary (one-line definitions)

Read this once. You will see these terms throughout the plan.

- **TOC (Table of Contents)** — the clickable list of sections in the left sidebar.
- **Semantic HTML** — using elements like `<header>`, `<nav>`, `<main>`, `<section>` instead of generic `<div>`s, so assistive tech and search engines understand the structure.
- **`<details>` / `<summary>`** — native HTML collapsible widget. No JS needed to toggle.
- **CSS custom properties (CSS variables)** — values declared once (`--bg: #1e1e1e;`) and reused everywhere (`background: var(--bg);`).
- **IntersectionObserver** — browser API that tells you when an element scrolls into or out of view. Used to highlight the TOC entry for the section you're currently reading.
- **Debounce** — delaying a function until the user stops typing for N ms, so search doesn't run on every keystroke.
- **`aria-current`** — accessibility attribute marking the currently active nav item.
- **WCAG AA** — web accessibility standard. We only need contrast ≥ 4.5:1 for text.
- **Deep link** — a URL with `#section-id` that jumps straight to a heading on page load.
- **Dark+ theme** — the default dark theme in VS Code; we're copying its color palette.
- **Monospace / sans-serif stack** — a CSS `font-family` list of system-installed fonts, so we never load external fonts.
- **`prefers-reduced-motion`** — OS-level user preference; if set, we disable smooth-scroll animations.

---

## 2. What you are building (high-level overview)

A single-page static website with:

- **Top bar:** site title, two "jump chips" (Track A / Track B), Collapse-All / Expand-All toggle.
- **Left sidebar (sticky):** search box + TOC listing 19 Parts and 95 numbered sections. The active section is highlighted as you scroll.
- **Main column:** the full roadmap rendered as nested `<section>` blocks. Each numbered node (Part, section, sub-section, leaf) has a short summary paragraph directly under it.
- **Floating "↑ Top" button** bottom-right.
- **Responsive:** two columns on desktop, collapses to a single column with a drawer-style TOC below ~900px.
- **Palette:** VS Code Dark+ colors (exact hex codes in §7).
- **Zero dependencies:** no npm, no bundler, no CDN, no external font.

**File layout (final state, all at repo root):**

```
.
├── PLAN.md                 ← this file
├── genai-roadmap.md        ← source roadmap outline (already in the repo — see Phase 0)
├── index.html              ← the whole site content + markup
├── styles.css              ← all styling
├── script.js               ← all interactivity
└── README.md               ← short description, how to open locally (optional, nice-to-have)
```

---

## 3. Prerequisites

Before writing any code:

1. **Tools installed on your machine:**
   - A modern browser (Chrome, Firefox, or Edge — latest stable).
   - A text editor (VS Code recommended).
   - Python 3 on PATH (the repo's environment has `python3` — verify with `python3 --version`).
   - Git (verify with `git --version`).
2. **Access to an LLM for content generation** — ChatGPT, Claude, Gemini, or any equivalent. You will use it in Phase 3 to batch-generate summaries. A paid tier is not required; free tiers work.
3. **Cloned repo** and a working branch. Confirm you are in the right directory:
   ```bash
   pwd           # should end with /GenAI-self-course
   git status    # should show you're on your working branch
   ```

---

## 4. Phase 0 — Understand the source roadmap

**Goal:** read `genai-roadmap.md` (already at the repo root) and understand its exact structure, because Phase 2's HTML conversion depends on parsing it correctly.

### The file's actual structure

Open `genai-roadmap.md` and confirm this shape. You will rely on it literally.

| Markdown element | What it means | Example |
|---|---|---|
| `# 🧠 The Complete Generative AI Roadmap` | The document title (h1, once) | `# 🧠 The Complete Generative AI Roadmap` |
| `# 🟢 TRACK A — EVERGREEN CORE` | **Track banner** (wraps Parts I–XV) | `# 🟢 TRACK A — EVERGREEN CORE` |
| `# 🔴 TRACK B — CURRENT LANDSCAPE` | **Track banner** (wraps Parts XVI–XIX) | `# 🔴 TRACK B — CURRENT LANDSCAPE` |
| `## Part I — Title` | A Part (Roman-numeral) | `## Part I — What AI Actually Is (And Isn't)` |
| `### 1. Title` | A **level-1 numbered section** (1–95) | `### 1. Defining Intelligence` |
| `- 1.1 Title` | A **level-2 subsection** (bulleted) | `- 1.1 Human intelligence — what it actually does` |
| `  - 1.1.1 Title` | A **level-3 leaf** (nested bullet, 2-space indent) | `  - 1.1.1 Reasoning, memory, perception, learning` |
| `    - 1.1.1.1 Title` | A **level-4 leaf** (nested bullet, 4-space indent) | `    - 7.4.1.1 Query, key, value intuition` |

**Critical takeaway for Phase 2:** only the **document title**, **Track banners**, **Parts**, and **level-1 sections** are markdown headings (`#`, `##`, `###`). Everything below level-1 is a **nested bulleted list**, not a heading. Your parser/LLM conversion must treat them differently.

**Track A ⇢ Parts I–XV**, **Track B ⇢ Parts XVI–XIX** — tracks are structural **wrappers around Parts**, not appendices at the end. In the HTML, each track becomes a container section that holds its Parts.

There is also a short preamble section ("How This Roadmap Is Built") before Track A. Render it once at the top of the main content, above Track A.

### Steps

1. Open `genai-roadmap.md` and skim the first ~100 lines to internalize the pattern above.
2. Sanity-count the structural elements with a quick grep from the repo root:
   ```bash
   grep -c "^## Part " genai-roadmap.md      # should print 19
   grep -cE "^### [0-9]+\. " genai-roadmap.md # should print 95
   grep -c "^# 🟢\|^# 🔴" genai-roadmap.md   # should print 2
   ```
3. Note any deviations in your notebook — if counts don't match, flag to the project owner before continuing.

### Pitfalls

- **Don't assume level-2+ are headings.** They're bullets. Tree-walking a markdown AST or an LLM-based conversion must be configured for mixed heading+list input.
- **Emojis in heading text** (`🧠`, `🟢`, `🔴`) are part of the titles. Strip them for IDs but keep them in the rendered HTML titles — they're part of the author's design.
- **Em-dashes (`—`) and en-dashes (`–`)** appear throughout titles ("Part I — What AI Actually Is"). Preserve exactly; don't substitute hyphens.
- **Encoding:** the file is UTF-8. If you see mojibake (`â€”` instead of `—`), your editor opened it with the wrong encoding. Switch VS Code's encoding to "UTF-8".

### ✅ Acceptance check

- [ ] `genai-roadmap.md` is at the repo root.
- [ ] The three grep counts above print `19`, `95`, `2`.
- [ ] You can point to a level-4 bullet (`- 7.4.1.1 …` or similar) in the file to prove depth-4 exists.

---

## 5. Phase 1 — Scaffold the three files

**Goal:** a minimal, valid site that opens in a browser and shows an empty layout (header + sidebar + main column). No content yet, no real styling — just structure.

### Steps

1. Create `index.html` with this skeleton. It's intentionally minimal; you'll fill it in the next phases.

   ```html
   <!doctype html>
   <html lang="en">
   <head>
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1">
     <meta name="description" content="A summarized, browsable guide to the complete Generative AI learning roadmap.">
     <meta property="og:title" content="The Complete Generative AI Roadmap">
     <title>The Complete Generative AI Roadmap</title>
     <link rel="stylesheet" href="styles.css">
     <script src="script.js" defer></script>
   </head>
   <body>
     <a class="skip-link" href="#main">Skip to main content</a>

     <header class="topbar">
       <h1 class="title">The Complete Generative AI Roadmap</h1>
       <nav class="top-nav" aria-label="Track jumps">
         <a class="chip" href="#track-a">Track A — Evergreen</a>
         <a class="chip" href="#track-b">Track B — Current</a>
       </nav>
       <button id="toggle-all" class="chip" aria-pressed="false">Expand all</button>
     </header>

     <div class="layout">
       <aside class="sidebar" aria-label="Table of contents">
         <div role="search">
           <label for="search" class="visually-hidden">Filter sections</label>
           <input id="search" type="search" placeholder="Search titles and summaries…" autocomplete="off">
         </div>
         <nav id="toc" aria-label="Roadmap sections">
           <!-- TOC list injected by Phase 2 -->
         </nav>
       </aside>

       <main id="main" class="content">
         <!-- Roadmap content injected by Phase 2 -->
       </main>
     </div>

     <button id="back-to-top" class="fab" aria-label="Back to top" hidden>↑ Top</button>
   </body>
   </html>
   ```

2. Create `styles.css` with just enough to see the layout:

   ```css
   :root {
     --bg: #1e1e1e;
     --sidebar-bg: #252526;
     --border: #333;
     --text: #d4d4d4;
     --muted: #a0a0a0;     /* NOTE: brighter than VS Code's #858585 to pass WCAG AA on body text */
     --accent: #569cd6;
     --accent-2: #4ec9b0;
     --warn: #ce9178;
     --link-hover: #9cdcfe;
     --focus: #007acc;
     --mono: "Cascadia Code", "Fira Code", Consolas, "JetBrains Mono", monospace;
     --sans: "Segoe UI", system-ui, -apple-system, sans-serif;
   }
   * { box-sizing: border-box; }
   html, body { margin: 0; padding: 0; background: var(--bg); color: var(--text); font-family: var(--sans); }
   .visually-hidden { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); }
   .layout { display: grid; grid-template-columns: 280px 1fr; min-height: 100vh; }
   .sidebar { background: var(--sidebar-bg); border-right: 1px solid var(--border); padding: 1rem; position: sticky; top: 0; height: 100vh; overflow-y: auto; }
   .content { padding: 1.5rem 2rem; max-width: 960px; }
   ```

3. Create `script.js` with a single placeholder line:

   ```js
   // Interactivity is wired up in Phase 5.
   console.log("GenAI Roadmap site loaded.");
   ```

4. Start a local server and open the page:
   ```bash
   python3 -m http.server 8000
   ```
   Visit `http://localhost:8000` in your browser.

### Pitfalls

- **Opening `index.html` directly via `file://`** works for this site, but some browsers restrict certain JS APIs. Always use `python3 -m http.server` while developing so you catch issues early.
- **`defer` on the script tag is non-negotiable.** Without it, the script runs before the DOM exists and every `document.querySelector` returns `null`.
- **File encoding on Windows:** if special characters (↑, —, é) render as garbage, your file isn't UTF-8. Re-save with "UTF-8 without BOM" in VS Code.

### ✅ Acceptance check

- [ ] Visiting `localhost:8000` shows a dark page with a title, two chips, an "Expand all" button, an empty sidebar with a search box, and an empty main area.
- [ ] DevTools console shows `"GenAI Roadmap site loaded."` and **no errors**.
- [ ] Tab key moves focus through: skip link → chips → Expand-all button → search input.

---

## 6. Phase 2 — Render the roadmap skeleton (structure only, no summaries yet)

**Goal:** every node from `genai-roadmap.md` exists in `index.html` as real markup, with stable IDs, in the correct nesting. Summaries are still empty placeholders — they are filled in Phase 3.

### Output HTML pattern (memorize this)

```html
<!-- Track banner wraps its Parts -->
<section class="track" id="track-a">
  <h2 class="track-title">🟢 Track A — Evergreen Core</h2>
  <p class="summary">{{SUMMARY_track-a}}</p>

  <!-- A Part inside the track -->
  <section class="part" id="part-i">
    <h3><span class="numprefix">I</span> What AI Actually Is (And Isn't)</h3>
    <p class="summary">{{SUMMARY_part-i}}</p>

    <!-- A level-1 section inside the Part -->
    <section class="sec lvl-1" id="s-1">
      <h4><span class="numprefix">1.</span> Defining Intelligence</h4>
      <p class="summary">{{SUMMARY_s-1}}</p>

      <!-- A level-2 subsection (was "- 1.1 …" in the markdown), open by default -->
      <details class="sec lvl-2" id="s-1-1" open>
        <summary><h5><span class="numprefix">1.1</span> Human intelligence — what it actually does</h5></summary>
        <p class="summary">{{SUMMARY_s-1-1}}</p>

        <!-- A level-3 leaf (was "  - 1.1.1 …"), closed by default -->
        <details class="sec lvl-3" id="s-1-1-1">
          <summary><h6><span class="numprefix">1.1.1</span> Reasoning, memory, perception, learning</h6></summary>
          <p class="summary">{{SUMMARY_s-1-1-1}}</p>
        </details>

        <!-- A level-4 leaf (was "    - 7.4.1.1 …") — same pattern, id has four segments -->
        <!-- <details class="sec lvl-4" id="s-7-4-1-1"> … </details> -->
      </details>
    </section>
  </section>
  <!-- …more Parts… -->
</section>

<section class="track warn" id="track-b">
  <h2 class="track-title">🔴 Track B — Current Landscape</h2>
  <div class="warn-banner">Track B is time-sensitive — refresh yearly. Summaries describe categories, not specific models or versions.</div>
  <p class="summary">{{SUMMARY_track-b}}</p>
  <!-- …Parts XVI–XIX nested here… -->
</section>
```

**ID rules:**
- Track banners: `track-a`, `track-b`.
- Parts: `part-{roman-lowercase}` (e.g., `part-i`, `part-xiv`).
- Numbered nodes: `s-{N}` → `s-{N}-{M}` → `s-{N}-{M}-{P}` → `s-{N}-{M}-{P}-{Q}` — dots replaced by hyphens.

**Heading level rules:** `<h2>` for track banners, `<h3>` for Parts, `<h4>` for level-1 sections, `<h5>` for level-2, `<h6>` for level-3 and level-4 (HTML only goes up to `<h6>`, so levels 3 and 4 share it — they're still visually distinguished by nesting depth and CSS).

### Steps

1. **Preamble block.** Copy the "How This Roadmap Is Built" section from `genai-roadmap.md` verbatim into the top of `<main>` as plain markup (one `<h2>` plus a short `<p>`). No numbering, no placeholder — it's a one-off intro, not a summarized node.

2. **Convert the roadmap body with an LLM** — this is the main conversion. Paste the **entire** `genai-roadmap.md` (or a full Track at a time if truncation happens) into this prompt:

   > **LLM prompt — "Convert roadmap markdown to HTML skeleton":**
   > ```
   > Convert the markdown roadmap below into nested HTML following EXACTLY the pattern in PLAN.md §6. Read these rules literally — the input mixes headings AND nested bullets, and each level maps to a specific HTML element.
   >
   > Input-to-output mapping:
   > - "# 🟢 TRACK A — EVERGREEN CORE"         → open <section class="track" id="track-a"> with <h2 class="track-title">…</h2> and a <p class="summary">{{SUMMARY_track-a}}</p>. Close it only after all its Parts (I–XV) are rendered inside.
   > - "# 🔴 TRACK B — CURRENT LANDSCAPE"       → open <section class="track warn" id="track-b"> with <h2 class="track-title">…</h2>, then a <div class="warn-banner">…yearly refresh warning…</div>, then <p class="summary">{{SUMMARY_track-b}}</p>. Close after Parts XVI–XIX.
   > - "## Part {ROMAN} — {Title}"              → <section class="part" id="part-{roman-lowercase}"> with <h3><span class="numprefix">{ROMAN}</span> {Title}</h3> and <p class="summary">{{SUMMARY_part-{roman-lowercase}}}</p>.
   > - "### {N}. {Title}"                       → <section class="sec lvl-1" id="s-{N}"> with <h4><span class="numprefix">{N}.</span> {Title}</h4> and <p class="summary">{{SUMMARY_s-{N}}}</p>.
   > - "- {N}.{M} {Title}"  (a top-level bullet under a level-1 section)
   >                                            → <details class="sec lvl-2" id="s-{N}-{M}" open> with <summary><h5><span class="numprefix">{N}.{M}</span> {Title}</h5></summary> and <p class="summary">{{SUMMARY_s-{N}-{M}}}</p>. Open by default.
   > - "  - {N}.{M}.{P} {Title}"  (bullet indented 2 spaces)
   >                                            → <details class="sec lvl-3" id="s-{N}-{M}-{P}"> with <summary><h6><span class="numprefix">{N}.{M}.{P}</span> {Title}</h6></summary> and <p class="summary">{{SUMMARY_s-{N}-{M}-{P}}}</p>. NOT open by default.
   > - "    - {N}.{M}.{P}.{Q} {Title}"  (bullet indented 4 spaces)
   >                                            → <details class="sec lvl-4" id="s-{N}-{M}-{P}-{Q}"> with <summary><h6><span class="numprefix">{N}.{M}.{P}.{Q}</span> {Title}</h6></summary> and <p class="summary">{{SUMMARY_s-{N}-{M}-{P}-{Q}}}</p>. NOT open by default.
   >
   > Hard constraints:
   > - Keep emojis inside heading text; strip them from IDs.
   > - Preserve em-dashes (—) and en-dashes (–) exactly as they appear.
   > - Escape &, <, > inside title text as &amp;, &lt;, &gt;.
   > - Do NOT write real summary text — emit the literal "{{SUMMARY_<id>}}" placeholders exactly.
   > - The document's top-level "# 🧠 The Complete Generative AI Roadmap" and the "How This Roadmap Is Built" section are NOT part of this conversion — they are handled separately.
   > - Close every <section> and <details> properly. Track A closes before Track B opens.
   >
   > Output ONLY the HTML, no commentary, no code fences.
   >
   > Markdown input:
   > <paste genai-roadmap.md here, starting from "# 🟢 TRACK A — EVERGREEN CORE">
   > ```

   Paste the result into `index.html` between `<main id="main" class="content">` and `</main>`, after the preamble block from step 1.

3. **Generate the TOC.** Second prompt:

   > **LLM prompt — "Build the sidebar TOC":**
   > ```
   > Build a two-level sidebar TOC from the same roadmap. Output one outer <ul>. Structure:
   >
   > <ul>
   >   <li class="toc-track"><a href="#track-a">🟢 Track A — Evergreen Core</a>
   >     <ul>
   >       <li class="toc-part"><a href="#part-i">Part I — What AI Actually Is (And Isn't)</a>
   >         <ul>
   >           <li><a href="#s-1">1. Defining Intelligence</a></li>
   >           <li><a href="#s-2">2. Types of AI Systems</a></li>
   >           <!-- …every level-1 section inside Part I… -->
   >         </ul>
   >       </li>
   >       <!-- …every Part in Track A… -->
   >     </ul>
   >   </li>
   >   <li class="toc-track"><a href="#track-b">🔴 Track B — Current Landscape</a>
   >     <!-- …Parts XVI–XIX with their level-1 sections… -->
   >   </li>
   > </ul>
   >
   > Do NOT include level-2+ (bulleted) nodes — the TOC only goes three levels: Track → Part → level-1 section. Output only the <ul>, no commentary.
   > ```

   Paste into the `<nav id="toc">` block.

4. **Update the topbar chips** in `index.html` to point to the track IDs (already done in the Phase 1 skeleton: `href="#track-a"` and `href="#track-b"`). Confirm they still match.

5. **Reload the page.** You should see the full outline with `{{SUMMARY_…}}` placeholders and a full two-level TOC.

### Pitfalls

- **LLMs merge adjacent bullets into single `<li>` blocks.** After pasting, grep for `{{SUMMARY_s-` and count — should be ≈ number of numbered nodes. If off by more than ~5%, re-run the conversion with a smaller batch (one Track at a time).
- **Mismatched `<details>` / `<section>` nesting.** If the page looks visually broken, a closing tag is missing. Browsers don't error — they render nonsense. Use VS Code's tag-match (`Ctrl+Shift+P` → "Go to Matching Pair").
- **Bullet indentation inconsistency.** The roadmap uses 2-space indent per level. If the LLM sees tab-indent or 4-space, it will mis-classify levels. Before pasting, verify in VS Code that indents are 2-space.
- **The emoji in Track B's banner** (`🔴`) is intentional — preserve it. The warning banner text must mention the yearly-refresh caveat.
- **Level-4 rarity.** Not every level-1 section has level-4 bullets. Don't force them where the markdown has none.

### ✅ Acceptance check

- [ ] The page shows **two track banners** (🟢 Track A and 🔴 Track B), each wrapping its Parts.
- [ ] **Part I** sits inside Track A; **Part XVI** sits inside Track B.
- [ ] At least one level-4 leaf (e.g., `s-7-4-1-1`) exists in the DOM — check with `document.getElementById('s-7-4-1-1')` in DevTools.
- [ ] Sidebar TOC has three levels: Track → Part → level-1 section.
- [ ] Clicking any TOC entry jumps to the matching section (scroll may be abrupt — smoothing comes in Phase 5).
- [ ] `document.querySelectorAll('.summary').length` matches the count of `{{SUMMARY_` occurrences in the HTML source.
- [ ] No mojibake anywhere (no `â€"` etc.).

---

## 7. Phase 3 — Generate and insert summaries with an LLM

**Goal:** every `{{SUMMARY_<id>}}` placeholder is replaced with a real 1–3 sentence summary following these depth-based length rules:

| Node type | Length |
|---|---|
| Part (I–XIX) | 2–3 sentences intro |
| Level-1 section (1–95) | 2–3 sentences |
| Level-2 subsection (1.1, 1.2) | 1–2 sentences |
| Level-3 / Level-4 leaf (1.1.1, 7.4.1.1) | 1 concise sentence |

### Steps

1. **Batch the work.** You have ~600 nodes. Process them in chunks of ~40 nodes at a time to stay inside LLM context windows.

2. **Use this prompt template** for every batch. Paste one Part (or half a Part) at a time:

   > **LLM prompt — "Generate summaries":**
   > ```
   > You are writing short educational summaries for a Generative AI learning roadmap. For each numbered heading below, write a plain-prose summary following these rules:
   >
   > - Parts (Roman numerals): 2–3 sentences giving the thematic arc of this Part.
   > - Level-1 sections (N.): 2–3 sentences — what the topic is and why it matters for GenAI.
   > - Level-2 subsections (N.M): 1–2 sentences — the specific concept and how it ties to the parent.
   > - Level-3 / Level-4 leaves (N.M.P, N.M.P.Q): exactly 1 sentence — crisp, concrete, the single idea.
   >
   > Constraints:
   > - No references to external sources, books, or courses.
   > - No filler phrases like "In this section, we'll explore…".
   > - Plain text only — no markdown, no code, no bullet points.
   > - Do NOT hedge Track B as "current" — describe the *category* (e.g., "frontier frontier-model families"), not specific model versions.
   >
   > Output format: one line per heading, exactly in this form:
   >   {id} || {summary}
   > Example:
   >   s-1-1-1 || The dot product measures how aligned two vectors are and underlies similarity, projection, and attention scores.
   >
   > Here are the headings (format: id :: heading text):
   > <paste batch here>
   > ```

3. **Generate the input list** once, from your HTML. In DevTools console:

   ```js
   copy(Array.from(document.querySelectorAll('section[id], details[id]'))
     .map(n => n.id + ' :: ' + n.querySelector('h2, h3, h4, h5, h6')?.innerText.trim())
     .join('\n'));
   ```

   This copies `id :: title` pairs to your clipboard. Paste into the prompt in chunks.

4. **Insert summaries back into `index.html`.** Easiest method: a tiny find-and-replace script. Paste in DevTools, or better, run as a one-off Node/Python script on the raw HTML file:

   ```python
   # tools/apply_summaries.py  (create, run once, delete)
   import re, pathlib, sys
   html = pathlib.Path("index.html").read_text(encoding="utf-8")
   for line in pathlib.Path("summaries.txt").read_text(encoding="utf-8").splitlines():
       if "||" not in line: continue
       sid, text = [s.strip() for s in line.split("||", 1)]
       placeholder = "{{SUMMARY_" + sid + "}}"
       if placeholder not in html:
           print(f"WARN: no placeholder for {sid}", file=sys.stderr)
       html = html.replace(placeholder, text)
   pathlib.Path("index.html").write_text(html, encoding="utf-8")
   print("Done. Unreplaced placeholders:", html.count("{{SUMMARY_"))
   ```

   Save all LLM outputs concatenated into `summaries.txt`, run `python3 tools/apply_summaries.py`, and verify the script reports `0` unreplaced placeholders.

5. **Spot-check 10 random summaries** for accuracy and tone. Rewrite any that are vague, off-topic, or hedge about specific products.

### Pitfalls

- **LLMs occasionally echo the placeholder `{{SUMMARY_…}}` back.** After insertion, grep for `{{SUMMARY` in the HTML — must be zero matches.
- **Summary length drift.** LLMs tend to over-write. If leaves are two sentences, send the batch back with: *"Rewrite every entry starting with `s-*-*-*` as exactly one sentence."*
- **Encoding/quotes.** Smart quotes (`"` vs `"`) and em-dashes can corrupt if your encoding isn't UTF-8. Re-save after insertion.
- **HTML escaping.** If a summary contains `<`, `>`, or `&`, escape them (`&lt;`, `&gt;`, `&amp;`). The apply script does not escape automatically — prompt the LLM to avoid these characters.
- **Token cost.** If you use a paid API, batch size matters. 40-node batches at ~20k tokens each totalling ~15 batches is well within a free ChatGPT / Claude session.

### ✅ Acceptance check

- [ ] Search the repo for `{{SUMMARY` — zero results.
- [ ] Every `<p class="summary">` has non-empty text.
- [ ] A random sample of 10 summaries reads like plain informative prose (not marketing, not academic hedging).
- [ ] Track B's summary and banner both mention the yearly-refresh caveat.

---

## 8. Phase 4 — Full VS Code Dark+ styling

**Goal:** the site visually matches VS Code's Dark+ theme and reads comfortably on any screen size ≥ 360px wide.

### Complete `styles.css` reference

Use this as the authoritative starting point, replacing the placeholder CSS from Phase 1:

```css
:root {
  /* Palette */
  --bg:          #1e1e1e;
  --sidebar-bg:  #252526;
  --panel:       #1e1e1e;
  --border:      #333;
  --text:        #d4d4d4;
  --muted:       #a0a0a0;
  --accent:      #569cd6;   /* keywords/types blue */
  --accent-2:    #4ec9b0;   /* functions/class teal */
  --warn:        #ce9178;   /* string orange — used for Track B banner */
  --link-hover:  #9cdcfe;
  --focus:       #007acc;

  /* Fonts */
  --mono: "Cascadia Code", "Fira Code", Consolas, "JetBrains Mono", monospace;
  --sans: "Segoe UI", system-ui, -apple-system, Roboto, "Helvetica Neue", sans-serif;
}

/* Reset */
*, *::before, *::after { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body { background: var(--bg); color: var(--text); font-family: var(--sans); line-height: 1.55; }

/* Skip link */
.skip-link { position: absolute; left: -9999px; top: 0; background: var(--focus); color: #fff; padding: .5rem 1rem; z-index: 100; }
.skip-link:focus { left: .5rem; top: .5rem; }

.visually-hidden { position: absolute !important; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }

/* Top bar */
.topbar { display: flex; gap: 1rem; align-items: center; padding: .75rem 1rem; background: var(--sidebar-bg); border-bottom: 1px solid var(--border); position: sticky; top: 0; z-index: 10; }
.title { font-size: 1rem; margin: 0; color: var(--accent); font-weight: 600; }
.top-nav { display: flex; gap: .5rem; margin-left: auto; }
.chip { background: transparent; color: var(--text); border: 1px solid var(--border); padding: .25rem .75rem; border-radius: 999px; font-size: .85rem; text-decoration: none; cursor: pointer; font-family: inherit; }
.chip:hover { border-color: var(--accent); color: var(--link-hover); }

/* Layout */
.layout { display: grid; grid-template-columns: 300px minmax(0, 1fr); }
.sidebar { background: var(--sidebar-bg); border-right: 1px solid var(--border); padding: 1rem; position: sticky; top: 49px; height: calc(100vh - 49px); overflow-y: auto; }
.content { padding: 1.5rem 2rem 4rem; max-width: 960px; }

/* Sidebar search */
#search { width: 100%; background: var(--panel); color: var(--text); border: 1px solid var(--border); padding: .5rem; font-family: inherit; }
#search:focus { outline: 1px solid var(--focus); border-color: var(--focus); }

/* TOC */
#toc ul { list-style: none; margin: .5rem 0; padding: 0; }
#toc ul ul { padding-left: .75rem; border-left: 1px solid var(--border); }
#toc a { display: block; padding: .25rem .5rem; color: var(--text); text-decoration: none; border-left: 2px solid transparent; font-size: .9rem; }
#toc a:hover { background: #2a2d2e; color: var(--link-hover); }
#toc a[aria-current="location"] { border-left-color: var(--accent); background: #2a2d2e; color: var(--link-hover); }
#toc .part-title { margin-top: .75rem; color: var(--accent-2); font-family: var(--mono); font-size: .85rem; text-transform: uppercase; letter-spacing: .05em; }

/* Content headings */
.content h2, .content h3, .content h4, .content h5, .content h6 { color: var(--accent); scroll-margin-top: 70px; /* clears sticky topbar when jumping */ }
.content h2 { border-bottom: 1px solid var(--border); padding-bottom: .25rem; margin-top: 2rem; }
.numprefix { font-family: var(--mono); color: var(--muted); margin-right: .5rem; font-weight: 500; }
.summary { color: var(--text); margin: .25rem 0 1rem; }

/* Sections */
.sec { margin: .5rem 0; }
.sec.lvl-2, .sec.lvl-3 { border-left: 1px solid var(--border); padding-left: .75rem; }
details > summary { cursor: pointer; list-style: none; }
details > summary::-webkit-details-marker { display: none; }
details > summary::before { content: "▸ "; color: var(--muted); font-family: var(--mono); }
details[open] > summary::before { content: "▾ "; }
details > summary h4, details > summary h5, details > summary h6 { display: inline; }

/* Track B warning */
#track-b .warn-banner { background: #3a2d22; border-left: 3px solid var(--warn); color: var(--warn); padding: .5rem .75rem; margin: .5rem 0 1rem; font-size: .9rem; }

/* Focus visibility */
:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; }

/* Back to top */
.fab { position: fixed; right: 1rem; bottom: 1rem; background: var(--sidebar-bg); color: var(--text); border: 1px solid var(--border); padding: .5rem .75rem; border-radius: 6px; cursor: pointer; font-family: inherit; }
.fab:hover { border-color: var(--accent); color: var(--link-hover); }
.fab[hidden] { display: none; }

/* Highlight (for search matches) */
mark { background: #515c6a; color: #fff; padding: 0 2px; border-radius: 2px; }

/* Responsive */
@media (max-width: 900px) {
  .layout { grid-template-columns: 1fr; }
  .sidebar { position: static; height: auto; max-height: 50vh; border-right: none; border-bottom: 1px solid var(--border); }
  .topbar { flex-wrap: wrap; }
}
@media (max-width: 600px) {
  .content { padding: 1rem; }
  .title { font-size: .95rem; }
  .chip { font-size: .8rem; padding: .2rem .6rem; }
}

/* Reduced motion */
@media (prefers-reduced-motion: no-preference) {
  html { scroll-behavior: smooth; }
}

/* Print: open every details so printed output includes all content */
@media print {
  .sidebar, .topbar, .fab { display: none; }
  details { display: block; } details > summary { list-style: none; }
  details > summary::before { content: ""; }
  details:not([open]) > *:not(summary) { display: block !important; }
}
```

### Pitfalls

- **Sticky topbar hiding section headings when you scroll-to-anchor.** The `scroll-margin-top: 70px` on `.content h2…h6` fixes this. If you change the topbar height, change this number too.
- **`scroll-behavior: smooth` on `html`** is gated behind `prefers-reduced-motion: no-preference` so OS-level reduced-motion users get snaps, not animations.
- **Custom `<summary>` marker:** hiding the default disclosure triangle requires both `list-style: none` *and* `::-webkit-details-marker { display: none; }` for Safari.
- **Muted color `#858585`** from VS Code is too dim on `#1e1e1e` for body prose (fails AA at ~4.58:1 for small text). We bumped to `#a0a0a0` for any *text* use. Keep `#858585` only if you use it for decorative labels in large type.

### ✅ Acceptance check

- [ ] All colors match the palette; no blue links, no default browser styling leaking through.
- [ ] Headings have hex-colored numeric prefixes in monospace font.
- [ ] Track B shows a visible orange warning banner.
- [ ] Resize the window to 800px, 600px, 400px — layout stays usable at every breakpoint.
- [ ] Print preview (`Ctrl+P`) shows the full content expanded and the sidebar hidden.

---

## 9. Phase 5 — Interactivity (`script.js`)

**Goal:** `script.js` wires up five behaviors: active-section highlight, search, expand/collapse-all, back-to-top, and hash-based deep-link sync.

### Complete `script.js` reference

```js
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
```

### Pitfalls

- **IntersectionObserver noise.** With many sections intersecting, multiple entries fire per event. The code above picks the topmost currently visible one. Don't replace this logic with a simple "last-seen" pattern — it flickers.
- **Search hiding orphan parents.** If a match is deep, you must un-hide every ancestor section *and* every ancestor `<li>` in the TOC. The reference code does this; removing the ancestor-walk breaks it.
- **Deep-link into collapsed `<details>`.** A bookmark like `#s-7-4-1-1` points at a node inside closed collapsibles. The Phase-5 script auto-opens all ancestors on load. Do not remove that block.
- **Listening to `scroll` without `{ passive: true }`.** Causes jank on mobile. Always pass the option.
- **`aria-current` on TOC** must be `"location"` (not `"page"` or `"true"`). Screen readers announce "current location" which matches our nav semantics.

### ✅ Acceptance check

- [ ] Scrolling through the page: the TOC entry for the section at the top of the viewport is highlighted and updates as you scroll.
- [ ] Typing `"attention"` in search filters both sidebar and main content to matching entries within ~150 ms.
- [ ] Clicking "Expand all" opens every `<details>`; clicking again collapses them. Button label flips.
- [ ] Opening `localhost:8000/#s-7-4-1-1` scrolls straight to section `7.4.1.1` with its ancestors open.
- [ ] Scrolling down reveals the `↑ Top` button; it scrolls back to top on click.
- [ ] DevTools console: no errors on load or during any interaction.

---

## 10. Phase 6 — Accessibility polish

**Goal:** a keyboard-only user and a screen-reader user can use the entire site comfortably.

### Steps

1. **Tab through the page once, top to bottom.** In order, focus must land on:
   1. Skip link (visible top-left).
   2. Each Track chip.
   3. Expand-all button.
   4. Search input.
   5. Every TOC link (in order).
   6. Every `<summary>` in the main content (they are natively focusable).

2. **Activate the skip link** → focus jumps into main content.

3. **Enter / Space on a `<summary>`** → it toggles the disclosure.

4. **Check focus rings.** Every focusable element shows a 2px blue outline (`:focus-visible`). If you see none, CSS is broken.

5. **Screen reader spot-check** (optional, skip if no tool available): NVDA on Windows or VoiceOver on Mac. Navigate by heading (H key) and confirm headings are announced with correct levels (h1 → h2 → h3 → …).

6. **Contrast audit.** Open DevTools → Lighthouse → Accessibility. Run. Target score ≥ 95. Fix any contrast issues it flags by nudging colors in the `:root` block.

### Pitfalls

- **Focus trap inside `<details>`.** Never add `tabindex="-1"` to headings; they should not be focusable at all. Only interactive controls get focus.
- **Missing `lang="en"`** on `<html>` — screen readers use this to pick pronunciation. Phase 1 template includes it; don't remove.
- **Empty `<a>` or `<button>`.** Every TOC link must have text content inside it. No icon-only navigation.

### ✅ Acceptance check

- [ ] Lighthouse Accessibility score ≥ 95.
- [ ] Tab order is logical and every control has a visible focus ring.
- [ ] Every heading is a real `<h2>…<h6>` (no fake headings made from `<div>`).

---

## 11. Phase 7 — Final verification

Run through every item below. Do not commit the final version until all boxes are checked.

### Visual QA
- [ ] Dark VS Code palette consistently applied, no light flashes on load.
- [ ] Track B banner is visible and orange.
- [ ] All 19 Parts and 95 level-1 sections present and numbered continuously.
- [ ] Deep leaves like `7.4.1.1` have summaries when expanded.

### Functional QA
- [ ] Search filters both TOC and main; clearing the input restores everything.
- [ ] Collapse-all / Expand-all toggles every `<details>`.
- [ ] Back-to-top appears only after scrolling.
- [ ] Direct URLs with hashes work (`#s-N-M-P`).

### Accessibility QA
- [ ] Lighthouse Accessibility ≥ 95.
- [ ] Keyboard-only navigation reaches every control.
- [ ] Focus is always visible.

### Code / Content QA
- [ ] DevTools console: zero errors, zero warnings from our code.
- [ ] `document.querySelectorAll('[id]').length` matches the expected node count (spot-check ≥ 600).
- [ ] Grep for `{{SUMMARY` returns zero results.
- [ ] Grep for `TODO` / `FIXME` returns zero results.
- [ ] Spot-check three random deep nodes (pick them randomly) — numbering and title must match `genai-roadmap.md` exactly.

### Performance QA
- [ ] `index.html` is under ~400 KB (expected ≈ 200–300 KB).
- [ ] Lighthouse Performance ≥ 90 on desktop.

---

## 12. Phase 8 — Git workflow & local delivery

**Goal:** clean commit history, branch pushed, ready for future GH Pages deployment.

### Commit strategy

Commit at the end of each phase, with short messages. Do **not** bundle everything into a single commit. Suggested messages:

```bash
git add PLAN.md
git commit -m "docs: add detailed implementation plan for junior dev"

git add genai-roadmap.md
git commit -m "content: add source GenAI roadmap outline"

git add index.html styles.css script.js
git commit -m "feat: scaffold three-file static site with empty layout"

git add index.html
git commit -m "feat: render full roadmap structure with placeholder summaries"

git add index.html tools/apply_summaries.py
git commit -m "content: generate and insert all LLM-written summaries"

git add styles.css
git commit -m "style: apply VS Code Dark+ palette and responsive layout"

git add script.js
git commit -m "feat: add active-section highlight, search, collapse, back-to-top"

git add index.html styles.css script.js
git commit -m "chore: accessibility polish and final verification"
```

### Push

```bash
git push -u origin <your-branch-name>
```

### Deployment (placeholder — do later)

Keep the site local for now. When the project owner approves, deploy to GitHub Pages:

1. Repo → Settings → Pages → Source: `main` branch, root folder.
2. Wait ~1 min, the URL will appear at the top of the Pages settings.
3. Because the site has no build step and no external resources, no further configuration is needed.

---

## 13. Consolidated pitfalls & gotchas (read before you start)

1. **UTF-8 everywhere.** Windows default encoding is *not* UTF-8. Save all three files as "UTF-8 without BOM" in VS Code. The `<meta charset="UTF-8">` in the HTML is not a substitute for correct file encoding.
2. **Always run a local server.** `python3 -m http.server 8000`. Don't open `index.html` directly while developing.
3. **`defer` on `<script>`** is mandatory. Without it, the DOM won't exist when JS runs.
4. **Sticky header hides scroll targets** unless `scroll-margin-top` is set on headings.
5. **`IntersectionObserver` picks the "topmost visible"** entry — the code pattern in Phase 5 does this. Do not simplify it.
6. **Search must un-hide ancestors**, both section ancestors and TOC `<li>` ancestors. Otherwise, deep matches get orphaned and look broken.
7. **Deep links into collapsed `<details>`** need the ancestor-opening logic on page load. Don't remove it.
8. **LLMs truncate large outputs.** Always chunk by ~40 nodes per batch and concatenate.
9. **Contrast.** VS Code's `#858585` muted fails WCAG AA on body text. We use `#a0a0a0`. If you go back to `#858585`, only use it for decorative labels.
10. **Commit small, often.** A single 3000-line commit at the end is a nightmare to review or roll back.
11. **Never `rm -rf`, force-push, or `git reset --hard`** without pausing to think. Git is append-only by default — keep it that way.
12. **Don't install anything.** No `npm install`, no `pip install`. The project has zero runtime dependencies.

---

## 14. Scope boundaries (do not expand without approval)

**Out of scope** — if you find yourself wanting to add these, stop and ask:
- Build tooling, bundlers, TypeScript, frameworks.
- Backend, database, analytics, telemetry.
- External fonts, icon libraries, CDN resources.
- Authenticating or personalizing the site.
- Rewriting Track B's "current" items to reflect the latest news — describe the *category*, not specific products or versions. Track B is intentionally coarse because its details go stale.

---

## 15. Estimated effort

| Phase | Task | Time (junior dev) |
|---|---|---|
| 0 | Obtain roadmap source | 30 min – 2 h |
| 1 | Scaffold three files | 1 h |
| 2 | Render skeleton from markdown | 2–4 h |
| 3 | Generate & insert summaries (LLM batches) | 4–8 h |
| 4 | Styling | 3–5 h |
| 5 | Interactivity | 3–5 h |
| 6 | Accessibility polish | 1–2 h |
| 7 | Final verification | 1–2 h |
| 8 | Git commits & push | 30 min |
| **Total** | | **~16–30 h** (2–4 working days) |

---

**Done when:** every checkbox in §11 is green, the branch is pushed, and `localhost:8000` shows a polished, searchable, keyboard-navigable, VS-Code-themed GenAI roadmap summary.
