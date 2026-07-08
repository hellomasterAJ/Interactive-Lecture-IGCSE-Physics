#!/usr/bin/env python3
"""ติตี้: Fix specific Thai errors in Aristotle's experiments and rebuild viewer."""
import json

with open('scientist_bio_library_v1.json', 'r', encoding='utf-8') as f:
    lib = json.load(f)

# Find Aristotle
for s in lib['scientists']:
    if s['id'] == 'aristotle':
        # Fix experiments_th
        if 'key_experiments' in s and len(s['key_experiments']) > 0:
            e = s['key_experiments'][0]
            e['title_th'] = 'Classification of Motion (การจำแนกประเภทการเคลื่อนที่)'
            e['desc_th'] = 'Aristotle (อริสโตเติล) จำแนกการเคลื่อนที่ทั้งหมดเป็น 2 ประเภท: การเคลื่อนที่ตามธรรมชาติ (วัตถุหาที่อยู่ตามธรรมชาติของตน) และการเคลื่อนที่แบบรุนแรง (การเคลื่อนที่ที่ต้องใช้แรงภายนอก) การจำแนกนี้ครอบงำฟิสิกส์นานเกือบ 2,000 ปี'
            e['myth_th'] = 'นี่ไม่ใช่การทดลองที่มีการควบคุม Aristotle (อริสโตเติล) อาศัยการสังเกตในชีวิตประจำวันและการใช้เหตุผลเชิงตรรกะ ข้อสรุปของเขา (เช่น วัตถุที่หนักกว่าตกลงเร็วกว่า) มีเหตุผลจากการสังเกตทั่วไป แต่เขาไม่เคยทดสอบบทบาทของแรงต้านอากาศ'
            print("✅ Fixed experiments_th[0] for Aristotle")
        
        # Ensure all other Thai fields are correct
        # Fix legacy_th
        s['legacy_th'] = [
            'แม้ทฤษฎีฟิสิกส์หลายอย่างของเขาจะถูกแทนที่โดย Galileo (กาลิเลโอ) และ Newton (นิวตัน) แต่วิธีการสังเกตและการจำแนกอย่างเป็นระบบของ Aristotle (อริสโตเติล) ได้หล่อหลอมวิธีการทำวิทยาศาสตร์',
            'แนวคิดที่ว่า "การเคลื่อนที่ต้องใช้แรง" เป็นกระบวนทัศน์หลัก จนกระทั่ง Newton\'s First Law of Motion (กฎข้อที่หนึ่งของนิวตัน) แทนที่ด้วยแนวคิดเรื่องความเฉื่อย',
            'ความท้าทายในการพิสูจน์ว่าทฤษฎีของ Aristotle (อริสโตเติล) ผิดเป็นแรงผลักดันสำคัญของการปฏิวัติวิทยาศาสตร์ — Galileo (กาลิเลโอ), Newton (นิวตัน) และคนอื่นๆ ได้ทดสอบและปรับปรุงแนวคิดของเขาโดยตรง'
        ]
        print("✅ Fixed legacy_th for Aristotle")
        break

# Save JSON
with open('scientist_bio_library_v1.json', 'w', encoding='utf-8') as f:
    json.dump(lib, f, indent=2, ensure_ascii=False)

# Rebuild HTML viewer
with open('scientist_bio_viewer_v1.html', 'r', encoding='utf-8') as f:
    html = f.read()

start = html.find('const scientists = [')
end = html.find('];\n\nfunction render')
formatted = json.dumps(lib['scientists'], indent=2, ensure_ascii=False)
html = html[:start] + 'const scientists = ' + formatted + ';\n\nfunction render' + html[end + len('];\n\nfunction render'):]

with open('scientist_bio_viewer_v1.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ HTML viewer rebuilt with ALL correct Aristotle Thai text")

# Final verification
for s in lib['scientists']:
    if s['id'] == 'aristotle':
        d = s['key_experiments'][0]['desc_th']
        m = s['key_experiments'][0]['myth_th']
        errors = []
        for w in ['จำแนัก','ฟิสิกส','เชน','แรงตานอากาศ']:
            if w in d or w in m:
                errors.append(w)
        if errors:
            print(f"⚠️ Still has errors: {errors}")
        else:
            print("✅ No more errors in experiments!")
        l = ' '.join(s['legacy_th'])
        for w in ['ฟิสิกส']:
            if w in l:
                print(f"⚠️ legacy_th still has '{w}'")
        print(f"🔍 desc_th: {d[:80]}...")