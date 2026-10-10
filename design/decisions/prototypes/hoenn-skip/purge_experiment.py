#!/usr/bin/env python3
"""purge_experiment.py - helpers for the Hoenn-purge experiments (run in a CLONE, never in /home/user/Veldris).

Usage:  purge_experiment.py <clone_root> <step> [options]

Steps (each is idempotent and only edits data files):

  list                 print the Veldris / Hoenn-only / FRLG split and the groups that are pure Hoenn
  tag-maps  --scope pure|all    set "region" of Hoenn-only maps to REGION_HOENN_SKIPPED
                       pure = only maps in groups that contain no Veldris map (whole group skipped,
                              so gMapGroups indices are untouched with the stock mapjson)
                       all  = every Hoenn-only map, including those inside group 0 (needs the
                              one-hunk mapjson patch `patch-mapjson`, otherwise indices shift)
  patch-mapjson        apply the NULL-placeholder patch to tools/mapjson/mapjson.cpp
  tag-layouts          set "layout_version": "skipped" on layouts used by no kept map
  skip-scripts         wrap the Hoenn-only `.include "data/maps/X/scripts.inc"` lines of
                       data/event_scripts.s in `.if HOENN_MAP_SCRIPTS`
  delete-maps          physically delete Hoenn-only map folders and drop them from map_groups.json
                       (true deletion; renumbers MAP_* and, with --layouts, LAYOUT_*)
  delete-layouts       drop layouts used by no kept map from layouts.json (renumbers LAYOUT_*)
  prune-wild           drop the gWildMonHeaders rows of every Hoenn-only map from src/data/wild_encounters.json
                       (keeps the Battle Pyramid / Pike tables; the Pokedex Area page reads every row's map header)
  delete-frlg          physically delete the FRLG (non-Hoenn) map folders and drop them from map_groups.json
                       (group names stay in group_order, empty, so MAP_GROUP numbers do not move); with --layouts also
                       drops the frlg layouts from layouts.json
  delete-listed        physically delete the Hoenn-only maps named in the 'free' list of deletable_maps.json (--list FILE), except
                       those in group --skip-group (default gMapGroup_TownsAndRoutes, so Veldris map numbers never move);
                       also drops their gWildMonHeaders rows.  Run it BEFORE tag-maps; tag the rest afterwards
  restore              git checkout + clean everything this script touched (tracked data only)

The 12 Veldris maps and any map named with --keep are never touched.
"""
import json, os, re, subprocess, sys, glob, argparse, shutil

VELDRIS = ['Hollowbrook', 'VeldrisRoute1', 'Crestfall', 'Hollowbrook_PlayersHouse_1F',
           'Hollowbrook_PlayersHouse_2F', 'Hollowbrook_ProfFennickLab', 'Hollowbrook_NeighboursHouse',
           'Crestfall_PokemonCenter_1F', 'Crestfall_Mart', 'Crestfall_HouseA', 'Crestfall_HouseB',
           'Crestfall_Gym']

ap = argparse.ArgumentParser()
ap.add_argument('root')
ap.add_argument('step')
ap.add_argument('--scope', default='pure')
ap.add_argument('--keep', default='')
ap.add_argument('--layouts', action='store_true')
ap.add_argument('--list', default='')
ap.add_argument('--skip-group', default='gMapGroup_TownsAndRoutes')
ap.add_argument('--keep-layouts', default='', help='comma list of LAYOUT_ ids that tag-layouts must leave live (templates the author reuses)')
ap.add_argument('--keep-scripts', default='', help='file with one map name per line whose scripts.inc stays assembled (skip-scripts)')
a = ap.parse_args()
ROOT = a.root
REAL = os.path.realpath(ROOT) == os.path.realpath('/home/user/Veldris')
if REAL and (a.step == 'restore' or not os.environ.get('PURGE_ALLOW_REAL_REPO')):
    # restore is destructive (git checkout of data/ tools/ src/ include/) and is never allowed on the real repo;
    # the other steps only run there when the lead sets PURGE_ALLOW_REAL_REPO=1 after the author has approved a level.
    sys.exit('refusing to run in /home/user/Veldris (set PURGE_ALLOW_REAL_REPO=1 for the non-destructive steps once approved)')

