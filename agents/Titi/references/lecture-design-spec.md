# 🎨 Lecture Design Spec — masterAJ

> อัปเดตล่าสุด: 2026-07-11
> มาตรฐานสำหรับ Lecture HTML + PDF ของ masterAJ
> เก็บที่: `~/InteractiveLecture/agents/Titi/references/lecture-design-spec.md`

---

## 📐 1. กระดาษ (PDF)

| รายการ | ค่า |
|--------|-----|
| **ขนาด** | A4 (210mm × 297mm) |
| **Margin ซ้าย** | 2.0 cm (เผื่อเข้าเล่ม) |
| **Margin ขวา** | 2.0 cm |
| **Margin บน** | 1.5 cm |
| **Margin ล่าง** | 1.5 cm |

---

## 🔤 2. Font Pairing (🥇 WINNER = Pairing B)

| ใช้สำหรับ | ฟอนต์ | ตัวอย่าง |
|-----------|-------|----------|
| **หัวข้อ (Heading)** | **Roboto Slab** (700/600) | 1.1 Scalars and Vectors |
| **เนื้อหา (Body)** | **Atkinson Hyperlegible** (400/700) | A scalar quantity has only magnitude… |
| **สมการ (Formula)** | **JetBrains Mono** (400/600) | F = ma  \|  v = u + at  \|  Eₖ = ½mv² |

### ตัวสำรอง (เผื่อเปลี่ยนใจ)
| ลำดับ | Pairing | Heading | Body | Formula |
|-------|---------|---------|------|---------|
| 🥈 | A — Academic Premium | Crimson Pro | Figtree | JetBrains Mono |
| 🥉 | C — Modern STEM | Figtree | Crimson Pro | JetBrains Mono |
| 4 | D — Tech Bold | Roboto Slab | Figtree | JetBrains Mono |

---

## 🎨 3. Color Scheme (เบื้องต้น — รอคุณ masterAJ)

| 用途 | สี (HEX) |
|------|----------|
| **Primary / Accent** | `#e3b341` (ทอง HAUS Academy) |
| **BG (HTML dark mode)** | `#0d1117` |
| **Text (HTML)** | `#e6edf3` |
| **Text (PDF)** | `#000000` (ดำล้วน) |
| **Highlight / Formula** | `#7ee787` (เขียว) |

> ⚠️ รอคุณ masterAJ เลือกธีมสีเพิ่มเติม

---

## 🏗️ 4. Lecture Structure Template

### 4.1 หัวข้อใหญ่ (Topic Page)
```
🏠 [Topic N: Name]
├── 📋 Sub-topic 1
├── 📋 Sub-topic 2
├── 📋 Sub-topic 3
└── 🧪 Key Experiments
```

### 4.2 หน้าเนื้อหา (Content Page)
```
─────────────────
 1.2  Sub-topic Title
─────────────────

📖 Definition & Formula
  → เนื้อหา + สมการ

💡 Key Points
  → ข้อควรจำ

⚠️ Common Mistake
  → ข้อผิดพลาดที่พบบ่อย

📝 Worked Example
  → โจทย์ + วิธีทำ

✅ Quick Check
  → คำถามสั้นๆ ท้ายหัวข้อย่อย
─────────────────
```

### 4.3 ท้าย Topic (End of Topic)
```
📌 Topic Summary
  → สรุป 5-8 บรรทัด

🔑 Formula Sheet
  → รวมสูตรทั้งหมดใน Topic

🧪 Experiments
  → การทดลองที่เกี่ยวข้อง

📚 Past Paper Practice
  → ข้อสอบเก่าแนะนำ
```

---

## ⚙️ 5. ขนาดตัวอักษร (Font Sizes)

| ระดับ | ขนาด (pt) | ใช้ที่ไหน |
|-------|-----------|----------|
| **Topic Title** | 24pt | หัวข้อใหญ่ |
| **Sub-topic** | 18pt | หัวข้อย่อย |
| **Sub-sub heading** | 14pt | หัวข้อย่อยย่อย |
| **Body text** | 11pt | เนื้อหาปกติ |
| **Formula inline** | 11pt | สมการในบรรทัด |
| **Caption / Note** | 9.5pt | เชิงอรรถ, คำอธิบายเล็ก |
| **Header/Footer** | 8pt | หัวกระดาษ / ท้ายกระดาษ |

---

## 📁 6. โครงสร้างไฟล์

```
InteractiveLecture/agents/Titi/lectures/
├── physics/
│   └── topic-01-general-physics/
│       ├── topic-01-detailed-syllabus.md   ← เนื้อหาดิบ
│       ├── html/
│       │   └── topic-01.html               ← Lecture HTML
│       └── pdf/
│           └── topic-01.pdf                 ← Lecture PDF
├── maths/
└── cs/
```

---

## 📋 7. Checklist ก่อนสร้าง Lecture

- [ ] เลือกฟอนต์ ✅ (Roboto Slab + Atkinson + JetBrains Mono)
- [ ] กำหนด Margin ✅
- [ ] กำหนด Structure Template
- [ ] กำหนด Color Scheme
- [ ] สร้าง HTML Template
- [ ] สร้าง CSS Print Style (สำหรับ PDF)
- [ ] ทดสอบ Print Preview
- [ ] คุณ masterAJ Review