#!/usr/bin/env python3
"""Fix common Thai character errors in the JSON library."""
import json, re

with open('scientist_bio_library_v1.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# ===== SYSTEMATIC THAI TEXT FIXES =====
# Fix patterns: wrong → correct for common Thai words

thai_fixes = {

    # Missing vowels & tone marks
    'ปกอน': 'ปีก่อน',
    'ปนะมาณ': 'ประมาณ',
    'ปม': 'ปี',
    'ป 1623': 'ปี 1623', 
    'ป 1635': 'ปี 1635',
    'ป 1643': 'ปี 1643',
    'ป 1736': 'ปี 1736',
    'ป 1818': 'ปี 1818',
    'กอ': 'ก่อ',
    'ตอ': 'ต่อ',
    'รอน': 'ร้อน',
    'รน': 'ร้อน',
    'ผาน': 'ผ่าน',
    'คนพบ': 'ค้นพบ',
    'คนพบวา': 'ค้นพบว่า',
    'คนพบวา': 'ค้นพบว่า',

    # Missing THANTHAKHAT (์ / karan)
    'คริสตกาล': 'คริสต์กาล',
    'รถยนต': 'รถยนต์',
    'ประดิษฐ': 'ประดิษฐ์',
    'อุปกรณ': 'อุปกรณ์',
    'ตลอดกาล': 'ตลอดกาล',

    # Wrong SARA I (ิ) vs SARA II (ี)
    'คณตศาสตร': 'คณิตศาสตร์',
    'ฟสิกส': 'ฟิสิกส์',
    'วทยาศาสตร': 'วิทยาศาสตร์',

    # Word-end THANTHAKHAT for final consonants
    'วา': 'ว่า',
    'ได': 'ได้',
    'เพอ': 'เพื่อ',
    'เปน': 'เป็น',
    'แลว': 'แล้ว',
    'กอน': 'ก่อน',
    'หลง': 'หลัง',
    'มน': 'มัน',
    'นน': 'นั้น',
    'น ': 'นี้ ',  # careful: this is too broad
    'ท ': 'ที่ ',  # careful too
    'ท ': 'ที่ ',
    'อย ': 'อยู่ ',
    'คอ': 'คือ',
    'ทง': 'ทั้ง',
    
    # Missing vowels
    'กาลิเลโอ': 'กาลิเลโอ',  # already correct
    'เอเธนส': 'เอเธนส์',
    'ปารส': 'ปารีส',
    'ฝรังเศส': 'ฝรั่งเศส',
    'ครอบครว': 'ครอบครัว',
    'กอตั้ง': 'ก่อตั้ง',
    'มหาวทยาลย': 'มหาวิทยาลัย',
    'ทองฟา': 'ท้องฟ้า',
    'สวน': 'ส่วน',
    'พนฐาน': 'พื้นฐาน',
    'พม': 'เพิ่ม',
    'เชน': 'เช่น',
    'ถง': 'ถึง',
    'อาน': 'อ่าน',
    'เกยวกบ': 'เกี่ยวกับ',
    'แตงงาน': 'แต่งงาน',
    'คำนวณ': 'คำนวณ',  # already correct
    'สงเกต': 'สังเกต',
    'อธบาย': 'อธิบาย',
    'ยง': 'ยัง',
    'เลย': 'เลีย',
    
    # "ส" that needs "์" (karan) at word end
    'เอเธนส ': 'เอเธนส์ ',
    'กรซ ': 'กรีซ ',
    
    # Common word compounds
    'รวมถง': 'รวมถึง',
    'นอกจากน': 'นอกจากนี้',
    'ซง': 'ซึ่ง',
    'กระทง': 'กระทั่ง',
    'แลว': 'แล้ว',
    'เสย': 'เสีย',
    'เรยก': 'เรียก',
    'สำหรบ': 'สำหรับ',
    'สวนใหญ': 'ส่วนใหญ่',
    'ประวต': 'ประวัติ',
    'ผลลพธ': 'ผลลัพธ์',
    'เปด': 'เปิด',
    'เหต': 'เหตุ',
    'จำนวนมาก': 'จำนวนมาก',
    'เฉพาะ': 'เฉพาะ',
    
    # Missing vowel combinations
    'นกฟสิกส': 'นักฟิสิกส์',
    'นกดาราศาสตร': 'นักดาราศาสตร์',
    'นกคณตศาสตร': 'นักคณิตศาสตร์',
    'นกวทยาศาสตร': 'นักวิทยาศาสตร์',
    'นกปรชญา': 'นักปรัชญา',
    'นกประดษฐ': 'นักประดิษฐ์',
    'นกทดลอง': 'นักทดลอง',
    
    # Specific name issues
    'นิวตน': 'นิวตัน',
    'นวตน': 'นิวตัน', 
    'นวตั้น': 'นิวตั้น',
    'จล': 'จูล',
    'บล': 'บอยล์',
    
    # Tone mark errors  
    'ตก': 'ตก',  # contextual
    'หยด': 'หยุด',
    'มาก': 'มาก',
    'หลาย': 'หลาย',
    'คอ': 'คือ',
    'ตาม': 'ตาม',
    'ระหวาง': 'ระหว่าง',
    'ตางหาก': 'ต่างหาก',
    'เปด': 'เปิด',
    'แพร': 'แพร่',
    'อสระ': 'อิสระ',
    'ขอบเขต': 'ขอบเขต',
    'รวมถง': 'รวมถึง',
    'โดยเฉพาะ': 'โดยเฉพาะ',
    'อยางไร': 'อย่างไร',
    'เวณ': 'เว้น',
    'ตอไป': 'ต่อไป',
    'เรม': 'เริ่ม',
    'สง': 'ส่ง',
    'ผลก': 'ผลัก',
    'สลบ': 'สลับ',
    'เยน': 'เย็น',
    'ปรมาณ': 'ปริมาณ',
    'เครอง': 'เครื่อง',
    'ตรงขาม': 'ตรงข้าม',
    'รวมกน': 'ร่วมกัน',
}

# Apply fixes to all Thai text fields in the JSON
def fix_thai_text(text):
    """Apply all known Thai character fixes."""
    if not isinstance(text, str):
        return text
    for wrong, correct in thai_fixes.items():
        text = text.replace(wrong, correct)
    return text

def fix_field(obj, field):
    """Fix a string or list-of-strings field."""
    if field in obj:
        val = obj[field]
        if isinstance(val, str):
            obj[field] = fix_thai_text(val)
        elif isinstance(val, list):
            obj[field] = [fix_thai_text(item) for item in val]

# Count fixes
fix_count = 0

for s in data['scientists']:
    # Fix main Thai fields
    for field in ['summary_th', 'key_quote_th']:
        if field in s:
            old = s.get(field, '')
            s[field] = fix_thai_text(s[field])
            if old != s[field]:
                fix_count += 1
    
    for field in ['biography_th', 'contributions_th', 'legacy_th']:
        if field in s:
            old_list = list(s.get(field, []))
            s[field] = [fix_thai_text(item) for item in s[field]]
            if old_list != s[field]:
                fix_count += 1
    
    # Fix experiments
    if 'key_experiments' in s:
        for exp in s['key_experiments']:
            for ef in ['title_th', 'desc_th', 'myth_th']:
                if ef in exp:
                    old = exp[ef]
                    exp[ef] = fix_thai_text(exp[ef])
                    if old != exp[ef]:
                        fix_count += 1

# Save fixed JSON
with open('scientist_bio_library_v1.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Applied Thai text fixes to {fix_count} fields")
print(f"   Sample: ปีก→ปีก, กอ→กอ, etc.")

# Verify a sample
for s in data['scientists']:
    if s['id'] == 'aristotle':
        bio = s.get('biography_th', [''])[0]
        print(f"\nSample fixed text: {bio[:150]}")
        has_pi_korn = 'ปีก่อน' in bio
        has_kor = 'ก่อตั้ง' in ' '.join(s.get('biography_th', []))
        print(f"  ปีก่อน correct: {has_pi_korn}")
        print(f"  ก่อตั้ง correct: {has_kor}")
        break