def load():
    maps = {}
    for p in glob.glob(os.path.join(ROOT, 'data/maps/*/map.json')):
        d = json.load(open(p))
        maps[d['name']] = d
    mg = json.load(open(os.path.join(ROOT, 'data/maps/map_groups.json')))
    return maps, mg

maps, mg = load()
keep = set(VELDRIS) | {x for x in a.keep.split(',') if x}
hoenn = {n for n, d in maps.items() if d.get('region', 'REGION_HOENN') in ('REGION_HOENN', 'REGION_HOENN_SKIPPED')}
honly = hoenn - keep
group_of = {}
for g in mg['group_order']:
    for m in mg[g]:
        group_of[m] = g
mixed_groups = {group_of[m] for m in keep if m in group_of}
pure_groups = [g for g in mg['group_order'] if mg[g] and all(m in honly or m not in hoenn for m in mg[g]) and any(m in honly for m in mg[g])]

def set_region(name, val):
    p = os.path.join(ROOT, 'data/maps', name, 'map.json')
    t = open(p).read()
    if '"region"' in t:
        t2 = re.sub(r'("region"\s*:\s*)"[A-Z_]+"', r'\1"%s"' % val, t, count=1)
    else:
        t2 = re.sub(r'("layout"\s*:\s*"[A-Z0-9_]+",\n)', r'\1  "region": "%s",\n' % val, t, count=1)
    if t2 != t:
        open(p, 'w').write(t2)
        return 1
    return 0

if a.step == 'list':
    print('Veldris', len(keep & hoenn), 'Hoenn-only', len(honly), 'FRLG', len(set(maps) - hoenn))
    print('groups containing a kept map (cannot be skipped whole):', sorted(mixed_groups))
    print('pure Hoenn groups:', len(pure_groups), 'covering', sum(len([m for m in mg[g] if m in honly]) for g in pure_groups), 'maps')
    print('Hoenn-only maps inside mixed groups:', sum(len([m for m in mg[g] if m in honly]) for g in mixed_groups))

elif a.step == 'tag-maps':
    n = 0
    for g in mg['group_order']:
        if a.scope == 'pure' and g in mixed_groups:
            continue
        for m in mg[g]:
            if m in honly:
                n += set_region(m, 'REGION_HOENN_SKIPPED')
    print('tagged', n, 'maps, scope', a.scope)

elif a.step == 'patch-mapjson':
    p = os.path.join(ROOT, 'tools/mapjson/mapjson.cpp')
    t = open(p).read()
    old = '''        vector<string> valid_maps;
        auto maps = groups_data[group].array_items();
        for (Json &map_name : maps) {
            string map_name_str = json_to_string(map_name);
            auto it = find(invalid_maps.begin(), invalid_maps.end(), map_name_str);
            if (it == invalid_maps.end()) {
                valid_maps.push_back(map_name_str);
            }
        }

        if (valid_maps.size() > 0) {'''
    new = '''        vector<string> valid_maps;
        size_t real_maps = 0;
        auto maps = groups_data[group].array_items();
        for (Json &map_name : maps) {
            string map_name_str = json_to_string(map_name);
            auto it = find(invalid_maps.begin(), invalid_maps.end(), map_name_str);
            if (it == invalid_maps.end()) {
                valid_maps.push_back(map_name_str);
                real_maps++;
            } else {
                // keep the slot so later maps keep their MAP_* numbers
                valid_maps.push_back("NULL");
            }
        }

        if (real_maps > 0) {'''
    if old not in t:
        print('already patched or text differs')
    else:
        open(p, 'w').write(t.replace(old, new))
        print('patched mapjson.cpp')

