#!/usr/bin/env python3
"""static_refs.py - what in the tree depends on Hoenn-only maps? (read-only analysis)

Usage: static_refs.py [repo_root] [out_dir]

Reads TRACKED files only (git ls-files), builds a token -> files index, then reports:

 1. Map inventory: Veldris (hack-added) maps, Hoenn-only maps, FRLG maps.
 2. For every MAP_* constant of a Hoenn-only map: which files OUTSIDE that map's own
    folder name it (C, shared scripts, wild_encounters, other maps).
 3. For every script label defined in a Hoenn-only map's scripts.inc: which files
    outside Hoenn-only map folders name it (these become undefined references if the
    Hoenn scripts are dropped from data/event_scripts.s).
 4. Flags, vars and trainer ids used ONLY inside Hoenn-only map folders (freeable).
 5. Layout and tileset sharing between Veldris and Hoenn maps.

Writes <out_dir>/static_refs.json and prints a text summary.
Nothing in the repo is modified.
"""
import json, os, re, subprocess, sys, collections

ROOT = sys.argv[1] if len(sys.argv) > 1 else '/home/user/Veldris'
OUT = sys.argv[2] if len(sys.argv) > 2 else '.'

VELDRIS = ['Hollowbrook', 'VeldrisRoute1', 'Crestfall', 'Hollowbrook_PlayersHouse_1F',
           'Hollowbrook_PlayersHouse_2F', 'Hollowbrook_ProfFennickLab', 'Hollowbrook_NeighboursHouse',
           'Crestfall_PokemonCenter_1F', 'Crestfall_Mart', 'Crestfall_HouseA', 'Crestfall_HouseB',
           'Crestfall_Gym']

TOK = re.compile(r'[A-Za-z_][A-Za-z0-9_]*')
TEXT_EXT = ('.c', '.h', '.s', '.inc', '.json', '.mk', '.party', '.txt', '.py', '.sh', '.md', '.ld', '.asm', '.pory')

def sh(cmd):
    return subprocess.run(cmd, shell=True, cwd=ROOT, capture_output=True, text=True, errors='replace').stdout

