#!/usr/bin/env python3
import json, re, sys
TIMES = ('Morning', 'Day', 'Evening', 'Night')
path = sys.argv[1] if len(sys.argv) > 1 else 'src/data/wild_encounters.json'
data = json.load(open(path)); bad = 0
def err(m):
    global bad; bad += 1; print('ERROR:', m)
for group in data['wild_encounter_groups']:
    slots = {f['type']: len(f['encounter_rates']) for f in group.get('fields', [])}
    shared = {}
    for e in group['encounters']:
        label = e['base_label']
        m = re.fullmatch(r'(.+)_(Morning|Day|Evening|Night)', label)
        stem, suffix = (m.group(1), m.group(2)) if m else (label, None)
        for t in TIMES:
            if t in stem: err(f'{label}: contains {t} outside the suffix; generator picks the wrong slot')
        for field, n in slots.items():
            if field in e and len(e[field]['mons']) != n: err(f'{label}.{field}: {len(e[field]["mons"])} mons, expected {n}')
        shared.setdefault((e.get('map'), stem), []).append(suffix)
    for (mp, stem), sufs in shared.items():
        if len(sufs) != len(set(sufs)): err(f'{stem}: same time twice')
        if sufs != [None] and None not in sufs and 'Day' not in sufs:
            print(f'WARN: {stem}: time tables {sufs} but no plain table (the Day table); empty times will have no encounters')
print('OK' if not bad else f'{bad} problem(s)'); sys.exit(1 if bad else 0)