elif a.step == 'tag-layouts':
    lp = os.path.join(ROOT, 'data/layouts/layouts.json')
    L = json.load(open(lp))
    used = {maps[m]['layout'] for m in maps if m in keep or m not in hoenn and False}
    # layouts used by any kept (Veldris) map or by any Hoenn map that is NOT skipped
    skipped = set()
    for m in honly:
        if json.load(open(os.path.join(ROOT, 'data/maps', m, 'map.json'))).get('region') == 'REGION_HOENN_SKIPPED':
            skipped.add(m)
    live = {d['layout'] for n, d in maps.items() if n not in skipped and d.get('region', 'REGION_HOENN') == 'REGION_HOENN'}
    live |= {maps[m]['layout'] for m in keep if m in maps}
    live |= {x for x in a.keep_layouts.split(',') if x}
    n = 0
    for l in L['layouts']:
        if l and l['id'] not in live and l.get('layout_version', 'emerald') == 'emerald':
            l['layout_version'] = 'skipped'
            n += 1
    json.dump(L, open(lp, 'w'), indent=2)
    open(lp, 'a').write('\n')
    print('tagged', n, 'layouts as skipped;', len(live), 'layouts stay live')

elif a.step == 'skip-scripts':
    p = os.path.join(ROOT, 'data/event_scripts.s')
    lines = open(p).read().split('\n')
    out = []
    inc = re.compile(r'^\s*\.include\s+"data/maps/([^/]+)/scripts.inc"')
    keep_scripts = set(open(a.keep_scripts).read().split()) if a.keep_scripts else set()
    in_frlg = False
    changed = 0
    for ln in lines:
        m = inc.match(ln)
        if m and m.group(1) in honly and m.group(1) not in keep_scripts:
            out.append('.if HOENN_MAP_SCRIPTS\n' + ln + '\n.endif')
            changed += 1
        else:
            out.append(ln)
    # define the switch at the top (0 = skipped)
    txt = '\n'.join(out)
    if '.set HOENN_MAP_SCRIPTS' not in txt:
        txt = txt.replace('\t.include "constants/constants.inc"', '\t.include "constants/constants.inc"\n\t.set HOENN_MAP_SCRIPTS, 0', 1)
    open(p, 'w').write(txt)
    print('wrapped', changed, 'includes')

elif a.step == 'delete-maps':
    n = 0
    for g in mg['group_order']:
        mg[g] = [m for m in mg[g] if m not in honly]
    for m in sorted(honly):
        shutil.rmtree(os.path.join(ROOT, 'data/maps', m), ignore_errors=True)
        n += 1
    json.dump(mg, open(os.path.join(ROOT, 'data/maps/map_groups.json'), 'w'), indent=2)
    open(os.path.join(ROOT, 'data/maps/map_groups.json'), 'a').write('\n')
    print('deleted', n, 'map folders')
    # drop their scripts.inc includes
    p = os.path.join(ROOT, 'data/event_scripts.s')
    inc = re.compile(r'^\s*\.include\s+"data/maps/([^/]+)/scripts.inc"')
    lines = [ln for ln in open(p).read().split('\n') if not (inc.match(ln) and inc.match(ln).group(1) in honly)]
    open(p, 'w').write('\n'.join(lines))

elif a.step == 'delete-layouts':
    lp = os.path.join(ROOT, 'data/layouts/layouts.json')
    L = json.load(open(lp))
    live = {d['layout'] for d in (json.load(open(p)) for p in glob.glob(os.path.join(ROOT, 'data/maps/*/map.json')))}
    keepL = [l for l in L['layouts'] if (not l) or l['id'] in live]
    removed = len(L['layouts']) - len(keepL)
    L['layouts'] = keepL
    json.dump(L, open(lp, 'w'), indent=2)
    open(lp, 'a').write('\n')
    print('removed', removed, 'layouts from layouts.json (kept', len(keepL), ')')

