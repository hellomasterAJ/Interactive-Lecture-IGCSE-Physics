# Prompt: Density 2D Simulation — IGCSE Physics (0625)
## สำหรับ Fable 5.0 (Anthropic)

---

## 1. ภาพรวม

สร้าง **2D Physics Simulation แบบโต้ตอบได้** (single-file HTML + Canvas 2D) สำหรับการทดลองหา **ค่า Density (ความหนาแน่น)** ตามหลักสูตร IGCSE Physics 0625

ผู้ใช้สามารถ:
- เลือกอุปกรณ์วัดมวลและปริมาตรได้อิสระ
- ลาก Object ไปวางบนอุปกรณ์วัด
- วัดมวลและปริมาตรตามลำดับใดก็ได้
- ดูผลลัพธ์ Density พร้อมขั้นตอนการแปลงหน่วย

---

## 2. Layout (3 ส่วนหลัก)

### 📐 Layout 1 — Main Panel for Options (แถบด้านบน)
แถบควบคุมสีเทาเข้มเต็มความกว้าง ประกอบด้วย:

**แถวที่ 1:**
- **Mode:** Simulate | Practice | Quiz (pill buttons)
- **g value Toggle:** Simple (g = 10 N/kg) ↔ Actual (g = 9.81 N/kg)
- **Theme Selector:** 6 ธีม (dropdown)
  - 🌙 Classic Dark | ⌂ HAUS Night | 🌃 Cyberpunk Neon | ☀️ Classic Light | ⌂ HAUS Day | 🏺 Warm Clay
- **HAUS Brand Logo** (มุมขวา)

**แถวที่ 2:**
- **Mass Device Selection:** Spring Balance | Top-pan Balance (pill toggle — แสดงที่ละอย่าง)
- **Volume Device Selection:** Measuring Cylinder | Eureka Can (pill toggle — แสดงที่ละอย่าง)
- **Reset Button**

### 📐 Layout 2 — Experiment Area (พื้นที่กลาง)
พื้นหลังสีอ่อน แบ่งเป็น 3 โซน:

**Zone 1 (บน, พื้นที่ไม่ต้องใหญ่):** Choose / Random Object
- แสดง Object ทั้งหมด 6+ ชิ้น (Irregular shape, ไม่ละลายน้ำ)
- ปุ่ม 🎲 Random — สุ่ม Object อย่างเดียว (อุปกรณ์ผู้ใช้เลือกเอง)

**Zone 2 (ล่างซ้าย, กว้างเท่ากับ Zone 3):** Finding Mass Zone
- แสดงอุปกรณ์วัดมวล/น้ำหนัก **ทีละอย่าง** ตามที่เลือกใน Layout 1
  - ถ้าเลือก **Spring Balance** → เห็นแค่ Spring Balance (ไม่มี Top-pan Balance)
  - ถ้าเลือก **Top-pan Balance** → เห็นแค่ Top-pan Balance
- Drag Object จาก Zone 1 มาวางบนอุปกรณ์เพื่อวัด
- Spring Balance: วัดน้ำหนัก (N) → ผู้ใช้หรือระบบแปลงเป็นมวล (m = W/g)
- Top-pan Balance: วัดมวลโดยตรง (g / kg)
- เมื่อวัดสำเร็จ → แสดง ✅ status

**Zone 3 (ล่างขวา, กว้างเท่ากับ Zone 2):** Finding Volume Zone
- แสดงอุปกรณ์วัดปริมาตร **ทีละอย่าง** ตามที่เลือกใน Layout 1
  - ถ้าเลือก **Measuring Cylinder** → เห็นแค่ Cylinder
  - ถ้าเลือก **Eureka Can** → เห็นแค่ Eureka Can
- Drag Object จาก Zone 1 มาวางบนอุปกรณ์เพื่อวัด
- เมื่อวัดสำเร็จ → แสดง ✅ status

**การทำงานของ Zone 2 & 3:**
- วัดส่วนไหนก่อนก็ได้ (อิสระ)
- ถ้าวัดสำเร็จทั้งสอง → **แสดงผลการคำนวณ Density**
- ถ้าเปลี่ยน Object → ต้องเริ่มวัดใหม่ทั้งหมด

