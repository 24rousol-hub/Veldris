#!/usr/bin/env python3
import json, re, sys
from pathlib import Path
TIMES = ('Morning', 'Day', 'Evening', 'Night')
path = sys.argv[1] if len(sys.argv) > 1 else str(Path(__file__).resolve().parents[2] / 'src/data/wild_encounters.json')
data = json.load(open(path)); bad = 0
# Author rule (2026-10-09): time tables only on open-air routes. Warn for any other map type.
MAP_TYPES = {}
ROOT = Path(__file__).resolve().parents[2]
for mj in (ROOT / 'data/maps').glob('*/map.json'):
    try:
        m = json.load(open(mj)); MAP_TYPES[m['id']] = m.get('map_type')
    except (OSError, ValueError, KeyError):
        pass
def err(m):
    global bad; bad += 1; print('ERROR:', m)
for group in data['wild_encounter_groups']:
    slots = {f['type']: len(f['encounter_rates']) for f in group.get('fields', [])}
    shared = {}
    for e in group['encounters']:
        label = e['base_label']
        m = re.fullmatch(r'(.+)_(Morning|Day|Evening|Night)', label)
        stem, suffix = (m.group(1), m.group(2)) if m else (label, None)
        if suffix and MAP_TYPES.get(e.get('map'), 'MAP_TYPE_ROUTE') != 'MAP_TYPE_ROUTE':
            print(f'WARN: {label}: a {suffix} table on a {MAP_TYPES[e["map"]]} map; time tables are for open-air routes only (design/time-of-day.md)')
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