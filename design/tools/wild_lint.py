#!/usr/bin/env python3
"""Lint src/data/wild_encounters.json (hack tool; the pre-commit hook runs it when the file is staged).

Usage (repo root):  python3 design/tools/wild_lint.py [path] [--staged]
  ERROR (exit 1)  a table with the wrong number of slots; Morning/Day/Evening/Night inside the label but outside the
                  suffix; the same time twice for one map; time tables with no plain (Day) table, because the empty
                  times then have no encounters and nothing else reports it (design/time-of-day.md)
  WARN            a time table on a map that is not MAP_TYPE_ROUTE (author rule 2026-10-09: open-air routes only)
--staged reads the staged blob (`git show :path`), the text the commit will hold, instead of the file on disk."""
import json, re, subprocess, sys
from pathlib import Path
TIMES = ('Morning', 'Day', 'Evening', 'Night')
ROOT = Path(__file__).resolve().parents[2]
staged = '--staged' in sys.argv[1:]
args = [a for a in sys.argv[1:] if a != '--staged']
path = Path(args[0]) if args else ROOT / 'src/data/wild_encounters.json'
data = None
if staged:
    try:
        blob = subprocess.run(['git', 'show', ':' + path.resolve().relative_to(ROOT).as_posix()], cwd=ROOT, capture_output=True, check=True).stdout
        data = json.loads(blob)
    except (OSError, ValueError, subprocess.CalledProcessError):
        pass                                   # not staged or outside the repo: the file on disk
if data is None:
    data = json.load(open(path))
bad = 0
# Author rule (2026-10-09): time tables only on open-air routes. Warn for any other map type.
MAP_TYPES = {}
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
            err(f'{stem}: time tables {sufs} but no plain table (the Day table); the empty times have no encounters')
print('OK' if not bad else f'{bad} problem(s)'); sys.exit(1 if bad else 0)