### 📐 Layout 3 — Outputs and Details (แถบล่าง)
แถบสีเทาเข้ม แสดงผลลัพธ์:

**Badges (ค่าสำคัญแบบย่อ):**
- m = [value] [unit]
- V = [value] [unit]
- ρ = [value] [unit]

**Cards (3 ใบ):**
- Card 1: ค่า Mass (g / kg)
- Card 2: ค่า Volume (mL / cm³)
- Card 3: ค่า Density (g/cm³ หรือ kg/m³ — ตามที่เลือก)

**Formula Panel:**
- ρ = m / V
- แสดงเลขแทนค่าพร้อมขั้นตอน
- **Unit Toggle:** g/cm³ ↔ kg/m³
  - เมื่อเลือก g/cm³ → แสดงขั้นตอนการแปลงหน่วยของมวลและปริมาตรเป็น g และ cm³ ตามลำดับ → จากนั้นแทนค่าในสูตร
  - เมื่อเลือก kg/m³ → แสดงขั้นตอนการแปลงหน่วยของมวลและปริมาตรเป็น kg และ m³ ตามลำดับ → จากนั้นแทนค่าในสูตร

**Info Boxes:**
- คำอธิบาย concept Density
- เปรียบเทียบค่า Density ที่คำนวณได้กับค่า Density จริงของวัตถุ (บอกว่าถูกต้องหรือไม่)

---

## 3. Object Data (อย่างน้อย 6 ชิ้น + Unknown Objects)

วัตถุทั้งหมดเป็น **Irregular Solid** (ไม่ละลายน้ำ) ใช้ค่า Density จริง

### 3A. Known Objects (วัตถุอ้างอิง)

วัตถุเหล่านี้มีค่ามวลและปริมาตรที่แน่นอน สอดคล้องกับ Density จริงของวัสดุ (ใช้ m = ρ × V โดยเลือก V เป็นเลขสวย):

| # | Object | Material | ρ (g/cm³) | V (cm³) | m (g) | ρ (kg/m³) | หมายเหตุ |
|---|--------|----------|-----------|---------|-------|-----------|---------|
| 1 | Copper Statue | Copper | 8.96 | 25 | 224.0 | 8960 | เหมือนจริง 3D |
| 2 | Granite Rock | Granite | 2.70 | 50 | 135.0 | 2700 | ผิวขรุขระ |
| 3 | Die-cast Toy | Zinc Alloy | 7.50 | 20 | 150.0 | 7500 | รายละเอียดสูง |
| 4 | Steel Sphere | Steel | 7.87 | 100 | 787.0 | 7870 | ขัดเงา |
| 5 | Lead Block | Lead | 11.34 | 50 | 567.0 | 11340 | หนัก ทึบ |
| 6 | Cast Aluminium | Aluminium | 2.70 | 20 | 54.0 | 2700 | สีเงินด้าน |
| 7 | Limestone Fossil | Limestone | 2.75 | 20 | 55.0 | 2750 | ผิวขรุขระ |
| 8 | Glass Marble | Glass | 2.50 | 20 | 50.0 | 2500 | ใส เงา |

### 3B. Unknown Objects (วัตถุสุ่ม — สำหรับ Practice / Quiz)

วัตถุประเภทนี้ **ไม่บอก m, V, ρ** ล่วงหน้า — ผู้ทดลองต้องวัดค่าทั้งหมดเอง

**ระบบ Random Unknown Object:**
- สุ่ม **Material** (จากตาราง Known Objects ด้านบน) — แต่ไม่บอกผู้ใช้ว่าเป็นวัสดุอะไร
- สุ่ม **Volume (V)** ภายในช่วงที่เหมาะสมของวัสดุนั้น เช่น:
  - Copper: 5–100 cm³ (step 1)
  - Steel: 10–200 cm³ (step 1)
  - Lead: 5–80 cm³ (step 1)
  - Granite: 20–500 cm³ (step 1)
  - อื่นๆ: ตามความเหมาะสม
