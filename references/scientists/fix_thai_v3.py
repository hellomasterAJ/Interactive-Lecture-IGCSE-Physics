#!/usr/bin/env python3
"""Careful Thai text fixes — word-boundary-aware replacements only."""
import json, re

with open('scientist_bio_library_v1.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# ===== WORD-LEVEL FIXES (full word match, not substring) =====
# Format: (wrong_word_pattern, correct_word)
# Only applied when the wrong word appears as a complete standalone word

word_fixes = [
    # Missing vowel "ี" (SARA II) - critical
    (r'\bปกอน\b', 'ปีก่อน'),
    (r'\bกอน\b', 'ก่อน'),
    (r'\bกอตั้ง\b', 'ก่อตั้ง'),
    (r'\bตก\b', 'ตก'),  # no change needed
    (r'\bตอ\b', 'ต่อ'),  
    (r'\bตอมา\b', 'ต่อมา'),
    (r'\bตอน\b', 'ตอน'),  # already correct!
    (r'\bตอไป\b', 'ต่อไป'),
    (r'\bเอเธนส\b', 'เอเธนส์'),
    (r'\bคริสตกาล\b', 'คริสต์กาล'),
    (r'\bอุปกรณ\b', 'อุปกรณ์'),
    (r'\bประดิษฐ\b', 'ประดิษฐ์'),
    (r'\bรถยนต\b', 'รถยนต์'),
    (r'\bผลลพธ\b', 'ผลลัพธ์'),
    (r'\bฟสิกส\b', 'ฟิสิกส์'),
    (r'\bวทยาศาสตร\b', 'วิทยาศาสตร์'),
    (r'\bมหาวทยาลย\b', 'มหาวิทยาลัย'),
    
    # Missing tone marks
    (r'\bกอ\b', 'ก่อ'),
    (r'\bรอน\b', 'ร้อน'),
    (r'\bรน\b', 'ร้อน'),
    (r'\bผาน\b', 'ผ่าน'),
    (r'\bพบ\b', 'พบ'),  # already correct
    (r'\bคนพบ\b', 'ค้นพบ'),
    (r'\bเปน\b', 'เป็น'),
    (r'\bได\b', 'ได้'),
    (r'\bแลว\b', 'แล้ว'),
    (r'\บเพอ\b', 'เพื่อ'),
    (r'\bรวมถง\b', 'รวมถึง'),
    (r'\บคอ\b', 'คือ'),
    (r'\บอย\b', 'อยู่'),
    (r'\บเชน\b', 'เช่น'),
    
    # Missing -karant (์) at word end
    (r'\บศาสตร\b', 'ศาสตร์'),
    (r'\บคริสต\b', 'คริสต์'),
    (r'\บกาลิเลโอ\b', 'กาลิเลโอ'),
    
    # Specific name issues
    (r'\บเอเธนส\b', 'เอเธนส์'),
    
    # Other common wrong spellings
    (r'\บครอบครว\b', 'ครอบครัว'),
    (r'\บทองฟา\b', 'ท้องฟ้า'),
    (r'\บอสระ\b', 'อิสระ'),
    (r'\บแพร\b', 'แพร่'),
    (r'\บเยน\b', 'เย็น'),
    (r'\บสลบ\b', 'สลับ'),
    (r'\บตรงขาม\b', 'ตรงข้าม'),
    (r'\บเครอง\b', 'เครื่อง'),
    (r'\บผลก\b', 'ผลัก'),
    (r'\บเรม\b', 'เริ่ม'),
    (r'\บฝรังเศส\b', 'ฝรั่งเศส'),
    (r'\บนิวตน\b', 'นิวตัน'),
    (r'\บจล\b', 'จูล'),
    (r'\บแตงงาน\b', 'แต่งงาน'),
    (r'\บเกยวกบ\b', 'เกี่ยวกับ'),
    (r'\บสงเกต\b', 'สังเกต'),
    (r'\บรวมกน\b', 'ร่วมกัน'),
    
    # Pascal specific
    (r'\บแบลส\b', 'แบลส'),
    
    # Common compound corrections  
    (r'\บเกอบ\b', 'เกี่ยวกับ'),
    (r'\บนอกจากน\b', 'นอกจากนี้'),
    (r'\บสำหรบ\b', 'สำหรับ'),
    (r'\บประวต\b', 'ประวัติ'),
    (r'\บเฉพาะ\b', 'เฉพาะ'),
    (r'\บปรมา\b', 'ประมาณ'),
]

apply_count = 0
total_fixes = 0

for s in data['scientists']:
    # Get all Thai text fields
    text_fields = []
    
    for field in ['summary_th', 'key_quote_th']:
        if field in s:
            text_fields.append((s, field, None))
    
    for field in ['biography_th', 'contributions_th', 'legacy_th']:
        if field in s and isinstance(s[field], list):
            for i in range(len(s[field])):
                text_fields.append((s[field], i, None))
    
    if 'key_experiments' in s:
        for ei, exp in enumerate(s['key_experiments']):
            for ef in ['title_th', 'desc_th', 'myth_th']:
                if ef in exp:
                    text_fields.append((exp, ef, None))
    
    # Apply word-boundary fixes to each field
    for obj, key, _ in text_fields:
        if isinstance(obj, dict):
            text = obj[key]
        else:
            text = obj
        
        if not isinstance(text, str):
            continue
            
        for pattern, replacement in word_fixes:
            new_text = re.sub(pattern, replacement, text)
            if new_text != text:
                total_fixes += 1
                if apply_count < 5:
                    print(f"  Fix: {pattern} -> {replacement} in {s.get('id','?')}")
                    apply_count += 1
                text = new_text
        
        if isinstance(obj, dict):
            obj[key] = text
        else:
            obj[key] = text

# Save
with open('scientist_bio_library_v1.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# Verify
for s in data['scientists']:
    if s['id'] == 'aristotle':
        bio = s.get('biography_th', [''])[0]
        print(f"\n✅ Verification (Aristotle):")
        print(f"   Has 'ปีก่อน': {'ปีก่อน' in bio}")
        print(f"   Has 'คริสต์': {'คริสต์' in bio}")
        print(f"   Text: {bio[:150]}")
        break

print(f"\n✅ Total fixes applied: {total_fixes}")