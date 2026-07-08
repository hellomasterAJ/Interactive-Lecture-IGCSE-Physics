#!/usr/bin/env python3
"""Thai text fixes v4 — direct substring replacement with safe ordering."""
import json, re

with open('scientist_bio_library_v1.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# === SAFE TWO-PASS REPLACEMENTS ===
# First pass: specific long strings (won't overlap)
fixes_pass1 = {
    # Missing vowel/specific word fixes  
    'ปกอนคริสตกาล': 'ปีก่อนคริสต์กาล',
    'ปกอนจะ': 'ปีก่อนจะ',
    'กอตั้ง': 'ก่อตั้ง',
    'กอนจะกอ': 'ก่อนจะก่อ',
    'เอเธนส': 'เอเธนส์',
    'รวมถง': 'รวมถึง',
    'นอกจากน': 'นอกจากนี้',
    'มหาวทยาลย': 'มหาวิทยาลัย',
    'รถยนต': 'รถยนต์',
    'อุปกรณ': 'อุปกรณ์',
    'ประดิษฐ': 'ประดิษฐ์',
    'เกยวกบ': 'เกี่ยวกับ',
    'ครอบครว': 'ครอบครัว',
    'แตงงาน': 'แต่งงาน',
    'ผลลพธ': 'ผลลัพธ์',
    'ศาสตร': 'ศาสตร์',
    
    # Tone mark fixes
    'แลว': 'แล้ว',
    'ผาน': 'ผ่าน',
    'รอน': 'ร้อน',
    'ตรงขาม': 'ตรงข้าม',
    'รวมกน': 'ร่วมกัน',
    'ตอมา': 'ต่อมา',
    'เยน': 'เย็น',
    'สลบ': 'สลับ',
    'เรม': 'เริ่ม',
    'เครอง': 'เครื่อง',
    'ผลก': 'ผลัก',
    'ทองฟา': 'ท้องฟ้า',
    
    # 'มี' fixes (missing vowel)
    'มความ': 'มีความ',
    'มผล': 'มีผล',
    'มก': 'มัก',
    
    # Name fixes  
    'นิวตน': 'นิวตัน',
    'แอปเปล': 'แอปเปิล',
    'แบลส': 'แบลส',
    
    # Word boundary issues
    'กอ': 'ก่อ',
    'ซง': 'ซึ่ง',
    'คอ': 'คือ',
    'ทง': 'ทั้ง',
    'นน': 'นั้น',
    'นเลย': 'นั้นเอง',
    'ได': 'ได้',
    'วา': 'ว่า',
    'ท': 'ที่',
    'ได ': 'ได้ ',
    'วา ': 'ว่า ',
    'ท ': 'ที่ ',
    'ของท ': 'ของที่ ',
    
    # Missing -karant
    'คริสต': 'คริสต์',
    
    # Compound words
    'เปนจํานวน': 'เป็นจำนวน',
    'สวน': 'ส่วน',
    'ถง': 'ถึง',
    
    # General missing vowels  
    'รอน': 'ร้อน',
    'อสระ': 'อิสระ',
    'ฝรังเศส': 'ฝรั่งเศส',
    'มหาสมทร': 'มหาสมุทร',
}

# Second pass: more aggressive replacements for remaining issues
# These are applied ONLY after pass1, and need to be careful
fixes_pass2 = {
    'คนพบ': 'ค้นพบ',
    'เกอบ': 'เกือบ',
    'เหมอน': 'เหมือน',
    'มอ น': 'มีอำนาจ',
    'เฉพาะ': 'เฉพาะ',
    'โดยเฉพาะ': 'โดยเฉพาะ',
    'อย': 'อยู่',
    'เชน': 'เช่น',
    'กอน': 'ก่อน',
    'เพอ': 'เพื่อ',
    'ผาน': 'ผ่าน',
    'สาขา': 'สาขา',
    'เปน': 'เป็น',
    'รวมถง': 'รวมถึง',
    'สวนใหญ': 'ส่วนใหญ่',
    'สวนหนง': 'ส่วนหนึ่ง',
    'สำหรบ': 'สำหรับ',
    'แต': 'แต่',
    'สำคญ': 'สำคัญ',
    'อธบาย': 'อธิบาย',
    'กวา': 'กว่า',
    'ยง': 'ยัง',
    'โดยเฉพาะ': 'โดยเฉพาะ',
    'รอน': 'ร้อน',
    'เยน': 'เย็น',
    'หนวย': 'หน่วย',
    'ปรมาณ': 'ปริมาณ',
    # Over-fix undos (fix what my earlier fixes broke)
    'คริสต์์': 'คริสต์',
    'ที่ี่': 'ที่',
    'ต่อน': 'ตอน',
    'ในี้': 'ใน',
    'ต่อไปป': 'ต่อไป',
}

def apply_fixes(obj, field, fixes):
    """Apply substring replacements to a text field."""
    if field not in obj:
        return 0
    val = obj[field]
    count = 0
    
    if isinstance(val, str):
        for wrong, correct in fixes.items():
            if wrong in val:
                val = val.replace(wrong, correct)
                count += 1
        obj[field] = val
    elif isinstance(val, list):
        new_list = []
        for item in val:
            for wrong, correct in fixes.items():
                if wrong in item:
                    item = item.replace(wrong, correct)
                    count += 1
            new_list.append(item)
        obj[field] = new_list
    
    return count

# Apply both passes
total = 0

for s in data['scientists']:
    # Fields to fix
    text_fields = ['summary_th', 'key_quote_th']
    list_fields = ['biography_th', 'contributions_th', 'legacy_th']
    exp_fields = ['title_th', 'desc_th', 'myth_th']
    
    for f in text_fields:
        total += apply_fixes(s, f, fixes_pass1)
        total += apply_fixes(s, f, fixes_pass2)
    
    for f in list_fields:
        total += apply_fixes(s, f, fixes_pass1)
        total += apply_fixes(s, f, fixes_pass2)
    
    if 'key_experiments' in s:
        for exp in s['key_experiments']:
            for f in exp_fields:
                total += apply_fixes(exp, f, fixes_pass1)
                total += apply_fixes(exp, f, fixes_pass2)

# Save
with open('scientist_bio_library_v1.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# Verify
for s in data['scientists']:
    if s['id'] == 'aristotle':
        bio = s.get('biography_th', [''])
        if bio:
            print(f"✅ Aristotle first bio line:")
            print(f"   {bio[0][:200]}")
            print(f"   Has 'ปีก่อน': {'ปีก่อน' in bio[0]}")
        break

print(f"\n✅ Total substring fixes: {total}")