#!/usr/bin/env python3
"""ติตี้: Fix specific Thai word errors across ALL scientists, then rebuild viewer."""
import json

with open('scientist_bio_library_v1.json', 'r', encoding='utf-8') as f:
    lib = json.load(f)

# === TARGETED WORD FIXES ===
fixes = {
    'จำแนัก': 'จำแนก',
    'ฟิสิกส': 'ฟิสิกส์',
    'เชน': 'เช่น',
    'แรงตานอากาศ': 'แรงต้านอากาศ',
}

total = 0

for s in lib['scientists']:
    # Fix string fields
    for field in ['summary_th', 'key_quote_th']:
        if field in s and isinstance(s[field], str):
            for wrong, correct in fixes.items():
                if wrong in s[field]:
                    s[field] = s[field].replace(wrong, correct)
                    total += 1
    
    # Fix list fields
    for field in ['biography_th', 'contributions_th', 'legacy_th']:
        if field in s and isinstance(s[field], list):
            for i in range(len(s[field])):
                for wrong, correct in fixes.items():
                    if wrong in s[field][i]:
                        s[field][i] = s[field][i].replace(wrong, correct)
                        total += 1
    
    # Fix experiments
    if 'key_experiments' in s:
        for exp in s['key_experiments']:
            for ef in ['title_th', 'desc_th', 'myth_th']:
                if ef in exp:
                    for wrong, correct in fixes.items():
                        if wrong in exp[ef]:
                            exp[ef] = exp[ef].replace(wrong, correct)
                            total += 1

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

# Verify
remaining = 0
for s in lib['scientists']:
    sid = s['id']
    text = json.dumps(s, ensure_ascii=False)
    for w in fixes:
        if w in text:
            print(f"  ⚠️ Still has '{w}' in {sid}")
            remaining += 1

print(f"✅ Fixed {total} occurrences across {len(lib['scientists'])} scientists")
print(f"✅ Remaining issues: {remaining}")
print("✅ HTML viewer rebuilt")