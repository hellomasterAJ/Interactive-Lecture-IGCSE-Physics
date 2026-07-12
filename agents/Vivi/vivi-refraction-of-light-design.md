# Vivi Design Spec — Refraction of Light 2D Simulation

> **Author:** วีวี่ (Vivi)
> **วันที่:** 2026-07-11
> **Version:** 0.3
> **ภาษา UI:** English (ล้วน, ไม่มีภาษาไทยปน)
> **หัวข้อ:** IGCSE Physics 0625 — Refraction of Light / Snell's Law / TIR
> **สร้างจากไอเดียของ:** masterAJ (ผู้ใช้)

---

## 1. ภาพรวม (Overview)

2D Simulation แบบ standalone HTML+Canvas แสดง **การหักเหของแสงระหว่างสองตัวกลาง** (2 mediums only)

### หลักสูตรอ้างอิง
- IGCSE Physics 0625 — Refraction at a boundary
- Snell's Law / refractive index (n)
- Total Internal Reflection + Critical angle

### ขอบเขต (Scope)
- ✅ Refraction ที่ boundary ระหว่างสองตัวกลาง (Case 1: เร็ว→ช้า, Case 2: ช้า→เร็ว)
- ✅ Snell's Law โดยใช้ refractive index n (IGCSE standard: n_air = 1)
- ✅ TIR + Critical angle (เฉพาะ Case 2)
- ❌ Dispersion / Prism — แยกทำต่างหาก
- ❌ Lens (convex/concave) — แยกทำต่างหาก
- ❌ Real & Apparent depth — ไม่รวม
- ❌ ตัวอย่างประยุกต์ (fibre optics, mirage) — ไม่รวม

---

## 2. Physics Logic

### 2.1 ค่า Refractive Index + Medium Background Colors

**ทั้งหมด 6 ชนิด:**

| # | Medium | Symbol | IGCSE n | Medium Fill Color | หมายเหตุ |
|---|--------|--------|---------|------------------|----------|
| 1 | Air | — | 1.00 | `#000000` | สีพื้นหลังดำ (ใช้เส้นแสงสีขาว) |
| 2 | Water | H₂O | 1.33 | `rgba(25, 80, 160, 0.38)` | Deep blue |
| 3 | Ice | H₂O (s) | 1.31 | `rgba(180, 215, 235, 0.3)` | Frost blue |
| 4 | Perspex | Acrylic | 1.49 | `rgba(220, 215, 200, 0.22)` | Warm clear |
| 5 | Crown Glass | — | 1.52 | `rgba(195, 205, 210, 0.22)` | Neutral glass |
| 6 | Diamond | C | 2.42 | `rgba(200, 210, 220, 0.18)` | Cool white |

- **n ของอากาศ = 1** เสมอ (IGCSE convention)
- ผู้ใช้สามารถเลือก Medium ได้ 2 ตัว (Medium 1 / Medium 2) จาก dropdown
- Snell's Law: \( n_1 \sin\theta_1 = n_2 \sin\theta_2 \)
- **เมื่อ Medium 1 = Medium 2** → ไม่มีการหักเห, Ray เป็นเส้นตรง (θ₁ = θ₂)
- สีพื้นหลังของ Medium — TBD (จะออกแบบทีหลังเมื่อจำลองสีให้ดู)

- **n ของอากาศ = 1** เสมอ (IGCSE convention)
- ผู้ใช้สามารถเลือก Medium ได้ 2 ตัว (Medium 1 / Medium 2) จาก dropdown
- Snell's Law: \( n_1 \sin\theta_1 = n_2 \sin\theta_2 \)

### 2.2 สอง Case (Direction)

#### Case 1: Fast → Slow (จากเร็วไปช้า)
- เช่น อากาศ (\(n=1.00\)) → น้ำ (\(n=1.33\))
- แสงเดินทาง **จาก Medium ด้านบน → ด้านล่าง**
- IGCSE สมการย่อ: \( n = \dfrac{\sin i}{\sin r} \)
- Ray หักเห **เข้าหา Normal** (\(\theta_2 < \theta_1\))
- ไม่มี TIR

