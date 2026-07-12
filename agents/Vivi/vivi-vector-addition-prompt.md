# 🎯 Vivi's Vector Addition Simulation — Master Prompt

> **Author:** วีวี่ (Vivi) — Science Content Agent  
> **Version:** 1.0.0  
> **วันที่:** 2026-07-09  
> **ประเภท:** 2D Simulation — Vector Addition (IGCSE Physics / A-Level)  
> **Skill Reference:** physics-simulation-2d + physics-graph-authoring  
> **เหมาะสำหรับ:** AI Agent ที่ต้องสร้าง Vector Addition Interactive Simulation

---

## 📋 ภาพรวม

สร้าง standalone HTML ไฟล์เดียวสำหรับสอนการรวมเวกเตอร์ (Vector Addition) ระดับ IGCSE Physics และ A-Level Physics
ผู้เรียนสามารถเลือกวิธีการแก้ปัญหาได้ 3 วิธีใน 3 Tabs แยกกัน

---

## 1. โครงสร้างหลัก

### 1.1 ไฟล์
- **ชื่อ:** `~/InteractiveLecture/simulations/Mathematics_1_vector_addition.html`
- **Standalone HTML ไฟล์เดียว** — CSS + JS + HTML ในไฟล์เดียว
- **External:** Google Fonts (Inter, JetBrains Mono), KaTeX (สำหรับสมการใน steps)
- **Encoding:** UTF-8, DOCTYPE html

### 1.2 Layout โดยรวม

```
┌─────────────────────────────────────────────────────┐
│ [Brand Logo HAUS]         Vector Addition Sim  v1.0 │
├─────────────────────────────────────────────────────┤
│ [Tab 1: Drawing Scale] [Tab 2: Triangle Rule] [Tab 3: Component Method] │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ┌───────────────────────┐  ┌── Scale Bar ──────┐  │
│  │                       │  │ 1 cm = [___] [unit]│  │
│  │   640×640 px Grid     │  │                    │  │
│  │   16×16 cm workspace  │  │ Grid size: [select]│  │
│  │                       │  │                    │  │
│  │  ── snap to grid      │  │ Tools:             │  │
│  │  ── vectors + labels  │  │ [📏 Ruler] [📐Prot]│  │
│  │  ── components (Tab3) │  │                    │  │
│  │                       │  │ [Toggle snaps]     │  │
│  └───────────────────────┘  │ [Toggle labels]    │  │
│                              └────────────────────┘  │
│                                                      │
│  ┌── Vector Controls ─────────────────────────┐      │
│  │ [Manual Input] [Click&Drag] [🎲 Random]    │      │
│  │ Mag: [____]  Angle: [____]°  [Add Vector]  │      │
│  └────────────────────────────────────────────┘      │
│                                                      │
│  ┌── Vector List ─────────────────────────────┐      │
│  │ # │ Color │ Vector │ Mag │ Angle │ Fx/Fy  │      │
│  │ 1 │ ■     │ A      │50.0 │ 30.0°│ 43.3/25.0│   │
│  │ 2 │ ■     │ B      │30.0 │120.0°│-15.0/26.0│   │
│  │   │       │        │     │      │          │      │
│  │ [➕ Add] [🗑️ Remove] [🔁 Edit]              │      │
│  └────────────────────────────────────────────┘      │
│                                                      │
│  ┌── Result / Calculation Panel ──────────────┐      │
│  │ [🎯 Show Resultant] 📐 Practice Mode       │      │
│  │                                            │      │
│  │ Resultant R = 58.3 N, θ = 61.0°           │      │
│  │ [📖 Show Steps ▼]                         │      │
│  └────────────────────────────────────────────┘      │
└─────────────────────────────────────────────────────┘
```

---

## 2. พื้นที่วาด + Grid

### 2.1 Canvas
- **ขนาด:** 640×640 px (logical CSS px)
- **1 cm จอ = 40 px** — ความสัมพันธ์ตายตัว
- **พื้นที่จริง:** 16 cm × 16 cm
- **DPR-aware:** `Math.round()` เสมอ

```javascript
const CM_PX = 40;           // 1 cm = 40 px
const CANVAS_SIZE = 640;     // 16 cm × 16 cm
const pad = { top: 18, right: 16, bottom: 32, left: 48 };  // เว้นที่ label
```

### 2.2 Grid
- **ขนาดช่อง:** เลือกได้จาก dropdown: 1×1, 5×5, 10×10, 50×50 (หน่วยของ scale)
- **ช่องใน canvas:** ขึ้นกับ scale ที่เลือก
- **สี:** `--grid` (current theme), เส้นบางๆ `lineWidth = 0.4`
- **Tick labels ที่ขอบ:** แสดงค่าที่ grid line หลักด้วย font `10px Inter`

