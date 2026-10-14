#!/usr/bin/env python3
"""skip_lint.py <repo_root> [--write-allowlist FILE | --allowlist FILE]   (read-only)

Guard for 'Option B' (Hoenn maps skipped by tagging `"region": "REGION_HOENN_SKIPPED"`).  The skip is silent: a tagged map
is simply not built, so these slips are easy to make and hard to see:

  E1  a LIVE map (region REGION_HOENN) uses a layout whose layout_version is not 'emerald'
        -> link error (undefined <Layout>), loud but late
  E2  a LIVE map has a warp or connection to a SKIPPED map
        -> at run time the game reads a NULL map header (crash or garbage)
  E3  a map is tagged skipped but is not on the allow-list of Hoenn maps that were skipped on purpose
        -> a Porymap 'Duplicate Map' of a skipped Hoenn map copied the tag; the new Veldris map is silently left out
  E4  gWildMonHeaders has a row for a SKIPPED map
        -> the Pokedex Area page dereferences every row's map header (src/pokedex_area_screen.c) -> garbage area
  W1  heal_locations.json respawn_map is a skipped map          (a white-out or Fly there would load a NULL header)
  W2  a layout is tagged skipped that a design doc names as a template to reuse (PC 1F/2F, Mart, House1/2, Harbor)

Exit code 1 if any E-line is printed.  Not part of the repo (proposal); if adopted it belongs in design/tools/ and the
pre-commit hook.
"""
import glob
import json
import os
import re
import sys

ROOT = sys.argv[1]
args = sys.argv[2:]
SKIP = 'REGION_HOENN_SKIPPED'
TEMPLATES = ['LAYOUT_POKEMON_CENTER_1F', 'LAYOUT_POKEMON_CENTER_2F', 'LAYOUT_MART', 'LAYOUT_HOUSE1', 'LAYOUT_HOUSE2', 'LAYOUT_HARBOR']

maps = {}
for p in glob.glob(os.path.join(ROOT, 'data/maps/*/map.json')):
    d = json.load(open(p))
    maps[d['name']] = d
byid = {d['id']: n for n, d in maps.items()}
skipped = {n for n, d in maps.items() if d.get('region') == SKIP}
live = {n for n, d in maps.items() if d.get('region', 'REGION_HOENN') == 'REGION_HOENN'}
layouts = {l['id']: l for l in json.load(open(os.path.join(ROOT, 'data/layouts/layouts.json')))['layouts'] if l}

if '--write-allowlist' in args:
    f = args[args.index('--write-allowlist') + 1]
    open(f, 'w').write('\n'.join(sorted(skipped)) + '\n')
    print('wrote', len(skipped), 'names to', f)
    sys.exit(0)
allow = None
if '--allowlist' in args:
    allow = set(open(args[args.index('--allowlist') + 1]).read().split())

errors = 0


def err(code, msg):
    global errors
    errors += 1
    print('%s %s' % (code, msg))


for n in sorted(live):
    d = maps[n]
    lv = layouts.get(d['layout'], {}).get('layout_version', 'emerald')
    if lv != 'emerald':
        err('E1', '%s uses %s, layout_version "%s"' % (n, d['layout'], lv))
    for w in d.get('warp_events', []):
        t = byid.get(w.get('dest_map'))
        if t in skipped:
            err('E2', '%s has a warp to the skipped map %s' % (n, t))
    for c in d.get('connections') or []:
        t = byid.get(c.get('map'))
        if t in skipped:
            err('E2', '%s connects to the skipped map %s' % (n, t))
if allow is not None:
    for n in sorted(skipped - allow):
        err('E3', '%s is tagged %s but is not on the allow-list (copied from a skipped map?)' % (n, SKIP))
W = json.load(open(os.path.join(ROOT, 'src/data/wild_encounters.json')))
for grp in W['wild_encounter_groups']:
    if grp['label'] != 'gWildMonHeaders':
        continue
    for e in grp['encounters']:
        t = byid.get(e['map'])
        if t in skipped:
            err('E4', 'gWildMonHeaders row for the skipped map %s (%s)' % (t, e.get('base_label')))
try:
    H = json.load(open(os.path.join(ROOT, 'src/data/heal_locations.json')))
    rows = H.get('heal_locations', [])
    for r in rows:
        t = byid.get(r.get('respawn_map'))
        if t in skipped:
            print('W1 heal location %s respawns in the skipped map %s' % (r.get('id'), t))
except (OSError, ValueError):
    pass
for l in TEMPLATES:
    if layouts.get(l, {}).get('layout_version', 'emerald') != 'emerald':
        print('W2 template layout %s is tagged skipped' % l)
print('%d skipped, %d live Hoenn-region maps, %d errors' % (len(skipped), len(live), errors))
sys.exit(1 if errors else 0)