#### Case 2: Slow → Fast (จากช้าไปเร็ว)
- เช่น น้ำ (\(n=1.33\)) → อากาศ (\(n=1.00\))
- แสงเดินทาง **จาก Medium ด้านล่าง → ด้านบน**
- IGCSE สมการย่อ: \( n = \dfrac{\sin r}{\sin i} \)
- Ray หักเห **ออกจาก Normal** (\(\theta_2 > \theta_1\))
- มี 3 เงื่อนไข:
  1. **Normal** — \(\theta_1 < \theta_c\) → refraction ตามปกติ
  2. **Critical Angle** — \(\theta_1 = \theta_c\) → \(\theta_2 = 90^\circ\) (Ray วิ่งตาม boundary)
  3. **TIR** — \(\theta_1 > \theta_c\) → Total Internal Reflection (ไม่มี refracted ray)

#### Critical Angle Calculation
\[
\theta_c = \sin^{-1}\left(\frac{n_2}{n_1}\right)
\]
โดยที่ \(n_1 > n_2\) (ตัวกลางช้า → ตัวกลางเร็ว)

---

## 3. Canvas Layout & Visual Elements

### 3.1 การแบ่งพื้นที่
- **Top half** — Medium 1 (เช่น Air)
- **Bottom half** — Medium 2 (เช่น Water)
- เส้นแบ่งกลาง (Boundary) — เส้นทึบแนวนอน
- เส้น Normal — เส้นประแนวตั้ง ที่จุดที่แสงตกกระทบ (midpoint ของ canvas)

### 3.2 Ray System

| Element | สี | ค่าเริ่มต้น | หมายเหตุ |
|---------|-----|---------|---------|
| **Incident Ray** | สีเหลือง/ทอง | ON | ปรับมุมได้ด้วย mouse drag หรือ input number |
| **Refracted Ray** | สีฟ้า | ON | คำนวณจาก Snell's Law |
| **Reflected Ray** | สีส้ม | OFF (toggle ได้) | แสดงในทุก Case (รวม Case 1), ON อัตโนมัติเมื่อ TIR |
| **Normal Line** | สีขาว/เทา | ON | เส้นประแนวตั้ง |
| **Boundary Line** | สีขาว/เทา | ON | เส้นทึบแนวนอน |
| **Reflected Angle Label (θᵣ)** | สีส้ม | ON พร้อม Reflected Ray | แสดง arc + label `θᵣ = XX.X°` |

#### Special Rule: TIR
เมื่อเป็น TIR (Case 2, θ₁ > θc):
- Refracted ray **หายไป** (ไม่แสดง)
- Reflected ray **แสดงอัตโนมัติ** (override toggle)
- Incident angle = Reflected angle (θᵣ = θ₁)
- ความหนา/สีของ Reflected Ray เท่าเดิม (ไม่ต้องเปลี่ยน)

#### Wavefront (Toggle — OFF by default)
- Wavefront แสดง **ทั้งความยาวคลื่นเปลี่ยน + ทิศทางเปลี่ยน (bending)** ตาม Snell's Law
- Animation: **เล่น/หยุดได้** (Play/Pause) — wavefront ค่อย ๆ เคลื่อนที่ไปตาม Ray
- Density: **ปรับอัตโนมัติ** ตามความยาวคลื่น (ความถี่คงที่, n เปลี่ยน → λ เปลี่ยน)
- แสดง wavefront เป็นเส้นโค้งแนวตั้งฉากกับ Ray
- ระยะห่างระหว่าง wavefront = λ (ความยาวคลื่นใน medium นั้น)
  - λ₁ / λ₂ = n₂ / n₁ — wavefront spacing แคบลงใน medium ที่ช้ากว่า (n สูง)

### 3.3 Angle Display + Critical Angle Status
- มุมตกกระทบ (Incident Angle / θ₁ หรือ i) — แสดงเป็น arc + label
- มุมหักเห (Refracted Angle / θ₂ หรือ r) — แสดงเป็น arc + label
- ค่ามุมแสดงเป็นตัวเลข: **XX.X°** (ทศนิยม 1 ตำแหน่ง)
- **ห้ามตัวอักษร/ป้ายบังเส้นทางเดินของแสง** — วาง label มุมด้านนอก ไม่ใช่บน Ray

**Critical Angle Status Display:**
- แสดงข้อความบอกสถานะปัจจุบันของ θ₁ เทียบกับ θc:
  - `θ₁ < θc  —  Normal Refraction`
  - `θ₁ = θc  —  Critical Angle`
  - `θ₁ > θc  —  Total Internal Reflection`
- ข้อความแสดงตรงมุมใดมุมหนึ่งของ canvas หรือใน Status badge ฝั่ง Side Panel
- ไม่ต้องมีเอฟเฟกต์พิเศษอื่น ๆ (กระพริบ, เปลี่ยนสี)