### 2.3 Coordinate System
- **จุด Origin (0,0):** กึ่งกลาง canvas **หรือ** มุมล่างซ้าย? → **มุมล่างซ้าย** (เหมือน Cartesian ปกติ)
- แกน X → ขวา, แกน Y → บน
- **เส้นแกน X และ Y:** สี `--text-dim` หนา 1px, หัวลูกศรชัดที่ปลาย
- **Label แกน:** "x (m)" / "y (m)" — ใช้ตาม unit ที่ผู้ใช้เลือก

---

## 3. ระบบ Vector

### 3.1 State Object

```javascript
const S = {
  vectors: [],        // [{id, color, label, mag, angle, x, y, fx, fy}, ...]
  tab: 1,             // 1 | 2 | 3
  scale: { val: 1, unit: 'N' },   // 1 cm = 1 N
  gridSize: 10,       // 10×10 units
  snapGrid: true,     // snap to grid toggle
  snapT2T: true,      // snap tail-to-tip toggle
  showLabels: false,  // label toggle (default OFF)
  showResultant: false,
  angleMode: 'east',  // 'east' | 'north'
  showComponents: false,  // Tab 3: show Fx/Fy on grid
  showSteps: false,       // Tab 3: show calculation steps
  mode: 'practice',       // 'practice' | 'auto'
  rulerActive: false,     // ruler tool active
  protractorActive: false,// protractor tool active
  dragTarget: null,       // which vector is being dragged (for edit)
};
```

### 3.2 การสร้าง Vector (3 วิธี)

#### Manual Input
```html
<div class="vector-input-group">
  <input type="number" id="vMag" placeholder="Magnitude" step="0.1">
  <input type="number" id="vAngle" placeholder="Angle (°)" step="0.1" min="0" max="360">
  <select id="vAngleMode">
    <option value="east">From East (0° →)</option>
    <option value="north">From North (0° ↑)</option>
  </select>
  <button class="btn primary" onclick="addVector()">➕ Add Vector</button>
</div>
```
- เมื่อกด Add → vector ปรากฏบน grid ที่ตำแหน่งเริ่มต้น (0,0) หรือต่อจาก vector สุดท้าย (ถ้า snap T2T เปิด)
- **Validation:** magnitude > 0, angle 0–360

#### Click & Drag
- **คลิกค้าง** บน grid → ลาก → **ปล่อย** → vector ถูกสร้าง
- แสดง **เส้นชั่วคราว (preview line)** ระหว่างลาก (สีเทา/เส้นประ)
- เมื่อปล่อย → snap ตาม snap settings
- ความยาว = pixel distance / 40 * scale → magnitude
- ทิศทาง = angle จากแนว East/North ตาม settings

#### Random (🎲)
- กด 🎲 → ระบบสุ่ม vector 1 ตัว หรือถามก่อน: "กี่ vector?" (1–6)
- สุ่มค่า:
  - magnitude: random ในช่วงที่เข้ากับ scale
  - angle: 0–360°
- เพิ่มเข้าตารางและวาดบน grid ทันที

### 3.3 Snap System (Toggle ทั้งคู่)

```javascript
const SNAP_RADIUS = 12;   // px — ระยะที่จะ snap

function snapToGrid(x, y) {
  if (!S.snapGrid) return { x, y };
  const gridPx = (S.canvasSize / S.gridSize) * (CM_PX / (S.scale.val / S.gridSize)); // ซับซ้อน — คำนวณจาก scale
  // จริงๆ: 1 ช่อง grid = กี่ px = (CANVAS_SIZE / gridSize_in_cm) * CM_PX
  return {
    x: Math.round(x / gridPx) * gridPx,
    y: Math.round(y / gridPx) * gridPx,
  };
}

function snapTailToTip(x, y, allVectors) {
  if (!S.snapT2T) return { x, y };
  for (const v of allVectors) {
    const tipX = v.x + v.endX; // tail + displacement
    const tipY = v.y + v.endY;
    const dist = Math.hypot(x - tipX, y - tipY);
    if (dist < SNAP_RADIUS) return { x: tipX, y: tipY, snappedTo: v.id };
  }
  return { x, y };
}
```

