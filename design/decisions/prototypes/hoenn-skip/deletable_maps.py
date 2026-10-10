#!/usr/bin/env python3
"""deletable_maps.py <repo_root> <rom_by_map.json> [out_dir]   (read-only; works on any checkout, run it on a CLEAN tree)

Which Hoenn-only maps could be physically deleted WITHOUT editing any C file, shared script or shared text?

A Hoenn-only map is PINNED when something that stays names one of
  * its MAP_ constant,
  * a LOCALID_ / warp-id constant defined in its map.json,
  * a script or text label defined in its scripts.inc,
and that something is not (a) a map folder (Hoenn-only and FRLG folders are deleted or skipped anyway), (b) a data table the
map tool can prune mechanically (wild_encounters.json, heal_locations.json, map_groups.json, layouts.json,
tools/mapjson/required_map_defines.json), or (c) documentation.
Everything else (C, headers, shared data/scripts and data/text, tests, the other json) pins the map: it would have to be edited.

Optional 4th argument: file listing the maps whose scripts.inc stays assembled (results/keep_scripts.txt).
Writes <out_dir>/deletable_maps.json and prints a summary: free vs pinned maps, ROM bytes of each, and the C/header/script
files that pin the most maps (this is the 'edit list' of a true purge).
"""
import collections
import json
import os
import re
import subprocess
import sys

ROOT = sys.argv[1]
ROMJ = json.load(open(sys.argv[2]))
OUT = sys.argv[3] if len(sys.argv) > 3 else '.'
# optional: a file with map names whose scripts.inc stays assembled (the 40 C needs); their text counts as a staying file
KEEP_SCRIPTS = set(open(sys.argv[4]).read().split()) if len(sys.argv) > 4 else set()
VELDRIS = {'Hollowbrook', 'VeldrisRoute1', 'Crestfall', 'Hollowbrook_PlayersHouse_1F', 'Hollowbrook_PlayersHouse_2F',
           'Hollowbrook_ProfFennickLab', 'Hollowbrook_NeighboursHouse', 'Crestfall_PokemonCenter_1F', 'Crestfall_Mart',
           'Crestfall_HouseA', 'Crestfall_HouseB', 'Crestfall_Gym'}


def sh(cmd):
    return subprocess.run(cmd, shell=True, cwd=ROOT, capture_output=True, text=True, errors='replace').stdout


files = [f for f in sh('git ls-files').split('\n') if f]
maps = {}
for f in files:
    if f.startswith('data/maps/') and f.endswith('/map.json'):
        d = json.load(open(os.path.join(ROOT, f)))
        maps[d['name']] = d
hoenn = {n for n, d in maps.items() if d.get('region', 'REGION_HOENN') == 'REGION_HOENN' and n not in VELDRIS}
frlg = {n for n, d in maps.items() if d.get('region', 'REGION_HOENN') != 'REGION_HOENN'}

MECH = {'data/maps/map_groups.json', 'src/data/wild_encounters.json', 'src/data/heal_locations.json',
        'data/layouts/layouts.json', 'tools/mapjson/required_map_defines.json'}
EXT = ('.c', '.h', '.s', '.inc', '.json', '.mk', '.party', '.txt', '.py', '.sh', '.pory', '.cpp', '.mk', '.ld')
TOK = re.compile(r'[A-Za-z_][A-Za-z0-9_]*')


def map_dir(f):
    p = f.split('/')
    return p[2] if len(p) > 3 and p[0] == 'data' and p[1] == 'maps' else None


# token -> set of "staying" files that mention it
users = collections.defaultdict(set)
for f in files:
    if not f.endswith(EXT) or f.startswith(('design/', 'docs/')) or f in MECH:
        continue
    md = map_dir(f)
    if md is not None and (md in hoenn or md in frlg):
        if not (md in KEEP_SCRIPTS and f.endswith('/scripts.inc')):
            continue  # a deleted / skipped map folder (its scripts.inc stays when C needs it)
    if f == 'data/event_scripts.s':
        # the .include lines of Hoenn maps are removed by the tool; ignore tokens that are just those paths
        pass
    try:
        t = open(os.path.join(ROOT, f), errors='replace').read()
    except OSError:
        continue
    for tok in set(TOK.findall(t)):
        users[tok].add(f)

