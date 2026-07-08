#!/usr/bin/env python3
"""Add Thai translations to all scientist content fields in JSON + update HTML viewer."""
import json, re

with open('scientist_bio_library_v1.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# ===== THAI TRANSLATIONS FOR ALL SCIENTISTS =====
# Field format: { id: { summary_th, biography_th: [...], contributions_th: [...], legacy_th: [...],
#                       quote_th, experiments_th: [{title_th, desc_th, myth_th}] } }

th = {}

# Helper to build name: "English (ไทย)"
def N(en, thai): return f"{en} ({thai})"
# Helper for places: "English (ไทย)"  
def P(en, thai): return f"{en} ({thai})"

# ============ TOPIC 1 ============

th['aristotle'] = {
  'summary_th': N('Aristotle','อริสโตเติล') + ' วางรากฐานแรกของฟิสิกส์ด้วยทฤษฎีการเคลื่อนที่แบบธรรมชาติและแบบรุนแรง',
  'biography_th': [
    N('Aristotle','อริสโตเติล') + f' เกิดเมื่อ 384 ปีก่อนคริสตกาลที่ {P("Stagira","สตากีรา")} ทางตอนเหนือของกรีซ เขาศึกษาที่ {P("Plato's Academy","สำนักของพลาโต")} ใน {P("Athens","เอเธนส์")} นาน 20 ปี ก่อนจะก่อตั้งโรงเรียนของตนเองที่ชื่อ {P("Lyceum","ไลเซียม")}',
    f'เขาเป็นหนึ่งในนักปรัชญาที่ทรงอิทธิพลมากที่สุดในประวัติศาสตร์ตะวันตก เขียนเกี่ยวกับฟิสิกส์ ชีววิทยา จริยศาสตร์ การเมือง และอภิปรัชญา คำสอนของเขาครอบงำความคิดทางวิทยาศาสตร์นานเกือบ 2,000 ปี',
    f'ในฟิสิกส์ {N("Aristotle","อริสโตเติล")} เสนอว่าการเคลื่อนที่ทั้งหมดแบ่งเป็น 2 ประเภท: การเคลื่อนที่ตามธรรมชาติ (วัตถุหาที่อยู่ตามธรรมชาติ — ของหนักตกลง, ของเบาลอยขึ้น) และการเคลื่อนที่แบบรุนแรง (การเคลื่อนที่ที่เกิดจากแรงภายนอก)',
    f'เขาโต้แย้งว่าวัตถุที่หนักกว่าตกลงมาเร็วกว่าวัตถุที่เบากว่า — ข้ออ้างที่ต่อมา {N("Galileo","กาลิเลโอ")} พิสูจน์ว่าผิด เขายังเชื่อว่าสุญญากาศ (ที่ว่างเปล่า) ไม่มีอยู่จริง และต้องใช้แรงเพื่อให้วัตถุเคลื่อนที่ต่อไป'
  ],
  'contributions_th': [
    f'การจำแนกการเคลื่อนที่อย่างเป็นระบบครั้งแรกเป็นแบบธรรมชาติและแบบรุนแรง',
    f'แนวคิดยุคแรกเกี่ยวกับ {P("aether","อีเทอร์")} ในฐานะธาตุที่ห้าเหนือโลก',
    f'บุกเบิกการสังเกตเชิงประจักษ์ในฐานะวิธีการทำความเข้าใจธรรมชาติ',
    f'มีอิทธิพลต่อการพัฒนาตรรกะและการใช้เหตุผลทางวิทยาศาสตร์'
  ],
  'legacy_th': [
    f'แม้ทฤษฎีฟิสิกส์ของเขาจะถูกแทนที่โดย {N("Galileo","กาลิเลโอ")} และ {N("Newton","นิวตัน")} แต่วิธีการสังเกตและการจำแนกอย่างเป็นระบบของ {N("Aristotle","อริสโตเติล")} ได้หล่อหลอมวิธีการทำวิทยาศาสตร์',
    f'แนวคิดที่ว่า \'การเคลื่อนที่ต้องใช้แรง\' เป็นกระบวนทัศน์หลักจนกระทั่ง {N("Newton\'s First Law","กฎข้อที่หนึ่งของนิวตัน")} แทนที่ด้วยแนวคิดเรื่องความเฉื่อย',
    f'ความท้าทายในการพิสูจน์ว่าทฤษฎีของ {N("Aristotle","อริสโตเติล")} ผิดเป็นแรงผลักดันสำคัญของการปฏิวัติวิทยาศาสตร์ — {N("Galileo","กาลิเลโอ")}, {N("Newton","นิวตัน")} และคนอื่นๆ ทดสอบและปรับปรุงแนวคิดของเขาโดยตรง'
  ],
  'quote_th': 'เราต้องไม่ปล่อยให้ตนเองถูกหลอกด้วยแนวคิดที่ว่าวัตถุที่กำลังเคลื่อนที่ต้องใช้แรงเพื่อให้มันเคลื่อนที่ต่อไป',
  'experiments_th': [
    {
      'title_th': f'{P("Classification of Motion","การจำแนกประเภทการเคลื่อนที่")}',
      'desc_th': f'{N("Aristotle","อริสโตเติล")} จำแนกการเคลื่อนที่ทั้งหมดเป็นสองประเภท: การเคลื่อนที่ตามธรรมชาติ (วัตถุหาที่อยู่ตามธรรมชาติของตน) และการเคลื่อนที่แบบรุนแรง (การเคลื่อนที่ที่ต้องใช้แรงภายนอก) การจำแนกนี้ครอบงำฟิสิกส์นานเกือบ 2,000 ปี',
      'myth_th': f'这不是การทดลองที่มีการควบคุม {N("Aristotle","อริสโตเติล")} อาศัยการสังเกตในชีวิตประจำวันและการใช้เหตุผลเชิงตรรกะ ข้อสรุปของเขา (เช่น วัตถุที่หนักกว่าตกลงเร็วกว่า) มีเหตุผลจากการสังเกตทั่วไป แต่เขาไม่เคยทดสอบบทบาทของแรงต้านอากาศ'
    }
  ]
}

# Let me save what we have so far and check the structure
print(f"✅ Prepared Thai translations for 1 scientist")
print(f"   Need to do 48 more...")
print(f"   File too large - need to split approach")

# Test: check if the existing structure supports biography_th, etc.
# The HTML template uses s.biography, s.contributions_to_physics, etc.
# I need to either:
# A) Add _th suffix fields in JSON + update HTML template
# B) Or make the existing fields bilingual {en:, th:}

# Let me go with approach A: add _th suffix fields
# Then update the HTML template to use lang-aware field access