### 3.4 การวาง Vector ติดกัน
- เมื่อ snap T2T เปิด → vector ใหม่จะเริ่มที่ **tip ของ vector ก่อนหน้า**
- สามารถลาก vector ที่มีอยู่แล้วไปต่อกับ vector อื่นได้ (เปลี่ยน tail position)
- **Auto-calculation ของ resultant ทำงานเมื่อ vector ต่อกันสนิทเท่านั้น** (snap แล้ว)

### 3.5 สี + Label

#### Auto Color Palette (default)
```javascript
const COLORS = ['#58a6ff', '#3fb950', '#e3b341', '#fb7185', '#a78bfa', '#f97316'];
```
- Resultant vector = **สีเด่นพิเศษ**: `#facc15` (ทอง) กับ glow
- User เปลี่ยนสี vector ของตัวเองได้ผ่าน color picker ในตาราง

#### Label
```html
<label class="tgroup">
  <span class="tlabel">LABELS</span>
  <button class="pill-toggle" onclick="toggleLabels()">
    <span class="pill ${S.showLabels ? 'active' : ''}">ON</span>
    <span class="pill ${!S.showLabels ? 'active' : ''}">OFF</span>
  </button>
</label>
```

- **Default: OFF** — ไม่แสดง label บน grid (เพื่อให้เด็กฝึกอ่านเอง)
- **Hover ⭕** — เมื่อเมาส์ hover ที่ vector → **แสดง label เสมอ** (override OFF)
- **เมื่อ ON** — แสดง label: `A = 50.0 N @ 30°` (หรือตามหน่วย) ติด vector
- **ตำแหน่ง label:** เหนือ vector เล็กน้อย, หมุนตาม vector

#### Vector List Table
| # | Color | Label | Mag | Angle | Fx | Fy |
|---|---|---|---|---|---|---|
| 1 | ■ picker | A | 50.0 | 30.0° | 43.3 | 25.0 |
| 2 | ■ picker | B | 30.0 | 120.0° | -15.0 | 26.0 |
| | | | | **Σ** | **28.3** | **51.0** |
| | | | **R** | **58.3** | **61.0°** | |

- แต่ละแถวมีปุ่ม: 🖍️ Edit, 🗑️ Remove
- Color cell = color picker (`<input type="color">`)
- Fx/Fy คำนวณอัตโนมัติเมื่อ vector ถูกเพิ่มหรือแก้ไข

### 3.6 การ Edit Vector (2 วิธี — toggle ได้)

1. **Double-click vector** → popup modal:
```html
<div class="edit-modal">
  <h3>Edit Vector A</h3>
  <div class="edit-row">
    <label>Magnitude: <input type="number" value="50.0" step="0.1"></label>
    <label>Angle: <input type="number" value="30.0" step="0.1" min="0" max="360">°</label>
  </div>
  <div class="edit-row">
    <label>Color: <input type="color" value="#58a6ff"></label>
    <label>Label: <input type="text" value="A" maxlength="2"></label>
  </div>
  <button onclick="confirmEdit()">✓ Apply</button>
  <button onclick="closeModal()">✕ Cancel</button>
</div>
```

2. **Drag head ตรงๆ** — คลิกที่หัว vector → ลาก → ปรับขนาด/มุม:
```javascript
vec.addEventListener('pointerdown', (e) => {
  if (e.target.closest('.vector-head')) {
    editing = vec.id;
    startMag = vec.mag;
    startAngle = vec.angle;
  }
});
vec.addEventListener('pointermove', (e) => {
  if (!editing) return;
  const dx = e.clientX - origin.x;
  const dy = origin.y - e.clientY;  // y แกนบน
  const newMag = Math.hypot(dx, dy) / CM_PX * S.scale.val;
  const newAngle = normalizeAngle(Math.atan2(dy, dx) * 180 / Math.PI, S.angleMode);
  vec.mag = snapToGridMag(newMag);
  vec.angle = snapToAngle(newAngle);
  updateUI();
});
```

---

## 4. 3 Tabs = 3 วิธีแก้ปัญหา

### 4.1 Tab 1: Drawing Scale Diagram
- **จำนวน vector สูงสุด:** 6
- **Vector ต่อกัน:** snap T2T + snap grid
- **เครื่องมือวัด:**
  - 📏 **ไม้บรรทัด 2-point** — คลิกจุดแรก → คลิกจุดที่สอง → วัดระยะทาง px → convert เป็น cm → คูณ scale → แสดงผล
  - 📐 **Protractor** — คลิกจุดศูนย์กลาง → ลากไปที่ vector → วัดมุม
