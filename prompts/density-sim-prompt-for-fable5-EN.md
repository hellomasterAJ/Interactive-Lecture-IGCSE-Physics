# Prompt: Density 2D Simulation — IGCSE Physics (0625)
## For Fable 5.0 (Anthropic)

---

## 1. Overview

Build an **interactive 2D Physics Simulation** (single-file HTML + Canvas 2D) for the **Density experiment** following the **IGCSE Physics 0625** curriculum.

Users can:
- Freely choose mass and volume measurement devices
- Drag objects onto measurement devices
- Measure mass and volume in any order
- View Density results with step-by-step unit conversion

---

## 2. Layout (3 Main Sections)

### 📐 Layout 1 — Main Panel for Options (Top toolbar)
Full-width dark gray toolbar containing:

**Row 1:**
- **Mode:** Simulate | Practice | Quiz (pill buttons)
- **g value Toggle:** Simple (g = 10 N/kg) ↔ Actual (g = 9.81 N/kg)
- **Theme Selector:** 6 themes (dropdown)
  - 🌙 Classic Dark | ⌂ HAUS Night | 🌃 Cyberpunk Neon | ☀️ Classic Light | ⌂ HAUS Day | 🏺 Warm Clay
- **HAUS Brand Logo** (top-right corner)

**Row 2:**
- **Mass Device Selection:** Spring Balance | Top-pan Balance (pill toggle — shows one at a time)
- **Volume Device Selection:** Measuring Cylinder | Eureka Can (pill toggle — shows one at a time)
- **Reset Button**

### 📐 Layout 2 — Experiment Area (Middle)
Light background, divided into 3 zones:

**Zone 1 (Top, compact area):** Choose / Random Object
- Shows all 6+ objects (Irregular shape, insoluble in water)
- 🎲 Random button — randomizes Object only (user chooses device manually)

**Zone 2 (Bottom-left, equal width with Zone 3):** Finding Mass Zone
- Shows the selected mass device **one at a time** (as chosen in Layout 1)
  - If **Spring Balance** selected → only Spring Balance visible (no Top-pan Balance)
  - If **Top-pan Balance** selected → only Top-pan Balance visible
- Drag Object from Zone 1 onto the device to measure
- Spring Balance: Measures weight (N) → user or system converts to mass (m = W/g)
- Top-pan Balance: Measures mass directly (g / kg)
- When measurement completes → shows ✅ status

**Zone 3 (Bottom-right, equal width with Zone 2):** Finding Volume Zone
- Shows the selected volume device **one at a time** (as chosen in Layout 1)
  - If **Measuring Cylinder** selected → only Cylinder visible
  - If **Eureka Can** selected → only Eureka Can visible
- Drag Object from Zone 1 onto the device to measure
- When measurement completes → shows ✅ status

**Zone 2 & 3 Behavior:**
- Measure in any order
- When both measurements complete → **show Density calculation**
- If user changes Object → both measurements reset

### 📐 Layout 3 — Outputs and Details (Bottom bar)
Dark gray bar showing results:

**Badges (compact key values):**
- m = [value] [unit]
- V = [value] [unit]
- ρ = [value] [unit]

**Cards (3):**
- Card 1: Mass value (g / kg)
- Card 2: Volume value (mL / cm³)
- Card 3: Density value (g/cm³ or kg/m³ — as selected)

**Formula Panel:**
- ρ = m / V
- Shows substitution with step-by-step working
- **Unit Toggle:** g/cm³ ↔ kg/m³
  - When g/cm³ selected → show unit conversion steps for mass and volume to g and cm³ respectively → then substitute into formula
  - When kg/m³ selected → show unit conversion steps for mass and volume to kg and m³ respectively → then substitute into formula

**Info Boxes:**
- Density concept explanation
- Compare calculated Density with the object's actual Density (shows whether measurement is correct)

---

## 3. Object Data (6+ Known Objects + Unknown Random Objects)

All objects are **Irregular Solids** (insoluble in water). Uses real Density values.

### 3A. Known Objects (Reference Objects)

These objects have fixed mass and volume values, consistent with the material's real Density (m = ρ × V, with V chosen as clean numbers):

