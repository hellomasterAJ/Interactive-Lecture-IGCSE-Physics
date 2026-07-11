# Vivi's Master Prompt — สร้าง 2D Physics Simulation / Interactive Graph

> **Author:** วีวี่ (Vivi) — Science Content Agent  
> **Version:** 1.0.0  
> **วันที่:** 2026-07-09  
> **ครอบคลุม:** physics-simulation-2d + physics-graph-authoring skills  
> **เหมาะสำหรับ:** AI Agent ที่ต้องสร้าง standalone HTML+Canvas physics simulation หรือ interactive graph

---

## 📋 ภาพรวม

Prompt นี้เป็นชุดคำสั่งที่สมบูรณ์สำหรับ AI ในการสร้าง **2D Physics Simulation** หรือ **Interactive Graph** แบบ standalone HTML ไฟล์เดียว สำหรับ HAUS Academy (IGCSE / A-Level Physics)

มี 2 ประเภทหลัก:
1. **ประเภท Simulation** — Equipment / Virtual Lab / Interactive Demo (มี Simulate/Practice/Quiz modes)
2. **ประเภท Graph** — Kinematics graphs, physics data visualization (มี 11 themes, niceStep ticks, animation loop)

---

## 🎯 ส่วนที่ 1: ข้อกำหนดพื้นฐาน (สำหรับทั้ง 2 ประเภท)

### 1.1 โครงสร้างไฟล์
- **ไฟล์เดียว standalone** — HTML + CSS + JS ทั้งหมดในไฟล์เดียว
- **ไม่พึ่งพา external libraries** (ยกเว้น Google Fonts Inter + JetBrains Mono, และ KaTeX สำหรับสมการ)
- **ชื่อไฟล์:** `~/InteractiveLecture/simulations/<topic>_<description>.html` หรือ `~/InteractiveLecture/graphs/<topic>_<description>.html`
- **Encoding:** UTF-8, DOCTYPE html

### 1.2 HAUS Design Tokens (ต้องใช้ทุกครั้ง)

```css
:root{
  --bg:#0d1117; --card:#161b22; --card2:#1c2430; --border:#30363d;
  --text:#e6edf3; --dim:#8b949e; --accent:#e3b341; --blue:#58a6ff;
  --green:#3fb950; --red:#f85149; --gold:#ffd700;
}
```

**บทบาทของสี:** `--accent` (ทอง) = ค่าอ่านหลัก, `--blue` = mode selection, `--green` = success, `--red` = wrong

### 1.3 State Discipline (สำคัญมาก!)

```javascript
const S = {
  // state variables ทั้งหมด
};
const $ = id => document.getElementById(id);
const snap = v => Math.round(v / step) * step;  // snap to grid
```

- **State object `S` ตัวเดียว** — `draw()` และ `updateUI()` เป็น pure functions ที่ derive ทุกอย่างจาก `S`
- **Derived quantities = arrow function getters** (`const obs = () => ...`) — ห้าม cached copy
- **Formatting function `fmt()` หนึ่งเดียว** — ใช้ทุกที่ (canvas, badges, cards, feedback) ไม่ให้ค่าไม่ตรงกัน

### 1.4 Brand Logo (toolbar corner)

```html
<div class="brand">...</div>
```
- **ตำแหน่ง:** absolute ที่ `right:16px; top:50%; translateY(-50%)` ใน toolbar
- **สี:** `background:#F4C01E; border-radius:10px; box-shadow:0 2px 5px rgba(0,0,0,.4)`
- **รูป:** HAUS logo base64 หรือ PNG ที่ `width:56px`
- **ซ่อนที่ 640px:** `@media (max-width:640px){.brand{display:none}}`

---

## 🎮 ส่วนที่ 2: ประเภท Simulation (Equipment / Virtual Lab)

ใช้สร้าง: Vernier caliper, Micrometer, Balance & Newtonmeter, Force lab, Density lab, Collision lab, Energy skate park, etc.

### 2.1 Toolbar — Fixed 2 Rows (Zero Layout Shift)

กฎเหล็ก: **toolbar ห้ามขยับ** เมื่อเปลี่ยน mode/tier ใช้ `.pills.locked{opacity:.5;pointer-events:none}` แทน `display:none`