- **Practice mode (default):** ผู้เรียนลาก vector ต่อกันเอง → ลาก resultant vector เอง → วัดเอง → กด "Check" → ระบบเฉลย
- **Show Resultant:** กดปุ่ม → ระบบวาด resultant vector (สีทอง) + แสดงขนาดและมุม
- **ไม้บรรทัด + protractor:** แบบเคลื่อนย้ายได้ (drag เพื่อ reposition)

```javascript
// Ruler logic
function rulerMeasure(x1, y1, x2, y2) {
  const pixelDist = Math.hypot(x2 - x1, y2 - y1);
  const cmDist = pixelDist / CM_PX;
  const realDist = cmDist * S.scale.val;
  return { cm: cmDist, real: realDist, unit: S.scale.unit };
}
```

### 4.2 Tab 2: Triangle Method + Sine/Cosine Rule
- **จำนวน vector สูงสุด:** 3 (สามเหลี่ยมปิด)
- **Visual:** vectors ต่อกันเป็นรูปสามเหลี่ยมปิด (tail → tip → tip → tail)
- **ส่วนประกอบ:**
  - vector 3 ตัวที่มุม A, B, C
  - ด้าน a (ตรงข้าม A), b (ตรงข้าม B), c (ตรงข้าม C)
  - มุม A, B, C
- **การคำนวณ (automated):**
  - Sine Rule: `a/sin(A) = b/sin(B) = c/sin(C)`
  - Cosine Rule: `a² = b² + c² - 2bc·cos(A)`
- **แสดงผล:**
  - สามเหลี่ยมบน grid พร้อม label ด้านและมุม
  - ตารางค่าที่已知และที่ต้องการหา
  - สูตร + substitution + answer
- ถ้าใส่ vector แค่ 2 ตัว → ระบบคำนวณตัวที่ 3 ให้โดยอัตโนมัติ

```
ตัวอย่าง layout:
        A
       / \
   c  /   \  b
     /     \
    /_______\
   B    a    C

  Known: b=50N, c=30N, A=80°
  By Cosine Rule: a² = b² + c² − 2bc·cos(A)
  a² = 2500 + 900 − 2(50)(30)cos(80°)
  a² = 3400 − 520.9
  a² = 2879.1
  a = 53.7 N
```

### 4.3 Tab 3: Component Method (A-Level)
- **จำนวน vector สูงสุด:** 6
- **Toggle "Show Components"** (default OFF):
  - เมื่อ ON → วาด Fx (สีฟ้า `--blue`) และ Fy (สีเขียว `--green`) เป็น **เส้นประ** จาก tail ของแต่ละ vector
  - โดย Fx = เส้นแนวนอน, Fy = เส้นแนวตั้ง ตั้งฉากกัน
  - พร้อม label: `Fx = 43.3 N`, `Fy = 25.0 N`
- **ตาราง Component:**

```html
<div class="component-table">
  <table>
    <thead>
      <tr><th>#</th><th>F (N)</th><th>θ (°)</th><th>Fx = Fcosθ</th><th>Fy = Fsinθ</th></tr>
    </thead>
    <tbody id="compTbody">
      <!-- JS render -->
    </tbody>
    <tfoot>
      <tr><td colspan="3"><b>Σ</b></td><td id="sumFx">28.3</td><td id="sumFy">51.0</td></tr>
    </tfoot>
  </table>
</div>
```

- **Resultant Calculation พร้อม toggle "Show Steps":**

```html
<div class="resultant-box">
  <div class="resultant-summary">
    <span class="resultant-label">Resultant</span>
    <span class="resultant-value">R = 58.3 N</span>
    <span class="resultant-angle">θ = 61.0°</span>
  </div>
  <button class="btn" onclick="toggleSteps()">
    📖 ${S.showSteps ? 'Hide Steps ▲' : 'Show Steps ▼'}
  </button>
  <div id="stepsPanel" class="${S.showSteps ? 'visible' : 'hidden'}">
    <div class="step">R = √(ΣFx² + ΣFy²)</div>
    <div class="step">R = √(28.3² + 51.0²)</div>
    <div class="step">R = √(800.9 + 2601.0)</div>
    <div class="step">R = √3401.9</div>
    <div class="step highlight">R = 58.3 N</div>
    <div class="step-separator"></div>
    <div class="step">θ = tan⁻¹(ΣFy / ΣFx)</div>
    <div class="step">θ = tan⁻¹(51.0 / 28.3)</div>
    <div class="step">θ = tan⁻¹(1.802)</div>
    <div class="step highlight">θ = 61.0°</div>
  </div>
</div>
```