pinned = {}
for n in sorted(hoenn):
    d = maps[n]
    names = {d['id']}
    for e in d.get('object_events', []):
        if e.get('local_id'):
            names.add(e['local_id'])
    for e in d.get('warp_events', []):
        if e.get('warp_id'):
            names.add(e['warp_id'])
    p = os.path.join(ROOT, 'data/maps', n, 'scripts.inc')
    if os.path.exists(p):
        for m in re.finditer(r'^([A-Za-z_]\w*)::?', open(p, errors='replace').read(), re.M):
            names.add(m.group(1))
    why = collections.defaultdict(set)
    for nm in names:
        for f in users.get(nm, ()):
            if f == 'data/event_scripts.s':
                continue
            why[f].add(nm)
    if why:
        pinned[n] = {f: sorted(v) for f, v in why.items()}

per = ROMJ['per_map']
lay = ROMJ['layouts']


def cost(n):
    r = per.get(n, {})
    return r.get('total_excl_layout', 0)


free = sorted(hoenn - set(pinned))
pin_cost = sum(cost(n) for n in pinned)
free_cost = sum(cost(n) for n in free)
print('Hoenn-only maps: %d  | pinned by something that stays: %d  | free to delete with no C/shared edit: %d' % (len(hoenn), len(pinned), len(free)))
print('map bytes (scripts+text, header, events, connections; layouts and tilesets counted separately): pinned %d, free %d' % (pin_cost, free_cost))

# layouts used only by free maps (and by no pinned / Veldris / FRLG map)
use = collections.defaultdict(set)
for n, d in maps.items():
    use[d['layout']].add(n)
free_set = set(free)
free_layouts = [l for l, us in use.items() if us and us <= free_set]
lay_bytes = {}
for l, info in lay.items():
    lay_bytes[l] = info['bytes']
# rom_by_map keys layouts by their label name (X_Layout); map layouts.json id -> name
L = json.load(open(os.path.join(ROOT, 'data/layouts/layouts.json')))['layouts']
idname = {x['id']: x['name'] for x in L if x}
fl_bytes = sum(lay_bytes.get(idname.get(l, ''), 0) for l in free_layouts)
print('layouts used only by free maps: %d (%d bytes)' % (len(free_layouts), fl_bytes))

by_file = collections.Counter()
for n, w in pinned.items():
    for f in w:
        by_file[f] += 1
print('\nfiles (outside map folders) that pin the most maps = the edit list of a true purge:')
for f, c in by_file.most_common(45):
    print('  %4d maps  %s' % (c, f))
kinds = collections.Counter()
for f in by_file:
    if f.startswith('src/') or f.startswith('include/'):
        kinds['C / headers'] += 1
    elif f.startswith('data/scripts') or f.startswith('data/text') or f.endswith('.s') or f.endswith('.inc'):
        kinds['shared scripts / text / asm'] += 1
    elif f.startswith('test/'):
        kinds['tests'] += 1
    else:
        kinds['other'] += 1
print('\npinning files by kind:', dict(kinds), '| total', len(by_file))

fam = collections.Counter()
famfree = collections.Counter()
groups = json.load(open(os.path.join(ROOT, 'data/maps/map_groups.json')))
gof = {m: g for g in groups['group_order'] for m in groups[g]}
for n in hoenn:
    fam[gof[n]] += 1
    if n not in pinned:
        famfree[gof[n]] += 1
print('\nper group: free / total')
for g in groups['group_order']:
    if fam[g]:
        print('  %-36s %3d / %3d' % (g, famfree[g], fam[g]))

json.dump({'free': free, 'pinned': {n: pinned[n] for n in pinned}, 'free_map_bytes': free_cost, 'pinned_map_bytes': pin_cost,
           'free_layouts': free_layouts, 'free_layout_bytes': fl_bytes}, open(os.path.join(OUT, 'deletable_maps.json'), 'w'), indent=1)
