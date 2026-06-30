#!/usr/bin/env python3
"""
build.py — InteractiveLecture Build System

Pipeline: lecture.md → rendered HTML → PDF export

Usage:
    python build.py lectures/topic1_motion.md
    python build.py lectures/topic1_motion.md --no-pdf
    python build.py lectures/topic1_motion.md --outdir custom_output/
    python build.py lectures/topic1_motion.md --version 2
    python build.py lectures/topic1_motion.md --preview     # Open in browser
"""

from __future__ import annotations

import argparse
import json
import sys
import webbrowser
from datetime import date
from pathlib import Path

# Add scripts dir to path for imports
_SCRIPTS_DIR = Path(__file__).parent.resolve()
sys.path.insert(0, str(_SCRIPTS_DIR))

from parse_lecture import (
    parse_lecture,
    Lecture,
    LectureSection,
    markdown_to_html,
)
from pdf_export import export_pdf, export_pdf_thumbnail


# ─── Paths ───

PROJECT_ROOT = _SCRIPTS_DIR.parent
DEFAULT_OUTDIR = PROJECT_ROOT / "output"
TEMPLATES_DIR = _SCRIPTS_DIR / "templates"
GRAPHS_DIR = PROJECT_ROOT / "graphs"


def resolve_graph_path(graph_type: str) -> str:
    """Resolve a graph type to its HTML file path (relative to output dir)."""
    graph_files = {
        "distance-time": "kinematics_graphs_v1.html",
        "speed-time": "kinematics_graphs_v1.html",
        "acceleration-time": "kinematics_graphs_v1.html",
        "horizontal-motion": "kinematics_graphs_v1.html",
        "freefall": "kinematics_freefall_v1.html",
        "free-fall": "kinematics_freefall_v1.html",
        "vertical-motion": "kinematics_freefall_v1.html",
    }
    filename = graph_files.get(graph_type, "kinematics_graphs_v1.html")
    graph_path = GRAPHS_DIR / filename

    if not graph_path.exists():
        return f"../graphs/{filename}"  # fallback relative path
    return f"../graphs/{filename}"


def build_lecture(
    md_path: str | Path,
    output_dir: str | Path | None = None,
    version: int | None = None,
    generate_pdf: bool = True,
    open_browser: bool = False,
) -> dict:
    """Main build pipeline: .md → HTML → PDF.

    Args:
        md_path: Path to the .md lecture file.
        output_dir: Output directory (default: project root / output/).
        version: Manual version override (default: auto from frontmatter).
        generate_pdf: Whether to generate PDF (default: True).
        open_browser: Open the HTML in browser after build (default: False).

    Returns:
        dict with paths to generated files: {html, pdf, json, thumbnail}
    """
    md_path = Path(md_path).resolve()
    output_dir = Path(output_dir or DEFAULT_OUTDIR).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    # ─── Phase 1: Parse ───
    print(f"📖 Parsing: {md_path.name}")
    lecture = parse_lecture(md_path)

    # Override version if provided
    if version is not None:
        lecture.version = version

    # ─── Phase 2: Render HTML ───

    # Build section data for template
    sections_data = []
    for section in lecture.sections:
        # Convert markdown content to HTML
        content_html = markdown_to_html(section.content_md)

        # Build graph directive HTML with resolved paths
        graph_directives = []
        for g in section.graph_directives:
            graph_src = resolve_graph_path(g.graph_type)

            # Build query params
            query_parts = [f"{k}={v}" for k, v in g.params.items() if k != 'type']
            query = "&".join(query_parts)
            if query:
                graph_src += f"?embedded=true&{query}"
            else:
                graph_src += "?embedded=true"

            graph_directives.append({
                "graph_type": g.graph_type,
                "graph_src": graph_src,
                "params": g.params,
            })

        sections_data.append({
            "heading": section.heading,
            "type": section.type,
            "content_html": content_html,
            "equations": [
                {"latex": eq.latex, "inline": eq.inline}
                for eq in section.equations
            ],
            "graph_directives": graph_directives,
        })

    # Render with Jinja2
    try:
        from jinja2 import Environment, FileSystemLoader
    except ImportError:
        print("❌ Jinja2 is required. Install with: pip install jinja2")
        sys.exit(1)

    env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)))
    template = env.get_template("lecture.html")

    html_content = template.render(
        lecture={
            "title": lecture.title,
            "topic": lecture.topic,
            "level": lecture.level,
            "version": lecture.version,
            "sections": sections_data,
        },
        generation_date=date.today().isoformat(),
    )

    # ─── Write HTML ───
    html_filename = f"{md_path.stem}_v{lecture.version}.html"
    html_path = output_dir / html_filename
    html_path.write_text(html_content, encoding='utf-8')
    print(f"   ✅ HTML: {html_path}")

    # ─── Write JSON data ───
    json_filename = f"{md_path.stem}_v{lecture.version}.json"
    json_path = output_dir / json_filename
    json_path.write_text(
        json.dumps(lecture.to_dict(), indent=2, ensure_ascii=False),
        encoding='utf-8',
    )
    print(f"   ✅ JSON: {json_path}")

    result = {
        "html": str(html_path),
        "json": str(json_path),
        "pdf": None,
        "thumbnail": None,
    }

    # ─── Phase 3: PDF Export ───
    if generate_pdf:
        pdf_filename = f"{md_path.stem}_v{lecture.version}.pdf"
        pdf_path = output_dir / pdf_filename

        try:
            print(f"   📄 Generating PDF...")
            export_pdf(
                html_path=html_path,
                output_path=pdf_path,
            )
            file_size = pdf_path.stat().st_size / 1024
            print(f"   ✅ PDF: {pdf_path} ({file_size:.0f} KB)")
            result["pdf"] = str(pdf_path)
        except Exception as e:
            print(f"   ⚠️  PDF export failed: {e}")
            print(f"      Tip: Make sure Playwright is installed:")
            print(f"        pip install playwright")
            print(f"        python -m playwright install chromium")

    # ─── Optional: Preview ───
    if open_browser:
        webbrowser.open(f"file://{html_path}")

    return result


