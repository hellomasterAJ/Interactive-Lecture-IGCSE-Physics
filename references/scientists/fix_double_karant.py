#!/usr/bin/env python3
"""ติตี้: Fix remaining Thai issues — double karant + verify correctly."""
import json

with open('scientist_bio_library_v1.json', 'r', encoding='utf-8') as f:
    lib = json.load(f)

# Fix double karant (์์) → single karant (์)
total = 0
for s in lib['scientists']:
    text = json.dumps(s, ensure_ascii=False)
    # Simple approach: apply fixes to each field directly
    
    def fix_text(t):
        if not isinstance(t, str):
            return t, 0
        c = 0
        # Fix double karant
        while '์์' in t:
            t = t.replace('์์', '์')
            c += 1
        return t, c
    
    # String fields
    for f in ['summary_th', 'key_quote_th']:
        if f in s:
            s[f], c = fix_text(s[f])
            total += c
    
    # List fields
    for f in ['biography_th', 'contributions_th', 'legacy_th']:
        if f in s and isinstance(s[f], list):
            for i in range(len(s[f])):
                s[f][i], c = fix_text(s[f][i])
                total += c
    
    # Experiments
    if 'key_experiments' in s:
        for exp in s['key_experiments']:
            for ef in ['title_th', 'desc_th', 'myth_th']:
                if ef in exp:
                    exp[ef], c = fix_text(exp[ef])
                    total += c

# Save JSON
with open('scientist_bio_library_v1.json', 'w', encoding='utf-8') as f:
    json.dump(lib, f, indent=2, ensure_ascii=False)

# Rebuild HTML
with open('scientist_bio_viewer_v1.html', 'r', encoding='utf-8') as f:
    html = f.read()

start = html.find('const scientists = [')
end = html.find('];\n\nfunction render')
formatted = json.dumps(lib['scientists'], indent=2, ensure_ascii=False)
html = html[:start] + 'const scientists = ' + formatted + ';\n\nfunction render' + html[end + len('];\n\nfunction render'):]

with open('scientist_bio_viewer_v1.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Final real verification
print("✅ Double karant fixes applied:", total)

# Check for REAL issues (NOT false positives from substring matching)
print("\n🔍 Verifying Spanish word 'จำแนัก'...")
remaining = 0
for s in lib['scientists']:
    text = json.dumps(s, ensure_ascii=False)
    if 'จำแนัก' in text:
        print(f"  ⚠️ Found in {s['id']}")
        remaining += 1
print(f"  Result: {remaining} remaining")

print("🔍 Verifying 'เชน' (not as substring of 'เช่น')...")
remaining = 0
for s in lib['scientists']:
    text = json.dumps(s, ensure_ascii=False)
    if 'เชน' in text:
        print(f"  ⚠️ Found in {s['id']}")
        remaining += 1
print(f"  Result: {remaining} remaining")

print("🔍 Verifying 'แรงตานอากาศ'...")
remaining = 0
for s in lib['scientists']:
    text = json.dumps(s, ensure_ascii=False)
    if 'แรงตานอากาศ' in text:
        print(f"  ⚠️ Found in {s['id']}")
        remaining += 1
print(f"  Result: {remaining} remaining")

print("🔍 Verifying 'ฟิสิกส' NOT followed by ์ (real error vs false positive)...")
for s in lib['scientists']:
    text = json.dumps(s, ensure_ascii=False)
    idx = text.find('ฟิสิกส')
    while idx >= 0:
        # Check if next char is karant (U+0E4C = ์)
        if idx + 6 < len(text) and text[idx+6] != '์':
            # Real error!
            context = text[max(0,idx-20):idx+30]
            print(f"  REAL in {s['id']}: ...{context}...")
        idx = text.find('ฟิสิกส', idx+1)