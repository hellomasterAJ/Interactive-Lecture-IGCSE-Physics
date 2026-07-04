#!/usr/bin/env python3
"""Apply all 6 changes to kinematics_stopping_v1.html"""

path = '/Users/masteraj/InteractiveLecture/graphs/kinematics_stopping_v1.html'

with open(path) as f:
    content = f.read()

changes = []

# ============================================================
# 1+2) Replace block from end of .theme-cosmic through .theme-sand
#      with: .theme-onedark, .theme-light, .theme-warm, .theme-sage
# ============================================================

old_block = '''  --green: #34d399; --rose: #fb7185; --violet: #c084fc; --amber: #fbbf24;
}
/* ── Light Theme 1: Warm Taupe ── */
.theme-warm {
  --bg: #cdc7bc; --card: #ddd7cc; --border: #bdb5a8;
  --text: #2d2a24; --text-dim: #635d52; --text-muted: #8c8578;
  --accent: #0f766e; --accent-glow: rgba(15,118,110,0.1);
  --grid: #c9c2b5; --graph-bg: #e8e2d7;
  --line-speed: #0f766e; --shade-think: rgba(15,118,110,0.06);
  --shade-brake: rgba(190,18,60,0.06);
  --green: #047857; --rose: #be123c; --violet: #6d28d9; --amber: #b45309;
}
/* ── Light Theme 2: Soft Sage ── */
.theme-sage {
  --bg: #d4d9cc; --card: #e3e7db; --border: #c2c9b5;
  --text: #2d2a24; --text-dim: #5d6b52; --text-muted: #8a9a78;
  --accent: #3d7a5a; --accent-glow: rgba(61,122,90,0.1);
  --grid: #c9d0bd; --graph-bg: #eef2e7;
  --line-speed: #3d7a5a; --shade-think: rgba(61,122,90,0.06);
  --shade-brake: rgba(157,78,60,0.06);
  --green: #2d6a4f; --rose: #9d4e3c; --violet: #6b4d8a; --amber: #9a7b3d;
}
/* ── Light Theme 3: Warm Sand ── */
.theme-sand {
  --bg: #d6cebd; --card: #e6ddd0; --border: #c4b9a6;
  --text: #2d2922; --text-dim: #6b6052; --text-muted: #928678;
  --accent: #b87a3a; --accent-glow: rgba(184,122,58,0.1);
  --grid: #ccc2b2; --graph-bg: #f0eae0;
  --line-speed: #b87a3a; --shade-think: rgba(184,122,58,0.06);
  --shade-brake: rgba(160,74,58,0.06);
  --green: #7a8a3d; --rose: #a04a3a; --violet: #7a4d8a; --amber: #c4902d;
}'''

new_block = '''  --green: #34d399; --rose: #fb7185; --violet: #c084fc; --amber: #fbbf24;
}
/* ── Dark Theme 4: One Dark ── */
.theme-onedark {
  --bg: #282c34; --card: #2c313a; --border: #3e4452;
  --text: #abb2bf; --text-dim: #848b98; --text-muted: #5c6370;
  --accent: #61afef; --accent-glow: rgba(97,175,239,0.12);
  --grid: #2c313a; --graph-bg: #21252b;
  --line-speed: #61afef; --shade-think: rgba(97,175,239,0.08);
  --shade-brake: rgba(224,108,117,0.08);
  --green: #98c379; --rose: #e06c75; --violet: #c678dd; --amber: #e5c07b;
}
/* ── Light Theme 1: Classic White ── */
.theme-light {
  --bg: #ffffff; --card: #f1f5f9; --border: #cbd5e1;
  --text: #0f172a; --text-dim: #475569; --text-muted: #94a3b8;
  --accent: #0f766e; --accent-glow: rgba(15,118,110,0.08);
  --grid: #c9c2b5; --graph-bg: #f8fafc;
  --line-speed: #0f766e; --shade-think: rgba(15,118,110,0.06);
  --shade-brake: rgba(190,18,60,0.06);
  --green: #047857; --rose: #be123c; --violet: #6d28d9; --amber: #b45309;
}
/* ── Light Theme 2: Warm Taupe ── */
.theme-warm {
  --bg: #cdc7bc; --card: #ddd7cc; --border: #bdb5a8;
  --text: #2d2a24; --text-dim: #635d52; --text-muted: #8c8578;
  --accent: #0f766e; --accent-glow: rgba(15,118,110,0.1);
  --grid: #c9c2b5; --graph-bg: #e8e2d7;
  --line-speed: #0f766e; --shade-think: rgba(15,118,110,0.06);
  --shade-brake: rgba(190,18,60,0.06);
  --green: #047857; --rose: #be123c; --violet: #6d28d9; --amber: #b45309;
}
/* ── Light Theme 3: Soft Sage ── */
.theme-sage {
  --bg: #d4d9cc; --card: #e3e7db; --border: #c2c9b5;
  --text: #2d2a24; --text-dim: #5d6b52; --text-muted: #8a9a78;
  --accent: #3d7a5a; --accent-glow: rgba(61,122,90,0.1);
  --grid: #c9d0bd; --graph-bg: #eef2e7;
  --line-speed: #3d7a5a; --shade-think: rgba(61,122,90,0.06);
  --shade-brake: rgba(157,78,60,0.06);
  --green: #2d6a4f; --rose: #9d4e3c; --violet: #6b4d8a; --amber: #9a7b3d;
}'''