```html
<div class="toolbar">
  <div class="trow">
    <!-- Row 1: Mode selectors (Simulate / Practice / Quiz) -->
  </div>
  <div class="trow">
    <!-- Row 2: Controls (resolution, zoom, guide toggle, etc.) -->
  </div>
</div>
```

```javascript
function bindPills(id, cb){
  $(id).addEventListener("click", e => {
    const b = e.target.closest(".pill"); if(!b) return;
    [...$(id).children].forEach(x => x.classList.remove("active"));
    b.classList.add("active"); cb(b.dataset);
  });
}
```

### 2.2 Three Standard Modes

| Mode | locked | reveal | กลไก |
|---|---|---|---|
| **Simulate** | false | true | Slider/🎲 ปรับค่าได้อิสระ |
| **Practice** | true | false→true on Check | Random target → กรอก answer → ✓ Check แสดง worked solution |
| **Quiz** | true | false→true จบ | 5 ข้อ → submit → stars (5/5→★★★, 4→★★, 3→★) + results table |

**Practice flow:** `newPractice()` → randomize target (ต้อง snap to grid: `5 + Math.round(Math.random()*steps) * resolution`) → animateTo → locked → กรอก answer → Check: เปรียบเทียบ `|ans − target| < resolution/2` → set `reveal=true` → แสดง decomposition (เช่น `MSR + VSR×LC`, `Observed − ZE = Corrected`)

**Quiz:** pre-generate 5 questions → submit → แสดง stars + ตาราง `{target, error, ans, ok}`

### 2.3 Reading Math + Zero Error Chain

```javascript
// Reading decomposition — ต้อง standalone test ได้!
const ze    = () => S.zeOn ? r2(S.zeDiv * S.lc) : 0;
const obs   = () => r2(S.opening + ze());
const reading = () => {
  // เช่น: MSR + VSR × LC
  const msr = Math.floor(obs() / PITCH) * PITCH;
  const vsr = Math.round((obs() - msr) / S.lc);
  return { msr, vsr, total: r2(msr + vsr * S.lc) };
};
```

**Zero Error chain visualization:** แสดงเป็น card 3 ช่อง: `Observed → ZE → Corrected`
- `ZE = zeDiv × LC` (zeDiv ∈ −5..+5)
- จัดการ negative ZE ที่ตำแหน่งปิด: `ZE = −(N − i) × LC`

### 2.4 Interaction Patterns

**Pointer-drag (หลัก):**
```javascript
cv.addEventListener("pointerdown", e => {
  if (S.locked) return;
  dragging = true; dragX = e.clientX; dragStart = S.value;
  cv.setPointerCapture(e.pointerId);
});
cv.addEventListener("pointermove", e => {
  if (!dragging || S.locked) return;
  const dx = (e.clientX - dragX) / (pxPerUnit * (S.zoom ? S.zoomF : 1));
  setValue(dragStart + dx);
});
cv.addEventListener("pointerup", () => dragging = false);
```
- ใช้ Pointer events (ไม่ใช่ mouse) = touch support ฟรี
- `touch-action:none` บน canvas

**Double-click zoom (มาตรฐาน):**
```javascript
canvas.ondblclick = () => { S.zoom = !S.zoom; updateUI(); };
if (S.zoom) {
  ctx.translate(W/2 - focusX*S.zoomF, H*0.48 - focusY*S.zoomF);
  ctx.scale(S.zoomF, S.zoomF);
}
```
- Zoom = mode (ไม่ใช่ lens) — double-click toggle, Esc exit
- มี corner pill: `"🔍 Zoom: ON — double-click to exit"`
- Drag ยัง work ขณะ zoom (delta หารด้วย zoomF)

**Keyboard fine-stepping:**
```javascript
window.addEventListener("keydown", e => {
  if (e.target.tagName === "INPUT" && e.target.type === "number") return;
  if (e.key === "Escape" && S.zoom) { S.zoom = false; updateUI(); }
  if (S.locked) return;
  const step = e.shiftKey ? coarse : S.resolution;
  if (e.key === "ArrowRight") { setValue(S.value + step); e.preventDefault(); }
  if (e.key === "ArrowLeft") { setValue(S.value - step); e.preventDefault(); }
});
```

