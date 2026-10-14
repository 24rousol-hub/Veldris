#!/usr/bin/env python3
"""rom_by_map.py - what do the Hoenn maps cost in ROM bytes?  (read-only analysis)

Usage: rom_by_map.py <repo_root> <syms.tsv from rom_symbols.py> <out_dir>

Attributes ROM bytes to:
  * map scripts+text      each `.include "data/maps/X/scripts.inc"` span in data/event_scripts.s
  * shared scripts/text   each `.include "data/scripts/*.inc"` / `data/text/*.inc` span
  * map headers/events    labels <Map>, <Map>_MapConnections, <Map>_ObjectEvents, ... in data/maps.o and data/map_events.o
  * layouts               <Layout>, _Border, _Blockdata in data/maps.o
  * tilesets              gTileset_X, gTilesetTiles_X, gTilesetPalettes_X, gMetatiles_X, gMetatileAttributes_X

Then rolls up by map group family and by Veldris / Hoenn-only.  Writes
  <out_dir>/rom_by_map.json   (full breakdown)
and prints a summary.
"""
import json, os, re, sys, glob, collections

ROOT, SYMS, OUT = sys.argv[1:4]

VELDRIS = ['Hollowbrook', 'VeldrisRoute1', 'Crestfall', 'Hollowbrook_PlayersHouse_1F',
           'Hollowbrook_PlayersHouse_2F', 'Hollowbrook_ProfFennickLab', 'Hollowbrook_NeighboursHouse',
           'Crestfall_PokemonCenter_1F', 'Crestfall_Mart', 'Crestfall_HouseA', 'Crestfall_HouseB',
           'Crestfall_Gym']

rows = []
addr_of = {}
for line in open(SYMS):
    a, sz, obj, sec, n = line.rstrip('\n').split('\t')
    rows.append((int(a, 16), int(sz), obj, sec, n))
    addr_of.setdefault(n, int(a, 16))

maps = {}
for p in glob.glob(os.path.join(ROOT, 'data/maps/*/map.json')):
    d = json.load(open(p))
    maps[d['name']] = d
groups = json.load(open(os.path.join(ROOT, 'data/maps/map_groups.json')))
group_of = {}
for g in groups['group_order']:
    for m in groups[g]:
        group_of[m] = g
layouts = {l['id']: l for l in json.load(open(os.path.join(ROOT, 'data/layouts/layouts.json')))['layouts'] if l}
layout_by_name = {l['name']: l for l in layouts.values()}
hoenn = {n for n, d in maps.items() if d.get('region', 'REGION_HOENN') == 'REGION_HOENN'}
veld = set(VELDRIS)
honly = hoenn - veld

# ---------------- event_scripts.o: include spans
es_rows = [r for r in rows if r[2].endswith('data/event_scripts.o') or r[2] == 'build/emerald/data/event_scripts.o']
es_start = min(r[0] for r in es_rows)
es_end = max(r[0] + r[1] for r in es_rows)
es_bytes = es_end - es_start  # includes script_data? (script_data is a separate input section)

src = open(os.path.join(ROOT, 'data/event_scripts.s'), errors='replace').read().split('\n')
inc_re = re.compile(r'^\s*\.include\s+"([^"]+)"')
lab_re = re.compile(r'^([A-Za-z_][A-Za-z0-9_]*)::?')
depth = 0
skip_stack = []
includes = []
for line in src:
    s = line.strip()
    if s.startswith('.if '):
        # only IS_FRLG blocks matter here (value 0 in this build)
        skip_stack.append('IS_FRLG' in s and '!' not in s)
        continue
    if s.startswith('.endif'):
        if skip_stack:
            skip_stack.pop()
        continue
    if s.startswith('.else'):
        if skip_stack:
            skip_stack[-1] = not skip_stack[-1]
        continue
    if any(skip_stack):
        continue
    m = inc_re.match(line)
    if m:
        includes.append(m.group(1))

def first_label(path):
    p = os.path.join(ROOT, path)
    if not os.path.exists(p):
        return None
    for line in open(p, errors='replace'):
        m = lab_re.match(line)
        if m and m.group(1) in addr_of:
            return m.group(1)
    return None