### 3.4 Animation — แบบ B (Line draws gradually)
- **เส้น Ray ค่อย ๆ ถูกวาดเพิ่ม** (เหมือนปากกากำลังวาดเส้น) จากจุดเริ่ม → boundary → ปลายทาง
- Animation เดินหน้าเมื่อกด Play/Pause
- เมื่อปรับ Incident Angle → Animation รีเซ็ตและเริ่มใหม่
- ใช้ requestAnimationFrame, dt คงที่
- ความเร็ว Animation สามารถปรับได้ (speed slider)

---

## 4. Layout (อ้างอิงจาก Vector Addition Simulator)

### 4.1 โครงสร้างโดยรวม
```
┌─────────────────────────────────────────────────┐
│  Top Bar: Title · Mode Tabs · Theme · Brand     │
├─────────────────────────────────────────────────┤
│  Toolbar Row 1: Medium 1 / Medium 2 / Direction │
│  Toolbar Row 2: Angle Slider · Toggles · Play   │
├────────────────────────┬────────────────────────┤
│                        │                        │
│   Canvas (Ray Tracing) │  Side Panel (~1/4)     │
│   ~3/4 width           │  - Readouts (badges)   │
│                        │  - Formula Panel       │
│   Medium 1 ▓▓▓▓▓▓▓▓   │  - Practice Panel      │
│   ───── Boundary ────  │  - Quiz Panel          │
│   Medium 2 ░░░░░░░░   │  - Working/Solutions   │
│                        │                        │
└────────────────────────┴────────────────────────┘
```

### 4.2 Top Bar
- เหมือน Vector Addition: Title, Mode Tabs (Simulate/Practice/Quiz), Theme selector, Brand logo

### 4.3 Toolbar (Fixed 2 Rows)
**Row 1:** Medium 1 dropdown · Medium 2 dropdown · Direction display (auto-calculated)
**Row 2:** Incident Angle slider + input · Play/Pause · Toggles (Show Reflected, Show Wavefront, Show Angles)

### 4.4 Main Grid
```css
.main-grid {
  display: grid;
  grid-template-columns: 3fr 1fr;   /* ~75% canvas, ~25% side */
  gap: 12px;
}
```

### 4.5 Canvas Area
- Canvas สำหรับวาด Ray tracing diagram
- **ขนาด:** Responsive — ~75% ของ viewport width (square aspect ratio)
- **Boundary position:** กึ่งกลางพอดี (50:50 — Top medium 50%, Bottom medium 50%)
- Chip overlays: Scale info, Zoom status, Hint text