**WebAudio tick (ข้าม unit):**
```javascript
function tickSound() {
  try {
    const ac = new (window.AudioContext || window.webkitAudioContext)();
    const osc = ac.createOscillator();
    const gain = ac.createGain();
    osc.type = 'sine'; osc.frequency.value = 1400;
    gain.gain.value = 0.025;
    gain.gain.exponentialRampToValueAtTime(0.001, ac.currentTime + 0.05);
    osc.connect(gain); gain.connect(ac.destination);
    osc.start(); osc.stop(ac.currentTime + 0.05);
  } catch(e) {}
}
```

**Drag-and-drop objects (วางวัตถุบนเครื่องมือ):**
- แต่ละ object มี state: `"shelf" | "pan" | "hook" | "drag"`
- Drop zones ต้อง cover ความสูงสูงสุดของ stack
- Rejected drop → snap กลับ home slot
- Auto-ranging: `effRange()` — include object ที่กำลังลาก
- Spring pointer: `v += (target-x)*0.16; v *= 0.74; x += v`

### 2.5 Canvas Realism (Procedural Drawing)

**Metal gradient helper:**
```javascript
function metal(x0,y0,x1,y1,bright){
  const g = ctx.createLinearGradient(x0,y0,x1,y1);
  if(bright){ g.addColorStop(0,"#aeb6bf"); g.addColorStop(.45,"#e2e7ec"); g.addColorStop(1,"#939da8"); }
  else      { g.addColorStop(0,"#8b95a0"); g.addColorStop(.5,"#c3cbd3"); g.addColorStop(1,"#7c8791"); }
  return g;
}
```

**Realism stack (apply ตามลำดับ):**
```javascript
const path = () => { ctx.beginPath(); /* faceted outline */ ctx.closePath(); };
// 1. body + drop shadow
ctx.save();
ctx.shadowColor="rgba(0,0,0,.45)"; ctx.shadowBlur=10;
ctx.shadowOffsetX=4; ctx.shadowOffsetY=4;
ctx.fillStyle = gradientBrightAtLitSide;
path(); ctx.fill();
ctx.restore();
// 2. clipped details
ctx.save(); path(); ctx.clip();
//   brushed texture: horizontal hairlines every 3px, rgba(255,255,255,.05)
//   polished contact face: 5-8px white→transparent gradient strip
//   ground step: lighter rect + dark 1px border
//   facet lines: bright on lit bevel, dark rgba(30,38,48,.5) on cutting edges
ctx.restore();
// 3. crisp 1px outline (#454f59)
path(); ctx.stroke();
```

**กฎเหล็ก Canvas:**
1. **Moving parts ต้องไม่บัง scales** — ถ้าชิ้นส่วนเคลื่อนที่บัง刻度ที่ตำแหน่งใด แสดงว่าออกแบบผิด
2. **ไม่มีข้อความบน scales** — ใช้ DOM chips/chrome overlays แทน
3. **รูปทรงเหลี่ยม faceted** — ไม่กลม (machined metal = sharp, chamfered, stepped)
4. **Chisel-point blade** — ปลาย sharp measuring edge + bevel ด้านเดียว

### 2.6 UI Components

**Badges row:**
```css
.badge{background:var(--card);border:1px solid var(--border);border-radius:20px;padding:5px 14px;font-size:12px;color:var(--dim)}
.badge b{color:var(--text);font-family:ui-monospace,monospace}
```

**Cards grid:**
```css
.card{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:12px 14px;text-align:center}
.card .cv{font-size:24px;font-weight:700;font-family:ui-monospace,monospace}
.card .cu{font-size:11px;color:var(--dim)}
.card .cl{font-size:11px;color:var(--dim);margin-top:3px}
```

**Formula panel:**
- Line 1: สูตรทั่วไป (blue, monospace) เช่น `TR = MSR + (VSR × LC)`
- Line 2: live substitution เช่น `= 23 + (4 × 0.1) = 23.4 mm`
- เมื่อ `reveal=false`: ใช้ `?` และข้อความ `← read the scales!`

