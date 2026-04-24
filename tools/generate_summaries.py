#!/usr/bin/env python3
"""Generate intelligent summaries from roadmap structure."""
import re
import pathlib

def generate_summaries() -> dict:
    """Parse markdown and generate smart summaries for each node."""
    content = pathlib.Path('genai-roadmap.md').read_text(encoding='utf-8')
    lines = content.split('\n')

    summaries = {}
    extended = {}  # Store extended explanations
    part_context = ""
    section_context = ""
    level2_context = ""

    part_num = 0
    part_title = ""

    for i, line in enumerate(lines):
        # Track current context for summary generation
        if line.startswith('## Part '):
            part_num += 1
            match = re.match(r'^##\s+Part\s+([IVXLCDM]+)\s+—\s+(.+)$', line)
            if match:
                rom = match.group(1).lower()
                part_title = match.group(2)
                part_id = f'part-{rom}'

                # Look ahead for content
                context_lines = []
                for j in range(i+1, min(i+10, len(lines))):
                    if lines[j].startswith('#'):
                        break
                    if lines[j].strip() and not lines[j].startswith(' '):
                        context_lines.append(lines[j].strip())
                part_context = ' '.join(context_lines)[:200]

                # Generate summary
                if part_title:
                    summary = f"{part_title} covers foundational concepts and principles essential for understanding this domain."
                    summaries[part_id] = summary

                # Look for extended explanation (blockquote immediately after Part heading)
                if i+1 < len(lines) and lines[i+1].startswith('> **Extended:**'):
                    extended_text = lines[i+1][2:]  # Remove '> '
                    # Convert **bold** to <strong>bold</strong>
                    extended_text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', extended_text)
                    # Wrap in HTML
                    extended_html = f'<p>{extended_text}</p>'
                    extended[part_id] = extended_html

        # Level-1 sections
        if re.match(r'^###\s+\d+\.\s+', line):
            match = re.match(r'^###\s+(\d+)\.\s+(.+)$', line)
            if match:
                num = match.group(1)
                title = match.group(2)
                sec_id = f's-{num}'

                # Look ahead for bullet points to infer content
                context_lines = []
                for j in range(i+1, min(i+5, len(lines))):
                    if re.match(r'^###\s+\d+', lines[j]) or lines[j].startswith('## '):
                        break
                    if re.match(r'^-\s+\d+\.\d+', lines[j]):
                        context_lines.append(lines[j].replace('- ', '').split(' — ')[0][:60])
                context = ', '.join(context_lines[:3])

                if context:
                    summary = f"{title} introduces {context}."
                else:
                    summary = f"This section covers {title.lower()} with practical depth."

                summaries[sec_id] = summary

        # Level-2 subsections
        if re.match(r'^-\s+\d+\.\d+\s+', line) and not line.startswith('  '):
            match = re.match(r'^-\s+([\d.]+)\s+(.+)$', line)
            if match:
                num = match.group(1).replace('.', '-')
                title = match.group(2)
                sec_id = f's-{num}'

                # Look ahead for leaves
                leaf_count = 0
                for j in range(i+1, min(i+10, len(lines))):
                    if re.match(r'^-\s+\d+\.\d+', lines[j]) or re.match(r'^###\s+\d+', lines[j]):
                        break
                    if re.match(r'^  -\s+\d+\.\d+\.\d+', lines[j]):
                        leaf_count += 1

                if leaf_count > 0:
                    summary = f"{title} breaks down into {leaf_count} specific concepts and techniques."
                else:
                    summary = f"Covers the fundamentals of {title.lower()}."

                summaries[sec_id] = summary

        # Level-3 subsections
        if re.match(r'^  -\s+\d+\.\d+\.\d+\s+', line) and not line.startswith('    '):
            match = re.match(r'^  -\s+([\d.]+)\s+(.+)$', line)
            if match:
                num = match.group(1).replace('.', '-')
                title = match.group(2)
                sec_id = f's-{num}'
                # For level-3, just use the title as summary (1 sentence)
                summary = f"{title}."
                summaries[sec_id] = summary

        # Level-4 leaves
        if re.match(r'^    -\s+\d+\.\d+\.\d+\.\d+\s+', line):
            match = re.match(r'^    -\s+([\d.]+)\s+(.+)$', line)
            if match:
                num = match.group(1).replace('.', '-')
                title = match.group(2)
                sec_id = f's-{num}'
                summary = f"{title}."
                summaries[sec_id] = summary

    # Track summaries
    summaries['track-a'] = "Evergreen Core — foundational GenAI concepts that remain constant and essential regardless of technological changes or market evolution."
    summaries['track-b'] = "Current Landscape — time-sensitive overview of existing models, tools, and platforms. Refresh annually for relevance."

    return summaries, extended

def apply_summaries(summaries: dict, extended: dict):
    """Apply summaries and extended explanations to index.html."""
    index_path = pathlib.Path('index.html')
    html = index_path.read_text(encoding='utf-8')

    missing = []
    for sid, text in summaries.items():
        placeholder = f'{{{{SUMMARY_{sid}}}}}'
        if placeholder not in html:
            missing.append(sid)
        else:
            # Escape HTML
            text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            html = html.replace(placeholder, text)

    # Apply extended explanations
    for ext_id, ext_html in extended.items():
        placeholder = f'{{{{EXTENDED_{ext_id}}}}}'
        if placeholder in html:
            html = html.replace(placeholder, ext_html)

    index_path.write_text(html, encoding='utf-8')

    remaining_summary = html.count('{{SUMMARY_')
    remaining_extended = html.count('{{EXTENDED_')
    print(f"[OK] Applied {len(summaries)} summaries")
    print(f"[OK] Applied {len(extended)} extended explanations")
    print(f"[INFO] Remaining SUMMARY placeholders: {remaining_summary}")
    print(f"[INFO] Remaining EXTENDED placeholders: {remaining_extended}")
    if missing:
        print(f"[WARN] Missing summary IDs: {', '.join(missing[:5])}")

if __name__ == '__main__':
    summaries, extended = generate_summaries()
    apply_summaries(summaries, extended)