starts = []
for inc in includes:
    if not (inc.startswith('data/maps/') or inc.startswith('data/scripts/') or inc.startswith('data/text/')):
        continue
    lab = first_label(inc)
    if lab and es_start <= addr_of[lab] < es_end + 0x400000:
        starts.append((addr_of[lab], inc))
starts.sort()
# script_data input section may live outside the event_scripts .rodata window; use all event_scripts.o rows
all_es = sorted(r for r in rows if 'event_scripts.o' in r[2])
span = {}
for i, (a, inc) in enumerate(starts):
    nxt = starts[i + 1][0] if i + 1 < len(starts) else None
    # bytes of event_scripts.o symbols between a and nxt
    tot = 0
    for r in all_es:
        if r[0] >= a and (nxt is None or r[0] < nxt):
            tot += r[1]
    span[inc] = tot
map_script_bytes = {}
shared_script_bytes = {}
for inc, b in span.items():
    if inc.startswith('data/maps/'):
        map_script_bytes[inc.split('/')[2]] = b
    else:
        shared_script_bytes[inc] = b
es_total = sum(r[1] for r in all_es)
unattributed_es = es_total - sum(span.values())

# ---------------- maps.o / map_events.o by label
map_names_sorted = sorted(maps, key=len, reverse=True)
def map_of_label(lab):
    # longest map name that is the label or a prefix followed by '_'
    parts = lab.split('_')
    for k in range(len(parts), 0, -1):
        cand = '_'.join(parts[:k])
        if cand in maps:
            return cand
    return None

hdr_bytes = collections.Counter()
ev_bytes = collections.Counter()
conn_bytes = collections.Counter()
lay_bytes = collections.Counter()
other_maps_o = collections.Counter()
for a, sz, obj, sec, n in rows:
    if obj.endswith('data/maps.o'):
        base = n
        for suf in ('_Blockdata', '_Border'):
            if n.endswith(suf):
                base = n[:-len(suf)]
        if base in layout_by_name:
            lay_bytes[base] += sz
        elif n in maps:
            hdr_bytes[n] += sz
        elif n.endswith('_MapConnections') and n[:-len('_MapConnections')] in maps:
            conn_bytes[n[:-len('_MapConnections')]] += sz
        else:
            m = map_of_label(n)
            if m:
                conn_bytes[m] += sz
            else:
                other_maps_o[n] += sz
    elif obj.endswith('data/map_events.o'):
        m = map_of_label(n)
        if m:
            ev_bytes[m] += sz
        else:
            other_maps_o[n] += sz

# ---------------- layouts -> users
lay_users = collections.defaultdict(list)
for n, d in maps.items():
    lay_users[layouts[d['layout']]['name']].append(n)

# ---------------- tilesets
tile_prefixes = ['gTileset_', 'gTilesetTiles_', 'gTilesetPalettes_', 'gMetatiles_', 'gMetatileAttributes_']
tile_bytes = collections.Counter()
for a, sz, obj, sec, n in rows:
    for p in tile_prefixes:
        if n.startswith(p):
            tile_bytes[n[len(p):]] += sz
            break

# ---------------- rollups
def fam(m):
    g = group_of.get(m, '?')
    return g.replace('gMapGroup_', '')

per_map = {}
for m in maps:
    per_map[m] = {'scripts_text': map_script_bytes.get(m, 0), 'header': hdr_bytes.get(m, 0),
                  'events': ev_bytes.get(m, 0), 'connections': conn_bytes.get(m, 0)}
    per_map[m]['total_excl_layout'] = sum(per_map[m].values())

