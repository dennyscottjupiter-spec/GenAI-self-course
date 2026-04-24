#!/usr/bin/env python3
"""Simple reliable markdown to HTML converter."""
import re
import pathlib

def escape_html(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def convert():
    lines = pathlib.Path('genai-roadmap.md').read_text(encoding='utf-8').split('\n')

    html = []
    toc = ['<ul>']

    preamble_added = False
    in_track_a = False
    in_track_b = False
    in_part = False
    in_section = False
    in_details = []  # Stack of open details tags

    for i, line in enumerate(lines):
        if not line.strip():
            continue

        # Preamble
        if line.startswith('## How This'):
            if not preamble_added:
                para = []
                j = i + 1
                while j < len(lines) and not lines[j].startswith('#'):
                    if lines[j].strip():
                        para.append(lines[j].strip())
                    j += 1
                html.append('<h2>How This Roadmap Is Built</h2>')
                html.append(f'<p>{" ".join(para)}</p>')
                preamble_added = True
            continue

        # Skip document title and Track headers (we'll inject them manually)
        if line.startswith('# '):
            continue

        # Part
        if line.startswith('## Part '):
            # Close previous section if open
            while in_details:
                html.append(in_details.pop())
            if in_section:
                html.append('</section>')
                in_section = False
            if in_part:
                html.append('</section>')
                in_part = False

            # Track B transition
            m = re.match(r'^##\s+Part\s+([IVXLCDM]+)\s+—', line)
            if m and m.group(1) == 'XVI' and not in_track_b:
                if in_track_a:
                    html.append('</section>')  # Close Track A
                html.append('<section class="track warn" id="track-b">')
                html.append('<h2 class="track-title">🟡 Track B — Current Landscape (2025–2026)</h2>')
                html.append('<div class="warn-banner">Track B is time-sensitive — refresh yearly.</div>')
                html.append('<p class="summary">{{SUMMARY_track-b}}</p>')
                toc.append('</ul>\n</li>')
                toc.append('<li class="toc-track"><a href="#track-b">🟡 Track B — Current Landscape (2025–2026)</a>\n<ul>')
                in_track_b = True
            elif not in_track_a and m and m.group(1) == 'I':
                html.append('<section class="track" id="track-a">')
                html.append('<h2 class="track-title">🟢 Track A — Evergreen Core</h2>')
                html.append('<p class="summary">{{SUMMARY_track-a}}</p>')
                toc.append('<li class="toc-track"><a href="#track-a">🟢 Track A — Evergreen Core</a>\n<ul>')
                in_track_a = True

            # Add part
            m = re.match(r'^##\s+Part\s+([IVXLCDM]+)\s+—\s+(.+)$', line)
            if m:
                part_id = f'part-{m.group(1).lower()}'
                html.append(f'<section class="part" id="{part_id}">')
                html.append(f'<h3><span class="numprefix">{m.group(1)}</span> {escape_html(m.group(2))}</h3>')
                html.append(f'<p class="summary">{{{{SUMMARY_{part_id}}}}}</p>')
                toc.append(f'<li class="toc-part"><a href="#{part_id}">{escape_html(m.group(2))}</a>\n<ul>')
                in_part = True
            continue

        # Level-1 section
        if line.startswith('### '):
            while in_details:
                html.append(in_details.pop())
            if in_section:
                html.append('</section>')

            m = re.match(r'^###\s+(\d+)\.\s+(.+)$', line)
            if m:
                sec_id = f's-{m.group(1)}'
                html.append(f'<section class="sec lvl-1" id="{sec_id}">')
                html.append(f'<h4><span class="numprefix">{m.group(1)}.</span> {escape_html(m.group(2))}</h4>')
                html.append(f'<p class="summary">{{{{SUMMARY_{sec_id}}}}}</p>')
                toc.append(f'<li><a href="#{sec_id}">{escape_html(m.group(2))}</a></li>')
                in_section = True
            continue

        # Level-2
        if re.match(r'^-\s+\d+\.\d+\s+', line):
            m = re.match(r'^-\s+([\d.]+)\s+(.+)$', line)
            if m:
                sec_id = f's-{m.group(1).replace(".", "-")}'
                html.append(f'<details class="sec lvl-2" id="{sec_id}" open>')
                html.append(f'<summary><h5><span class="numprefix">{m.group(1)}</span> {escape_html(m.group(2))}</h5></summary>')
                html.append(f'<p class="summary">{{{{SUMMARY_{sec_id}}}}}</p>')
                in_details.append('</details>')
            continue

        # Level-3
        if re.match(r'^  -\s+\d+\.\d+\.\d+\s+', line) and not re.match(r'^    ', line):
            m = re.match(r'^  -\s+([\d.]+)\s+(.+)$', line)
            if m:
                sec_id = f's-{m.group(1).replace(".", "-")}'
                html.append(f'<details class="sec lvl-3" id="{sec_id}">')
                html.append(f'<summary><h6><span class="numprefix">{m.group(1)}</span> {escape_html(m.group(2))}</h6></summary>')
                html.append(f'<p class="summary">{{{{SUMMARY_{sec_id}}}}}</p>')
                in_details.append('</details>')
            continue

        # Level-4
        if re.match(r'^    -\s+\d+\.\d+\.\d+\.\d+\s+', line):
            m = re.match(r'^    -\s+([\d.]+)\s+(.+)$', line)
            if m:
                sec_id = f's-{m.group(1).replace(".", "-")}'
                html.append(f'<details class="sec lvl-4" id="{sec_id}">')
                html.append(f'<summary><h6><span class="numprefix">{m.group(1)}</span> {escape_html(m.group(2))}</h6></summary>')
                html.append(f'<p class="summary">{{{{SUMMARY_{sec_id}}}}}</p>')
                html.append('</details>')
            continue

    # Close all remaining open tags
    while in_details:
        html.append(in_details.pop())
    if in_section:
        html.append('</section>')
    if in_part:
        html.append('</section>')
    if in_track_a or in_track_b:
        html.append('</section>')

    toc.append('</ul>\n</li>')
    toc.append('</ul>')

    # Inject into index.html
    index = pathlib.Path('index.html').read_text(encoding='utf-8')
    index = re.sub(
        r'(<main id="main" class="content">).*?(</main>)',
        lambda m: m.group(1) + '\n' + '\n'.join(html) + '\n' + m.group(2),
        index, flags=re.DOTALL
    )
    index = re.sub(
        r'(<nav id="toc"[^>]*>).*?(</nav>)',
        lambda m: m.group(1) + '\n' + '\n'.join(toc) + '\n' + m.group(2),
        index, flags=re.DOTALL
    )
    pathlib.Path('index.html').write_text(index, encoding='utf-8')
    print("[OK] Converted roadmap")

if __name__ == '__main__':
    convert()