---

## 📈 ส่วนที่ 3: ประเภท Graph (Interactive Physics Graph)

ใช้สร้าง: Kinematics graphs (d-t, v-t, a-t), freefall, terminal velocity, stopping distance, etc.

### 3.1 Theme System (11 Themes)

| Value | Label | Type |
|---|---|---|
| `dark` (default :root) | Classic Dark | Dark |
| `hausnight` | HAUS Night | Dark |
| `vintage` | Vintage Dark | Dark |
| `neon` | Cyberpunk Neon | Dark |
| `cosmic` | Cosmic Void | Dark |
| `onedark` | One Dark | Dark |
| `light` | Classic Light | Light |
| `haus` | HAUS Day | Light |
| `clay` | Warm Clay | Light |
| `sage` | Soft Sage | Light |
| `mist` | Mist Blue | Light |

**CSS variables ต่อ theme:**
```css
--bg --card --border --text --text-dim --text-muted
--accent --accent-glow --grid --graph-bg
--green --rose --violet --amber --blue --orange
```

**HAUS brand themes (พิเศษ):**
```css
.theme-haus{--bg:#F4EEE0;--card:#FFFFFF;--border:#E4DAC4;--text:#1A1712;--text-dim:#5B5344;--accent:#A9820F;--graph-bg:#FCFAF2}
.theme-hausnight{--bg:#1a1c20;--card:#26282d;--border:#3a3c42;--text:#FFFFFF;--text-dim:#e0e2e8;--accent:#F4C01E;--graph-bg:#121418}
```

**setTheme() function:**
```javascript
function setTheme(name) {
  const tc = ['theme-neon','theme-vintage','theme-cosmic','theme-onedark','theme-light','theme-warm','theme-sage','theme-mist','theme-clay','theme-haus','theme-hausnight'];
  document.body.classList.remove(...tc);
  if (name !== 'dark') document.body.classList.add('theme-' + name);
  state.theme = name;
  document.body.classList.toggle('logo-dark', isDark());
  drawGraph(); // redraw
}
function isDark() {
  return ['dark','neon','vintage','cosmic','onedark','hausnight'].includes(state.theme);
}
```

**HAUS overrides (ทุก graph ต้องมี):**
```css
.theme-haus .top-bar h1,.theme-haus .top-bar h1 span{color:#1A1712;}
.theme-haus .badge-top{background:#F4C01E;color:#1A1712;border-color:#1A1712;}
.theme-hausnight .top-bar h1,.theme-hausnight .top-bar h1 span{color:#FFFFFF;}
```

### 3.2 DPR-aware Canvas Setup

```javascript
function drawGraph() {
  const c = document.getElementById('graphCanvas');
  const ctx = c.getContext('2d');
  const dpr = window.devicePixelRatio || 1;
  const cssW = c.clientWidth || 520;
  const cssH = Math.round(cssW * (300 / 520));  // aspect ratio
  if (c.width !== Math.round(cssW * dpr) || c.height !== Math.round(cssH * dpr)) {
    c.width = Math.round(cssW * dpr);
    c.height = Math.round(cssH * dpr);
  }
  c.style.height = cssH + 'px';
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  // drawing code ใช้ cssW, cssH
}
```

**หมายเหตุ:** ใช้ `Math.round()` เสมอสำหรับ DPR dimensions — fractional values ทำให้ sub-pixel aliasing

### 3.3 Standard Padding (ทุก graph ใช้ค่าเดียวกัน!)

```javascript
const pad = { top: 18, right: 16, bottom: 32, left: 38 };
const gW = cssW - pad.left - pad.right;
const gH = cssH - pad.top - pad.bottom;
```

### 3.4 niceStep() Tick Algorithm (MANDATORY!)

**ทุก graph ต้องใช้ `niceStep()` สำหรับทั้ง X และ Y axis ห้ามใช้ step ตายตัวเด็ดขาด**