| # | Object | Material | ρ (g/cm³) | V (cm³) | m (g) | ρ (kg/m³) | Notes |
|---|--------|----------|-----------|---------|-------|-----------|-------|
| 1 | Copper Statue | Copper | 8.96 | 25 | 224.0 | 8960 | Realistic 3D model |
| 2 | Granite Rock | Granite | 2.70 | 50 | 135.0 | 2700 | Rough surface |
| 3 | Die-cast Toy | Zinc Alloy | 7.50 | 20 | 150.0 | 7500 | High detail |
| 4 | Steel Sphere | Steel | 7.87 | 100 | 787.0 | 7870 | Polished |
| 5 | Lead Block | Lead | 11.34 | 50 | 567.0 | 11340 | Heavy, dense |
| 6 | Cast Aluminium | Aluminium | 2.70 | 20 | 54.0 | 2700 | Matte silver |
| 7 | Limestone Fossil | Limestone | 2.75 | 20 | 55.0 | 2750 | Rough surface |
| 8 | Glass Marble | Glass | 2.50 | 20 | 50.0 | 2500 | Transparent, glossy |

### 3B. Unknown Objects (Random — for Practice / Quiz)

These objects do **NOT** reveal m, V, or ρ in advance — the student must measure all values themselves.

**Random Unknown Object System:**
- Randomize **Material** (from the Known Objects table above) — without revealing the material to the user
- Randomize **Volume (V)** within an appropriate range for that material, e.g.:
  - Copper: 5–100 cm³ (step 1)
  - Steel: 10–200 cm³ (step 1)
  - Lead: 5–80 cm³ (step 1)
  - Granite: 20–500 cm³ (step 1)
  - Others: similarly appropriate ranges