- คำนวณ **Mass (m) = ρ × V** (ใช้ Density จริงของวัสดุนั้น)
- แสดงผลเป็น **Unknown Object #N** (เช่น "Unknown Object #1", "#2")
- **Physical appearance:** วาดเป็น irregular shape แบบสุ่ม (เปลี่ยนรูปร่างทุกครั้ง) — ดูสมจริง

**การสุ่ม Volume (V) ต้องเป็นไปตามข้อจำกัดของอุปกรณ์:**
- ต้องสามารถใส่ลงใน Measuring Cylinder ที่ auto-size ได้
- ต้องไม่เกินช่วงของ Spring Balance (auto-range)
- ควรเหมาะสมกับ Top-pan Balance (ไม่เกิน 2 kg)

**ตัวอย่าง Unknown Object:**
```
Unknown Object #3
Material: Steel (ซ่อนจากผู้ใช้)
V = 73 cm³
m = 7.87 × 73 = 574.51 g
ρ = 7.87 g/cm³ (คำตอบที่ถูกต้อง)
```

> **หมายเหตุ:** Known Objects ใช้ใน Simulate Mode (ให้เห็นค่าจริง)  
> **Unknown Objects** ใช้ใน Practice / Quiz Mode (ผู้ใช้ต้องวัดเอง)

---

## 4. อุปกรณ์วัดมวล (Mass Zone)

### Spring Balance (Newtonmeter)
- วัดน้ำหนัก (Weight) เป็น **N**
- ผู้ใช้ต้องแปลงเป็นมวล: **m = W / g**
- Simple Mode: g = 10 N/kg → m = W / 10
- Actual Mode: g = 9.81 N/kg → m = W / 9.81
- มีสเกลแสดง N พร้อมเข็มชี้
- Auto-range ตามน้ำหนักของ object
- **แสดง spring balance ทีละอัน** (ไม่แสดง Top-pan Balance พร้อมกัน)

### Top-pan Balance
- วัดมวล (Mass) โดยตรง เป็น **g** หรือ **kg** (เลือกหน่วยได้)
- มี LCD แสดงตัวเลข
- **แสดง Top-pan Balance ทีละอัน** (ไม่แสดง Spring Balance พร้อมกัน)

---

## 5. อุปกรณ์วัดปริมาตร (Volume Zone)

### Measuring Cylinder
- **Auto-select ขนาด** ตาม Object ที่เลือก (object ต้องใส่เข้าไปใน cylinder ได้)
- แสดงขีดสเกลชัดเจน
- **อ่านค่า Meniscus** (ผิวเว้าของน้ำ)
- **ระบบ Zoom In/Out เฉพาะที่สเกล** ที่กำลังวัดอยู่
- ของเหลว: น้ำเปล่า
- **Simulate:** แสดงค่าปริมาตรอัตโนมัติ
- **Practice/Quiz:** ผู้ใช้ต้องอ่านค่าจากสเกลและพิมพ์คำตอบเอง

### Eureka Can (Displacement Can)
- **Simulate:** ทำงานอัตโนมัติ
  1. เติมน้ำจนล้น
  2. รอให้น้ำหยุด
  3. ใส่ Object ลงไป
  4. น้ำล้นออกมา
  5. แสดงปริมาตร
- **Practice/Quiz:** ผู้ใช้ต้องอ่านค่าจากสเกลและพิมพ์คำตอบเอง
- **Simulate:** เทน้ำที่ล้นใส่ Measuring Cylinder ให้ดูอัตโนมัติ
- **Practice/Quiz:** ผู้ใช้ดำเนินการเอง → อ่านค่าจากสเกล → ใส่คำตอบ

---

## 6. Modes

### Simulate Mode
- ทดลองอิสระ
- แสดงค่าทั้งหมด (Mass, Volume, Density)
- ไม่มีข้อจำกัด
- เปลี่ยน Object / อุปกรณ์ ได้ตลาด

### Practice Mode
- ผู้ใช้คลิก "New Question" → สุ่ม Object
- ระบบ Lock อุปกรณ์ (เปลี่ยนไม่ได้)
- ผู้ใช้ต้อง:
  1. Drag Object ไปวัดมวล (อ่านค่าเอง)
  2. Drag Object ไปวัดปริมาตร (อ่านค่าเอง)
  3. ใส่ค่า Density ที่คำนวณได้
