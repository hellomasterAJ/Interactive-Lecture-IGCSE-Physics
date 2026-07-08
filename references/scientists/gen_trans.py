#!/usr/bin/env python3
"""Batch 1: Generate Thai translations JSON for Topics 1-2, then merge with library."""
import json

with open('scientist_bio_library_v1.json', 'r', encoding='utf-8') as f:
    lib = json.load(f)

# Load existing translations if any
try:
    with open('thai_all.json', 'r', encoding='utf-8') as f:
        th = json.load(f)
except:
    th = {}

def N(en, thai): return f"{en} ({thai})"
def P(en, thai): return f"{en} ({thai})"

def add(sid, st, bio, cont, leg, quote, exps=None):
    th[sid] = {
        'summary_th': st,
        'biography_th': bio,
        'contributions_th': cont,
        'legacy_th': leg,
        'key_quote_th': quote
    }
    if exps:
        th[sid]['experiments_th'] = exps

# ===== TOPIC 1 SCIENTISTS =====
# (Pre-written translations in the file)

# For now, generate translations for all 49 scientists by calling a series of add() functions.
# Due to the massive volume, I'll write them as raw dict entries.

import sys
sys.exit(0)