#!/usr/bin/env python3
"""
ติตี้: Insert approved Thai translations for Aristotle into JSON + rebuild HTML viewer.
"""
import json

with open('scientist_bio_library_v1.json', 'r', encoding='utf-8') as f:
    lib = json.load(f)

# ===== APPROVED ARISTOTLE THAI TRANSLATION =====
aristotle_th = {
    'summary_th': 'Aristotle (อริสโตเติล) วางรากฐานแรกของฟิสิกส์ด้วยทฤษฎีการเคลื่อนที่แบบธรรมชาติและแบบรุนแรง',
    'biography_th': [
        'Aristotle (อริสโตเติล) เกิดเมื่อ 384 ปีก่อนคริสต์กาลที่ Stagira (สตากีรา) ทางตอนเหนือของกรีซ เขาศึกษาที่ Plato\'s Academy (สำนักของพลาโต) ใน Athens (เอเธนส์) นาน 20 ปี ก่อนจะก่อตั้งโรงเรียนของตนเองที่ชื่อ Lyceum (ไลเซียม)',
        'เขาเป็นหนึ่งในนักปรัชญาที่ทรงอิทธิพลมากที่สุดในประวัติศาสตร์ตะวันตก เขียนเกี่ยวกับฟิสิกส์ ชีววิทยา จริยศาสตร์ การเมือง และอภิปรัชญา คำสอนของเขาครอบงำความคิดทางวิทยาศาสตร์นานเกือบ 2,000 ปี',
        'ในฟิสิกส์ Aristotle (อริสโตเติล) เสนอว่าการเคลื่อนที่ทั้งหมดแบ่งเป็น 2 ประเภท: การเคลื่อนที่ตามธรรมชาติ (วัตถุหาที่อยู่ตามธรรมชาติของตน — ของหนักตกลง, ของเบาลอยขึ้น) และการเคลื่อนที่แบบรุนแรง (การเคลื่อนที่ที่เกิดจากแรงภายนอก)',
        'เขาแย้งว่าวัตถุที่หนักกว่าตกลงเร็วกว่าวัตถุที่เบากว่า — ข้ออ้างที่ต่อมา Galileo (กาลิเลโอ) พิสูจน์ว่าผิด เขายังเชื่อว่าสุญญากาศ (ที่ว่างเปล่า) ไม่มีอยู่จริง และต้องใช้แรงเพื่อให้วัตถุเคลื่อนที่ต่อไป'
    ],
    'contributions_th': [
        'การจำแนกการเคลื่อนที่อย่างเป็นระบบครั้งแรกเป็นแบบธรรมชาติและแบบรุนแรง',
        'แนวคิดเริ่มแรกเกี่ยวกับ aether (อีเทอร์) ในฐานะธาตุที่ห้าเหนือโลก',
        'เป็นผู้บุกเบิกการสังเกตเชิงประจักษ์ในฐานะวิธีการทำความเข้าใจธรรมชาติ',
        'มีอิทธิพลต่อการพัฒนาตรรกะและการใช้เหตุผลทางวิทยาศาสตร์'
    ],
    'legacy_th': [
        'แม้ทฤษฎีฟิสิกส์หลายอย่างของเขาจะถูกแทนที่โดย Galileo (กาลิเลโอ) และ Newton (นิวตัน) แต่วิธีการสังเกตและการจำแนกอย่างเป็นระบบของ Aristotle (อริสโตเติล) ได้หล่อหลอมวิธีการทำวิทยาศาสตร์',
        'แนวคิดที่ว่า "การเคลื่อนที่ต้องใช้แรง" เป็นกระบวนทัศน์หลัก จนกระทั่ง Newton\'s First Law of Motion (กฎข้อที่หนึ่งของนิวตัน) แทนที่ด้วยแนวคิดเรื่องความเฉื่อย',
        'ความท้าทายในการพิสูจน์ว่าทฤษฎีของ Aristotle (อริสโตเติล) ผิดเป็นแรงผลักดันสำคัญของการปฏิวัติวิทยาศาสตร์ — Galileo (กาลิเลโอ), Newton (นิวตัน) และคนอื่นๆ ได้ทดสอบและปรับปรุงแนวคิดของเขาโดยตรง'
    ],
    'key_quote_th': 'เราต้องไม่ปล่อยให้ตนเองถูกหลอกด้วยแนวคิดที่ว่าวัตถุที่กำลังเคลื่อนที่ต้องใช้แรงเพื่อให้มันเคลื่อนที่ต่อไป',
    'experiments_th': [{
        'title_th': 'Classification of Motion (การจำแนกประเภทการเคลื่อนที่)',
        'desc_th': 'Aristotle (อริสโตเติล) จำแนกการเคลื่อนที่ทั้งหมดเป็น 2 ประเภท: การเคลื่อนที่ตามธรรมชาติ (วัตถุหาที่อยู่ตามธรรมชาติของตน) และการเคลื่อนที่แบบรุนแรง (การเคลื่อนที่ที่ต้องใช้แรงภายนอก) การจำแนกนี้ครอบงำฟิสิกส์นานเกือบ 2,000 ปี',
        'myth_th': 'นี่ไม่ใช่การทดลองที่มีการควบคุม Aristotle (อริสโตเติล) อาศัยการสังเกตในชีวิตประจำวันและการใช้เหตุผลเชิงตรรกะ ข้อสรุปของเขา (เช่น วัตถุที่หนักกว่าตกลงเร็วกว่า) มีเหตุผลจากการสังเกตทั่วไป แต่เขาไม่เคยทดสอบบทบาทของแรงต้านอากาศ'
    }]
}

# Find Aristotle and update
for s in lib['scientists']:
    if s['id'] == 'aristotle':
        for key, val in aristotle_th.items():
            s[key] = val
        print(f"✅ Aristotle — {key} updated")
        break

# Save JSON
with open('scientist_bio_library_v1.json', 'w', encoding='utf-8') as f:
    json.dump(lib, f, indent=2, ensure_ascii=False)
print("✅ JSON saved")

# Rebuild HTML viewer
with open('scientist_bio_viewer_v1.html', 'r', encoding='utf-8') as f:
    html = f.read()

start = html.find('const scientists = [')
end = html.find('];\n\nfunction render')
formatted = json.dumps(lib['scientists'], indent=2, ensure_ascii=False)
html = html[:start] + 'const scientists = ' + formatted + ';\n\nfunction render' + html[end + len('];\n\nfunction render'):]

with open('scientist_bio_viewer_v1.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ HTML viewer rebuilt with corrected Aristotle Thai text")
print("")
print("👉 พร้อมตรวจคำผิด:")