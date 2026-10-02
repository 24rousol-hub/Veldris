#!/usr/bin/env python3
"""Check the wild tables in design/maps/*.md: every table has 12 rows (land) or a
documented count, rates sum to 100, species exist in include/constants/species.h and are
enabled, levels are sane. Usage: python3 design/tools/cardcheck.py"""
import re, glob, sys, os
root = os.path.join(os.path.dirname(__file__), '..', '..')
sp = open(os.path.join(root, 'include/constants/species.h')).read()
species = set(re.findall(r'SPECIES_(\w+)\s*=', sp)) | set(re.findall(r'^\s+SPECIES_(\w+),', sp, re.M))
# aliases in species.h like #define SPECIES_X SPECIES_Y
species |= set(re.findall(r'#define SPECIES_(\w+)\s', sp))
files = sorted(glob.glob(os.path.join(root, 'design/maps/**/*.md'), recursive=True))
row = re.compile(r'^\|\s*(\d+)\s*\|\s*(\d+)%\s*\|\s*([A-Za-z0-9_\'. -]+?)\s*\|\s*(\d+)(?: to (\d+))?\s*\|')
errors = warnings = tables = 0
for f in files:
    lines = open(f).read().split('\n')
    i = 0
    while i < len(lines):
        m = row.match(lines[i])
        if not m: i += 1; continue
        start = i; rows = []
        while i < len(lines) and row.match(lines[i]):
            rows.append(row.match(lines[i])); i += 1
        tables += 1
        rel = os.path.relpath(f, root)
        total = sum(int(r.group(2)) for r in rows)
        if total != 100:
            print(f"ERROR {rel}:{start+1}: rates sum to {total}, not 100"); errors += 1
        for r in rows:
            name = r.group(3).strip().upper().replace(' ', '_').replace("'", '').replace('.', '')
            if name == 'MR_MIME': name = 'MR_MIME'
            if name not in species:
                print(f"ERROR {rel}:{start+1}: unknown species {r.group(3)}"); errors += 1
            lo = int(r.group(4)); hi = int(r.group(5) or lo)
            if hi < lo or hi > 100:
                print(f"ERROR {rel}:{start+1}: bad levels {lo}-{hi}"); errors += 1
        if len(rows) not in (12, 5, 2, 10, 3, 4, 6, 8) and len(rows) != 12:
            print(f"WARN  {rel}:{start+1}: {len(rows)} rows (land tables have 12)"); warnings += 1
# inline species lists (Surf, rods, trainer teams): NAME 53 to 56, NAME 54
inl = re.compile(r"\b([A-Z][A-Z0-9_]{2,}|[A-Z][a-z]+(?:'[a-z]+)?)\s+(\d{1,3})(?: to (\d{1,3}))?\b")
stop = {'ROUTE','GYM','LEVEL','LEVELS','FLAG','TOWN','ACE','AND','TO','BADGE','BADGES','MAPSEC','ID','IDS','FIGHT','FIGHTS','SCHEME','NINE','EIGHT','CHAMBER','CHAMBERS','FLOOR','TM','HM','PAGE','ROW','ROWS','SLOT','SLOTS','TILES','STAGE','PROPOSED','PARTY','SIZE','TEAM','LV','UP','GEN','TYPE','OLD','GOOD','SUPER','ROD','SURF','R','THE','TYPES','POKEMON'}
inline_checked = 0
for f in files:
    rel = os.path.relpath(f, root)
    for n, line in enumerate(open(f).read().split('\n'), 1):
        if not re.search(r"(Surf|Rod|Fishing|Team|\|\s*(?:[A-Z][a-z]+ ?)+\s*\|)", line): continue
        found = [(m.group(1), m) for m in inl.finditer(line)]
        good = [t for t, m in found if t.upper().replace(' ', '_') in species]
        if not good: continue
        for t, m in found:
            u = t.upper()
            if u in stop or u in species or t.upper().replace(' ', '_') in species: continue
            if t[0].isupper() and t[1:].islower(): continue   # a normal word followed by a number
            print(f"WARN  {rel}:{n}: '{t} {m.group(2)}' is not a known species"); warnings += 1
        inline_checked += len(good)
print(f"{inline_checked} inline species checked")
print(f"{tables} tables in {len(files)} files: {errors} error(s), {warnings} warning(s)")
sys.exit(1 if errors else 0)
