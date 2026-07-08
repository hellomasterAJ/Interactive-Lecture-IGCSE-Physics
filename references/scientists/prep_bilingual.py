#!/usr/bin/env python3
"""Phase 1: Update HTML viewer template for full bilingual content support."""
import json

# Read files
with open('scientist_bio_library_v1.json', 'r', encoding='utf-8') as f:
    lib = json.load(f)

with open('scientist_bio_viewer_v1.html', 'r', encoding='utf-8') as f:
    html = f.read()

# === Update 1: Biography array → bilingual ===
old_bio = """<div class="section-label">📜 Biography</div>
          <ul>${bioShort}</ul>
          ${hasMore ? `
            <div id="bio-more-${s.id}" style="display:none;"><ul>${bioRest}</ul></div>
            <button class="show-more-btn" onclick="toggleBio('${s.id}")" id="bio-btn-${s.id}">Show more +</button>
          ` : ''}"""

new_bio = """<div class="section-label">📜 ${lang === 'en' ? 'Biography' : 'ชีวประวัติ'}</div>
          <ul>${bioShort}</ul>
          ${hasMore ? `
            <div id="bio-more-${s.id}" style="display:none;"><ul>${bioRest}</ul></div>
            <button class="show-more-btn" onclick="toggleBio('${s.id}')" id="bio-btn-${s.id}">${lang === 'en' ? 'Show more +' : 'แสดงเพิ่ม +'}</button>
          ` : ''}"""

html = html.replace(old_bio, new_bio)
print("[OK] Biography section bilingual")

# === Update 2: Contributions → bilingual ===
old_contrib = """<div class="section-label">🔬 Key Contributions</div>
          <ul>${s.contributions_to_physics.map(c => `<li>${c}</li>`).join('')}</ul>"""

new_contrib = """<div class="section-label">🔬 ${lang === 'en' ? 'Key Contributions' : 'ผลงานสำคัญ'}</div>
          <ul>${(lang === 'en' ? s.contributions_to_physics : (s.contributions_th || s.contributions_to_physics)).map(c => `<li>${c}</li>`).join('')}</ul>"""

html = html.replace(old_contrib, new_contrib)
print("[OK] Contributions section bilingual")

# === Update 3: Experiments heading + body → bilingual ===
old_exp = """${expHtml ? `
            <div class="section-label">🧪 Key Experiments &amp; Events</div>
            ${expHtml}
          ` : ''}"""

new_exp = """${expHtml ? `
            <div class="section-label">🧪 ${lang === 'en' ? 'Key Experiments &amp; Events' : 'การทดลองสำคัญและเหตุการณ์'}</div>
            ${expHtml}
          ` : ''}"""

html = html.replace(old_exp, new_exp)
print("[OK] Experiments heading bilingual")

# === Update 4: Legacy → bilingual ===
old_legacy = """<div class="section-label">🏛️ Legacy</div>
          <ul>${s.legacy.map(l => `<li>${l}</li>`).join('')}</ul>"""

new_legacy = """<div class="section-label">🏛️ ${lang === 'en' ? 'Legacy' : 'มรดกทางวิทยาศาสตร์'}</div>
          <ul>${(lang === 'en' ? s.legacy : (s.legacy_th || s.legacy)).map(l => `<li>${l}</li>`).join('')}</ul>"""

html = html.replace(old_legacy, new_legacy)
print("[OK] Legacy section bilingual")

# === Update 5: Quote → bilingual ===
old_quote = """<div class="quote">${s.key_quote}</div>"""

new_quote = """<div class="quote">${lang === 'en' ? s.key_quote : (s.key_quote_th || s.key_quote)}</div>"""

html = html.replace(old_quote, new_quote)
print("[OK] Quote bilingual")

# === Update 6: Summary in card header → bilingual ===
old_summary = '<div class="summary">"${s.summary}"</div>'

new_summary = '<div class="summary">"${lang === \'en\' ? s.summary : (s.summary_th || s.summary)}"</div>'

html = html.replace(old_summary, new_summary)
print("[OK] Card summary bilingual")

# === Update 7: Experiment template in render function to use bilingual fields ===
# Find the experiment rendering section
old_exp_render = """    const expHtml = s.key_experiments.map(e => {
      let mythHtml = '';
      if (e.myth_vs_fact) {
        const isMyth = e.myth_vs_fact.includes('DID NOT') || e.myth_vs_fact.includes('MISREPRESENTED') || e.myth_vs_fact.includes('legend');
        mythHtml = `<div class="exp-myth"><span class="${isMyth ? 'myth-label' : 'fact-label'}">${isMyth ? '⚠️ Myth vs Fact' : '📌 Note'}</span><br>${e.myth_vs_fact}</div>`;
      }
      return `<div class="experiment-card">
        <div class="exp-title">🔬 ${e.title} <span class="exp-year">${e.year}</span></div>
        <div class="exp-desc">${e.description}</div>
        ${mythHtml}
      </div>`;
    }).join('');"""

new_exp_render = """    const expHtml = s.key_experiments.map(e => {
      const isEn = lang === 'en';
      const title = isEn ? e.title : (e.title_th || e.title);
      const desc = isEn ? e.description : (e.desc_th || e.description);
      const myth = isEn ? e.myth_vs_fact : (e.myth_th || e.myth_vs_fact);
      let mythHtml = '';
      if (myth) {
        const isMyth = !isEn || (e.myth_vs_fact && (e.myth_vs_fact.includes('DID NOT') || e.myth_vs_fact.includes('MISREPRESENTED') || e.myth_vs_fact.includes('legend')));
        mythHtml = `<div class="exp-myth"><span class="${isMyth ? 'myth-label' : 'fact-label'}">${isEn ? (isMyth ? '⚠️ Myth vs Fact' : '📌 Note') : (isMyth ? '⚠️ ตำนานvsความจริง' : '📌 หมายเหตุ')}</span><br>${myth}</div>`;
      }
      return `<div class="experiment-card">
        <div class="exp-title">🔬 ${title} <span class="exp-year">${e.year}</span></div>
        <div class="exp-desc">${desc}</div>
        ${mythHtml}
      </div>`;
    }).join('');"""

html = html.replace(old_exp_render, new_exp_render)
print("[OK] Experiment rendering bilingual")

# === Update 8: Bio lines → use bilingual arrays ===
# The bio rendering builds bioShort and bioRest from s.biography
# Need to change to use s.biography_th when lang='th'
old_bio_render = """    const bioShort = s.biography.slice(0, 1).map(p => `<li>${p}</li>`).join('');
    const bioRest = s.biography.slice(1).map(p => `<li>${p}</li>`).join('');"""

new_bio_render = """    const bioArr = lang === 'en' ? s.biography : (s.biography_th || s.biography);
    const bioShort = bioArr.slice(0, 1).map(p => `<li>${p}</li>`).join('');
    const bioRest = bioArr.slice(1).map(p => `<li>${p}</li>`).join('');"""

html = html.replace(old_bio_render, new_bio_render)
print("[OK] Bio array bilingual")

# Save
with open('scientist_bio_viewer_v1.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("\n✅ HTML viewer template updated for full bilingual content")
print("   Waiting for Thai translations to be added to JSON...")