- **Resultant vector บน grid:** วาดด้วย **สีทอง `#facc15`** หนากว่า vector ปกติ มี glow effect
  - แสดงเฉพาะเมื่อกด "Show Resultant" หรือกด "Check" ใน Practice mode

---

## 5. Tools (Tab 1)

### 5.1 Ruler (ไม้บรรทัดวัด 2-point)
```javascript
let rulerPoints = [];

function activateRuler() {
  S.rulerActive = true;
  canvas.style.cursor = 'crosshair';
}

canvas.addEventListener('click', (e) => {
  if (!S.rulerActive) return;
  const { x, y } = getCanvasCoords(e);
  rulerPoints.push({ x, y });
  if (rulerPoints.length === 2) {
    const result = rulerMeasure(rulerPoints[0].x, rulerPoints[0].y, rulerPoints[1].x, rulerPoints[1].y);
    showRulerResult(result);
    drawRulerLine(rulerPoints[0], rulerPoints[1]);
    rulerPoints = [];
    S.rulerActive = false;
    canvas.style.cursor = 'default';
  }
});
```

- แสดงผล: `Distance: 5.2 cm → 260.0 N`
- จุดวัด = จุด + มีรัศมี snap 6px (snap ไปที่ tail/tip ของ vector ที่ใกล้ที่สุด)

### 5.2 Protractor (วัดมุม)
- **Center point:** คลิกตั้ง center (ควร snap ไปที่ tail/tip vector)
- **Drag ออก** → protractor หมุนตาม → อ่านมุม
- แสดงผลเป็นองศา XX.X°
- Visual: ครึ่งวงกลม transparent พร้อมขีด度数และเส้น reference

---

## 6. Scale Bar

```html
<div class="scale-bar">
  <span class="tlabel">SCALE</span>
  <span class="scale-visual">⎯⎯⎯</span>
  <span>1 cm =</span>
  <input type="number" id="scaleVal" value="1" step="0.5" min="0.1" onchange="updateScale()">
  <input type="text" id="scaleUnit" value="N" maxlength="5" placeholder="unit" onchange="updateScale()">
  <span class="scale-example">→ 1 cm = 1 N</span>
</div>
```

- เมื่อเปลี่ยน scale → vector ทั้งหมดบน grid ปรับขนาด (magnitude visualization) ตาม
- **ค่าตัวเลขของ vector ไม่เปลี่ยน** — แค่ความยาวบนจอเปลี่ยน
- ตัวอย่าง: ถ้า vector A = 50 N, scale จาก 1 cm = 1 N → 1 cm = 10 N → ความยาวบนจอลดลง 10 เท่า

---

## 7. Angle System

### 7.1 Toggle: East (0°) vs North (0°)

```javascript
function normalizeAngle(deg, mode) {
  // 0 → 360
  deg = ((deg % 360) + 360) % 360;
  if (mode === 'north') {
    // 0° = ↑ (North), คำนวณตามเข็มนาฬิกา
    return deg;  // input angle ยังคงเป็นตัวเลขปกติ
  }
  // east: 0° = → (East), + ทวนเข็ม
  return deg;
}

function vectorFromMagAngle(mag, angle, mode) {
  const rad = mode === 'east'
    ? (90 - angle) * Math.PI / 180   // east → cartesian
    : angle * Math.PI / 180;          // north → cartesian
  return {
    dx: mag * Math.cos(rad),
    dy: mag * Math.sin(rad),
  };
}
```

### 7.2 Display Format: XX.X°
- แสดงมุมเป็นทศนิยม 1 ตำแหน่งเสมอ
- ในตาราง: `30.0°`, `120.0°`

---

## 8. Theme System (11 Themes)

ใช้ theme เดียวกับ **physics-graph-authoring** skill ทุกประการ:

| Value | Label | Type |
|---|---|---|
| `dark` | Classic Dark | Dark |
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

**HAUS brand themes:**
```css
.theme-haus{--bg:#F4EEE0;--card:#FFFFFF;--border:#E4DAC4;--text:#1A1712;--text-dim:#5B5344;--accent:#A9820F;--grid:#EBE3D0;--graph-bg:#FCFAF2}
.theme-hausnight{--bg:#1a1c20;--card:#26282d;--border:#3a3c42;--text:#FFFFFF;--text-dim:#e0e2e8;--accent:#F4C01E;--grid:#2a2c32;--graph-bg:#121418}
```

`setTheme()` + `isDark()` + logo-dark toggle — ตาม physics-graph-authoring ทุกประการ

---

## 9. Brand Logo

