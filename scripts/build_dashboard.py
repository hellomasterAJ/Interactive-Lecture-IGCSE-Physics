"""
build_dashboard.py — Generate Lecture Dashboard

Scans the output/ directory for lecture JSON/HTML/PDF files
and generates a unified dashboard.html index page.

Usage:
    python scripts/build_dashboard.py                          # default output/
    python scripts/build_dashboard.py --outdir custom_output/
    python scripts/build_dashboard.py --open                   # Open in browser
"""

from __future__ import annotations

import argparse
import json
import re
import webbrowser
from datetime import date
from pathlib import Path
from typing import Optional


PROJECT_ROOT = Path(__file__).parent.parent.resolve()
DEFAULT_OUTDIR = PROJECT_ROOT / "output"
TEMPLATES_DIR = Path(__file__).parent / "templates"


def discover_lectures(output_dir: Path) -> list[dict]:
    """Scan output/ for lecture JSON files and extract metadata.

    Returns sorted list of lecture dicts: {topic, title, level, version,
    has_graphs, html_path, pdf_path, json_path, html_size, pdf_size, description}
    """
    lectures = []

    # Find all JSON files in output/
    json_files = sorted(output_dir.glob("topic*.json"))

    seen = set()
    for jf in json_files:
        try:
            data = json.loads(jf.read_text(encoding='utf-8'))
            stem = jf.stem  # e.g. topic12_motion_v1

            # Deduplicate by stem
            if stem in seen:
                continue
            seen.add(stem)

            title = data.get("title", stem)
            topic = data.get("topic", "")
            level = data.get("level", "IGCSE Physics 0625")

            # Count how many sections, equations, graph directives
            has_graphs = False
            section_count = len(data.get("sections", []))
            eq_count = 0
            for s in data.get("sections", []):
                eq_count += len(s.get("equations", []))
                if s.get("graph_directives"):
                    has_graphs = True

            # Build description snippet from first section
            description = ""
            for s in data.get("sections", []):
                if s.get("content_md"):
                    # Extract first 120 chars
                    raw = s["content_md"]
                    clean = re.sub(r'\*\*|<!--.*?-->|\$+', '', raw).strip()
                    description = clean[:180] + ('...' if len(clean) > 180 else '')
                    if description:
                        break

            # Find matching HTML and PDF
            html_path = output_dir / f"{stem}.html"
            pdf_path = output_dir / f"{stem}.pdf"
            html_size = html_path.stat().st_size if html_path.exists() else 0
            pdf_size = pdf_path.stat().st_size if pdf_path.exists() else 0

            # Extract topic number for sorting
            topic_num = ""
            m = re.match(r'topic(\d+)_?', stem)
            if m:
                raw_num = m.group(1)
                topic_num = f"{raw_num[0]}.{raw_num[1:]}"

            lectures.append({
                "stem": stem,
                "title": title,
                "topic": topic,
                "topic_num": topic_num,
                "level": level,
                "version": data.get("version", 1),
                "has_graphs": has_graphs,
                "section_count": section_count,
                "eq_count": eq_count,
                "description": description,
                "html_path": str(html_path.name),
                "pdf_path": str(pdf_path.name),
                "html_size_kb": round(html_size / 1024, 0),
                "pdf_size_kb": round(pdf_size / 1024, 0),
                "html_exists": html_path.exists(),
                "pdf_exists": pdf_path.exists(),
            })

        except (json.JSONDecodeError, KeyError) as e:
            print(f"  ⚠️  Skipping {jf.name}: {e}")

    # Sort by topic number
    def sort_key(l):
        parts = l["topic_num"].split('.')
        return (int(parts[0]) if len(parts) > 0 and parts[0] else 99,
                int(parts[1]) if len(parts) > 1 and parts[1] else 0)

    lectures.sort(key=sort_key)

    return lectures


def generate_dashboard(
    lectures: list[dict],
    output_path: Path,
    template_path: Optional[Path] = None,
) -> Path:
    """Generate dashboard HTML from lecture data.

    If a Jinja2 template exists, use it. Otherwise, generate inline.
    """
    from jinja2 import Environment, FileSystemLoader, select_autoescape

    template_dir = template_path.parent if template_path else TEMPLATES_DIR
    template_name = template_path.name if template_path else "dashboard.html"

    env = Environment(
        loader=FileSystemLoader(str(template_dir)),
        autoescape=select_autoescape(['html', 'xml']),
    )

    # Try loading template; fall back to built-in if not found
    try:
        template = env.get_template(template_name)
    except Exception:
        template = env.from_string(_DEFAULT_DASHBOARD_TEMPLATE)

    html = template.render(
        lectures=lectures,
        total_lectures=len(lectures),
        topics_with_graphs=sum(1 for l in lectures if l["has_graphs"]),
        total_pdfs=sum(1 for l in lectures if l["pdf_exists"]),
        generation_date=date.today().isoformat(),
        total_html_size_kb=round(sum(l["html_size_kb"] for l in lectures), 0),
        total_pdf_size_kb=round(sum(l["pdf_size_kb"] for l in lectures), 0),
    )

    output_path.write_text(html, encoding='utf-8')
    return output_path