```javascript
function niceStep(range, targetTicks) {
  if (range <= 0) return 1;
  const rough = range / targetTicks;
  const magnitude = Math.pow(10, Math.floor(Math.log10(rough)));
  const norm = rough / magnitude;
  let nice;
  if (norm < 1.5) nice = 1;
  else if (norm < 3.5) nice = 2;
  else if (norm < 7.5) nice = 5;
  else nice = 10;
  return nice * magnitude;
}
```

**X-axis ticks:**
```javascript
const xStep = niceStep(xMax, 8);
const xMaxNice = Math.ceil(xMax / xStep) * xStep;
ctx.font = '10px Inter, sans-serif';
ctx.textAlign = 'center'; ctx.textBaseline = 'top';
for (let i = 0; i <= Math.round(xMaxNice / xStep); i++) {
  const xv = i * xStep;
  ctx.fillText(xv % 1 === 0 ? xv.toFixed(0) : xv.toFixed(1), pad.left + (xv / xMaxNice) * gW, pad.top + gH + 5);
}
```

**Y-axis ticks:**
```javascript
const yStep = niceStep(yMax, 8);
ctx.textAlign = 'right'; ctx.textBaseline = 'middle';
ctx.font = '10px Inter, sans-serif';
for (let yv = 0; yv <= yMax + 0.001; yv += yStep) {
  const y = pad.top + gH - (yv / yMax) * gH;
  ctx.fillText(yv % 1 === 0 ? yv.toFixed(0) : yv.toFixed(1), pad.left - 4, y);
}
```

### 3.5 Font Sizes (ตายตัว!)

| Element | Size | Font |
|---|---|---|
| Tick labels | `10px` | Inter, sans-serif |
| Axis titles | `11px` | Inter, sans-serif |
| Data values | `0.65rem` / `0.75rem` | JetBrains Mono |
| Stat labels | `0.45rem` / `0.55rem` | JetBrains Mono |

**Axis titles position:**
```javascript
// X-axis
ctx.font = '11px Inter, sans-serif';
ctx.textAlign = 'center'; ctx.textBaseline = 'alphabetic';
ctx.fillText('Time / s', pad.left + gW / 2, cssH - 9);

// Y-axis (rotated)
ctx.save();
ctx.translate(14, pad.top + gH / 2);  // Y-label x=14 เสมอ!
ctx.rotate(-Math.PI / 2);
ctx.textAlign = 'center'; ctx.textBaseline = 'bottom';
ctx.fillText('Velocity / (m/s)', 0, 0);
ctx.restore();
```

### 3.6 Physics Engine Patterns

#### Uniform Acceleration (suvat)
```javascript
function getFinalV(u, a, t) { return u + a * t; }
function getDisplacement(u, a, t) { return u * t + 0.5 * a * t * t; }
```

#### Jerk Model (a(t) = a₀ + j·t)
```javascript
function getJerk() { return state.accelPattern === 'constant' ? 0 : state.accelPattern === 'increase' ? 0.5 : -0.5; }
function getAccelAt(t) { return a0 + j * t; }
function getSpeedAt(t) { return u + a0*t + 0.5*j*t*t; }
function getDistance(t) { return s0 + u*t + 0.5*a0*t*t + (1/6)*j*t*t*t; }
function getStopTime() { /* solve v(t)=0 */ }
```

#### Freefall (g ∈ [-100, +100], y ∈ [0, 100])
```javascript
function getY(t) { return state.y0 + state.u*t + 0.5*state.g*t*t; }
function getV(t) { return state.u + state.g*t; }
```

#### Stopping Distance
```javascript
const sd = speed * reactionTime;        // thinking distance
const tb = -speed / deceleration;       // braking time
const bd = speed*tb + 0.5*decel*tb*tb; // braking distance
const st = sd + bd;                     // total stopping distance
```

#### Terminal Velocity (tanh model)
```javascript
function vAt(t) {
  if(t <= td) return vt1 * Math.tanh(G * t / vt1);               // Phase 1: freefall
  const vDeploy = vAt(td);
  return vt2 + (vDeploy - vt2) * Math.exp(-(t - td) / tau2Eff);   // Phase 2: parachute
}
```

### 3.7 Animation Loop