elif a.step == 'delete-frlg':
    frlg = {n for n, d in maps.items() if d.get('region', 'REGION_HOENN') not in ('REGION_HOENN', 'REGION_HOENN_SKIPPED')}
    for g in mg['group_order']:
        mg[g] = [m for m in mg[g] if m not in frlg]
    for m in sorted(frlg):
        shutil.rmtree(os.path.join(ROOT, 'data/maps', m), ignore_errors=True)
    json.dump(mg, open(os.path.join(ROOT, 'data/maps/map_groups.json'), 'w'), indent=2)
    open(os.path.join(ROOT, 'data/maps/map_groups.json'), 'a').write('\n')
    p = os.path.join(ROOT, 'data/event_scripts.s')
    inc = re.compile(r'^\s*\.include\s+"data/maps/([^/]+)/scripts.inc"')
    lines = [ln for ln in open(p).read().split('\n') if not (inc.match(ln) and inc.match(ln).group(1) in frlg)]
    open(p, 'w').write('\n'.join(lines))
    if a.layouts:
        lp = os.path.join(ROOT, 'data/layouts/layouts.json')
        L = json.load(open(lp))
        L['layouts'] = [l for l in L['layouts'] if not l or l.get('layout_version', 'emerald') != 'frlg']
        json.dump(L, open(lp, 'w'), indent=2)
        open(lp, 'a').write('\n')
    print('deleted', len(frlg), 'FRLG map folders')

elif a.step == 'delete-listed':
    free = set(json.load(open(a.list))['free'])
    in_skip = set(mg.get(a.skip_group, []))
    gone = sorted((free & honly) - in_skip)
    ids = {maps[m]['id'] for m in gone}
    for g in mg['group_order']:
        mg[g] = [m for m in mg[g] if m not in gone]
    for m in gone:
        shutil.rmtree(os.path.join(ROOT, 'data/maps', m), ignore_errors=True)
    json.dump(mg, open(os.path.join(ROOT, 'data/maps/map_groups.json'), 'w'), indent=2)
    open(os.path.join(ROOT, 'data/maps/map_groups.json'), 'a').write('\n')
    p = os.path.join(ROOT, 'data/event_scripts.s')
    inc = re.compile(r'^\s*\.include\s+"data/maps/([^/]+)/scripts.inc"')
    lines = [ln for ln in open(p).read().split('\n') if not (inc.match(ln) and inc.match(ln).group(1) in gone)]
    open(p, 'w').write('\n'.join(lines))
    wp = os.path.join(ROOT, 'src/data/wild_encounters.json')
    W = json.load(open(wp))
    nrows = 0
    for grp in W['wild_encounter_groups']:
        if grp['label'] == 'gWildMonHeaders':
            before = len(grp['encounters'])
            grp['encounters'] = [e for e in grp['encounters'] if e['map'] not in ids]
            nrows += before - len(grp['encounters'])
    open(wp, 'w').write(json.dumps(W, indent=2) + '\n')
    print('deleted', len(gone), 'map folders and', nrows, 'wild rows; skipped', len((free & honly) & in_skip), 'free maps in', a.skip_group)

elif a.step == 'prune-wild':
    wp = os.path.join(ROOT, 'src/data/wild_encounters.json')
    W = json.load(open(wp))
    ids = {maps[m]['id'] for m in honly}
    n = 0
    for grp in W['wild_encounter_groups']:
        if grp['label'] == 'gWildMonHeaders':
            before = len(grp['encounters'])
            grp['encounters'] = [e for e in grp['encounters'] if e['map'] not in ids]
            n += before - len(grp['encounters'])
    open(wp, 'w').write(json.dumps(W, indent=2) + '\n')
    print('removed', n, 'wild headers of Hoenn-only maps')

elif a.step == 'restore':
    subprocess.run('git checkout -- data tools src include && git clean -fdq data/maps data/layouts', shell=True, cwd=ROOT)
    print('restored')
else:
    sys.exit('unknown step')