- Calculate **Mass (m) = ρ × V** (using the material's real Density)
- Display as **Unknown Object #N** (e.g., "Unknown Object #1", "#2")
- **Physical appearance:** Draw as a random irregular shape (changes every time) — realistic look

**Volume (V) randomization must respect equipment constraints:**
- Must fit inside the auto-sized Measuring Cylinder
- Must not exceed the Spring Balance auto-range
- Should be suitable for the Top-pan Balance (max 2 kg)

**Unknown Object Example:**
```
Unknown Object #3
Material: Steel (hidden from user)
V = 73 cm³
m = 7.87 × 73 = 574.51 g
ρ = 7.87 g/cm³ (correct answer)
```

> **NOTE:** Known Objects are used in Simulate Mode (values visible)  
> **Unknown Objects** are used in Practice / Quiz Mode (student measures everything)

---

## 4. Mass Measurement Devices (Mass Zone)

### Spring Balance (Newtonmeter)
- Measures **Weight** in **N**
- User must convert to mass: **m = W / g**
- Simple Mode: g = 10 N/kg → m = W / 10
- Actual Mode: g = 9.81 N/kg → m = W / 9.81
- Has an N scale with pointer needle
- Auto-range based on object weight
- **Shows only one at a time** (no Top-pan Balance visible simultaneously)

### Top-pan Balance
- Measures **mass** directly in **g** or **kg** (unit selectable)
- Has an LCD digital display
- **Shows only one at a time** (no Spring Balance visible simultaneously)

---

## 5. Volume Measurement Devices (Volume Zone)

### Measuring Cylinder
- **Auto-selects size** based on the selected object (object must fit inside the cylinder)
- Clear scale markings
- **Read the Meniscus** (water surface curvature)
- **Zoom In/Out system** for the specific scale being read
- Liquid: plain water
- **Simulate:** shows volume reading automatically
- **Practice/Quiz:** user must read the scale and type the answer

### Eureka Can (Displacement Can)
- **Simulate:** runs automatically
  1. Fill water to overflowing
  2. Wait for water to stop dripping
  3. Place the object in
  4. Water overflows
  5. Show volume reading
- **Practice/Quiz:** user must read from the scale and type the answer
- **Simulate:** automatically pours overflow water into Measuring Cylinder for viewing
- **Practice/Quiz:** user performs the steps → reads the scale → enters the answer

---

## 6. Modes

### Simulate Mode
- Free exploration
- All values shown (Mass, Volume, Density)
- No restrictions
- Change Object / device at any time

### Practice Mode
- User clicks "New Question" → random Object generated
- System locks the device (cannot be changed)
- User must:
  1. Drag Object to measure mass (read scale yourself)
  2. Drag Object to measure volume (read scale yourself)
  3. Enter the calculated Density
- Press "Check" → shows ✅/❌ + **detailed step-by-step working** (unit conversion + formula substitution)
- Running score (Score: X/Y)

### Quiz Mode
- 5 questions per round
- Random Object + Random device (Spring/Top-pan, Cylinder/Eureka)
- User must measure, enter values, and calculate Density
- Submit → check answer → next question
- End of round: show score + ★★★ (5/5=★★★, 4/5=★★, 3/5=★)
- Quiz results summary table

---

## 7. Unit Conversion (Layout 3)

When both mass and volume measurements complete:

**If g/cm³ selected:**
1. Show: "Convert mass: [value] kg → [value] g (× 1000)"
2. Show: "Convert volume: [value] m³ → [value] cm³ (× 1,000,000)"
3. Show: "ρ = m / V = [value] g / [value] cm³ = [result] g/cm³"

**If kg/m³ selected:**
1. Show: "Convert mass: [value] g → [value] kg (÷ 1000)"
2. Show: "Convert volume: [value] cm³ → [value] m³ (÷ 1,000,000)"
3. Show: "ρ = m / V = [value] kg / [value] m³ = [result] kg/m³"

---

## 8. Visual & Theme

### 6 Themes (Balanced)
| # | Value | Label | Type |
|---|-------|-------|------|
| 1 | `dark` | 🌙 Classic Dark | Dark |
| 2 | `hausnight` | ⌂ HAUS Night | Dark |
| 3 | `neon` | 🌃 Cyberpunk Neon | Dark |
| 4 | `light` | ☀️ Classic Light | Light |
| 5 | `haus` | ⌂ HAUS Day | Light |
| 6 | `clay` | 🏺 Warm Clay | Light |

### Design Tokens (HAUS Academy)
- Font: Inter (UI), JetBrains Mono (formulas/values)
- DPR-aware Canvas
- Drop shadows, metal gradients, realistic textures
- Dark theme: bg #0d1117, card #161b22, accent #e3b341
- HAUS Brand: logo with yellow background on dark themes

### Layout Proportions
- Layout 1: ~60px height (toolbar)
- Layout 2: ~70% of remaining space (experiment area)
- Layout 3: ~30% of remaining space (outputs)

---

## 9. Interaction Patterns

### Drag & Drop
- Object → Zone 1 (source area)
- Drag object from Zone 1 → Zone 2 (snap to device)
- Drag object from Zone 1 → Zone 3 (snap to device)
- Drag object back to Zone 1 to remove from device

### Zoom on Scale
- Double-click or hover near scale → zoom in
- Show magnified view of the scale reading area
- Zoom out automatically or via button

### Measurement Complete
- ✅ badge appears on the zone when measurement is done
- Both zones ✅ → Layout 3 shows density calculation
- If user changes object → both ✅ reset

---

## 10. Reference Implementation

See `Measurement_3_balance_newtonmeter.html` (Mass vs Weight simulation) as reference for:
- Canvas rendering pattern (DPR, coordinate transforms)
- Drag-and-drop interaction
- Pill button UI pattern
- Mode machine (Simulate/Practice/Quiz)
- Feedback system (check/feed/work)
- Quiz scoring with stars

---

## 11. File Requirements

- **Single HTML file** (standalone, no external dependencies except Google Fonts)
- Place at: `~/InteractiveLecture/simulations/Measurement_4_density.html`
- Use real density values in calculations
- IGCSE-friendly numbers (clean integers preferred)
- Use English in UI (default)

---

## Feature Checklist

- [x] 3 Layouts (Options / Experiment / Outputs)
- [x] 3 Zones in Experiment Area (Object / Mass / Volume)
- [x] 6+ Irregular Solid Objects (Real Density)
- [x] Spring Balance + Top-pan Balance (selectable, one at a time)
- [x] Measuring Cylinder + Eureka Can (selectable, one at a time)
- [x] Auto-size Cylinder based on Object
- [x] Meniscus + Zoom on Scale
- [x] 3 Modes (Simulate / Practice / Quiz)
- [x] Unit Toggle (g/cm³ ↔ kg/m³) with step-by-step conversion
- [x] g value Toggle (Simple 10 / Actual 9.81)
- [x] 6 Themes
- [x] Drag & Drop Objects
- [x] ✅ Status when measurement completes
- [x] Unknown Objects (random m = ρ × V) for Practice/Quiz
- [x] Density Calculation + Formula + Step-by-step working
- [x] Compare with actual Density