ตามมาตรฐาน HAUS Academy:
- `.brand` absolute ใน toolbar, yellow rounded rect (#F4C01E, border-radius 10px)
- Width 56px
- `top:50%; translateY(-50%); right:16px`
- ซ่อนที่ < 640px

---

## 10. Code Architecture

### 10.1 File Structure
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vector Addition Simulator | HAUS Academy</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <style>
    /* CSS theme variables + layout */
  </style>
</head>
<body>
  <!-- HTML layout -->
  <script>
    // JavaScript (see sections below)
  </script>
</body>
</html>
```

### 10.2 JavaScript Section Order
```javascript
/* ══════════════════════════════════════════════════════════
   1. CONSTANTS
   2. STATE (S)
   3. CORE MATH
      - vectorToComponents, addVectors, resultant, 
        sineRule, cosineRule, pythagoras
   4. CANVAS DRAWING
      - drawGrid, drawAxes, drawVector, drawComponents,
        drawResultant, drawRuler, drawProtractor
   5. VECTOR OPERATIONS
      - addVector, editVector, removeVector, randomVector
   6. INTERACTIONS
      - pointer-drag, double-click, keyboard, snap logic
   7. TAB SYSTEM
      - switchTab(1|2|3), renderTabContent
   8. TOOLS
      - rulerMeasure, protractorMeasure, showResultant
   9. UI UPDATES
      - renderVectorTable, renderComponentTable, 
        renderSteps, updateScale, toggleLabels
   10. INIT
       - resizeCanvas, init, event listeners
   ══════════════════════════════════════════════════════════ */
```

### 10.3 Key Math Functions

```javascript
// Vector → components
function vectorToComponents(mag, angle, angleMode) {
  const rad = angleMode === 'east'
    ? (90 - angle) * Math.PI / 180
    : angle * Math.PI / 180;
  return {
    fx: mag * Math.cos(rad),
    fy: mag * Math.sin(rad),
  };
}

// Sum all vectors
function sumVectors(vectors) {
  let sumFx = 0, sumFy = 0;
  for (const v of vectors) {
    const c = vectorToComponents(v.mag, v.angle, S.angleMode);
    v.fx = c.fx; v.fy = c.fy;
    sumFx += c.fx; sumFy += c.fy;
  }
  return { sumFx, sumFy };
}

// Resultant
function calcResultant(sumFx, sumFy) {
  const R = Math.hypot(sumFx, sumFy);
  const angleRad = Math.atan2(sumFy, sumFx);
  const angleEast = (angleRad * 180 / Math.PI + 360) % 360;
  // Convert to user's angle mode
  const angle = S.angleMode === 'east'
    ? angleEast
    : (90 - angleEast + 360) % 360;
  return { R, angle };
}

// Cosine Rule
function cosineRule(b, c, A_deg) {
  const A = A_deg * Math.PI / 180;
  return Math.sqrt(b*b + c*c - 2*b*c*Math.cos(A));
}

// Sine Rule
function sineRule(side, angle, targetAngle) {
  return side / Math.sin(angle * Math.PI / 180) * Math.sin(targetAngle * Math.PI / 180);
}
```

---

## 11. Interaction Details

### 11.1 Canvas Pointer Events

```javascript
canvas.addEventListener('pointerdown', onPointerDown);
canvas.addEventListener('pointermove', onPointerMove);
canvas.addEventListener('pointerup', onPointerUp);
canvas.addEventListener('dblclick', onDoubleClick);
canvas.addEventListener('wheel', onWheel);  // zoom grid
canvas.style.touchAction = 'none';
```

**Mode Machine สำหรับ Interaction:**
```javascript
const InteractionMode = {
  IDLE: 'idle',
  DRAW_VECTOR: 'draw_vector',       // click & drag to create
  DRAG_VECTOR_HEAD: 'drag_head',    // drag head to resize
  RULER_POINT_1: 'ruler_pt1',       // ruler: first point
  RULER_POINT_2: 'ruler_pt2',       // ruler: second point
  PROTRACTOR: 'protractor',         // protractor active
  PANNING: 'panning',               // pan canvas (if needed)
};
```

### 11.2 Vector Rendering on Canvas

```javascript
function drawVector(ctx, v, isResultant = false) {
  const originX = CANVAS_SIZE / 2;  // center, or could be cumulative
  const originY = CANVAS_SIZE / 2;
  const scalePx = v.mag / S.scale.val * CM_PX;  // mag → pixel length
  const rad = S.angleMode === 'east'
    ? (90 - v.angle) * Math.PI / 180
    : v.angle * Math.PI / 180;

  const endX = v.x + scalePx * Math.cos(rad);
  const endY = v.y - scalePx * Math.sin(rad);  // y-axis inverted

  ctx.save();
  // Resultant = thicker, glowing
  if (isResultant) {
    ctx.shadowColor = 'rgba(250,204,21,0.5)';
    ctx.shadowBlur = 8;
    ctx.strokeStyle = '#facc15';
    ctx.lineWidth = 3.5;
  } else {
    ctx.strokeStyle = v.color;
    ctx.lineWidth = 2.5;
  }
  ctx.beginPath();
  ctx.moveTo(v.x, v.y);
  ctx.lineTo(endX, endY);
  ctx.stroke();
  drawArrowHead(ctx, endX, endY, rad);
  ctx.restore();
}
```

---

## 12. Tab 2 (Triangle) Special Layout

เมื่อ Tab 2 ถูกเลือก:
- 3 vectors ถูกจัดเรียงเป็นรูปสามเหลี่ยมปิด **อัตโนมัติ**
- Label ด้าน: `a`, `b`, `c`
- Label มุม: `A`, `B`, `C` (ที่ vertex ตรงข้ามด้าน a, b, c)
- แสดงตาราง Known/Unknown:

```
┌─────────────────────────────────────┐
│  Triangle ABC                       │
│                                     │
│  Known:                             │
│  [✓] b = 50.0 N    [✓] c = 30.0 N  │
│  [✓] A = 80.0°                      │
│                                     │
│  Unknown (calculated):              │
│  a² = b² + c² − 2bc·cos(A)         │
│  a² = 2500 + 900 − 520.9           │
│  a² = 2879.1                        │
│  a = 53.7 N                         │
│                                     │
│  [Show full solution ▼]             │
└─────────────────────────────────────┘
```

- **ถ้าใส่ vector แค่ 2 ตัว** → ระบบคำนวณตัวที่ 3 ให้ (สามเหลี่ยมปิด)

---

## 13. Fixed Button Order

```html
<div class="control-buttons">
  <button class="ctrl-btn" onclick="resetAll()">↺ Reset</button>
  <button class="ctrl-btn random" onclick="randomVector()">🎲 Random</button>
  <button class="ctrl-btn primary" onclick="showResultant()">🎯 Resultant</button>
</div>
```

**ลำดับ: Reset → Random → Resultant** (คงที่ตลอด)

---

## 14. Label Toggle Component (Default OFF)

```html
<div class="tgroup">
  <span class="tlabel">LABELS</span>
  <button class="pills" onclick="toggleLabels()">
    <span class="pill ${S.showLabels ? 'active' : ''}">ON</span>
    <span class="pill ${!S.showLabels ? 'active' : ''}">OFF</span>
  </button>
</div>
```

- **global state:** `S.showLabels`
- **Hover:** `canvas.addEventListener('mousemove')` → checK closest vector → `if (dist < 20px) showLabel(v);`
- แสดง label เป็น DOM element ลอย (ไม่ใช่ paint บน canvas) เพื่อความ sharp

---

## 15. Responsive Considerations

- ที่ viewport < 800px: Tab panels ซ้อนแนวตั้ง (พื้นที่วาดอยู่บน, tools อยู่ล่าง)
- toolbar และ brand logo: ตาม physics-simulation-2d convention
- grid ยังคง 16×16 cm logic แต่ scale CSS ให้พอดีจอ

---

### 16.1 Lessons Learned Checklist (ถามก่อนสร้าง Prompt ทุกครั้ง!)

จากประสบการณ์สร้าง Vector Addition Simulator พบว่ามีข้อที่พลาดไป — ต้องถามให้ครบถ้วน:

#### 🔴 อย่าลืมถาม!
- [ ] **Erase / Delete** — เมื่อมี Add ต้องมี Delete! ต้องถาม: ต้องการลบ vector หรือไม่? (eraser tool, ปุ่มลบใน table, etc.)
- [ ] **Undo History** — ต้องถาม: ต้องการ Undo (Ctrl+Z) ไหม? ต้องการ history กี่ขั้น?
- [ ] **Zoom + Pan** คู่กัน — Double-click zoom → พอ zoom แล้วต้อง Pan (click-drag) เพื่อเลื่อน viewport ได้ด้วย
- [ ] **Keyboard shortcuts** — Escape = exit zoom/tool, Ctrl+Z = undo, Arrow keys = fine-stepping

#### 💡 Tips จากประสบการณ์:
- Zoom without Pan = useless (มองไม่เห็นส่วนอื่น)
- Add without Delete/Undo = frustrates user (ไม่สามารถแก้ไขความผิดพลาด)
- Undo without history limit = memory leak (จำกัดที่ 60 steps เหมาะสม)
- Eraser with hover highlight = better UX (เห็นว่าจะลบอะไรก่อนคลิก)

ก่อน deliver ต้องตรวจ:

- [ ] DPR-aware canvas, `Math.round()` dimensions
- [ ] Snap T2T ทำงานถูกต้อง (12 px radius)
- [ ] Snap grid ทำงานถูกต้อง
- [ ] Auto-calculation เฉพาะเมื่อต่อกันสนิท
- [ ] Tab switching: vectors คงอยู่? (Tab 1 ↔ 3 ควรแชร์ vectors, Tab 2 แยก)
- [ ] Scale change: ความยาว vector ปรับตาม, ค่าเลขคงเดิม
- [ ] Label toggle ON/OFF + Hover แสดง
- [ ] Ruler 2-point → วัด cm → แปลง scale → แสดงผล
- [ ] Protractor → วัดมุม → XX.X°
- [ ] Component table: Fx = Fcosθ, Fy = Fsinθ, ΣFx, ΣFy
- [ ] Steps toggle → แสดง/ซ่อน calculation
- [ ] Show Resultant → vector สีทอง + glow
- [ ] Random → สุ่มค่าในช่วงที่เหมาะสม
- [ ] Double-click vector → edit popup
- [ ] Drag head → ปรับ magnitude + angle
- [ ] Sine/Cosine Rule → คำนวณถูก
- [ ] 11 themes → setTheme() + isDark() + HAUS overrides
- [ ] Toolbar zero layout shift
- [ ] Button order: Reset → Random → Resultant
- [ ] `isDark()` function ครบ
- [ ] Brand logo yellow rounded rect

---

## 📝 Ready-to-Use Prompt

Copy ข้อความข้างล่างนี้ไปให้ AI สร้าง simulation:

```
[INSTRUCTION]
Create a standalone HTML file for a Vector Addition Interactive Simulation for HAUS Academy (IGCSE Physics).

## CANVAS
- 640×640 px, 40 px = 1 cm (16×16 cm workspace)
- Grid with selectable size (1×1, 5×5, 10×10, 50×50 units)
- Origin at bottom-left, axes with labels

## VECTORS
- 3 creation modes: Manual Input (mag + angle), Click&Drag on canvas, 🎲 Random
- Max 6 vectors per session (Tab 1 & 3), max 3 vectors (Tab 2)
- Snap system: tail-to-tip + grid snap, both toggleable
- Auto-color palette (6 colors), user can change via color picker
- Label toggle default OFF, hover ALWAYS shows label
- Double-click to edit (popup), drag head to resize/rotate directly

## 3 TABS = 3 METHODS
Tab 1 - Drawing Scale Diagram:
  - Ruler (2-point click to measure distance in cm → convert via scale)
  - Protractor (center point + drag to measure angle)
  - Practice mode (student draws + measures, then Check)
  - "Show Resultant" button (gold vector + glow)

Tab 2 - Triangle + Sine/Cosine Rule:
  - 3 vectors form a closed triangle
  - Labels: sides a,b,c and angles A,B,C
  - Auto-calculates using Sine Rule and Cosine Rule
  - Shows formula + substitution + answer

Tab 3 - Component Method:
  - Toggle "Show Components": draws Fx (blue dashed) + Fy (green dashed) on grid
  - Component table: F, θ, Fx=Fcosθ, Fy=Fsinθ, ΣFx, ΣFy
  - Resultant: R = √(ΣFx²+ΣFy²), θ = tan⁻¹(ΣFy/ΣFx)
  - Toggle "Show Steps": shows step-by-step calculation

## GLOBAL
- Scale bar: "1 cm = [value] [unit]" — user defines unit (N, m/s, m, etc.)
- Angle mode toggle: From East (0°→) or From North (0°↑), format XX.X°
- 11 themes (physics-graph-authoring standard, including HAUS Day/Night)
- HAUS brand logo (yellow rounded rect top-right)
- Button order: Reset → Random → Resultant
- Theme selector dropdown

## CODE STANDARDS
- Single state object S, pure draw()/updateUI() functions
- Pointer events (not mouse), touch-action:none
- DPR-aware Math.round() dimensions
- All HAUS design tokens from physics-simulation-2d skill
- Verification: static check + logic test + screenshots

Reference existing files for patterns:
- ~/InteractiveLecture/simulations/ (for UI/state patterns)
- physics-graph-authoring skill (for theme system + niceStep)
```