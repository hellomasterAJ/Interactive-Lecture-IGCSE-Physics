"""
parse_lecture.py — Lecture.md Parser

Parses a Lecture.md file with the following structure:
- YAML frontmatter (title, topic, level, etc.)
- Section headers (##) for the 5-part structure
- LaTeX equations ($$...$$)
- Graph directives (```graph ... ```)

Usage:
    from parse_lecture import parse_lecture, Lecture

    lecture = parse_lecture("lectures/topic1_motion.md")
    print(lecture.title)
    for section in lecture.sections:
        print(section.heading, section.type)
"""

from __future__ import annotations

import re
import json
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Optional


# ──────────────── Data Models ────────────────

@dataclass
class GraphDirective:
    """A ```graph ... ``` block inside a section."""
    graph_type: str          # e.g. "distance-time", "velocity-time", "freefall"
    params: dict             # e.g. {"mode": "constant-speed", "speed": 8}
    raw: str                 # Original markdown block text


@dataclass
class Equation:
    """A LaTeX equation block $$...$$."""
    latex: str               # The LaTeX content (without $$ delimiters)
    inline: bool = False     # True for $...$, False for $$...$$


@dataclass
class LectureSection:
    """One section (## heading) inside a lecture."""
    heading: str             # Section title (e.g. "📜 History")
    type: str                # Section type: history, nature, theory, graphs, examples, other
    content_md: str          # Raw markdown content (excluding heading)
    equations: list[Equation] = field(default_factory=list)
    graph_directives: list[GraphDirective] = field(default_factory=list)


@dataclass
class Lecture:
    """Parsed lecture document."""
    filepath: str = ""
    title: str = ""
    topic: str = ""
    level: str = "IGCSE Core / Extended"
    version: int = 1
    sections: list[LectureSection] = field(default_factory=list)
    frontmatter: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        """Serialize to dict (for JSON export)."""
        return {
            "title": self.title,
            "topic": self.topic,
            "level": self.level,
            "version": self.version,
            "sections": [
                {
                    "heading": s.heading,
                    "type": s.type,
                    "content_md": s.content_md,
                    "equations": [{"latex": e.latex, "inline": e.inline} for e in s.equations],
                    "graph_directives": [
                        {"graph_type": g.graph_type, "params": g.params}
                        for g in s.graph_directives
                    ],
                }
                for s in self.sections
            ],
        }


# ──────────────── Section Type Detection ────────────────

SECTION_TYPE_MAP = {
    "hist": "history",
    "ประวัติ": "history",
    "nature": "nature",
    "applications": "nature",
    "theory": "theory",
    "ทฤษฎี": "theory",
    "graph": "graphs",
    "animation": "graphs",
    "กราฟ": "graphs",
    "example": "examples",
    "โจทย์": "examples",
    "ข้อสอบ": "examples",
    "worked": "examples",
}


def detect_section_type(heading: str) -> str:
    """Detect section type from heading text."""
    h = heading.lower().strip()
    # Remove emoji/icon prefixes
    h_clean = re.sub(r'^[^\w\s]+\s*', '', h)

    for keyword, stype in SECTION_TYPE_MAP.items():
        if keyword in h_clean:
            return stype
    return "other"


# ──────────────── Parser ────────────────

