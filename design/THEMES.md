# Interactive Lecture — Theme System

ระบบธีมของเครื่องมือ `kinematics_graphs.html` (Kinematics Graphs of Horizontal Motion)
ทุกธีมทำงานผ่าน **CSS custom properties** ที่สลับด้วย class บน `<body>`
(ค่าเริ่มต้น = Classic Dark คือ `:root` ไม่มี class)

อัปเดตล่าสุด: 2026-07-06

---

## 1. โครงสร้างตัวแปรสี (CSS Variables)

แต่ละธีมกำหนดตัวแปรชุดเดียวกัน:

| ตัวแปร | หน้าที่ |
|---|---|
| `--bg` | พื้นหลังหน้าเว็บ |
| `--card` | พื้นการ์ด/ปุ่ม |
| `--border` | เส้นขอบ |
| `--text` / `--text-dim` / `--text-muted` | ตัวอักษร (เข้ม→จาง) |
| `--accent` / `--accent-glow` | สีเน้น + พื้นเน้นแบบจาง |
| `--grid` / `--graph-bg` | เส้นตาราง + พื้นกราฟ (canvas อ่านค่านี้โดยตรง) |
| `--line-color` / `--shade` | เส้นกราฟหลัก + พื้นใต้เส้น |
| `--green` / `--rose` / `--violet` | สีเชิงความหมาย |

> **สำคัญ:** canvas ของกราฟดึงสีจาก `--graph-bg`, `--grid`, `--text-muted`, `--text-dim`
> จึงเข้ากับทุกธีมโดยอัตโนมัติ — ถ้าเพิ่มธีมใหม่ ไม่ต้องแก้โค้ด JS

---

## 2. ธีม HAUS (Brand themes)

### HAUS Day — `.theme-haus` (สว่าง: ครีม + ทอง + ดำ)
```
--bg:#F4EEE0;  --card:#FFFFFF;  --border:#E4DAC4;
--text:#1A1712;  --text-dim:#5B5344;  --text-muted:#948A74;
--accent:#A9820F;  --accent-glow:rgba(169,130,15,0.12);
--grid:#EBE3D0;  --graph-bg:#FCFAF2;
--line-color:#A9820F;  --shade:rgba(169,130,15,0.06);
--green:#4E7A3F;  --rose:#B5502E;  --violet:#8A6D3B;
```

### HAUS Night — `.theme-hausnight` (มืด: ถ่าน + ทองแบรนด์)
```
--bg:#14110C;  --card:#201C15;  --border:#3A3327;
--text:#F3ECDD;  --text-dim:#B7AB93;  --text-muted:#83795F;
--accent:#F4C01E;  --accent-glow:rgba(244,192,30,0.12);
--grid:#211D15;  --graph-bg:#0E0B07;
--line-color:#F4C01E;  --shade:rgba(244,192,30,0.06);
--green:#A6B36A;  --rose:#D68B57;  --violet:#CBAA6A;
```

> Random button และปุ่มต่างๆ ในธีม HAUS ถูก override ให้ใช้ **ทอง** แทนม่วง เพื่อความกลมกลืน

---

## 3. ลำดับธีมในเมนู (Theme selector order)

| # | ค่า (value) | ชื่อที่แสดง | ประเภท |
|---|---|---|---|
| 1 | `dark` | Classic Dark *(ค่าเริ่มต้น)* | มืด |
| 2 | `hausnight` | HAUS Night | มืด (แบรนด์) |
| 3 | `vintage` | Vintage Dark | มืด |
| 4 | `neon` | Cyberpunk Neon | มืด |
| 5 | `cosmic` | Cosmic Void | มืด |
| 6 | `light` | Classic Light | สว่าง |
| 7 | `haus` | HAUS Day | สว่าง (แบรนด์) |
| 8 | `clay` | Warm Clay | สว่าง |
| 9 | `sage` | Soft Sage | สว่าง |
| 10 | `mist` | Mist Blue | สว่าง |

> ธีม **One Dark** และ **Warm Taupe** ถูกตัดออกจากเมนูแล้ว

ฟังก์ชัน `isDark()` ระบุธีมมืด: `dark, neon, vintage, cosmic, onedark, hausnight`
(ใช้กำหนดการแสดงโลโก้ — พื้นเหลืองตัวดำเมื่อมืด, ตัวดำโปร่งใสเมื่อสว่าง)

---

## 4. สีเส้นกราฟตามแท็บ (Graph line — semantic per tab)

เส้นข้อมูลในกราฟใช้สีต่างกันตามชนิดกราฟ เพื่อแยกความหมาย (โหมดสว่าง/มืด):
| แท็บ | สี |
|---|---|
| Distance–Time | ทอง/อำพัน — มืด `#fbbf24` / สว่าง `#d97706` |
| Speed–Time | ฟ้า/เขียวน้ำเงิน — มืด `#22d3ee` / สว่าง `#0891b2` |
| Acceleration–Time | ดินเผา/กุหลาบ — มืด `#fb7185` / สว่าง `#e11d48` |

---

## 5. วิธีเพิ่มธีมใหม่

1. เพิ่ม CSS block `.theme-<ชื่อ> { ...ตัวแปรทั้งหมด... }`
2. เพิ่ม `<option value="<ชื่อ>">...</option>` ในเมนู
3. เพิ่มชื่อ class ใน array `themeClasses` (ฟังก์ชัน `setTheme`)
4. ถ้าเป็นธีมมืด → เพิ่มเงื่อนไขใน `isDark()`
5. canvas จะปรับสีตามอัตโนมัติ ไม่ต้องแก้เพิ่ม
