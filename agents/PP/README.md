# 🤖 พีพี (PP) — Project Portfolio Agent

**Project Portfolio Dashboard & Priority Planning Agent**

พีพีคือ Agent ผู้ดูแลโปรเจคทั้งหมดของ masterAJ — ทำ Dashboard, คำนวณต้นทุน, วางแผนลำดับงาน

## โครงสร้างไฟล์

```
agents/PP/
├── README.md          ← ไฟล์นี้
├── projects.json      ← ฐานข้อมูลทะเบียนโปรเจค
├── pp.py              ← สคริปต์หลัก (dashboard, status, cost, scan, update, next)
├── pp-dashboard.html  ← HTML Dashboard (auto-generated)
└── pp.log             ← Log กิจกรรมของพีพี
```

## วิธีใช้

### แสดง Dashboard

```bash
# Markdown in terminal
python3 ~/InteractiveLecture/agents/PP/pp.py dashboard

# HTML Dashboard → เปิด browser
python3 ~/InteractiveLecture/agents/PP/pp.py dashboard --html
open ~/InteractiveLecture/agents/PP/pp-dashboard.html
```

### ดูสถานะ

```bash
# ทั้งหมด
python3 ~/InteractiveLecture/agents/PP/pp.py status

# เฉพาะโปรเจค
python3 ~/InteractiveLecture/agents/PP/pp.py status interactive-lecture-physics
```

### Scan โปรเจค (นับไฟล์ล่าสุด)

```bash
python3 ~/InteractiveLecture/agents/PP/pp.py scan
```

### ดูต้นทุน

```bash
python3 ~/InteractiveLecture/agents/PP/pp.py cost
```

### แนะนำลำดับงาน

```bash
python3 ~/InteractiveLecture/agents/PP/pp.py next
```

### อัปเดตโปรเจค

```bash
python3 ~/InteractiveLecture/agents/PP/pp.py update <project_id> key=value
```

## การเรียกใช้ผ่าน Hermes

ใน Hermes Agent สามารถโหลด skill `pp-agent` ได้โดยตรง:

```
โหลด skill pp-agent ให้หน่อย
คุณพีพี ช่วยดู dashboard โปรเจค
พีพี scan โปรเจคล่าสุด
```