assert old_block in content, "FAIL: old CSS block not found!"
content = content.replace(old_block, new_block, 1)
changes.append("1) Replaced .theme-sand with .theme-light (Classic White)")
changes.append("2) Added .theme-onedark CSS block")

# 3) Update road selector
old_road = '.theme-warm .road, .theme-sage .road, .theme-sand .road, .theme-mist .road, .theme-clay .road'
new_road = '.theme-warm .road, .theme-sage .road, .theme-light .road, .theme-mist .road, .theme-clay .road'
assert old_road in content, "FAIL: road selector not found!"
content = content.replace(old_road, new_road, 1)
changes.append("3) Updated road selector: .theme-sand .road -> .theme-light .road")

# 4) Reorder dropdown
old_dd = '''      <option value="dark">\U0001f319 Classic Dark</option>
      <option value="neon">\U0001f303 Cyberpunk Neon</option>
      <option value="vintage">\U0001f4dc Vintage Dark</option>
      <option value="cosmic">\U0001f30c Cosmic Void</option>
      <option value="warm">\U0001f305 Warm Taupe</option>
      <option value="sage">\U0001f33f Soft Sage</option>
      <option value="sand">\U0001f3dc\ufe0f Warm Sand</option>
      <option value="mist">\U0001f32b\ufe0f Mist Blue</option>
      <option value="clay">\U0001f3fa Warm Clay</option>'''

new_dd = '''      <option value="dark">\U0001f319 Classic Dark</option>
      <option value="neon">\U0001f303 Cyberpunk Neon</option>
      <option value="vintage">\U0001f4dc Vintage Dark</option>
      <option value="cosmic">\U0001f30c Cosmic Void</option>
      <option value="onedark">\U0001f535 One Dark</option>
      <option value="light">\u2600\ufe0f Classic White</option>
      <option value="warm">\U0001f305 Warm Taupe</option>
      <option value="sage">\U0001f33f Soft Sage</option>
      <option value="mist">\U0001f32b\ufe0f Mist Blue</option>
      <option value="clay">\U0001f3fa Warm Clay</option>'''

if old_dd in content:
    content = content.replace(old_dd, new_dd, 1)
    changes.append("4) Reordered dropdown (added onedark, light; removed sand)")
else:
    # Find the dropdown block by its open/close tags
    import re
    idx_start = content.find('value="dark"')
    idx_end = content.find('</select>', idx_start)
    assert idx_start > 0 and idx_end > 0, "FAIL: dropdown not found!"
    # Find start of line containing 'value="dark"'
    line_start = content.rfind('\n', 0, idx_start) + 1
    old_block_dd = content[line_start:idx_end]
    new_block_dd = '''      <option value="dark">\U0001f319 Classic Dark</option>
      <option value="neon">\U0001f303 Cyberpunk Neon</option>
      <option value="vintage">\U0001f4dc Vintage Dark</option>
      <option value="cosmic">\U0001f30c Cosmic Void</option>
      <option value="onedark">\U0001f535 One Dark</option>
      <option value="light">\u2600\ufe0f Classic White</option>
      <option value="warm">\U0001f305 Warm Taupe</option>
      <option value="sage">\U0001f33f Soft Sage</option>
      <option value="mist">\U0001f32b\ufe0f Mist Blue</option>
      <option value="clay">\U0001f3fa Warm Clay</option>'''
    content = content.replace(old_block_dd, new_block_dd, 1)
    changes.append("4) Reordered dropdown (relaxed match)")

# 5) Update setTheme()
old_set = "function setTheme(name){const tc=['theme-neon','theme-vintage','theme-cosmic','theme-warm','theme-sage','theme-sand','theme-mist','theme-clay'];document.body.classList.remove(...tc);if(name!=='dark')document.body.classList.add('theme-'+name);state.theme=name;drawGraph();}"
new_set = "function setTheme(name){const tc=['theme-neon','theme-vintage','theme-cosmic','theme-onedark','theme-light','theme-warm','theme-sage','theme-mist','theme-clay'];document.body.classList.remove(...tc);if(name!=='dark')document.body.classList.add('theme-'+name);state.theme=name;drawGraph();}"
assert old_set in content, "FAIL: setTheme() not found!"
content = content.replace(old_set, new_set, 1)
changes.append("5) Updated setTheme() (added onedark,light; removed sand)")

# 6) Update isDark()
old_id = "function isDark(){return state.theme==='dark'||state.theme==='neon'||state.theme==='vintage'||state.theme==='cosmic';}"
new_id = "function isDark(){return state.theme==='dark'||state.theme==='neon'||state.theme==='vintage'||state.theme==='cosmic'||state.theme==='onedark';}"
assert old_id in content, "FAIL: isDark() not found!"
content = content.replace(old_id, new_id, 1)
changes.append("6) Updated isDark() to include 'onedark'")

with open(path, 'w') as f:
    f.write(content)

print("SUCCESS - All changes applied:")
for c in changes:
    print(f"  {c}")
print(f"\nFile: {path}")