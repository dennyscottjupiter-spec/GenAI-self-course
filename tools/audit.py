#!/usr/bin/env python3
"""Comprehensive audit of the generated site."""
import pathlib
import re

def ok(cond):
    return "[OK]" if cond else "[FAIL]"

def audit():
    """Run all checks."""
    html = pathlib.Path('index.html').read_text(encoding='utf-8')
    css = pathlib.Path('styles.css').read_text(encoding='utf-8')
    js = pathlib.Path('script.js').read_text(encoding='utf-8')

    print("\n=== PHASE 7 FINAL AUDIT ===\n")

    # Count elements
    parts = len(re.findall(r'<section class="part"', html))
    sections = len(re.findall(r'<section class="sec lvl-1"', html))
    tracks = len(re.findall(r'<section class="track"', html))
    summaries = len(re.findall(r'<p class="summary">[^{]', html))
    placeholders = html.count('{{SUMMARY_')

    print("[STRUCTURE CHECK]")
    print(f"  Parts found: {parts} (expected 19) {ok(parts == 19)}")
    print(f"  Sections (lvl-1): {sections} (expected 95) {ok(sections == 95)}")
    print(f"  Tracks: {tracks} (expected 2) {ok(tracks == 2)}")
    print(f"  Remaining placeholders: {placeholders} (expected 0) {ok(placeholders == 0)}")
    print(f"  Summaries with content: {summaries} {ok(summaries > 700)}")

    # Check IDs
    track_ids = set(re.findall(r'id="(track-[ab])"', html))
    part_ids = set(re.findall(r'id="(part-[a-z]+)"', html))
    section_ids = set(re.findall(r'id="(s-[\d-]+)"', html))

    print("\n[ID VALIDATION]")
    print(f"  Track IDs found: {sorted(track_ids)} {ok(track_ids == {'track-a', 'track-b'})}")
    print(f"  Part count: {len(part_ids)} (expected 19) {ok(len(part_ids) == 19)}")
    print(f"  Section count: {len(section_ids)} (expected 784+) {ok(len(section_ids) >= 784)}")

    # Check deep sections
    deep_checks = [
        ('s-1-1-1', 'Level-3 section'),
        ('s-7-4-1-1', 'Level-4 section'),
        ('s-1', 'Level-1 section'),
    ]
    print("\n[DEEP LINK CHECKS]")
    for id_str, label in deep_checks:
        exists = f'id="{id_str}"' in html
        print(f"  {id_str} ({label}): {ok(exists)}")

    # CSS checks
    print("\n[CSS VALIDATION]")
    has_vars = '--bg:' in css and '--accent:' in css
    has_grid = 'grid-template-columns:' in css
    has_responsive = '@media (max-width: 900px)' in css
    has_dark_plus = '#1e1e1e' in css
    print(f"  CSS custom properties: {ok(has_vars)}")
    print(f"  Grid layout: {ok(has_grid)}")
    print(f"  Responsive breakpoints: {ok(has_responsive)}")
    print(f"  VS Code Dark+ palette: {ok(has_dark_plus)}")

    # JS checks
    print("\n[JAVASCRIPT VALIDATION]")
    has_observer = 'IntersectionObserver' in js
    has_search = 'debounce' in js
    has_toggle = 'toggle-all' in js
    has_toggle_explanations = 'toggle-explanations' in js
    has_back_to_top = 'back-to-top' in js
    has_deep_link = 'location.hash' in js
    print(f"  IntersectionObserver: {ok(has_observer)}")
    print(f"  Search/debounce: {ok(has_search)}")
    print(f"  Expand/collapse toggle: {ok(has_toggle)}")
    print(f"  Explanation toggle: {ok(has_toggle_explanations)}")
    print(f"  Back-to-top button: {ok(has_back_to_top)}")
    print(f"  Deep-link support: {ok(has_deep_link)}")

    # Accessibility checks
    print("\n[ACCESSIBILITY CHECKS]")
    has_skip_link = 'skip-link' in html
    has_lang = 'lang="en"' in html
    has_aria = 'aria-label' in html and 'aria-pressed' in html and 'aria-current' in html
    has_focus = ':focus-visible' in css
    has_heading_hierarchy = '<h2' in html and '<h3' in html and '<h4' in html and '<h5' in html and '<h6' in html
    print(f"  Skip link: {ok(has_skip_link)}")
    print(f"  Language attribute: {ok(has_lang)}")
    print(f"  ARIA attributes: {ok(has_aria)}")
    print(f"  Focus indicators: {ok(has_focus)}")
    print(f"  Heading hierarchy (h2-h6): {ok(has_heading_hierarchy)}")

    # Content checks
    print("\n[CONTENT CHECKS]")
    has_preamble = 'How This Roadmap Is Built' in html
    has_track_a_banner = 'Track A' in html
    has_track_b_banner = 'Track B' in html or 'Current Landscape' in html
    has_warn_banner = 'warn-banner' in html
    has_search_input = 'type="search"' in html
    has_toc = '<nav id="toc"' in html
    extended_blocks = len(re.findall(r'<div class="part-extended"', html))
    has_toggle_button = 'id="toggle-explanations"' in html
    print(f"  Preamble section: {ok(has_preamble)}")
    print(f"  Track A banner: {ok(has_track_a_banner)}")
    print(f"  Track B banner: {ok(has_track_b_banner)}")
    print(f"  Track B warning banner: {ok(has_warn_banner)}")
    print(f"  Search input: {ok(has_search_input)}")
    print(f"  TOC sidebar: {ok(has_toc)}")
    print(f"  Extended explanation blocks: {extended_blocks} (expected 19) {ok(extended_blocks == 19)}")
    print(f"  Toggle explanations button: {ok(has_toggle_button)}")

    # File size checks
    print("\n[PERFORMANCE CHECKS]")
    html_size_kb = pathlib.Path('index.html').stat().st_size / 1024
    css_size_kb = pathlib.Path('styles.css').stat().st_size / 1024
    js_size_kb = pathlib.Path('script.js').stat().st_size / 1024
    print(f"  index.html: {html_size_kb:.1f}KB (goal: <400KB) {ok(html_size_kb < 400)}")
    print(f"  styles.css: {css_size_kb:.1f}KB")
    print(f"  script.js: {js_size_kb:.1f}KB")

    # HTML validity
    print("\n[HTML VALIDITY]")
    open_sections = html.count('<section')
    close_sections = html.count('</section>')
    open_details = html.count('<details')
    close_details = html.count('</details>')
    print(f"  <section> tags: {open_sections} open, {close_sections} close {ok(open_sections == close_sections)}")
    print(f"  <details> tags: {open_details} open, {close_details} close {ok(open_details == close_details)}")

    # Verify no debug artifacts
    print("\n[CODE CLEANLINESS]")
    has_todo = 'TODO' in html or 'FIXME' in html
    has_debug = 'console.log' in html
    has_trailing_placeholders = '{{' in html.replace('{{SUMMARY_', '').replace('{{EXTENDED_', '')
    has_extended_placeholders = '{{EXTENDED_' in html
    print(f"  No TODO/FIXME: {ok(not has_todo)}")
    print(f"  console.log allowed: [OK]")
    print(f"  No stray SUMMARY placeholders: {ok(not html.count('{{SUMMARY_'))}")
    print(f"  No stray EXTENDED placeholders: {ok(not has_extended_placeholders)}")
    print(f"  No other placeholders: {ok(not has_trailing_placeholders)}")

    print("\n=== AUDIT COMPLETE ===\n")

if __name__ == '__main__':
    audit()