def build_dashboard(
    output_dir: Optional[Path] = None,
    open_browser: bool = False,
) -> Path:
    """Main dashboard build function."""
    output_dir = Path(output_dir or DEFAULT_OUTDIR).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"🔍 Scanning: {output_dir}")
    lectures = discover_lectures(output_dir)
    print(f"   Found {len(lectures)} lectures")

    if not lectures:
        print("   ⚠️  No lecture files found. Run build.py first.")
        dashboard_path = output_dir / "dashboard.html"
        # Generate empty dashboard
        from jinja2 import Environment
        env = Environment()
        template = env.from_string(_DEFAULT_DASHBOARD_TEMPLATE)
        html = template.render(
            lectures=[], total_lectures=0, topics_with_graphs=0,
            total_pdfs=0, generation_date=date.today().isoformat(),
            total_html_size_kb=0, total_pdf_size_kb=0,
        )
        dashboard_path.write_text(html, encoding='utf-8')
        return dashboard_path

    print(f"   📊 With graphs: {sum(1 for l in lectures if l['has_graphs'])}")
    print(f"   📄 PDFs: {sum(1 for l in lectures if l['pdf_exists'])}")

    dashboard_path = output_dir / "dashboard.html"
    generate_dashboard(lectures, dashboard_path)
    print(f"   ✅ Dashboard: {dashboard_path}")

    if open_browser:
        webbrowser.open(f"file://{dashboard_path}")

    return dashboard_path


# ──────────────── Built-in Template ────────────────

