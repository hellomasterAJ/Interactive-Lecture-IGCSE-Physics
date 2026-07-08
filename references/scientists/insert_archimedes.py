#!/usr/bin/env python3
"""ติตี้: Insert Archimedes approved Thai translation into JSON + rebuild viewer."""
import json

with open('scientist_bio_library_v1.json', 'r', encoding='utf-8') as f:
    lib = json.load(f)

archimedes_th = {
    'summary_th': 'Archimedes (อาร์คิมิดีส) ค้นพบกฎแรงลอยตัวและหลักการของคาน — ฟิสิกส์เชิงคณิตศาสตร์ยุคแรก',
    'biography_th': [
        'Archimedes (อาร์คิมิดีส) เกิดเมื่อ 287 ปีก่อนคริสต์กาลในนครรัฐ Syracuse (ซีราคิวส์) ของกรีก (ปัจจุบันคือ Sicily (ซิซิลี), Italy (อิตาลี)) เขาเป็นนักคณิตศาสตร์ นักฟิสิกส์ วิศวกร และนักประดิษฐ์',
        'เขาศึกษาที่ Alexandria (อเล็กซานเดรีย), Egypt (อียิปต์) — ศูนย์กลางปัญญาของโลกโบราณ — ก่อนจะกลับไปยัง Syracuse (ซีราคิวส์) ซึ่งเขาใช้ชีวิตส่วนใหญ่',
        'การค้นพบที่โด่งดังที่สุดของเขาเกิดขึ้นเมื่อก้าวลงอ่างอาบน้ำและสังเกตเห็นระดับน้ำสูงขึ้น เขาตระหนักว่าสามารถวัดปริมาตรของวัตถุรูปทรงไม่แน่นอนได้จากปริมาณน้ำที่ถูกแทนที่ ตำนานเล่าว่าเขาวิ่งเปลือยเปล่าตามถนนตะโกนว่า \'Eureka (ยูเรก้า)!\' (ฉันพบแล้ว!)',
        'เขายังเป็นวิศวกรอัจฉริยะ — ออกแบบเครื่องจักรสงคราม (หนังสติก, ปั้นจั่นตะขอ) ที่ป้องกัน Syracuse (ซีราคิวส์) จากการรุกรานของโรมันนานถึง 3 ปี เมื่อเมืองแตกในที่สุด ทหารโรมันคนหนึ่งสังหารเขาทั้งที่มีคำสั่งให้ไว้ชีวิต'
    ],
    'contributions_th': [
        'Archimedes\' Principle (หลักการของอาร์คิมิดีส): แรงลอยตัวบนวัตถุเท่ากับน้ำหนักของของไหลที่ถูกแทนที่',
        'Law of the Lever (กฎแห่งคาน): อัตราส่วนของแรงสมดุลกับอัตราส่วนของระยะห่างจากฟัลครัม',
        'คำนวณค่า π (พาย) ได้อย่างแม่นยำ',
        'พัฒนาแนวคิดเรื่องจุดศูนย์ถ่วง',
        'Archimedes screw (สกรูของอาร์คิมิดีส) — ยังใช้อยู่ในปัจจุบันสำหรับสูบน้ำ'
    ],
    'legacy_th': [
        'Archimedes (อาร์คิมิดีส) ถือเป็นนักวิทยาศาสตร์ที่ยิ่งใหญ่ที่สุดในสมัยโบราณและเป็นนักคณิตศาสตร์ที่ยิ่งใหญ่ที่สุดคนหนึ่งตลอดกาล',
        'หลักการแรงลอยตัวของเขาเป็นส่วนสำคัญของหลักสูตร IGCSE Physics (ฟิสิกส์ IGCSE) (ความหนาแน่นและการลอย/จม)',
        'หลักการคานเป็นรากฐานของเครื่องกลอย่างง่ายทั้งหมด — ตั้งแต่กรรไกรถึงปั้นจั่น',
        'วิธีการระบาย (method of exhaustion) ของเขาล้ำหน้าแคลคูลัสอินทิกรัลเกือบ 2,000 ปี'
    ],
    'key_quote_th': 'ขอจุดยืนให้ฉันสักแห่ง แล้วฉันจะเคลื่อนโลกทั้งใบ',
    'experiments_th': [
        {
            'title_th': 'The Golden Crown — Eureka! (มงกุฎทองคำ — ยูเรก้า!)',
            'desc_th': 'กษัตริย์ Hiero II (เฮียโรที่ 2) ทรงสงสัยว่าช่างทองเจือเงินลงในมงกุฎทองคำ Archimedes (อาร์คิมิดีส) ต้องตรวจสอบโดยไม่ทำให้มงกุฎเสียหาย เมื่อก้าวลงอ่างอาบน้ำ เขาสังเกตระดับน้ำสูงขึ้นและตระหนักว่าปริมาตรน้ำที่ถูกแทนที่เท่ากับปริมาตรของวัตถุที่จม — ทำให้วัดความหนาแน่นของมงกุฎได้',
            'myth_th': 'เรื่องหลักเป็นที่ยอมรับอย่างกว้างขวาง รายละเอียด \'วิ่งเปลือยบนถนน\' อาจเป็นการเสริมแต่งโดยนักเขียนโรมันยุคหลัง การทดลองนั้นใช้ได้ทางวิทยาศาสตร์: ใช้การแทนที่วัดปริมาตรแล้วใช้ความหนาแน่นตรวจสอบสิ่งเจือปน'
        },
        {
            'title_th': 'The Lever — Moving a Ship (คาน — การเคลื่อนย้ายเรือ)',
            'desc_th': 'Archimedes (อาร์คิมิดีส) กล่าวกันว่าดึงเรือบรรทุกสินค้าที่เต็มลำขึ้นมาบนบกเพียงคนเดียวโดยใช้ระบบรอกผสม แสดงให้เห็นข้อได้เปรียบเชิงกลของคานและรอก เขาได้กล่าวว่า: "ขอจุดยืนให้ฉันสักแห่ง แล้วฉันจะเคลื่อนโลกทั้งใบ"',
            'myth_th': 'เรื่องนี้ถูกบันทึกโดยนักประวัติศาสตร์ร่วมสมัย (Plutarch) และถือว่าน่าเชื่อถือ ระบบรอกที่ออกแบบดีสามารถทำให้คนคนเดียวเคลื่อนย้ายของหนักมากได้จริง'
        }
    ]
}