### 4.6 Side Panel (~25%)
- **Panel Structure:** Section แยกตาม Mode — สลับทั้งหมดเมื่อเปลี่ยน Mode
  - **Simulate Mode:** Readouts (badges) + Formula Panel (Snell's Law + live substitution)
  - **Practice Mode:** Readouts (badges) + Practice Panel (target, input, Check, Score, Worked solution)
  - **Quiz Mode:** Readouts (badges) + Quiz Panel (questions, Submit, Stars, Results table)
- **Working Solution Detail (Practice Mode):** แสดงทั้ง Step-by-step เต็ม + สรุปคำตอบ
  - Step 1–4: แสดงการคำนวณทีละขั้น
  - สรุป: `θ₂ = 22.1° (your answer: 23.0°, error: 0.9°)`

หมายเหตุ: สัดส่วน 3/4 : 1/4 อาจปรับเปลี่ยนได้ถ้าการแสดงผล Ray ไม่พอ เนื่องจาก Vector Addition ใช้ 640px + ~300px side (ประมาณ 68%:32%)
| Button | ความหมาย |
|--------|---------|
| **Simulate** | ปรับค่าอิสระ, ดูผลทันที |
| **Practice** | สุ่มค่า, นักเรียนกรอกคำตอบ, แสดง working |
| **Quiz** | 5 ข้อ, submit, แสดงคะแนน + เฉลย |

### 4.2 Parameter Controls (Row 2)

#### Medium Selection
- **Medium 1 (Top):** dropdown: Air, Water, Ice, Perspex, Crown Glass, Diamond
- **Medium 2 (Bottom):** dropdown: Air, Water, Ice, Perspex, Crown Glass, Diamond
- **เมื่อ Medium 1 = Medium 2:** ไม่มีการหักเห → Ray เป็นเส้นตรง (θ₁ = θ₂) — ปล่อยให้เลือกได้, แสดงผลตามจริง
- แต่ละ Medium มีสีพื้นหลังเฉพาะ (ดู Section 2.1)

#### Case Selector
- **Direction:** Fast→Slow / Slow→Fast (คำนวณอัตโนมัติจากค่า n, หรือให้เลือกเองได้)
- หรือคำนวณอัตโนมัติ: ถ้า n₁ < n₂ → Case 1 (Fast→Slow), ถ้า n₁ > n₂ → Case 2 (Slow→Fast)

#### Incident Angle Control
- **Slider** หรือ **Number Input** (0° — 89°)
- **Mouse Drag** — คลิกบน Incident Ray แล้ว drag เพื่อปรับมุม (drag ใกล้ปลาย ray)

#### Display Toggles
| Toggle | Default | Note |
|--------|---------|------|
| Show Reflected Ray | OFF | ON อัตโนมัติใน TIR |
| Show Wavefront | OFF | แสดง wavefront animation |
| Show Angles | ON | แสดง arc + label \(\theta_1, \theta_2\) |

### 4.3 Readout Panel (Badges/Cards)
| Card | แสดง |
|------|------|
| \(\theta_1\) | Incident Angle |
| \(\theta_2\) | Refracted Angle |
| \(n_1\) | Refractive Index Medium 1 |
| \(n_2\) | Refractive Index Medium 2 |
| \(\theta_c\) | Critical Angle (เฉพาะ Case 2) |
| Status | Normal / Critical Angle / TIR |

### 4.4 Formula Panel
แสดง Snell's Law:
\[ n_1 \sin\theta_1 = n_2 \sin\theta_2 \]
พร้อม live substitution:
\[ 1.00 \times \sin(30.0°) = 1.33 \times \sin(22.1°) \]

สำหรับ Case 1 IGCSE: \( n = \dfrac{\sin i}{\sin r} \)
สำหรับ Case 2 IGCSE: \( n = \dfrac{\sin r}{\sin i} \)

---

## 5. Three Modes

### 5.1 Simulate Mode
- **locked = false, reveal = true**
- เลือก Medium อิสระ
- ปรับ Incident Angle ด้วย Slider / Drag / Input
- ทุกค่าอ่านได้ทันที
- Toggle Reflected Ray, Wavefront, Angles

### 5.2 Practice Mode
- **locked = true, reveal = false → true on Check**
- สุ่ม Medium (สุ่มคู่ Medium แบบ logical)
- สุ่ม Incident Angle
- นักเรียนกรอกค่ามุมหักเห (หรือ n, หรือ Critical Angle)
- ✓ Check → แสดง worked solution แบบขั้นตอน:
  ```
  Step 1: n₁ sin θ₁ = n₂ sin θ₂
  Step 2: 1.00 × sin(30.0°) = 1.33 × sin(θ₂)
  Step 3: sin(θ₂) = 0.500 / 1.33 = 0.376
  Step 4: θ₂ = sin⁻¹(0.376) = 22.1°
  ```
- เปรียบเทียบคำตอบ: |student - correct| < tolerance → ✓

### 5.3 Quiz Mode
- **locked = true, reveal = false**
- 5 ข้อ (pre-generated)
- นักเรียนทำโดยไม่มีคำใบ้
- Submit → แสดงผลคะแนน
- Stars: 5/5 → ★★★, 4/5 → ★★, 3/5 → ★
- Results table: {ข้อ, target, student answer, correct?}
- เฉลยแสดงทีละข้อ

---

## 6. Interaction Patterns

### 6.1 Incident Ray Drag
```javascript
// คลิกใกล้ปลาย Incident Ray → drag เพื่อปรับมุม
cv.addEventListener("pointerdown", e => {
  if (S.locked) return;
  const world = screenToWorld(e.clientX, e.clientY);
  if (distance(world, incidentRayTip) < 20) {
    dragging = true; // lock to angle adjustment
  }
});
cv.addEventListener("pointermove", e => {
  if (!dragging || S.locked) return;
  const world = screenToWorld(e.clientX, e.clientY);
  const angle = Math.atan2(world.y - origin.y, world.x - origin.x);
  S.incidentAngle = clampAngle(angle);
  updateSimulation();
});
```

### 6.2 Double-click Zoom
- Double-click → toggle zoom mode (zoom into boundary area)
- Esc → exit zoom

### 6.3 Keyboard
- Arrow Up/Down → ปรับ Incident Angle (±1°)
- Shift + Arrow → ±5°
- Esc → exit zoom
- Enter (ใน input) → submit check/quiz

---

## 7. HAUS Design Tokens

```css
:root{
  --bg: #0d1117;
  --card: #161b22;
  --card2: #1c2430;
  --border: #30363d;
  --text: #e6edf3;
  --dim: #8b949e;
  --accent: #e3b341;     /* ทอง — Incident Ray, ค่าหลัก */
  --blue: #58a6ff;       /* Refracted Ray */
  --orange: #f0883e;     /* Reflected Ray */
  --green: #3fb950;
  --red: #f85149;
  --gold: #ffd700;
}
```

---

## 8. Ray Color Scheme

| Element | Color (Dark theme) | Hex |
|---------|-------------------|-----|
| Incident Ray | Gold / Yellow | `#e3b341` |
| Refracted Ray | Blue | `#58a6ff` |
| Reflected Ray | Orange | `#f0883e` |
| Normal Line | Dim white (dashed) | `#8b949e` |
| Boundary Line | Dim white (solid) | `#8b949e` |
| Medium 1 Fill | Transparent tint | — |
| Medium 2 Fill | Transparent tint (different) | — |
| Wavefront | Cyan (translucent) | `rgba(56, 178, 255, 0.3)` |

---

## 9. State Object Structure

```javascript
const S = {
  // Medium
  medium1: { name: 'Air', n: 1.00 },
  medium2: { name: 'Water', n: 1.33 },
  
  // Case
  caseDirection: 'fast-to-slow', // 'fast-to-slow' | 'slow-to-fast'
  
  // Angles (degrees)
  incidentAngle: 30.0,   // θ₁ (0°–89°)
  refractedAngle: 0,     // θ₂ (calculated)
  criticalAngle: 0,      // θc (calculated, case 2 only)
  
  // Ray toggles
  showReflected: false,
  showWavefront: false,
  showAngles: true,
  
  // Animation
  animating: false,
  animProgress: 0,       // 0–1
  animSpeed: 1.0,
  
  // Mode
  mode: 'simulate',      // 'simulate' | 'practice' | 'quiz'
  locked: false,
  reveal: true,
  
  // Zoom
  zoom: false,
};
```

---

## 10. Derived Quantities

```javascript
const isCase1 = () => S.medium1.n < S.medium2.n;  // Fast→Slow
const isCase2 = () => S.medium1.n > S.medium2.n;  // Slow→Fast
const hasRefraction = () => S.medium1.n !== S.medium2.n;

const calcRefractedAngle = () => {
  // n₁ sin θ₁ = n₂ sin θ₂
  const sinθ2 = (S.medium1.n * Math.sin(degToRad(S.incidentAngle))) / S.medium2.n;
  if (sinθ2 > 1) return null; // TIR
  if (sinθ2 < -1) return null;
  return radToDeg(Math.asin(sinθ2));
};

const calcCriticalAngle = () => {
  if (S.medium1.n <= S.medium2.n) return null; // No TIR
  return radToDeg(Math.asin(S.medium2.n / S.medium1.n));
};

const getCondition = () => {
  if (isCase1()) return 'normal';
  const θc = calcCriticalAngle();
  if (θc === null) return 'normal';
  if (S.incidentAngle < θc) return 'normal';
  if (Math.abs(S.incidentAngle - θc) < 0.1) return 'critical';
  return 'tir';
};
```

---

## 11. Verification

- ✅ [ ] Static: node --check script syntax
- ✅ [ ] Logic: Snell's Law round-trip (θ₁ → θ₂ → θ₁) exhaustive
- ✅ [ ] Boundary: θ₁ = 0° (straight through), θ₁ = 89° (near grazing)
- ✅ [ ] TIR threshold: θ₁ = θc → θ₂ = 90°
- ✅ [ ] TIR region: θ₁ > θc → no refracted ray
- ✅ [ ] Case direction swapped automatically when medium swapped
- ✅ [ ] Angles arc labels don't overlap rays
- ✅ [ ] Animation reset on parameter change
- ✅ [ ] Mediums can't be identical (or at least handle n₁ = n₂)
- ✅ [ ] Screenshot every mode + every condition

---

> *📌 บันทึกโดย วีวี่ — Refraction of Light Design Spec v0.2  |  สร้างจากไอเดียของ masterAJ*