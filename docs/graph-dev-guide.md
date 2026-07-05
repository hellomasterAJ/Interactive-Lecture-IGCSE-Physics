# Interactive Graph Development Guide

> คู่มือสร้างและพัฒนา interactive kinematics graphs สำหรับ IGCSE Physics 0625

## Graph Library

Location: `~/InteractiveLecture/graphs/`

| File | Topic | Type |
|------|-------|------|
| `kinematics_graphs_v1.html` | Horizontal Motion (D‑T, V‑T, A‑T) | 3 stacked canvases + car animation + scene bg |
| `kinematics_freefall_v1.html` | Free-Fall (Vertical) | 3 stacked canvases + apple + scene backgrounds |
| `kinematics_stopping_v1.html` | Stopping Distance | V‑T graph + car SVG + road/obstacle/scenarios |
| `kinematics_vt_graph_v1.html` | Advanced VT Graph | Dual-mode: Uniform (SUVAT proofs) + Non-uniform (scenarios) |

---

## Layout Structure (VT Graph — `kinematics_vt_graph_v1.html`)

### Main Grid
```css
.main-grid{display:grid; grid-template-columns: 3fr 1fr; gap:12px; align-items:start; min-width:0;}
```

### Left Column (`.graph-col`)
```css
.graph-col{display:flex; flex-direction:column; gap:10px; min-width:0;}
```
**Order:**
1. **Velocity–Time Graph card** (`.graph-card`) — always shown
2. **Uniform Acceleration Parameters** (`#uniformControls`, `.ctrl-card`) — shown in Uniform mode, `display:none` in Non-uniform
3. **Motion Scenario** (`#nuScenarioCard`, `.ctrl-card`) — shown in Non-uniform mode, `display:none` in Uniform
4. **Key Concept** (`#descBox`, `.desc-box`) — always shown

All children auto-width to the column (same width as graph card).

### Right Panel (`.right-panel`)
```css
.right-panel{display:flex; flex-direction:column; gap:10px; min-width:0; overflow:hidden;}
```
**Order:**
1. **Values** — `#valGridUniform` / `#valGridNonuniform`
2. **Equation** (`#eqCard`, `.info-card`) — Uniform only
   - Title → eqDisplay → proofTabs → areaBreakdownContainer → **📖 Define button + panel**
3. **Scenario Equations** (`#nuEqCard`, `.info-card`) — Non-uniform only
4. **Analysis Tool** (`#nuAnalysisCard`, `.ctrl-card`) — Non-uniform only
   - Gradient/Area buttons → dynamic params (time/strips slider) → ▶ Animate button

---

## switchMode() Toggle Pattern

```javascript
function switchMode(mode) {
  // HIDE ALL
  document.getElementById('uniformControls').style.display = mode === 'uniform' ? 'block' : 'none';
  document.getElementById('nuScenarioCard').style.display = mode === 'nonuniform' ? 'block' : 'none';
  document.getElementById('nuAnalysisCard').style.display = mode === 'nonuniform' ? 'block' : 'none';
  document.getElementById('valGridUniform').style.display = mode === 'uniform' ? 'grid' : 'none';
  document.getElementById('valGridNonuniform').style.display = mode === 'nonuniform' ? 'grid' : 'none';
  document.getElementById('eqCard').style.display = mode === 'uniform' ? 'block' : 'none';
  document.getElementById('nuEqCard').style.display = mode === 'nonuniform' ? 'block' : 'none';
  document.getElementById('proofTabs').style.display = mode === 'uniform' ? 'flex' : 'none';
}
```

---

## 📖 Define Button — ใน Equation Card

วาง **📖 Define** + definePanel ไว้ที่ **ล่างสุดของ `#eqCard`** ต่อจาก `areaBreakdownContainer`

```html
<!-- Equation card -->
<div class="info-card" id="eqCard">
  <div class="i-title">📐 Equation</div>
  <div class="eq-box" id="eqDisplay">...</div>
  <div class="proof-tabs" id="proofTabs">...</div>
  <div id="areaBreakdownContainer"></div>
  
  <!-- Define — ใช้ <div> ธรรมดา ห้ามใช้ .ctrl-row -->
  <div style="margin-top:8px;">
    <button class="ctrl-btn" onclick="toggleDefine()" id="defineBtn">📖 Define</button>
  </div>
  <div id="definePanel" style="display:none;margin-top:6px;background:var(--bg);
       border:1px solid var(--border);border-radius:6px;padding:8px 10px;
       box-sizing:border-box;...">
    <b style="color:var(--accent);">s</b> = displacement ...<br>
    ...
  </div>
</div>
```

