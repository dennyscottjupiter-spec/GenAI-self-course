#!/usr/bin/env python3
"""Fix three issues in index.html:
1. TOC nesting (parts were never closed — infinite indent)
2. TOC missing Roman numeral + section number prefixes
3. Preamble containing raw Markdown instead of rendered HTML
"""
import re
import pathlib


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def build_toc():
    md = pathlib.Path('genai-roadmap.md').read_text(encoding='utf-8')
    lines = md.split('\n')

    tracks = []
    cur_track = None
    cur_part = None

    for line in lines:
        if line.startswith('## Part '):
            m = re.match(r'^##\s+Part\s+([IVXLCDM]+)\s+—\s+(.+)$', line)
            if not m:
                continue
            rom, title = m.group(1), m.group(2).strip()
            part_id = f'part-{rom.lower()}'

            if rom == 'I':
                cur_track = {'id': 'track-a', 'label': '🟢 Track A — Evergreen Core', 'parts': []}
                tracks.append(cur_track)
            elif rom == 'XVI':
                cur_track = {'id': 'track-b', 'label': '🟡 Track B — Current Landscape (2025–2026)', 'parts': []}
                tracks.append(cur_track)

            cur_part = {'id': part_id, 'roman': rom, 'title': title, 'sections': []}
            if cur_track:
                cur_track['parts'].append(cur_part)

        elif line.startswith('### '):
            m = re.match(r'^###\s+(\d+)\.\s+(.+)$', line)
            if m and cur_part is not None:
                cur_part['sections'].append({
                    'id': f's-{m.group(1)}',
                    'num': m.group(1),
                    'title': m.group(2).strip(),
                })

    out = ['<ul>']
    for track in tracks:
        out.append(f'<li class="toc-track"><a href="#{track["id"]}">{esc(track["label"])}</a>')
        out.append('<ul>')
        for part in track['parts']:
            label = f'{part["roman"]} — {esc(part["title"])}'
            out.append(f'<li class="toc-part"><a href="#{part["id"]}">{label}</a>')
            out.append('<ul>')
            for sec in part['sections']:
                out.append(f'<li><a href="#{sec["id"]}">{sec["num"]}. {esc(sec["title"])}</a></li>')
            out.append('</ul>')
            out.append('</li>')
        out.append('</ul>')
        out.append('</li>')
    out.append('</ul>')
    return '\n'.join(out)


PREAMBLE_HTML = """\
<h2>How This Roadmap Is Built</h2>
<p>This outline is split into <strong>two tracks</strong>:</p>
<ul class="preamble-list">
  <li><strong>Track A &mdash; Evergreen Core (Parts I&ndash;XV)</strong> &mdash; Stable concepts that age slowly. The backbone you study once and carry forever.</li>
  <li><strong>Track B &mdash; Current Landscape (Parts XVI&ndash;XIX)</strong> &mdash; Named models, tools, and frontier topics. Expect to refresh this section once a year.</li>
</ul>
<p><strong>Sequencing logic:</strong> each Part builds on the previous one. You can safely skip any leaf whose number you don&#8217;t care about (e.g., skip <code>7.4.1.1</code> and go to <code>7.4.2</code>) without losing the thread.</p>
<p><strong>Depth convention:</strong> up to four levels of nesting (e.g., <code>7.4.1.1</code>). Every leaf is atomic &mdash; one idea per bullet.</p>\
"""


def fix():
    index = pathlib.Path('index.html').read_text(encoding='utf-8')

    # 1. Replace TOC
    toc_html = build_toc()
    index = re.sub(
        r'(<nav id="toc"[^>]*>).*?(</nav>)',
        lambda m: m.group(1) + '\n' + toc_html + '\n' + m.group(2),
        index, flags=re.DOTALL
    )

    # 2. Fix preamble (raw markdown → proper HTML)
    index = re.sub(
        r'<h2>How This Roadmap Is Built</h2>\s*<p>.*?---</p>',
        PREAMBLE_HTML,
        index, flags=re.DOTALL
    )

    pathlib.Path('index.html').write_text(index, encoding='utf-8')
    print('[OK] TOC regenerated with correct nesting and Roman numerals')
    print('[OK] Preamble converted from Markdown to HTML')


if __name__ == '__main__':
    fix()
