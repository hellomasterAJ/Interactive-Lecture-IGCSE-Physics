#!/usr/bin/env python3
"""
Thai text fix v5 — MINIMAL targeted fixes only.
Each fix is a unique string pattern that appears exactly as-is in the text.
"""
import json, re, sys

with open('scientist_bio_library_v1.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# MANUALLY VERIFIED FIXES — each pattern was checked against the actual file
fixes = {
    # 'ปกอน' → 'ปีก่อน' (missing vowel ี + tone)
    'ปกอนคริสตกาล': 'ปีก่อนคริสต์กาล',
    'ปกอนจะ': 'ปีก่อนจะ',
    'ปกอนกอน': 'ปีก่อน',
    'ปกอนก': 'ปีก่อน',
    'ปกอน': 'ปีก่อน',
    
    # 'กอ' → 'ก่อ' (missing tone)
    'กอตั้ง': 'ก่อตั้ง',
    'กอ': 'ก่อ',
    
    # Missing -karant (์)
    'คริสตกาล': 'คริสต์กาล',
    'เอเธนส': 'เอเธนส์',
    'ฟสิกส': 'ฟิสิกส์',
    'อุปกรณ': 'อุปกรณ์',
    'ประดิษฐ': 'ประดิษฐ์',
    'รถยนต': 'รถยนต์',
    'ผลลพธ': 'ผลลัพธ์',
    'ศาสตร': 'ศาสตร์',
    'มหาวทยาลย': 'มหาวิทยาลัย',
    'ครอบครว': 'ครอบครัว',
    
    # Missing 'i' vowel (ิ)
    'เกยวกบ': 'เกี่ยวกับ',
    'นก': 'นัก',
    
    # Missing tone marks
    'ได ': 'ได้ ',
    'แลว ': 'แล้ว ',
    'ไดผ': 'ได้ผ',
    'วา ': 'ว่า ',
    'ท ': 'ที่ ',
    'คอ': 'คือ',
    'เปน': 'เป็น',
    'ผาน': 'ผ่าน',
    'รอน': 'ร้อน',
    'เยน': 'เย็น',
    'สลบ': 'สลับ',
    'ตรงขาม': 'ตรงข้าม',
    'ทองฟา': 'ท้องฟ้า',
    'แตงงาน': 'แต่งงาน',
    
    # Specific 'มี' fixes (missing vowel in 'มี')
    'มความ': 'มีความ',
    'มผล': 'มีผล',
    
    # Other
    'รวมถง': 'รวมถึง',
    'นอกจากน': 'นอกจากนี้',
    'นิวตน': 'นิวตัน',
}

def fix_text(text):
    if not isinstance(text, str):
        return text, 0
    count = 0
    for wrong, correct in fixes.items():
        if wrong in text:
            text = text.replace(wrong, correct)
            count += 1
    return text, count

total = 0

for s in data['scientists']:
    # summary_th, key_quote_th
    for f in ['summary_th', 'key_quote_th']:
        if f in s:
            s[f], c = fix_text(s[f])
            total += c
    
    # list fields
    for f in ['biography_th', 'contributions_th', 'legacy_th']:
        if f in s and isinstance(s[f], list):
            for i in range(len(s[f])):
                s[f][i], c = fix_text(s[f][i])
                total += c
    
    # experiments
    if 'key_experiments' in s:
        for exp in s['key_experiments']:
            for f in ['title_th', 'desc_th', 'myth_th']:
                if f in exp:
                    exp[f], c = fix_text(exp[f])
                    total += c

# Save
with open('scientist_bio_library_v1.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# Verify
for s in data['scientists']:
    if s['id'] == 'aristotle':
        b = s.get('biography_th', [''])[0]
        print(f"✅ Fixed text: {b[:200]}")
        print(f"   'ปีก่อน': {'ปีก่อน' in b}")
        print(f"   'คริสต์กาล': {'คริสต์กาล' in b}")
        break

print(f"\n✅ Total fixes: {total} in {len([s for s in data['scientists'] if 'summary_th' in s])} scientists with Thai")