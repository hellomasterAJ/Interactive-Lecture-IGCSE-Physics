#!/usr/bin/env python3
"""
พีพี (PP) — Project Portfolio Agent
=====================================
Dashboard, cost tracking, status, priority planning.

Usage:
    python3 pp.py dashboard              # Show dashboard (Markdown)
    python3 pp.py dashboard --html       # Generate HTML dashboard
    python3 pp.py status [project_id]    # Show project status
    python3 pp.py scan                   # Rescan project folders
    python3 pp.py cost                   # Show cost estimation
    python3 pp.py update <project_id> <key=value> [key=value ...]
    python3 pp.py next                   # Show recommended next actions

Data stored in:  ~/InteractiveLecture/agents/PP/
"""

import json
import os
import sys
import subprocess
from datetime import datetime

PP_DIR = os.path.expanduser("~/InteractiveLecture/agents/PP")
PROJECTS_FILE = os.path.join(PP_DIR, "projects.json")
DASHBOARD_HTML = os.path.join(PP_DIR, "pp-dashboard.html")
LOG_FILE = os.path.join(PP_DIR, "pp.log")

# ── Utility ────────────────────────────────────────────────────────

def log(msg):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{ts}] {msg}\n")

def load_projects():
    with open(PROJECTS_FILE, "r") as f:
        return json.load(f)