def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Parse YAML-like frontmatter between --- markers.

    Returns (frontmatter_dict, remaining_text).
    Uses simple key: value parsing (no PyYAML dependency needed).
    """
    text = text.lstrip()
    if not text.startswith('---'):
        return {}, text

    # Find ALL --- markers; skip the first (opening), use the second (closing)
    matches = list(re.finditer(r'^---[\s]*$', text, re.MULTILINE))
    if len(matches) < 2:
        # No closing marker — treat entire block as frontmatter
        fm_text = text[3:].strip()
        rest = ""
    else:
        open_match = matches[0]
        close_match = matches[1]
        fm_text = text[open_match.end():close_match.start()].strip()
        rest = text[close_match.end():].strip()

    frontmatter = {}
    for line in fm_text.split('\n'):
        line = line.strip()
        if ':' in line:
            key, _, val = line.partition(':')
            key = key.strip().lower()
            val = val.strip().strip('"').strip("'")
            frontmatter[key] = val

    return frontmatter, rest


def extract_equations(md_text: str) -> tuple[list[Equation], str]:
    """Extract $$...$$ and $...$ equations from markdown.

    Returns (equations, text_with_placeholders).
    """
    equations = []
    text = md_text

    # Extract block equations $$...$$
    def replace_block_eq(m: re.Match) -> str:
        latex = m.group(1).strip()
        equations.append(Equation(latex=latex, inline=False))
        idx = len(equations) - 1
        return f'<!-- EQ_BLOCK_{idx} -->'

    text = re.sub(r'\$\$(.*?)\$\$', replace_block_eq, text, flags=re.DOTALL)

    # Extract inline equations $...$
    def replace_inline_eq(m: re.Match) -> str:
        latex = m.group(1).strip()
        equations.append(Equation(latex=latex, inline=True))
        idx = len(equations) - 1
        return f'<!-- EQ_INLINE_{idx} -->'

    text = re.sub(r'(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)', replace_inline_eq, text)

    return equations, text


def extract_graph_directives(md_text: str) -> tuple[list[GraphDirective], str]:
    """Extract ```graph ... ``` blocks from markdown.

    Returns (directives, text_with_placeholders).
    """
    directives = []
    text = md_text

    pattern = re.compile(
        r'```graph\s*\n'
        r'(.*?)'
        r'```',
        re.DOTALL
    )

    def replace_graph(m: re.Match) -> str:
        block = m.group(1).strip()
        lines = block.split('\n')
        params = {}
        graph_type = "unknown"

        for line in lines:
            line = line.strip()
            if ':' in line:
                key, _, val = line.partition(':')
                key = key.strip().lower()
                val = val.strip().strip('"').strip("'")

                # Try to parse as number
                try:
                    if '.' in val:
                        val = float(val)
                    else:
                        val = int(val)
                except (ValueError, TypeError):
                    pass

                if key == 'type':
                    graph_type = str(val)
                else:
                    params[key] = val

        directives.append(GraphDirective(
            graph_type=graph_type,
            params=params,
            raw=m.group(0),
        ))
        idx = len(directives) - 1
        return f'<!-- GRAPH_DIRECTIVE_{idx} -->'

    text = pattern.sub(replace_graph, text)
    return directives, text


def parse_sections(md_text: str) -> list[LectureSection]:
    """Split markdown into sections by ## headings."""
    # Split on ## headings (but not ###)
    parts = re.split(r'^## (.+)$', md_text, flags=re.MULTILINE)

    sections = []
    if len(parts) < 2:
        # No sections found, treat entire text as one section
        if parts and parts[0].strip():
            eqs, content = extract_equations(parts[0].strip())
            graphs, content = extract_graph_directives(content)
            sections.append(LectureSection(
                heading="",
                type="other",
                content_md=content,
                equations=eqs,
                graph_directives=graphs,
            ))
        return sections

    # First part is text before any ## heading (intro / metadata)
    if parts[0].strip():
        eqs, content = extract_equations(parts[0].strip())
        graphs, content = extract_graph_directives(content)
        sections.append(LectureSection(
            heading="Introduction",
            type="other",
            content_md=content,
            equations=eqs,
            graph_directives=graphs,
        ))

    # Remaining parts are heading-content pairs
    for i in range(1, len(parts), 2):
        heading = parts[i].strip()
        content = parts[i + 1].strip() if i + 1 < len(parts) else ""

        eqs, content_clean = extract_equations(content)
        graphs, content_clean = extract_graph_directives(content_clean)

        sections.append(LectureSection(
            heading=heading,
            type=detect_section_type(heading),
            content_md=content_clean,
            equations=eqs,
            graph_directives=graphs,
        ))

    return sections