**⚠️ Pitfall:** ห้ามใช้ `.ctrl-row` (`display:flex;flex-wrap:wrap`) ภายใน `info-card` ฝั่งขวา เพราะ `overflow:hidden` บน `.right-panel` ทำให้ flex-wrap ทำงานผิด → layout แตก ใช้ `<div>` เปล่าธรรมดาแทน + `box-sizing:border-box` ใน panel.

---

## Analysis Tool — Animate Button ใต้ Slider

ลำดับใน `.ctrl-card#nuAnalysisCard`:
```
📐 Gradient / 📊 Area  (ปุ่ม mode)
─────────────────────────────────
t = [====slider====] 10.0 s   (time slider → nuAnalysisParams)
─────────────────────────────────
▶ Animate                     (ปุ่ม tracer → อยู่ล่างสุด)
```

```html
<div class="ctrl-card" id="nuAnalysisCard">
  <div class="c-title">🔬 Analysis Tool</div>
  <div class="ctrl-row">
    <button class="mode-tab" data-analysis="gradient">📐 Gradient</button>
    <button class="mode-tab" data-analysis="area">📊 Area</button>
  </div>
  <div id="nuAnalysisParams" class="ctrl-row" style="margin-top:4px;"></div>
  <div class="ctrl-row" style="margin-top:4px;">
    <button class="ctrl-btn primary" id="animTracerBtn">▶ Animate</button>
  </div>
</div>
```

`buildNuAnalysis()` เติม HTML เข้าไปใน `#nuAnalysisParams`:
```javascript
function buildNuAnalysis() {
  const el = document.getElementById('nuAnalysisParams');
  if(state.nuAnalysis === 'gradient') {
    el.innerHTML = `<div class="slider-group"><label>t =</label>
      <input type="range" id="nuGradSlider" min="0" max="${tMax}" value="..." step="0.1" ...>
      <span class="slider-val" id="nuGradVal">...</span><label>s</label></div>`;
  } else {
    el.innerHTML = `<div class="slider-group"><label>Strips</label>
      <input type="range" id="nuStripSlider" min="1" max="20" value="..." step="1" ...>
      <span class="slider-val" id="nuStripVal">...</span></div>`;
  }
}
```

---

## Axis Tick Standard: `niceStep()`

```javascript
function niceStep(range, targetTicks = 5) {
  if(range <= 0) return 1;
  const rough = range / targetTicks;
  const magnitude = Math.pow(10, Math.floor(Math.log10(rough)));
  const norm = rough / magnitude;
  let nice;
  if(norm < 1.5) nice = 1;
  else if(norm < 3.5) nice = 2;
  else if(norm < 7.5) nice = 5;
  else nice = 10;
  return nice * magnitude;
}
```
Apply in ALL draw functions. Use `let` for yMin/yMax.

---

## SUVAT Proofs (Uniform Mode)

| Proof | Equation | Visual | Colors |
|-------|----------|--------|--------|
| 0 | `v = u + a t` | No shading | — |
| 1 | `s = u·t + ½·a·t²` | Rectangle (u·t) + Right triangle (½·a·t²) at RIGHT `(0,u)→(t,u)→(t,v)` | 🟢 Green + 🩷 Rose |
| 2 | `s = v·t − ½·a·t²` | Big rect (v·t) + Subtracted triangle at LEFT `(0,u)→(0,v)→(t,v)` | 🔵 Blue + 🟠 Orange |
| 3 | `s = ½(u+v)·t` | Rectangle at average velocity = ½(u+v) | 🟡 Amber |
| 4 | `v² = u² + 2 a s` | Algebraic derivation only, no shading | — |

---

## Non-uniform Scenario Pattern