def save_projects(data):
    data["last_updated"] = datetime.now().isoformat()
    with open(PROJECTS_FILE, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    log("projects.json saved")

def get_project(data, pid):
    for p in data["projects"]:
        if p["id"] == pid:
            return p
    return None

# ── Scan ───────────────────────────────────────────────────────────

def scan_project(p):
    """Scan actual filesystem to verify project state."""
    base = os.path.expanduser(p.get("path", ""))
    if not base or not os.path.isdir(base):
        return p, "path_not_found"

    changes = {}

    # Count lecture source files
    lec_path = os.path.join(base, "lectures")
    if os.path.isdir(lec_path):
        mds = sorted([f for f in os.listdir(lec_path) if f.endswith(".md")])
        changes["lecture_count"] = len(mds)
        components = p.get("components", {})
        if "lectures" in components:
            components["lectures"]["count"] = len(mds)
            components["lectures"]["files"] = mds

    # Count output files — only topic_*.html (not dashboard.html)
    out_path = os.path.join(base, "output")
    if os.path.isdir(out_path):
        htmls = [f for f in os.listdir(out_path) if f.endswith(".html") and f.startswith("topic")]
        pdfs = [f for f in os.listdir(out_path) if f.endswith(".pdf") and f.startswith("topic")]
        jsons = [f for f in os.listdir(out_path) if f.endswith(".json") and f.startswith("topic")]
        changes["output_html"] = len(htmls)
        changes["output_pdf"] = len(pdfs)
        changes["output_json"] = len(jsons)
        changes["lectures_built"] = len(htmls)

    # Count simulations
    sim_path = os.path.join(base, "simulations")
    if os.path.isdir(sim_path):
        sims = [f for f in os.listdir(sim_path) if f.endswith(".html")]
        changes["simulations"] = len(sims)

    # Count graphs
    g_path = os.path.join(base, "graphs")
    if os.path.isdir(g_path):
        graphs = [f for f in os.listdir(g_path) if f.endswith(".html")]
        changes["graphs"] = len(graphs)

    p.update(changes)
    return p, "scanned"

def cmd_scan():
    data = load_projects()
    for i, p in enumerate(data["projects"]):
        updated, status = scan_project(p)
        data["projects"][i] = updated
        print(f"  {'✅' if status == 'scanned' else '⚠️'} {p['short_name']:25s} → {status}")
    save_projects(data)

# ── Status ─────────────────────────────────────────────────────────

def cmd_status(pid=None):
    data = load_projects()
    if pid:
        p = get_project(data, pid)
        if not p:
            print(f"❌ Project '{pid}' not found")
            return
        print_project_detail(p)
    else:
        for p in sorted(data["projects"], key=lambda x: x.get("priority", 99)):
            print_project_summary(p)

def progress_bar(value, total, width=20):
    if total == 0:
        return "─" * width
    filled = int((value / total) * width)
    return "█" * filled + "░" * (width - filled)

def print_project_summary(p):
    status_icon = {"active": "🟢", "exploring": "🟡", "paused": "🟠", "completed": "✅"}.get(p.get("status", ""), "⚪")
    prio = p.get("priority", 99)
    lec_total = p.get("lecture_count", 0)
    lec_built = p.get("lectures_built", 0)
    sims = p.get("simulations", 0)
    graphs = p.get("graphs", 0)

    bar = progress_bar(lec_built, lec_total) if lec_total > 0 else ""

    print(f"\n{status_icon}  #{prio}  {p['name']}")
    if bar:
        print(f"     📚 Lectures:  [{bar}] {lec_built}/{lec_total}")
    if sims:
        print(f"     🎮 Sims:      {sims}")
    if graphs:
        print(f"     📈 Graphs:    {graphs}")
    cost = p.get("cost", {}).get("estimated_total_cost_usd", 0)
    if cost:
        print(f"     💰 Est. Cost: ${cost:.2f}")
    print(f"     📁 {p.get('path', '')}")

def print_project_detail(p):
    sep = "─" * 60
    status_icon = {"active": "🟢", "exploring": "🟡", "paused": "🟠", "completed": "✅"}.get(p.get("status", ""), "⚪")
    print(f"\n{sep}")
    print(f"{status_icon}  {p['name']}")
    print(f"   ID:          {p['id']}")
    print(f"   Priority:    #{p.get('priority', '—')}")
    print(f"   Status:      {p.get('status', '—')}")
    print(f"   Path:        {p.get('path', '—')}")
    print(f"   Description: {p.get('description', '—')}")
    print()

    components = p.get("components", {})
    if components:
        print("   📦 Components:")
        for key, comp in components.items():
            c = comp if isinstance(comp, dict) else {}
            name = c.get("path", key)
            count = c.get("count", "")
            status = c.get("status", "")
            icon = {"complete": "✅", "built": "✅", "built_v1": "✅", "source_complete": "✅", "reference_complete": "✅"}.get(status, "🔄")
            print(f"      {icon} {key:25s}  {name}  {f'({count})' if count else ''}  {status}")

    print()
    print("   📋 Milestones:")
    for m in p.get("milestones", []):
        print(f"      • {m['date']} — {m['title']}")

    print()
    print("   🎯 Next Actions:")
    for a in p.get("next_actions", []):
        print(f"      ☐ {a}")

    cost = p.get("cost", {})
    if cost.get("estimated_total_cost_usd"):
        print()
        print(f"   💰 Cost: ${cost['estimated_total_cost_usd']:.2f} est. ({cost.get('estimated_total_tokens', 0):,} tokens)")
    print(f"\n{sep}")

# ── Dashboard ──────────────────────────────────────────────────────

def cmd_dashboard(html=False):
    data = load_projects()
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    if html:
        generate_html_dashboard(data, now)
        return

    # Markdown dashboard
    print(f"\n{'═'*60}")
    print(f"📊  PP Portfolio Dashboard  —  {now}")
    print(f"{'═'*60}")

    active = [p for p in data["projects"] if p.get("status") in ("active",)]
    exploring = [p for p in data["projects"] if p.get("status") in ("exploring",)]
    total_cost = sum(p.get("cost", {}).get("estimated_total_cost_usd", 0) for p in data["projects"])

    print(f"\n🟢 Active: {len(active)}  |  🟡 Exploring: {len(exploring)}  |  Total: {len(data['projects'])}")
    print(f"💰 Total Est. Cost: ${total_cost:.2f}")
    print()

    # Table
    print(f"{'Prio':>4}  {'Status':8}  {'Project':40s}  {'Lectures':10s}  {'Sims':4s}  {'Graphs':5s}  {'Cost':8s}")
    print(f"{'─'*4}  {'─'*8}  {'─'*40}  {'─'*10}  {'─'*4}  {'─'*5}  {'─'*8}")
    for p in sorted(data["projects"], key=lambda x: x.get("priority", 99)):
        prio = p.get("priority", 99)
        st = p.get("status", "")
        name = p["short_name"]
        lec = f"{p.get('lectures_built', 0)}/{p.get('lecture_count', 0)}" if p.get('lecture_count', 0) > 0 else "—"
        sim = p.get("simulations", 0)
        gr = p.get("graphs", 0)
        cost = p.get("cost", {}).get("estimated_total_cost_usd", 0)
        print(f"  #{prio:<2}  {st:8}  {name:40s}  {lec:>10}  {sim:<4}  {gr:<5}  ${cost:<5.2f}")

    print(f"\n{'═'*60}")
    print("🏆  Recommended Order:")
    print(f"{'═'*60}")
    for p in sorted(data["projects"], key=lambda x: (x.get("priority", 99), x.get("status", ""))):
        icon = {"active": "▶️", "exploring": "👉", "paused": "⏸️", "completed": "✅"}.get(p.get("status", ""), "❓")
        print(f"  {icon}  #{p['priority']}  {p['name']:45s}  [{p.get('status', '')}]")

def generate_html_dashboard(data, now):
    from datetime import datetime

    total_projects = len(data["projects"])
    active_count = len([p for p in data["projects"] if p.get("status") == "active"])
    exploring_count = len([p for p in data["projects"] if p.get("status") == "exploring"])
    total_cost = sum(p.get("cost", {}).get("estimated_total_cost_usd", 0) for p in data["projects"])
    total_lectures = sum(p.get("lecture_count", 0) for p in data["projects"])
    total_built = sum(p.get("lectures_built", 0) for p in data["projects"])
    total_sims = sum(p.get("simulations", 0) for p in data["projects"])
    total_graphs = sum(p.get("graphs", 0) for p in data["projects"])

    projects_html = ""
    for p in sorted(data["projects"], key=lambda x: x.get("priority", 99)):
        bar = progress_bar(p.get("lectures_built", 0), p.get("lecture_count", 0), 30)
        status_colors = {"active": "#4CAF50", "exploring": "#FF9800", "paused": "#FF5722", "completed": "#2196F3"}
        sc = status_colors.get(p.get("status", ""), "#9E9E9E")
        cost = p.get("cost", {}).get("estimated_total_cost_usd", 0)
        lec_str = f"{p.get('lectures_built', 0)}/{p.get('lecture_count', 0)}" if p.get('lecture_count', 0) > 0 else "—"

        next_actions = ""
        for a in p.get("next_actions", []):
            next_actions += f'<li>☐ {a}</li>'

        projects_html += f"""
        <div class="project-card" style="border-left: 4px solid {sc};">
            <div class="project-header">
                <span class="priority-badge" style="background:{sc};">#{p['priority']}</span>
                <h2>{p['name']}</h2>
                <span class="status-badge" style="background:{sc};">{p.get('status','')}</span>
            </div>
            <p class="desc">{p.get('description','')}</p>
            <div class="stats">
                <div class="stat"><span class="stat-label">📚 Lectures</span><span>{lec_str}</span></div>
                <div class="stat"><span class="stat-label">🎮 Sims</span><span>{p.get('simulations',0)}</span></div>
                <div class="stat"><span class="stat-label">📈 Graphs</span><span>{p.get('graphs',0)}</span></div>
                <div class="stat"><span class="stat-label">💰 Cost</span><span>${cost:.2f}</span></div>
            </div>
            <div class="progress-bar"><div class="progress-fill" style="width:{p.get('lectures_built',0)/max(p.get('lecture_count',0),1)*100}%; background:{sc};"></div></div>
            <div class="progress-label">Lecture Build Progress: {lec_str}</div>
            <details>
                <summary>🎯 Next Actions</summary>
                <ul>{next_actions}</ul>
            </details>
        </div>
        """

    html = f"""<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>📊 PP Dashboard — Project Portfolio</title>
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif; background:#1a1a2e; color:#e0e0e0; padding:20px; }}
.container {{ max-width:1200px; margin:0 auto; }}
h1 {{ font-size:1.8em; margin-bottom:5px; color:#e94560; }}
.subtitle {{ color:#888; margin-bottom:20px; }}
.stats-row {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(150px,1fr)); gap:12px; margin-bottom:24px; }}
.stat-card {{ background:#16213e; padding:16px; border-radius:12px; text-align:center; }}
.stat-card .number {{ font-size:2em; font-weight:700; color:#e94560; }}
.stat-card .label {{ font-size:0.85em; color:#888; margin-top:4px; }}
.project-card {{ background:#16213e; padding:20px; border-radius:12px; margin-bottom:16px; }}
.project-header {{ display:flex; align-items:center; gap:12px; margin-bottom:8px; flex-wrap:wrap; }}
.priority-badge {{ padding:2px 10px; border-radius:20px; font-size:0.8em; color:#fff; font-weight:600; }}
.status-badge {{ padding:2px 10px; border-radius:20px; font-size:0.8em; color:#fff; }}
.project-card h2 {{ font-size:1.2em; flex:1; }}
.desc {{ color:#aaa; font-size:0.9em; margin-bottom:12px; }}
.stats {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(120px,1fr)); gap:8px; margin-bottom:12px; }}
.stat {{ display:flex; justify-content:space-between; padding:6px 10px; background:#1a1a2e; border-radius:6px; font-size:0.9em; }}
.stat-label {{ color:#888; }}
.progress-bar {{ height:8px; background:#333; border-radius:4px; margin-bottom:4px; }}
.progress-fill {{ height:100%; border-radius:4px; transition:width 0.5s; }}
.progress-label {{ font-size:0.85em; color:#888; margin-bottom:10px; }}
details summary {{ cursor:pointer; color:#e94560; font-weight:600; padding:4px 0; }}
details ul {{ margin-top:8px; padding-left:20px; color:#aaa; }}
details li {{ margin-bottom:4px; }}
.footer {{ text-align:center; color:#555; margin-top:32px; font-size:0.85em; }}
</style>
</head>
<body>
<div class="container">
    <h1>📊 PP — Portfolio Dashboard</h1>
    <div class="subtitle">Last updated: {now}</div>

    <div class="stats-row">
        <div class="stat-card"><div class="number">{total_projects}</div><div class="label">Total Projects</div></div>
        <div class="stat-card"><div class="number">{active_count}</div><div class="label">🟢 Active</div></div>
        <div class="stat-card"><div class="number">{exploring_count}</div><div class="label">🟡 Exploring</div></div>
        <div class="stat-card"><div class="number">{total_lectures}</div><div class="label">📚 Lectures</div></div>
        <div class="stat-card"><div class="number">{total_sims}</div><div class="label">🎮 Sims</div></div>
        <div class="stat-card"><div class="number">${total_cost:.2f}</div><div class="label">💰 Est. Cost</div></div>
    </div>

    {projects_html}

    <div class="footer">PP Agent — InteractiveLecture/agents/PP/</div>
</div>
</body>
</html>"""

    with open(DASHBOARD_HTML, "w") as f:
        f.write(html)
    print(f"✅ HTML Dashboard generated: {DASHBOARD_HTML}")

# ── Cost ───────────────────────────────────────────────────────────

def cmd_cost():
    data = load_projects()
    rates = data.get("cost_rates", {}).get("deepseek_v4_flash", {})
    in_rate = rates.get("input_per_1k_tokens", 0)
    out_rate = rates.get("output_per_1k_tokens", 0)

    print(f"\n{'═'*60}")
    print("💰  PP Cost Analysis")
    print(f"{'═'*60}")
    print(f"\nModel: DeepSeek V4 Flash (OpenRouter)")
    print(f"  Input rate:  ${in_rate:.4f}/1K tokens")
    print(f"  Output rate: ${out_rate:.4f}/1K tokens")
    print()

    total_all = 0
    print(f"{'Project':40s}  {'Tokens':>10s}  {'Cost':>8s}")
    print(f"{'─'*40}  {'─'*10}  {'─'*8}")
    for p in sorted(data["projects"], key=lambda x: x.get("priority", 99)):
        cost = p.get("cost", {}).get("estimated_total_cost_usd", 0)
        tokens = p.get("cost", {}).get("estimated_total_tokens", 0)
        total_all += cost
        print(f"  {p['short_name']:38s}  {tokens:>8,}  ${cost:<5.2f}")

    print(f"\n{'─'*60}")
    print(f"{'TOTAL':40s}  {'':>10s}  ${total_all:.2f}")
    print()

    # What could still be done
    remaining_actions = 0
    for p in data["projects"]:
        remaining_actions += len(p.get("next_actions", []))
    est_remaining_tokens = remaining_actions * 50000  # rough estimate per action
    est_remaining_cost = (est_remaining_tokens * 0.7 * in_rate + est_remaining_tokens * 0.3 * out_rate) / 1000
    print(f"📊 Remaining tasks: {remaining_actions}")
    print(f"📊 Est. remaining tokens: {est_remaining_tokens:,}")
    print(f"📊 Est. remaining cost:   ${est_remaining_cost:.2f}")
    print(f"{'═'*60}")

# ── Update ─────────────────────────────────────────────────────────

def cmd_update(pid, *kv_pairs):
    data = load_projects()
    p = get_project(data, pid)
    if not p:
        print(f"❌ Project '{pid}' not found")
        print(f"   Available: {', '.join(x['id'] for x in data['projects'])}")
        return

    changes = []
    for pair in kv_pairs:
        if "=" not in pair:
            continue
        key, val = pair.split("=", 1)
        # Try numeric conversion
        try:
            val = int(val)
        except ValueError:
            try:
                val = float(val)
            except ValueError:
                pass
        p[key] = val
        changes.append(f"{key}={val}")

    # Re-scan if path changed
    if "path" in [c.split("=")[0] for c in changes]:
        scan_project(p)

    save_projects(data)
    print(f"✅ Updated '{pid}': {', '.join(changes)}")

# ── Next Actions ───────────────────────────────────────────────────

def cmd_next():
    data = load_projects()
    print(f"\n{'═'*60}")
    print("🎯  PP — Recommended Priority Plan")
    print(f"{'═'*60}")
    count = 1
    for p in sorted(data["projects"], key=lambda x: (x.get("priority", 99), x.get("status", ""))):
        actions = p.get("next_actions", [])
        if actions:
            icon = {"active": "▶️", "exploring": "👉"}.get(p.get("status", ""), "•")
            print(f"\n{icon}  #{p['priority']}  {p['name']}")
            for a in actions:
                print(f"     {count}. ☐  {a}")
                count += 1
    print(f"\n{'═'*60}")
    print(f"Total: {count-1} actions remaining")

# ── Main ───────────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return

    cmd = sys.argv[1]
    args = sys.argv[2:]

    commands = {
        "dashboard": cmd_dashboard,
        "status": cmd_status,
        "scan": cmd_scan,
        "cost": cmd_cost,
        "update": cmd_update,
        "next": cmd_next,
    }

    if cmd == "dashboard":
        html = "--html" in args
        cmd_dashboard(html)
    elif cmd == "status":
        pid = args[0] if args else None
        cmd_status(pid)
    elif cmd == "update":
        if len(args) < 2:
            print("Usage: pp.py update <project_id> <key=value> [...]")
        else:
            cmd_update(args[0], *args[1:])
    elif cmd in commands:
        commands[cmd]()
    else:
        print(f"❌ Unknown command: {cmd}")
        print("Available: dashboard, status, scan, cost, update, next")

if __name__ == "__main__":
    main()