```javascript
state.dt = 0.04;   // time step
state.animId = null;
state.playing = false;

function loop() {
  if(!state.playing) return;
  state.time += state.dt;
  if(state.time >= getStopTime()) { state.time = getStopTime(); pause(); updateDisplay(); return; }
  updateDisplay();
  state.animId = requestAnimationFrame(loop);
}

function togglePlay() {
  if(state.playing) pauseAnimation();
  else startAnimation();
}
function startAnimation() { state.playing = true; state.animId = requestAnimationFrame(loop); }
function pauseAnimation() { state.playing = false; if(state.animId) cancelAnimationFrame(state.animId); }
```

**Velocity-aware ground check (freefall) → CRITICAL:**
```javascript
if (y < 0 || (y <= 0 && v <= 0) || state.time >= state.maxTime) { pauseStop(); return; }
```
ถ้าไม่มี `v <= 0` — การโยนขึ้น (y₀=0, u>0) จะตายทันที!

### 3.8 Scene Backgrounds

**Earth:** ไล่สีฟ้า `earth-sky` opacity 12%, ☁️ clouds drift left, 🕊️ birds fly
**Moon/Space:** 🚀 spaceship drift, 👨‍🚀 astronauts, ✨ twinkle stars (JS seeded random, ห้าม `Math.random()` ใน `draw()`)
**Mars:** ส้ม/แดง terrain gradient, Mars rover (CSS art: wheels + solar panel + antenna), heat haze shimmer
**City:** 3-layer buildings, window lights
**Highway:** Sunset gradient, barriers, skyline
**Rain:** 100 raindrops JS, lightning flash
**Snow:** 50 snowflakes JS, white ground cover

### 3.9 Button Order (MUST!)

```html
<button class="ctrl-btn" onclick="reset()">↺ Reset</button>
<button class="ctrl-btn random" onclick="random()">🎲 Random</button>
<button class="ctrl-btn primary" onclick="togglePlay()">▶ Play</button>
```

ลำดับนี้ห้ามเปลี่ยน: **Reset → Random → Play**

### 3.10 Theme Selector HTML

```html
<select class="theme-select" onchange="setTheme(this.value)">
  <option value="dark">🌙 Classic Dark</option>
  <option value="hausnight">⌂ HAUS Night</option>
  <option value="vintage">📜 Vintage Dark</option>
  <option value="neon">🌃 Cyberpunk Neon</option>
  <option value="cosmic">🌌 Cosmic Void</option>
  <option value="light">☀️ Classic Light</option>
  <option value="haus">⌂ HAUS Day</option>
  <option value="clay">🏺 Warm Clay</option>
  <option value="sage">🌿 Soft Sage</option>
  <option value="mist">🌫️ Mist Blue</option>
</select>
```

### 3.11 Brand Logo (Graph version)

```html
<div class="brand-lockup">
  <span class="brand-logo-box">
    <img class="brand-logo" src="assets/HAUS_logo_black.png" alt="HAUS Academy">
  </span>
  <h1><span>Title</span> <span class="badge-top">v1.0.0</span></h1>
</div>
```

```css
.brand-logo-box{display:inline-flex;align-items:center;border-radius:8px;padding:4px 10px;transition:background 0.3s;}
.brand-logo{height:30px;width:auto;display:block;}
body.logo-dark .brand-logo-box{background:#F4C01E;}
body:not(.logo-dark) .brand-logo-box{background:transparent;}
```

---

## ✅ ส่วนที่ 4: Verification Checklist (ต้องทำก่อน deliver)

### 4.1 Static Checks
```bash
python3 - <<'EOF'
import re
html = open('file.html').read()
js = re.search(r'<script>\n(.*)</script>', html, re.S).group(1)
open('/tmp/check.js','w').write(js)
used = set(re.findall(r'\$\(\"([\w-]+)\"\)', js)) | set(re.findall(r'getElementById\(\"([\w-]+)\"\)', js))
defined = set(re.findall(r'id=\"([\w-]+)\"', html))
print("missing ids:", used - defined or "none")
EOF
node --check /tmp/check.js
```

### 4.2 Logic Tests
- Test reading math: `value → decompose → recompose === value` (exhaustive ทุก resolution)
- Test known textbook values
- Test boundary rollovers (fraction → next whole unit)
- Test zero error edge cases (negative ZE at closed position)