def main():
    files = [f for f in sh('git ls-files').split('\n') if f]
    # ---- maps
    maps = {}
    for f in files:
        if f.startswith('data/maps/') and f.endswith('/map.json'):
            d = json.load(open(os.path.join(ROOT, f)))
            maps[d['name']] = d
    hoenn = {n for n, d in maps.items() if d.get('region', 'REGION_HOENN') == 'REGION_HOENN'}
    frlg = set(maps) - hoenn
    veld = set(VELDRIS) & hoenn
    honly = hoenn - veld
    print(f'maps: {len(maps)} folders, Hoenn-region {len(hoenn)} (Veldris {len(veld)}, Hoenn-only {len(honly)}), FRLG {len(frlg)}')

    # ---- token index (skip generated/huge junk by extension)
    index = collections.defaultdict(set)
    texts = {}
    for f in files:
        if not f.endswith(TEXT_EXT):
            continue
        if f.startswith(('graphics/', 'sound/songs/midi', 'tools/', 'docs/', 'build/', 'migration_scripts/', 'dev_scripts/')):
            continue
        p = os.path.join(ROOT, f)
        try:
            if os.path.getsize(p) > 8_000_000:
                continue
            t = open(p, errors='replace').read()
        except OSError:
            continue
        for tok in set(TOK.findall(t)):
            index[tok].add(f)
        texts[f] = None  # remember we saw it

    def in_map_dir(f, names):
        parts = f.split('/')
        return len(parts) > 3 and parts[0] == 'data' and parts[1] == 'maps' and parts[2] in names

    GENERATED_LISTS = {'include/constants/map_groups.h', 'include/constants/layouts.h',
                       'include/constants/map_event_ids.h'}

    report = {}

    # ---- 2. MAP_ constants
    mapref = {}
    for n in sorted(honly):
        cid = maps[n]['id']
        refs = sorted(f for f in index.get(cid, ())
                      if not in_map_dir(f, {n}) and f not in GENERATED_LISTS
                      and f not in ('data/maps/map_groups.json',) and not f.startswith('design/'))
        if refs:
            mapref[cid] = refs
    report['hoenn_map_const_refs'] = mapref
    # split by kind
    kinds = collections.Counter()
    byfile = collections.Counter()
    for cid, refs in mapref.items():
        for f in refs:
            if f.startswith('src/') or f.startswith('include/'):
                kinds['C/headers'] += 1
            elif f.startswith('data/maps/'):
                kinds['other map folders'] += 1
            elif f.startswith('data/scripts') or f.startswith('data/text') or f.startswith('data/event_scripts') or f.startswith('data/specials') :
                kinds['shared scripts/text'] += 1
            elif f.startswith('test/'):
                kinds['tests'] += 1
            else:
                kinds['other'] += 1
            byfile[f] += 1
    print('\nMAP_* constants of Hoenn-only maps referenced outside their own folder:')
    print(f'  {len(mapref)} constants referenced; (constant, file) pairs by kind: {dict(kinds)}')
    print('  files with most such references:')
    for f, c in byfile.most_common(25):
        print(f'    {c:4d}  {f}')

    # ---- 3. script labels defined in Hoenn-only maps
    LABEL = re.compile(r'^([A-Za-z_][A-Za-z0-9_]*)::?', re.M)
    labels = {}
    for n in honly:
        p = os.path.join(ROOT, 'data/maps', n, 'scripts.inc')
        if os.path.exists(p):
            t = open(p, errors='replace').read()
            for m in LABEL.finditer(t):
                labels[m.group(1)] = n
    print(f'\nscript labels defined in Hoenn-only map scripts.inc: {len(labels)}')
    labref = collections.defaultdict(set)
    for lab, n in labels.items():
        for f in index.get(lab, ()):
            if in_map_dir(f, honly) or in_map_dir(f, frlg):
                continue  # Hoenn-to-Hoenn references vanish together
            if f == 'data/event_scripts.s':
                continue
            labref[f].add(lab)
    report['hoenn_label_refs_outside'] = {f: sorted(v) for f, v in labref.items()}
    print('  files OUTSIDE Hoenn-only maps that name those labels:')
    for f, v in sorted(labref.items(), key=lambda kv: -len(kv[1]))[:40]:
        print(f'    {len(v):4d}  {f}  e.g. {sorted(v)[:3]}')

    # also: which Hoenn-only map folders' generated events reference script labels of... skip

    # ---- 4. flags / vars / trainers only used inside Hoenn-only maps
    const_re = {
        'FLAG': re.compile(r'^#define\s+(FLAG_[A-Za-z0-9_]+)\s', re.M),
        'VAR': re.compile(r'^#define\s+(VAR_[A-Za-z0-9_]+)\s', re.M),
        'TRAINER': re.compile(r'^#define\s+(TRAINER_[A-Za-z0-9_]+)\s', re.M),
    }
    defs = {'FLAG': 'include/constants/flags.h', 'VAR': 'include/constants/vars.h', 'TRAINER': 'include/constants/opponents.h'}
    freeable = {}
    for kind, hdr in defs.items():
        t = open(os.path.join(ROOT, hdr)).read()
        names = const_re[kind].findall(t)
        only = []
        used_hoenn_only = []
        unref = []
        for nme in names:
            fs = index.get(nme, set()) - {hdr}
            # other constants headers that alias it do not count as uses, but we keep them visible
            real = {f for f in fs if f not in ('include/constants/flags_frlg.h', 'include/constants/vars_frlg.h')}
            if not real:
                unref.append(nme)
                continue
            if all(in_map_dir(f, honly) or in_map_dir(f, frlg) for f in real):
                used_hoenn_only.append(nme)
        freeable[kind] = {'total_names': len(names), 'unreferenced_anywhere': len(unref),
                          'used_only_in_hoenn_or_frlg_map_folders': len(used_hoenn_only),
                          'used_only_in_hoenn_only_folders_names': used_hoenn_only}
    report['freeable'] = {k: {kk: vv for kk, vv in v.items() if kk != 'used_only_in_hoenn_only_folders_names'} for k, v in freeable.items()}
    report['freeable_names'] = {k: v['used_only_in_hoenn_only_folders_names'] for k, v in freeable.items()}
    print('\nconstants whose ONLY uses are inside Hoenn-only (or FRLG) map folders:')
    for k, v in report['freeable'].items():
        print(f'  {k}: {v}')

    # ---- 5. layouts & tilesets
    lay = {l['id']: l for l in json.load(open(os.path.join(ROOT, 'data/layouts/layouts.json')))['layouts'] if l}
    lay_users = collections.defaultdict(list)
    for n, d in maps.items():
        lay_users[d['layout']].append(n)
    shared = {}
    for lid, users in lay_users.items():
        if set(users) & veld and set(users) & honly:
            shared[lid] = sorted(users)
    print('\nlayouts shared between Veldris and Hoenn-only maps:', {k: len(v) for k, v in shared.items()})
    tilesets_v = set()
    for n in veld:
        l = lay[maps[n]['layout']]
        tilesets_v.add(l['primary_tileset'])
        tilesets_v.add(l['secondary_tileset'])
    tilesets_h = collections.defaultdict(set)
    for n in honly:
        l = lay[maps[n]['layout']]
        tilesets_h[l['primary_tileset']].add(n)
        tilesets_h[l['secondary_tileset']].add(n)
    print('Veldris tilesets:', sorted(tilesets_v))
    only_h_tilesets = sorted(t for t in tilesets_h if t not in tilesets_v)
    print(f'tilesets used only by Hoenn-only/other maps (candidates, not counting FRLG): {len(only_h_tilesets)}')
    report['layout_shared'] = shared
    report['veldris_tilesets'] = sorted(tilesets_v)
    report['hoenn_only_tilesets'] = only_h_tilesets
    # layouts used by no Veldris map at all
    veld_layouts = {maps[n]['layout'] for n in veld}
    h_layouts = {maps[n]['layout'] for n in honly} - veld_layouts
    f_layouts = {maps[n]['layout'] for n in frlg} - veld_layouts - h_layouts
    report['layout_counts'] = {'veldris_used': len(veld_layouts), 'hoenn_only_layouts': len(h_layouts),
                               'frlg_only_layouts': len(f_layouts), 'total_layouts': len(lay)}
    print('layouts: ', report['layout_counts'])

    report['maps'] = {'veldris': sorted(veld), 'hoenn_only': sorted(honly), 'frlg': sorted(frlg)}
    json.dump(report, open(os.path.join(OUT, 'static_refs.json'), 'w'), indent=1)

if __name__ == '__main__':
    main()