```javascript
const SCENARIOS = {
  terminal: {
    name: '🪂 Skydriver', tMax: 8, vMin: 0,
    v: (t, p) => p.Vt * (1 - Math.exp(-t / p.tau)),
    dv: (t, p) => (p.Vt / p.tau) * Math.exp(-t / p.tau),
    integral: (t, p) => p.Vt * (t + p.tau * (Math.exp(-t / p.tau) - 1)),
    params: [{id: 'Vt', label: 'V_term', min:5, max:80, def:40, step:1, unit:'m/s'},
             {id: 'tau', label: 'τ', min:0.5, max:8, def:2, step:0.1, unit:'s'}]
  },
  rocket: { /* v = vex·ln(1 + t/τ) */ },
  shm: { /* v = A·(2π/T)·sin(2πt/T) */ },
  jerk: { /* v = ½·k·t², a = k·t */ }
};
```

Dynamic sliders from `params[]` via `buildNuSliders()`.

**Analysis tools:**
- **Gradient:** Tangent line at t → `a = dv/dt`
- **Area:** Trapezoidal rule with N strips (1–20), estimate vs exact vs error%

---

## Tangent Line — Pixel-Space Slope

```javascript
const xScale = gW / tMax;
const yScale = gH / (yMax - yMin);
const slopePx = -aPt * yScale / xScale;    // invert Y-axis
const angle = Math.atan(slopePx);
const len = 80;
ctx.moveTo(tx - len*Math.cos(angle), ty - len*Math.sin(angle));
ctx.lineTo(tx + len*Math.cos(angle), ty + len*Math.sin(angle));
```

---

## KaTeX Integration

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
```

**Per-line render (recommended for multi-line):**
```javascript
el.innerHTML = '';
const container = document.createElement('div');
container.style.cssText = 'display:flex;flex-direction:column;gap:2px;padding:4px 0;';

for(const line of eqLines) {
  const div = document.createElement('div');
  try { katex.render(line, div, {displayMode:false, throwOnError:false}); }
  catch(e) { div.textContent = line; }
  container.appendChild(div);
}
el.appendChild(container);
```

### Backslash Escaping in Template Literals

| LaTeX Command | In HTML Template Literal | JS String | Rule |
|---|---|---|---|
| `\frac`, `\tau`, `\omega`, `\cos`, `\sin`, `\text` | `\\frac` = **2** backslashes | `\frac` (1) | ✅ Normal |
| `\begin{aligned}`, `\end{aligned}` | `\\\\begin` = **4** backslashes | `\\begin` (2) | ✅ Special  |

**Golden rule:** `\command` → `\\command` (2→1). `\begin/end` → `\\\\begin/end` (4→2). Never write 4 before `frac`, `tau`, `text`.

---

## Graph Canvas
- Size: `780×400`
- Padding: `{top:22, right:18, bottom:28, left:48}`
- Axis font: 11px Inter
- Area labels: bold 13px JetBrains Mono

---

## Common Pitfalls

| # | Pitfall | Fix |
|---|---------|-----|
| 1 | **Y-axis scaling** | accel-time range = `value × 1.5` |
| 2 | **Stray `</div>` after remove** | Verify `open-div count === close-div count` after removing elements |
| 3 | **`.ctrl-row` in `info-card`** | ใช้ `<div>` เปล่าแทนสำหรับ single-element inserts |
| 4 | **`write_file` destroys large files** | Always use `patch` for files > 500 lines |
| 5 | **niceStep not applied** | Apply in ALL draw functions, use `let` for yMin/yMax |
| 6 | **a=0 handling** | Skip triangle rendering AND area breakdown row |
| 7 | **KaTeX backslash** | `\\command` in template literal (2→1), `\\\\begin` (4→2) |
| 8 | **isDark() undefined** | Must define before use — causes silent ReferenceError |
| 9 | **Constant Jerk defaults** | k: 0.5, range 0.1–2, tMax=8s, emoji 🏎️ |
| 10 | **eq-box-sm class** | Add `.eq-box-sm .katex{font-size:0.85rem;}` for compact equations |

---

## File Organization

```
~/InteractiveLecture/
├── references/scientists/   ← Bio library
├── graphs/                  ← Interactive HTML files
├── lectures/                ← Lecture.md source files
├── scripts/                 ← Build system (build.py, parse_lecture.py, pdf_export.py)
├── docs/                    ← Development guides (this file)
└── output/                  ← Generated HTML + PDF + JSON
```