def parse_lecture(filepath: str | Path) -> Lecture:
    """Parse a .md lecture file into a Lecture dataclass.

    Args:
        filepath: Path to the .md file

    Returns:
        Lecture object with parsed sections, equations, and graph directives
    """
    filepath = Path(filepath)
    if not filepath.exists():
        raise FileNotFoundError(f"Lecture file not found: {filepath}")

    md_text = filepath.read_text(encoding='utf-8')

    # Parse frontmatter
    frontmatter, rest = parse_frontmatter(md_text)

    # Parse sections
    sections = parse_sections(rest)

    # Build lecture object
    lecture = Lecture(
        filepath=str(filepath.resolve()),
        title=frontmatter.get('title', filepath.stem.replace('_', ' ').title()),
        topic=frontmatter.get('topic', ''),
        level=frontmatter.get('level', 'IGCSE Core / Extended'),
        version=int(frontmatter.get('version', 1)),
        sections=sections,
        frontmatter=frontmatter,
    )

    return lecture


def render_equations_html(equations: list[Equation]) -> str:
    """Render equations to HTML with KaTeX placeholders.

    Returns HTML string with <span class="equation"> tags.
    """
    parts = []
    for i, eq in enumerate(equations):
        if eq.inline:
            parts.append(
                f'<span class="equation inline-eq" data-eq-idx="{i}">'
                f'`{eq.latex}`'
                f'</span>'
            )
        else:
            parts.append(
                f'<div class="equation block-eq" data-eq-idx="{i}">'
                f'$${eq.latex}$$'
                f'</div>'
            )
    return '\n'.join(parts)


def render_graph_html(directive: GraphDirective) -> str:
    """Generate HTML for a graph directive.

    Returns an iframe or embed tag that loads the appropriate graph file.
    """
    gtype = directive.graph_type
    params = directive.params

    # Map graph types to HTML files
    graph_files = {
        "distance-time": "kinematics_graphs_v1.html",
        "speed-time": "kinematics_graphs_v1.html",
        "acceleration-time": "kinematics_graphs_v1.html",
        "horizontal-motion": "kinematics_graphs_v1.html",
        "freefall": "kinematics_freefall_v1.html",
        "free-fall": "kinematics_freefall_v1.html",
        "vertical-motion": "kinematics_freefall_v1.html",
    }

    html_file = graph_files.get(gtype, "kinematics_graphs_v1.html")
    graph_path = f"../graphs/{html_file}"

    # Build query params for auto-config
    query_parts = []
    for k, v in params.items():
        if k != 'type':
            query_parts.append(f"{k}={v}")
    query = '&'.join(query_parts)
    src = f"{graph_path}?embedded=true&{'&'.join(query_parts)}" if query_parts else f"{graph_path}?embedded=true"

    return (
        f'<div class="graph-embed" data-graph-type="{gtype}">\n'
        f'  <iframe src="{src}" frameborder="0" loading="lazy" '
        f'    title="{gtype} graph" class="graph-iframe"></iframe>\n'
        f'</div>'
    )


def render_section_html(section: LectureSection, idx: int) -> str:
    """Render a LectureSection to HTML."""
    type_labels = {
        "history": "📜",
        "nature": "🌍",
        "theory": "⚛️",
        "graphs": "📊",
        "examples": "✍️",
        "other": "📌",
    }
    icon = type_labels.get(section.type, "📌")

    # Render equations found in section
    eq_html = render_equations_html(section.equations) if section.equations else ""

    # Render graph directives
    graph_html = ""
    for g in section.graph_directives:
        graph_html += render_graph_html(g) + "\n"

    # Markdown content → simple HTML (basic conversion)
    content_html = markdown_to_html(section.content_md)

    return f"""<section class="lecture-section section-{section.type}" data-section-idx="{idx}">
  <h2 class="section-heading">{icon} {section.heading}</h2>
  <div class="section-body">
    {content_html}
    {eq_html}
    {graph_html}
  </div>
</section>"""


