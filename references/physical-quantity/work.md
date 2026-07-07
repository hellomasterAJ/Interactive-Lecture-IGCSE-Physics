---
title: Work
field: Mechanics
type: physical-quantity
si_unit: joule (J)
symbol: W
dimension: [M·L²·T⁻²]
version: 1
tags: [work, mechanics, energy, force, displacement]
related_lectures: [topic17_energy]
related_terminology: [energy, newtons_laws]
related_physical_quantity: [energy, power, force, torque]
---

# 🔧 Work

> **Work = แรงกระทำ × ระยะทางในทิศของแรง**
>
> W = F·s·cosθ — หน่วย J (N·m)

---

## 📜 ประวัติศาสตร์

| ปี | บุคคล | การค้นพบ |
|----|-------|-----------|
| **~1820s** | **Gustave Coriolis** | ใช้คำว่า **"travail"** (work) เป็นครั้งแรก — W = F·s |
| | | → วางรากฐานของแนวคิด work–energy |
| **1829** | **Coriolis** | *Du Calcul de l'Effet des Machines* — ½mv² = kinetic energy |
| **~1840s** | **Joule** | Mechanical equivalent of heat: W→Q |
| | | — ใช้ระบบล้อถ่วงน้ำหนัก → stirring → วัดความร้อน |
| **~1850** | **Clausius, Kelvin** | First Law: ΔU = Q − W |

---

## ⚛️ นิยามทางฟิสิกส์

### Work done by constant force
```
W = F · s · cosθ

W = F · d (เฉพาะเมื่อ F ∥ d → cosθ = 1)
W = 0 เมื่อ F ⟂ d (cosθ = 0)
W < 0 เมื่อ F ตรงข้ามกับ d (cosθ = −1 → friction)
```

### Work done by non-constant force
```
W = ∫ F · dr = ∫ F(x) dx (ใน 1D)

ตัวอย่าง: spring: W = ∫₀ˣ kx dx = ½kx²
```

### Work–Energy Theorem
```
W_net = ΔK = ½mv² − ½mu²

Work ที่ทำต่อวัตถุ = การเปลี่ยนแปลงของ kinetic energy
```

### Work with friction
```
W_friction = −f·d
W_net = W_applied + W_gravity + W_friction + W_normal + ...

เมื่อ W_net = ΔK
```

---

## 🌍 ตัวอย่างในชีวิตจริง

| กิจกรรม | Work (J) |
|---------|----------|
| 📖 ยกหนังสือ 2 kg ขึ้น 1 m | ≈ 19.6 J |
| 🏃 วิ่งขึ้นบันได 10 ชั้น (~30 m) | ≈ 20,000 J (70 kg × 10 m × 9.81 × ~3) |
| 🚲 ปั่นจักรยาน 1 km (flat) | ≈ 50,000–100,000 J |
| 🚗 รถ 1,000 kg → 100 km/h | ½ × 1,000 × (27.8)² ≈ 386,000 J (ไม่รวม friction) |
| 🎾 ตีลูกเทนนิส | ≈ 100–150 J |
| ☀️ โลกโคจรรอบดวงอาทิตย์ | **0** (F ⟂ v เสมอ → gravity do no work!) |

---

## 💡 ความเข้าใจผิดที่พบบ่อย

| ความเข้าใจผิด | ความจริง |
|----------------|---------|
| "ถือของนิ่งๆ = เหนื่อย → ทำงาน" | **ไม่** — W = F·d — distance = 0 → W = 0 — กล้ามเนื้อเรา hiccup ทำ work ทางชีววิทยา |
| "Work = force × distance เสมอ" | **W = F·s·cosθ** — แรงไม่ขนานกับ displacement → work ลดลง |
| "Work = energy" | **Work = เปลี่ยนรูปของ energy** — W > 0 → energy เพิ่ม — W < 0 → energy ลด |
| "ถ้า F ⟂ v → work" | **W = 0** — gravity ในวงโคจร = 0 |
| "No work done = ไม่เหนื่อย" | การออกแรงนิ่งไม่ทำ work ทางฟิสิกส์ แต่กล้ามเนื้อใช้ energy จริง | 

---

## 🔗 อ้างอิง

- Coriolis, G. (1829). *Du Calcul de l'Effet des Machines*
- Joule, J. P. (1843). *On the Calorific Effects of Magneto-Electricity*
- Feynman R. P. (1963). *Feynman Lectures Vol. I* — Ch. 13–14