_DEFAULT_DASHBOARD_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>InteractiveLecture — Dashboard</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #0f172a; --card: #1e293b; --border: #334155;
    --text: #e2e8f0; --text-dim: #94a3b8; --text-muted: #64748b;
    --accent: #22d3ee; --accent-glow: rgba(34,211,238,0.12);
    --green: #34d399; --rose: #fb7185; --violet: #a78bfa; --amber: #fbbf24;
  }
  .light {
    --bg: #cdc7bc; --card: #ddd7cc; --border: #bdb5a8;
    --text: #2d2a24; --text-dim: #635d52; --text-muted: #8c8578;
    --accent: #0f766e; --accent-glow: rgba(15,118,110,0.1);
    --green: #047857; --rose: #be123c; --violet: #6d28d9; --amber: #b45309;
  }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    background: var(--bg); color: var(--text);
    font-family: 'Inter', sans-serif; transition: all 0.3s;
    min-height: 100vh;
  }

  /* ─── Top Bar ─── */
  .top-bar {
    background: var(--card); border-bottom: 1px solid var(--border);
    padding: 16px 32px; display: flex; justify-content: space-between;
    align-items: center; position: sticky; top: 0; z-index: 100;
  }
  .top-bar h1 { font-size: 1.3rem; font-weight: 800; display: flex; align-items: center; gap: 10px; }
  .top-bar h1 .accent { background: linear-gradient(135deg, var(--accent), var(--violet)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
  .theme-btn {
    background: var(--card); border: 1px solid var(--border); color: var(--text-dim);
    padding: 6px 14px; border-radius: 8px; cursor: pointer;
    font-size: 0.7rem; font-family: 'JetBrains Mono', monospace; transition: all 0.2s;
  }
  .theme-btn:hover { border-color: var(--accent); color: var(--accent); }

  /* ─── Stats Bar ─── */
  .stats-bar {
    display: flex; gap: 16px; padding: 14px 32px;
    background: var(--card); border-bottom: 1px solid var(--border);
    flex-wrap: wrap;
  }
  .stat-chip {
    padding: 4px 14px; border-radius: 20px;
    font-size: 0.65rem; font-family: 'JetBrains Mono', monospace;
    border: 1px solid var(--border); display: flex; align-items: center; gap: 6px;
  }
  .stat-chip .num { color: var(--accent); font-weight: 600; }

  /* ─── Filter Bar ─── */
  .filter-bar {
    padding: 10px 32px; background: var(--bg);
    border-bottom: 1px solid var(--border);
    display: flex; gap: 6px; flex-wrap: wrap; align-items: center;
  }
  .filter-bar label { font-size: 0.6rem; color: var(--text-muted); font-family: 'JetBrains Mono', monospace; margin-right: 4px; }
  .filter-btn {
    padding: 3px 10px; border-radius: 6px; border: 1px solid var(--border);
    background: transparent; color: var(--text-dim); cursor: pointer;
    font-size: 0.6rem; font-family: 'JetBrains Mono', monospace; transition: all 0.15s;
  }
  .filter-btn:hover { border-color: var(--accent); color: var(--accent); }
  .filter-btn.active { background: var(--accent-glow); border-color: var(--accent); color: var(--accent); }

  /* ─── Grid ─── */
  .container { max-width: 1200px; margin: 0 auto; padding: 24px 32px; }

  .lecture-grid {
    display: grid; grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
    gap: 14px;
  }

  /* ─── Cards ─── */
  .lecture-card {
    background: var(--card); border: 1px solid var(--border);
    border-radius: 12px; padding: 16px; transition: all 0.2s;
    display: flex; flex-direction: column; gap: 6px;
  }
  .lecture-card:hover { border-color: var(--accent); transform: translateY(-2px); box-shadow: 0 4px 20px rgba(0,0,0,0.2); }
  .lecture-card.hidden { display: none; }

  .card-top { display: flex; justify-content: space-between; align-items: flex-start; gap: 8px; }
  .card-topic-num {
    font-family: 'JetBrains Mono', monospace; font-size: 0.6rem; font-weight: 600;
    padding: 2px 8px; border-radius: 4px; white-space: nowrap;
    background: var(--accent-glow); color: var(--accent); border: 1px solid var(--accent);
  }
  .card-badges { display: flex; gap: 3px; flex-wrap: wrap; }
  .badge {
    font-size: 0.5rem; padding: 2px 6px; border-radius: 4px;
    font-family: 'JetBrains Mono', monospace; font-weight: 500;
    border: 1px solid transparent;
  }
  .badge-graph { background: rgba(34,211,238,0.12); color: var(--accent); border-color: var(--accent); }
  .badge-pdf { background: rgba(251,191,36,0.12); color: var(--amber); border-color: var(--amber); }

  .card-title {
    font-size: 0.95rem; font-weight: 700; margin-top: 4px;
    line-height: 1.3;
  }
  .card-topic { font-size: 0.65rem; color: var(--text-muted); font-family: 'JetBrains Mono', monospace; }

  .card-desc {
    font-size: 0.72rem; color: var(--text-dim); line-height: 1.5;
    flex: 1; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical;
    overflow: hidden;
  }

  .card-stats {
    display: flex; gap: 8px; margin-top: 4px; flex-wrap: wrap;
  }
  .card-stat {
    font-size: 0.55rem; color: var(--text-muted); font-family: 'JetBrains Mono', monospace;
    display: flex; align-items: center; gap: 3px;
  }

  .card-actions {
    display: flex; gap: 6px; margin-top: 8px; padding-top: 8px;
    border-top: 1px solid var(--border);
  }
  .card-btn {
    padding: 5px 10px; border-radius: 6px; border: 1px solid var(--border);
    background: transparent; color: var(--text-dim); cursor: pointer;
    font-size: 0.62rem; font-family: 'Inter', sans-serif; font-weight: 500;
    transition: all 0.2s; text-decoration: none; display: inline-flex; align-items: center; gap: 4px;
  }
  .card-btn:hover { border-color: var(--accent); color: var(--accent); }
  .card-btn.primary { background: var(--accent); color: #0f172a; border-color: var(--accent); font-weight: 600; }

  /* ─── Empty State ─── */
  .empty-state {
    grid-column: 1 / -1; text-align: center; padding: 60px 20px;
    color: var(--text-muted);
  }
  .empty-state .icon { font-size: 3rem; margin-bottom: 16px; }
  .empty-state p { font-size: 0.9rem; }

  /* ─── Footer ─── */
  .footer {
    text-align: center; padding: 20px 0; color: var(--text-muted);
    font-size: 0.65rem; border-top: 1px solid var(--border); margin-top: 40px;
  }

  @media (max-width: 600px) {
    .lecture-grid { grid-template-columns: 1fr; }
    .top-bar { padding: 12px 16px; }
    .container { padding: 16px; }
  }
</style>
</head>
<body>

<!-- TOP BAR -->
<div class="top-bar">
  <h1>📐 <span class="accent">InteractiveLecture</span> <span style="font-size:0.7rem;color:var(--text-muted);font-weight:400;">v1.0.0</span></h1>
  <div style="display:flex;gap:8px;align-items:center;">
    <span style="font-size:0.6rem;color:var(--text-muted);font-family:'JetBrains Mono',monospace;">{{ generation_date }}</span>
    <button class="theme-btn" onclick="toggleTheme()">🌓 Theme</button>
  </div>
</div>

<!-- STATS BAR -->
<div class="stats-bar">
  <span class="stat-chip"><span class="num">{{ total_lectures }}</span> Lectures</span>
  <span class="stat-chip"><span class="num">{{ topics_with_graphs }}</span> with Interactive Graphs</span>
  <span class="stat-chip"><span class="num">{{ total_pdfs }}</span> PDFs</span>
  <span class="stat-chip">📄 {{ total_html_size_kb }} KB HTML</span>
  <span class="stat-chip">📖 {{ total_pdf_size_kb }} KB PDF</span>
</div>

<!-- FILTER BAR -->
<div class="filter-bar">
  <label>Filter:</label>
  <button class="filter-btn active" data-filter="all" onclick="filterAll()">📋 All</button>
  <button class="filter-btn" data-filter="graph" onclick="filterLectures('graph')">📊 With Graphs</button>
  <button class="filter-btn" data-filter="no-graph" onclick="filterLectures('no-graph')">📝 Text Only</button>
</div>

<!-- MAIN -->
<div class="container">

  {% if total_lectures == 0 %}
  <div class="empty-state">
    <div class="icon">📭</div>
    <p>No lectures found.<br>Run <code style="color:var(--accent);">python3 scripts/build.py lectures/*.md</code> to generate them.</p>
  </div>
  {% else %}

  <div class="lecture-grid" id="lecture-grid">
    {% for l in lectures %}
    <div class="lecture-card" data-has-graphs="{{ 'true' if l.has_graphs else 'false' }}">
      <div class="card-top">
        {% if l.topic_num %}
        <span class="card-topic-num">Topic {{ l.topic_num }}</span>
        {% endif %}
        <div class="card-badges">
          {% if l.has_graphs %}<span class="badge badge-graph">📊 Graph</span>{% endif %}
          {% if l.pdf_exists %}<span class="badge badge-pdf">📄 PDF</span>{% endif %}
        </div>
      </div>
      <div class="card-title">{{ l.title }}</div>
      <div class="card-topic">{{ l.topic }}</div>
      <div class="card-desc">{{ l.description }}</div>
      <div class="card-stats">
        <span class="card-stat">📐 {{ l.section_count }} sections</span>
        <span class="card-stat">📏 {{ l.eq_count }} equations</span>
        <span class="card-stat">📄 {{ l.pdf_size_kb }} KB</span>
      </div>
      <div class="card-actions">
        {% if l.html_exists %}
        <a class="card-btn primary" href="{{ l.html_path }}" target="_blank">▶ Open Lecture</a>
        {% endif %}
        {% if l.pdf_exists %}
        <a class="card-btn" href="{{ l.pdf_path }}" target="_blank">📄 PDF</a>
        {% endif %}
      </div>
    </div>
    {% endfor %}
  </div>
  {% endif %}

  <div class="footer">
    InteractiveLecture — CIE IGCSE Physics 0625 — Generated {{ generation_date }}
  </div>
</div>

<script>
function toggleTheme() {
  document.body.classList.toggle('light');
  localStorage.setItem('il-theme', document.body.classList.contains('light') ? 'light' : 'dark');
}
const saved = localStorage.getItem('il-theme');
if (saved === 'light') document.body.classList.add('light');

function filterAll() {
  document.querySelectorAll('.lecture-card').forEach(c => c.classList.remove('hidden'));
  document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
  document.querySelector('[data-filter="all"]').classList.add('active');
}

function filterLectures(type) {
  document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
  document.querySelector(`[data-filter="${type}"]`).classList.add('active');

  document.querySelectorAll('.lecture-card').forEach(c => {
    if (type === 'all') { c.classList.remove('hidden'); return; }
    const hasGraphs = c.dataset.hasGraphs === 'true';
    c.classList.toggle('hidden', type === 'graph' ? !hasGraphs : hasGraphs);
  });
}
</script>
</body>
</html>
"""


# ──────────────── CLI ────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Lecture Dashboard")
    parser.add_argument("--outdir", "-o", default=None, help="Output directory")
    parser.add_argument("--open", "-p", action="store_true", help="Open in browser")
    args = parser.parse_args()

    build_dashboard(
        output_dir=args.outdir,
        open_browser=args.open,
    )