- กด "Check" → แสดง ✅/❌ + **ขั้นตอนการทำแบบละเอียด** (วิธีแปลงหน่วย + แทนค่าในสูตร)
- นับคะแนนสะสม (Score: X/Y)

### Quiz Mode
- 5 ข้อต่อรอบ
- สุ่ม Object + สุ่มอุปกรณ์ (Spring/Top-pan, Cylinder/Eureka)
- ผู้ใช้ต้องวัด ใส่ค่า และคำนวณ Density
- Submit → เช็คคำตอบ → ข้อต่อไป
- จบรอบ: แสดงคะแนน + ★★★ (5/5=★★★, 4/5=★★, 3/5=★)
- ตารางสรุปผลการทำ Quiz

---

## 7. การแปลงหน่วย (Unit Conversion in Layout 3)

เมื่อวัดมวลและปริมาตรสำเร็จ:

**ถ้าเลือกหน่วย g/cm³:**
1. แสดง: "Convert mass: [value] kg → [value] g (× 1000)"
2. แสดง: "Convert volume: [value] m³ → [value] cm³ (× 1,000,000)"
3. แสดง: "ρ = m / V = [value] g / [value] cm³ = [result] g/cm³"

**ถ้าเลือกหน่วย kg/m³:**
1. แสดง: "Convert mass: [value] g → [value] kg (÷ 1000)"
2. แสดง: "Convert volume: [value] cm³ → [value] m³ (÷ 1,000,000)"
3. แสดง: "ρ = m / V = [value] kg / [value] m³ = [result] kg/m³"

---

## 8. Visual & Theme

### 6 ธีม (Balanced)
| # | Value | Label | Type |
|---|-------|-------|------|
| 1 | `dark` | 🌙 Classic Dark | Dark |
| 2 | `hausnight` | ⌂ HAUS Night | Dark |
| 3 | `neon` | 🌃 Cyberpunk Neon | Dark |
| 4 | `light` | ☀️ Classic Light | Light |
| 5 | `haus` | ⌂ HAUS Day | Light |
| 6 | `clay` | 🏺 Warm Clay | Light |

### Design Tokens (อ้างอิงจาก HAUS Academy)
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

ดูไฟล์ `Measurement_3_balance_newtonmeter.html` (Mass vs Weight simulation) เป็น reference สำหรับ:
- Canvas rendering pattern (DPR, coordinate transforms)
- Drag-and-drop interaction
- Pill button UI pattern
- Mode machine (Simulate/Practice/Quiz)
- Feedback system (check/feed/work)
- Quiz scoring with stars

---

## 11. File Requirements

- **Single HTML file** (standalone, no external dependencies except Google Fonts)
- วางที่: `~/InteractiveLecture/simulations/Measurement_4_density.html`
- ใช้ค่าจริง (real density values) ในการคำนวณ
- ตัวเลขที่ใช้ใน IGCSE ควรเป็น integer-friendly
- ใช้ภาษาไทย/อังกฤษใน UI (default: English)

---

## สรุป Feature ที่ต้องมี

- [x] 3 Layout (Options / Experiment / Outputs)
- [x] 3 Zones ใน Experiment Area (Object / Mass / Volume)
- [x] 6+ Irregular Solid Objects (Real Density)
- [x] Spring Balance + Top-pan Balance (เลือกได้)
- [x] Measuring Cylinder + Eureka Can (เลือกได้)
- [x] Auto-size Cylinder ตาม Object
- [x] Meniscus + Zoom on Scale
- [x] 3 Modes (Simulate / Practice / Quiz)
- [x] Unit Toggle (g/cm³ ↔ kg/m³) พร้อมขั้นตอนแปลง
- [x] g value Toggle (Simple 10 / Actual 9.81)
- [x] 6 ธีม
- [x] Drag & Drop Object
- [x] ✅ Status เมื่อวัดสำเร็จ
- [x] Unknown Objects (สุ่ม m = ρ × V) สำหรับ Practice/Quiz
- [x] Density Calculation + Formula + Step-by-step
- [x] เปรียบเทียบกับ Density จริง