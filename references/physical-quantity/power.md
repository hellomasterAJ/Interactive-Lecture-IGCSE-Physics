---
title: Power
field: General Physics
type: physical-quantity
si_unit: watt (W)
symbol: P
dimension: [M·L²·T⁻³]
version: 1
tags: [power, energy, work, rate, si-units]
related_lectures: [topic17_energy]
related_terminology: []
related_physical_quantity: [energy, work, force, torque, current, voltage]
---

# ⚡ Power

> **Power = อัตราการทำงาน หรือ อัตราการใช้พลังงาน**
>
> P = dW/dt = F·v (mechanical) = VI (electrical) — หน่วย W = J/s

---

## 📜 ประวัติศาสตร์

| ปี | บุคคล | การค้นพบ |
|----|-------|-----------|
| **~1760s** | **James Watt** 🏭 | ปรับปรุงเครื่องจักรไอน้ำของ Newcomen → ต้องการบอกว่าเครื่องจักรของเขา "แรงแค่ไหน" |
| **~1780** | **James Watt** | กำหนด **horsepower (hp)** = 33,000 ft·lbf/min ≈ 745.7 W |
| | | — ทำการตลาด: "เครื่องจักรของผมแทนม้าได้กี่ตัว!" |
| **1882** | **SI** | ตั้งชื่อหน่วย **watt (W)** ตาม James Watt |
| **1889** | — | 1 horsepower = 746 W (UK/US) / 736 W (metric PS) |

---

## ⚛️ นิยามทางฟิสิกส์

### Mechanical Power
```
P = dW/dt = F·v (แรง-velocity)

P_avg = W/Δt
P_instantaneous = F·v (เมื่อ F ∥ v)
  = F·v·cosθ
```

### Electrical Power
```
P = V·I (DC หรือ instantaneous AC)

P = I²R (กำลังงานที่ dissipate ใน resistor)
P = V²/R
P = ω·τ (rotational: torque × angular velocity)
```

---

## 🌍 ตัวอย่างในชีวิตจริง

| สิ่งนี้ | กำลัง (W) | หมายเหตุ |
|--------|-----------|----------|
| 💡 LED bulb | 5–15 W | บ้าน |
| 🧠 สมองมนุษย์ | ≈ 20 W | ใช้ energy ~400 kcal/day → ≈ 20 W |
| 🚲 ปั่นจักรยานเบาๆ | ~50–100 W | รักษาความเร็ว |
| 🚲 นักปั่น Pro | ~400–500 W (sustained) | Tour de France ≈ 1.5 ชม. |
| 💻 laptop | 30–100 W | เฉลี่ย |
| 🚗 รถยนต์ (100 km/h) | ~30,000 W (30 kW) | highway |
| 🚗 Ferrari V12 (peak) | ~588,000 W (800 hp) | peak |
| ✈️ Boeing 747 (per engine) | ~52,000,000 W (70,000 hp) | takeoff thrust |
| 🚀 Saturn V (F-1 engine) | **≈ 1.6×10¹⁰ W** | 160 GW = ใหญ่ที่สุดที่มนุษย์สร้าง |
| ☀️ Sun (total) | **≈ 3.8×10²⁶ W** | fusion in core |
| ⚡ Lightning strike (peak) | ~10¹² W | แต่สั้นมาก ~30 μs |

---

## 📐 หน่วยของกำลัง

| หน่วย | สัญลักษณ์ | ค่า (W) | ใช้ที่ไหน |
|-------|-----------|---------|----------|
| **watt** | W | 1 | SI |
| **milliwatt** | mW | 10⁻³ | RF, laser |
| **kilowatt** | kW | 10³ | บ้าน, รถยนต์ |
| **megawatt** | MW | 10⁶ | โรงไฟฟ้า |
| **gigawatt** | GW | 10⁹ | โรงไฟฟ้าขนาดใหญ่ |
| **terawatt** | TW | 10¹² | การใช้ energy ของโลก (~18 TW) |
| **horsepower (hp)** | hp | 745.7 | รถยนต์ US/UK |
| **metric PS** | PS | 735.5 | รถยนต์ยุโรป |
| **BTU/h** | — | 0.293 | HVAC, US |
| **kcal/h** | — | 1.163 | อาหาร |
| **Planck power** | Pᴘ | c⁵/G ≈ 3.6×10⁵² | ขีดจำกัดสูงสุด |

---

## 🔥 คำถามขั้นสูง

**1. "Peak power" vs "Average power"**
— Lightning: 10¹² W peak, average = น้อยมาก (ครั้ง/วินาที?)
— Sun: 3.8×10²⁶ W **steady** = average = peak

**2. 1 light bulb = 10 W — 1 Year = energy เท่าไหร่?**
E = P·t = 10 W × 365 × 24 × 3,600 = 315,360,000 J = 87.6 kWh
— ≈ ฿350 (ที่ค่าไฟ ~4 บาท/kWh)

**3. Power-to-weight ratio — ทำไมสำคัญ**
— Ferrari: ≈ 0.4 hp/kg
— Nissan Leaf: ≈ 0.1 hp/kg
— Hummingbird: ≈ 0.5 hp/kg (กล้ามเนื้อบิน)
— F1 car: ≈ 1.3 hp/kg (850 hp / 650 kg)

---

## 🔗 อ้างอิง

- Watt, J. (1765). Improvements in the Steam Engine
- BIPM (2019). *SI Brochure*
- Feynman R. P. (1963). *Feynman Lectures Vol. I* — Ch. 14