def main():
    parser = argparse.ArgumentParser(
        description="InteractiveLecture Build System — .md → HTML → PDF",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python build.py lectures/topic1_motion.md
  python build.py lectures/topic1_motion.md --no-pdf
  python build.py lectures/topic1_motion.md --preview
  python build.py lectures/topic1_motion.md --version 2
  python build.py lectures/topic1_motion.md --outdir ~/Desktop/output
        """,
    )
    parser.add_argument("input", help="Path to the .md lecture file")
    parser.add_argument(
        "--outdir", "-o",
        default=None,
        help="Output directory (default: project output/)",
    )
    parser.add_argument(
        "--version", "-v",
        type=int,
        default=None,
        help="Manually set version number",
    )
    parser.add_argument(
        "--no-pdf",
        action="store_true",
        help="Skip PDF generation",
    )
    parser.add_argument(
        "--preview", "-p",
        action="store_true",
        help="Open generated HTML in browser",
    )

    args = parser.parse_args()

    # Validate input
    md_path = Path(args.input)
    if not md_path.exists():
        print(f"❌ File not found: {md_path}")
        sys.exit(1)
    if md_path.suffix not in ('.md', '.markdown'):
        print(f"⚠️  Warning: '{md_path.suffix}' is not a .md file")

    # Build
    result = build_lecture(
        md_path=md_path,
        output_dir=args.outdir,
        version=args.version,
        generate_pdf=not args.no_pdf,
        open_browser=args.preview,
    )

    # Summary
    print(f"\n{'─' * 50}")
    print(f"✅ Build complete: {md_path.stem}")
    print(f"   HTML:  {result['html']}")
    if result['pdf']:
        print(f"   PDF:   {result['pdf']}")
    print(f"   JSON:  {result['json']}")
    print(f"{'─' * 50}")

    # Auto-regenerate dashboard
    try:
        from build_dashboard import build_dashboard as rebuild_dashboard
        outdir = Path(args.outdir) if args.outdir else _SCRIPTS_DIR.parent / "output"
        rebuild_dashboard(output_dir=outdir)
    except Exception as e:
        print(f"   ⚠️  Dashboard refresh: {e}")


if __name__ == "__main__":
    main()