### 4.3 Visual Checks (Playwright screenshot)
- Screenshot ทุก mode, ทุก parameter tier, ทุก zoom state
- ดูว่า: shapes clip ที่ edge? moving parts บัง scales? labels ทับ ticks? toolbar shift?
- Crop รูปมาดู detail regions (jaw tips, scale junction, toolbar)

### 4.4 Common Pitfalls Checklist
- [ ] `isDark()` function ต้องมี — ถ้าขาด script จะตายเงียบ
- [ ] theme class list ใน `setTheme()` ต้องครบทุก theme (ยกเว้น default `dark`)
- [ ] HAUS Day/Night overrides CSS ต้องมี (`badge-top`, `top-bar h1`)
- [ ] Grid lines `lineWidth = 0.4` — เบา intentionally
- [ ] Zero line ใน a-t graphs: dashed `[3, 3]`, วาดหลัง grid ก่อน data curve
- [ ] Light themes ห้าม pure white — ใช้ warm tones (`#cdc7bc`, `#ddd7cc`)
- [ ] `Math.round()` DPR dimensions — ห้าม fractional
- [ ] `min-height` บน variable-height containers
- [ ] Random→Custom flow: เรียก `setScenario('custom')` ก่อน randomize
- [ ] Logo path: `assets/HAUS_logo_black.png`
- [ ] ถ้าใช้ KaTeX: ต้องมี CDN link และฟังก์ชัน `renderMathInElement()`
- [ ] Toolbar ต้องไม่ shift — ใช้ `.pills.locked` ไม่ใช่ `display:none`
- [ ] Enter key ใน input = submit check/quiz

---

## 📝 ส่วนที่ 5: Ready-to-Use Prompt Template

คัดลอก prompt นี้ไปให้ AI อื่นเพื่อสร้าง Simulation หรือ Graph:

---

```
[INSTUCTION]
คุณต้องสร้าง 2D Physics Simulation แบบ standalone HTML ไฟล์เดียว สำหรับ HAUS Academy
เลือกประเภท: [SIMULATION หรือ GRAPH]

--- ถ้าเป็น SIMULATION ---
หัวข้อ: [topic name]
ครอบคลุมเนื้อหา: [syllabus points]
ต้องการ 3 modes: Simulate / Practice / Quiz
Zero error: [yes/no]
ภาษาไทย: [yes/no]

ต้องมี:
1. Toolbar fixed 2 rows (zero layout shift)
2. State object S ตัวเดียว, draw()/updateUI() pure functions
3. Pointer-drag + double-click zoom + keyboard fine-step
4. 3 modes: Simulate (free), Practice (locked+worked solution), Quiz (5 questions+stars)
5. HAUS design tokens (--bg:#0d1117, --accent:#e3b341, ฯลฯ)
6. Brand logo yellow rounded rect top-right
7. Verification: static check + logic test + screenshot

--- ถ้าเป็น GRAPH ---
หัวข้อ: [topic name]
สมการ: [physics equations]
ต้องการ theme: [11 themes]
Animation: [yes/no]

ต้องมี:
1. 11 themes (Dark/Light) via CSS variables
2. DPR-aware canvas, pad={top:18,right:16,bottom:32,left:38}
3. niceStep() ticks (MANDATORY — ห้าม step ตายตัว)
4. Fonts: ticks=10px Inter, titles=11px Inter (y at x=14 rotated)
5. Physics engine: [suvat/jerk/freefall/stopping/terminal velocity]
6. Animation loop: rAF, dt=0.04, velocity-aware ground check
7. Button order: Reset → Random → Play
8. HAUS brand logo + isDark() toggle
9. Theme selector dropdown + setTheme()
```

รายละเอียดเต็มอยู่ในคู่มือด้านบน ใช้ reference implementations ที่:
- Simulations: ~/InteractiveLecture/simulations/Measurement_1_vernier_caliper.html
- Graphs: ~/InteractiveLecture/graphs/kinematics_1_horizontal_graphs.html
```

---

*📌 บันทึกโดย วีวี่ — Master Prompt for AI 2D Simulation Builder v1.0.0*