# layout cost: exclusive to Hoenn-only vs shared with Veldris
lay_class = {'hoenn_only': 0, 'shared_with_veldris': 0, 'veldris_only': 0, 'frlg_only_in_rom': 0}
lay_detail = {}
for name, b in lay_bytes.items():
    users = lay_users.get(name, [])
    u_h = [u for u in users if u in honly]
    u_v = [u for u in users if u in veld]
    u_f = [u for u in users if u not in hoenn]
    if u_v and u_h:
        c = 'shared_with_veldris'
    elif u_v:
        c = 'veldris_only'
    elif u_h:
        c = 'hoenn_only'
    else:
        c = 'frlg_only_in_rom'
    lay_class[c] += b
    lay_detail[name] = {'bytes': b, 'class': c, 'users': len(users)}

# tilesets: which are used by Veldris layouts / only Hoenn layouts / only FRLG
ts_users = collections.defaultdict(set)
for lid, l in layouts.items():
    users = lay_users.get(l['name'], [])
    for t in (l['primary_tileset'], l['secondary_tileset']):
        for u in users:
            ts_users[t.replace('gTileset_', '')].add(u)
ts_class = collections.defaultdict(int)
ts_detail = {}
for t, b in tile_bytes.items():
    users = ts_users.get(t, set())
    if users & veld:
        c = 'used_by_veldris'
    elif users & honly:
        c = 'hoenn_only'
    elif users:
        c = 'frlg_only'
    else:
        c = 'unreferenced_by_any_layout'
    ts_class[c] += b
    ts_detail[t] = {'bytes': b, 'class': c}

fam_tot = collections.defaultdict(lambda: collections.Counter())
fam_count = collections.Counter()
for m in honly:
    f = fam(m)
    fam_count[f] += 1
    for k, v in per_map[m].items():
        fam_tot[f][k] += v

summary = {
    'event_scripts_o_total': es_total,
    'event_scripts_unattributed': unattributed_es,
    'hoenn_only_map_scripts_text': sum(map_script_bytes.get(m, 0) for m in honly),
    'veldris_map_scripts_text': sum(map_script_bytes.get(m, 0) for m in veld),
    'shared_scripts_text_total': sum(shared_script_bytes.values()),
    'hoenn_only_headers': sum(hdr_bytes.get(m, 0) for m in honly),
    'hoenn_only_events': sum(ev_bytes.get(m, 0) for m in honly),
    'hoenn_only_connections': sum(conn_bytes.get(m, 0) for m in honly),
    'veldris_headers_events_conn': sum(hdr_bytes.get(m, 0) + ev_bytes.get(m, 0) + conn_bytes.get(m, 0) for m in veld),
    'layouts_in_rom_total': sum(lay_bytes.values()),
    'layouts_by_class': lay_class,
    'tilesets_total': sum(tile_bytes.values()),
    'tilesets_by_class': dict(ts_class),
}
print(json.dumps(summary, indent=1))
print('\nHoenn-only maps by family (map count, scripts+text, header, events, connections):')
for f, c in sorted(fam_tot.items(), key=lambda kv: -sum(kv[1].values())):
    print(f'  {f:34s} {fam_count[f]:4d} maps  scripts {c["scripts_text"]:9,}  hdr {c["header"]:7,}  ev {c["events"]:8,}  conn {c["connections"]:6,}')
print('\nshared script/text files over 8 KB:')
for inc, b in sorted(shared_script_bytes.items(), key=lambda kv: -kv[1]):
    if b > 8000:
        print(f'  {b:9,}  {inc}')
print('\nbiggest Hoenn-only tilesets:')
for t, d in sorted(ts_detail.items(), key=lambda kv: -kv[1]['bytes'])[:12]:
    print(f'  {d["bytes"]:9,}  {d["class"]:28s} {t}')
print('\nbiggest Hoenn-only layouts:')
for t, d in sorted(((k, v) for k, v in lay_detail.items() if v['class'] == 'hoenn_only'), key=lambda kv: -kv[1]['bytes'])[:8]:
    print(f'  {d["bytes"]:9,}  {t}')

json.dump({'summary': summary, 'per_map': per_map, 'shared_scripts': shared_script_bytes,
           'layouts': lay_detail, 'tilesets': ts_detail,
           'family_totals': {f: dict(c, maps=fam_count[f]) for f, c in fam_tot.items()}},
          open(os.path.join(OUT, 'rom_by_map.json'), 'w'), indent=1)
