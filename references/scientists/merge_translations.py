#!/usr/bin/env python3
"""Merge thai_all.json translations into main library and rebuild HTML viewer."""
import json

# Load
with open('scientist_bio_library_v1.json', 'r', encoding='utf-8') as f:
    lib = json.load(f)

with open('thai_all.json', 'r', encoding='utf-8') as f:
    th = json.load(f)

# Merge by matching scientist IDs
merged = 0
for s in lib['scientists']:
    sid = s['id']
    if sid in th:
        t = th[sid]
        s['summary_th'] = t['summary_th']
        s['biography_th'] = t['biography_th']
        s['contributions_th'] = t['contributions_th']
        s['legacy_th'] = t['legacy_th']
        s['key_quote_th'] = t['key_quote_th']
        
        if 'experiments_th' in t:
            for i, exp_th in enumerate(t['experiments_th']):
                if i < len(s.get('key_experiments', [])):
                    s['key_experiments'][i]['title_th'] = exp_th['title_th']
                    s['key_experiments'][i]['desc_th'] = exp_th['desc_th']
                    if 'myth_th' in exp_th:
                        s['key_experiments'][i]['myth_th'] = exp_th['myth_th']
        merged += 1

# Update version
lib['meta']['version'] = '7.2.0'
lib['meta']['features_added'] = '49 scientists - Topics 1-6 + partial Thai translations (9 scientists, Topics 1-2)'

# Save library
with open('scientist_bio_library_v1.json', 'w', encoding='utf-8') as f:
    json.dump(lib, f, indent=2, ensure_ascii=False)

print(f"✅ Merged {merged} scientists with Thai translations")
print(f"✅ Library saved v7.2.0")

# Now rebuild HTML viewer
with open('scientist_bio_viewer_v1.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = 'const scientists = ['
end_marker = '];\n\nfunction render'
start_idx = html.find(start_marker)
end_idx = html.find(end_marker)
formatted = json.dumps(lib['scientists'], indent=2, ensure_ascii=False)
new_array = 'const scientists = ' + formatted + ';\n\nfunction render'
html = html[:start_idx] + new_array + html[end_idx + len(end_marker):]

# Update meta line
html = html.replace('v7.0.0 • 49 scientists', 'v7.2.0 • 49 scientists')

with open('scientist_bio_viewer_v1.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ HTML viewer rebuilt with Thai translations (v7.2.0)")
print("   Topics 1-2 scientists have full Thai bio/contrib/legacy/quote/experiments")
print("   Topics 3-6 still need translations")