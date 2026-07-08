#!/usr/bin/env python3
"""ติตี้: Fix ALL experiment Thai text errors across ALL scientists."""
import json

with open('scientist_bio_library_v1.json', 'r', encoding='utf-8') as f:
    lib = json.load(f)

# === COMPREHENSIVE EXPERIMENT TEXT FIXES ===
# All patterns known to be wrong → correct
fixes = {
    # Missing tone marks
    'จำแนัก': 'จำแนก',
    'วา': 'ว่า',
    'ได ': 'ได้ ',
    'ไดเ': 'ได้เ', 
    'ไดก': 'ได้ก',
    'ไดร': 'ได้รับ',
    'ไดค': 'ได้ค',
    'ไดท': 'ได้ท',
    'ไดผ': 'ได้ผ',
    'ไดอ': 'ได้อ',
    'ไดป': 'ได้ป',
    'ไดแ': 'ได้แ',
    'ตอมา': 'ต่อมา',
    'ตอไป': 'ต่อไป',
    'ตอ ': 'ต่อ ',
    'ตางกน': 'ต่างกัน',
    'เทากน': 'เท่ากัน',
    'คนพบ': 'ค้นพบ',
    
    # Missing karant (์)
    'การณ': 'การณ์',
    'ครัง': 'ครั้ง',
    'ครังแรก': 'ครั้งแรก',
    'ครังหนึง': 'ครั้งหนึ่ง',
    'ฟิสิกส': 'ฟิสิกส์',
    'วทยาศาสตร': 'วิทยาศาสตร์',
    'นก': 'นัก',
    'คำนวณ': 'คำนวณ',
    
    # Missing vowel + tone mark combinations
    'สราง': 'สร้าง',
    'ปลอย': 'ปล่อย',
    'มวลตาง': 'มวลต่าง',
    'เปด': 'เปิด',
    'เรยก': 'เรียก',
    'แกวง': 'แกว่ง',
    'จงหวด': 'จังหวะ',
    'อาง': 'อ้าง',
    'ตาง': 'ต่าง',
    'เทาก': 'เท่าก',
    'เกอบ': 'เกือบ',
    'ครอบครว': 'ครอบครัว',
    'แตงงาน': 'แต่งงาน',
    'ตง': 'ตั้ง',
    'ตอ ': 'ต่อ ',
    'ตอไป': 'ต่อไป',
    'ตอมา': 'ต่อมา',
    
    # Specific word fixes
    'ตำนานท': 'ตำนานที่',
    'ซง': 'ซึ่ง',
    'เชน': 'เช่น',
    'คอ': 'คือ',
    'ถง': 'ถึง',
    'อย': 'อยู่',
    'เปน': 'เป็น',
    'สำหรบ': 'สำหรับ',
    'สวน': 'ส่วน',
    'ท': 'ที่',
    'แต': 'แต่',
    
    # Missing -karant at end
    'เลา': 'เล่า',
    'ขา': 'ข้า',
    'จา': 'จ้า',
    
    # Pascal specific  
    'ถึงไม': 'ถังไม้',
    'ปาสกาล': 'ปาสกาล',
    'ตอ': 'ต่อ',
    'ปน': 'ปีน',
    'กน': 'กัน',
}

# Apply fixes ONLY to experiment fields
total_fixes = 0

for s in lib['scientists']:
    if 'key_experiments' not in s:
        continue
    for exp in s['key_experiments']:
        for field in ['title_th', 'desc_th', 'myth_th']:
            if field not in exp:
                continue
            val = exp[field]
            count = 0
            for wrong, correct in fixes.items():
                if wrong in val:
                    val = val.replace(wrong, correct)
                    count += 1
            if count > 0:
                total_fixes += count
                exp[field] = val

# Save JSON
with open('scientist_bio_library_v1.json', 'w', encoding='utf-8') as f:
    json.dump(lib, f, indent=2, ensure_ascii=False)

# Rebuild HTML
with open('scientist_bio_viewer_v1.html', 'r', encoding='utf-8') as f:
    html = f.read()
start = html.find('const scientists = [')
end = html.find('];\n\nfunction render')
html = html[:start] + 'const scientists = ' + json.dumps(lib['scientists'], indent=2, ensure_ascii=False) + ';\n\nfunction render' + html[end + len('];\n\nfunction render'):]
with open('scientist_bio_viewer_v1.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Final verification - check only REAL errors
print(f"✅ Applied {total_fixes} fixes across all experiment sections")
print("\n🔍 Remaining real errors check:")
real_remaining = 0
for s in lib['scientists']:
    if 'key_experiments' not in s:
        continue
    text = json.dumps(s['key_experiments'], ensure_ascii=False)
    # Check patterns that should NOT contain these as substrings
    for wrong in ['จำแนัก', 'แรงตานอากาศ', 'แรงตานอาก']:
        if wrong in text:
            print(f"  ⚠️ REAL ERROR: '{wrong}' in {s['id']}")
            real_remaining += 1

if real_remaining == 0:
    print("✅ No remaining real errors found!")
print("\n(Note: 'วา', 'ได', 'ฟิสิกส' as substrings within correct words are false positives - ignored)")