def markdown_to_html(md_text: str) -> str:
    """Simple markdown-to-HTML conversion for common patterns.

    Handles: bold, italic, lists, links, paragraphs, code blocks.
    Uses Python's markdown library when available, falls back to basic regex.
    Strips out placeholder comments (GRAPH_DIRECTIVE, EQ_BLOCK, EQ_INLINE).
    """
    if not md_text or not md_text.strip():
        return ""

    # Strip internal placeholders (rendered separately by template)
    md_text = re.sub(r'<!-- (GRAPH_DIRECTIVE|EQ_BLOCK|EQ_INLINE)_\d+ -->', '', md_text)

    try:
        import markdown as md_lib
        return md_lib.markdown(
            md_text,
            extensions=['fenced_code', 'codehilite', 'nl2br'],
        )
    except ImportError:
        pass

    # Fallback: basic regex conversion
    html = md_text.strip()

    # Code blocks (```...```)
    html = re.sub(
        r'```(\w*)\n(.*?)```',
        lambda m: f'<pre><code class="language-{m.group(1)}">{_escape_html(m.group(2).strip())}</code></pre>',
        html,
        flags=re.DOTALL,
    )

    # Inline code
    html = re.sub(r'`([^`]+)`', r'<code>\1</code>', html)

    # Bold
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)

    # Italic
    html = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<em>\1</em>', html)

    # Links
    html = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', html)

    # Unordered lists
    html = re.sub(r'(?:^|\n)- (.+)', r'\n<li>\1</li>', html)
    html = re.sub(r'(<li>.*</li>\n?)+', lambda m: f'<ul>\n{m.group(0)}\n</ul>', html)

    # Ordered lists
    html = re.sub(r'(?:^|\n)\d+\. (.+)', r'\n<li>\1</li>', html)
    html = re.sub(r'(?:<li>.*</li>\n?)+', lambda m: f'<ol>\n{m.group(0)}\n</ol>', html, count=1)

    # Horizontal rule
    html = re.sub(r'^---+\s*$', '<hr>', html, flags=re.MULTILINE)

    # Paragraphs (double newlines)
    paragraphs = re.split(r'\n\n+', html)
    html = ''.join(
        f'<p>{p.strip()}</p>\n' if not p.strip().startswith(('<', '<li', '<ul', '<ol', '<pre', '<hr'))
        else p.strip() + '\n'
        for p in paragraphs if p.strip()
    )

    # Single newlines → <br>
    html = re.sub(r'(?<!\n)\n(?!\n)', '<br>\n', html)

    return html


def _escape_html(text: str) -> str:
    """Escape HTML special characters."""
    return (text
        .replace('&', '&amp;')
        .replace('<', '&lt;')
        .replace('>', '&gt;')
        .replace('"', '&quot;'))


# ──────────────── Convenience ────────────────

def export_lecture_json(lecture: Lecture, output_path: str | Path) -> None:
    """Export parsed lecture data to JSON for the web renderer."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(lecture.to_dict(), indent=2, ensure_ascii=False),
        encoding='utf-8',
    )


# ──────────────── CLI Test ────────────────

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python parse_lecture.py <lecture.md>")
        sys.exit(1)

    lecture = parse_lecture(sys.argv[1])
    print(f"📖 {lecture.title}")
    print(f"   Topic: {lecture.topic}")
    print(f"   Level: {lecture.level}")
    print(f"   Version: {lecture.version}")
    print(f"   Sections: {len(lecture.sections)}\n")

    for i, section in enumerate(lecture.sections):
        print(f"  [{i}] {section.type.upper():8s} | {section.heading}")
        if section.equations:
            for eq in section.equations:
                tag = "inline" if eq.inline else "block"
                print(f"         📐 [{tag}] ${eq.latex[:60]}...")
        if section.graph_directives:
            for g in section.graph_directives:
                print(f"         📊 {g.graph_type} {json.dumps(g.params)}")
        print()