# Find and update Archimedes
for s in lib['scientists']:
    if s['id'] == 'archimedes':
        s['summary_th'] = archimedes_th['summary_th']
        s['biography_th'] = archimedes_th['biography_th']
        s['contributions_th'] = archimedes_th['contributions_th']
        s['legacy_th'] = archimedes_th['legacy_th']
        s['key_quote_th'] = archimedes_th['key_quote_th']
        if 'key_experiments' in s:
            for i, exp in enumerate(archimedes_th['experiments_th']):
                if i < len(s['key_experiments']):
                    s['key_experiments'][i]['title_th'] = exp['title_th']
                    s['key_experiments'][i]['desc_th'] = exp['desc_th']
                    s['key_experiments'][i]['myth_th'] = exp['myth_th']
        print('✅ Archimedes Thai fields updated')
        break

# Save JSON
with open('scientist_bio_library_v1.json', 'w', encoding='utf-8') as f:
    json.dump(lib, f, indent=2, ensure_ascii=False)
print('✅ JSON saved')

# Rebuild HTML
with open('scientist_bio_viewer_v1.html', 'r', encoding='utf-8') as f:
    html = f.read()
start = html.find('const scientists = [')
end = html.find('];\n\nfunction render')
html = html[:start] + 'const scientists = ' + json.dumps(lib['scientists'], indent=2, ensure_ascii=False) + ';\n\nfunction render' + html[end + len('];\n\nfunction render'):]
with open('scientist_bio_viewer_v1.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('✅ HTML viewer rebuilt')

# Verify
for s in lib['scientists']:
    if s['id'] == 'archimedes':
        print(f'\n🔍 TH mode summary: {s["summary_th"][:60]}...')
        print(f'🔍 TH mode bio[0]: {s["biography_th"][0][:80]}...')
        errors = []
        text = json.dumps(s, ensure_ascii=False)
        for w in ['จำแนัก','ฟิสิกส','เชน','แรงตานอากาศ']:
            if w in text:
                errors.append(w)
        if errors:
            print(f'⚠️ Still has: {errors}')
        else:
            print('✅ No remaining errors found')
        break