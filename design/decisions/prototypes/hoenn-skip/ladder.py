#!/usr/bin/env python3
"""ladder.py : print the ROM ladder (bytes used, saved, free of 32 MiB) from the build_stage.sh / resolve_undefined.py results."""
import json, re, os
H = os.path.dirname(os.path.abspath(__file__)) + '/results/'
BASE = 26822384
def rom(f):
    t = open(H + f).read()
    m = re.search(r'rom_used_bytes (\d+)', t)
    return int(m.group(1)) if m else None
rows = [
 ('A  leave as is (HEAD e250a8e6)', BASE),
 ('B0 tag the 461 Hoenn maps in pure-Hoenn groups (stock tool)', rom('s1_tag_pure.time')),
 ('B0+ B0 + skip the 383 layouts only skipped maps use (stock tool)', rom('s1b_tag_pure_layouts.time')),
 ('B1 all 518 Hoenn-only maps + 440 layouts, 7-line mapjson patch (NULL slots)', rom('s2_tag_all_patch_layouts.time')),
 ('B2 B1 + do not assemble 428 Hoenn map scripts (40 stay, C needs them)', json.load(open(H + 's3_resolve-result.json'))['history'][-1][2]),
 ('B3 B2 + drop the C data of 87 dead tilesets', rom('s4_tilesets_pruned.time')),
 ('B4 B3 + drop the 124 Hoenn rows of gWildMonHeaders', rom('s6_optionB_plus_wild_pruned.time')),
 ('--- variants ---', None),
 ('L1 apply_skip.sh level 1 (templates live)', rom('level1_apply_skip_default.time')),
 ('L2 apply_skip.sh level 2 (+ scripts not assembled)', rom('level2_apply_skip_default.time')),
 ('R  RECOMMENDED SKIP level 3 (apply_skip.sh 3 + Battle Tower kept): templates live, no tileset pruning', rom('r1_recommended_level3_keep_templates_and_battle_tower.time')),
 ('H  hybrid: B2 + physically delete 253 unreferenced Hoenn maps + 421 FRLG folders (no tileset pruning)', rom('h1_hybrid_delete_free_skip_rest.time')),
 ('F  only delete the 421 FRLG map folders (zero code edits)', rom('f2_delete_frlg_keep_layouts.time')),
]
print('| step | ROM used (bytes) | saved vs HEAD | free of 32 MiB |')
print('|---|---:|---:|---:|')
for n, r in rows:
    if r is None:
        print('| %s | | | |' % n); continue
    print('| %s | %s | %s | %.3f MiB |' % (n, format(r, ','), format(BASE - r, ',') if r != BASE else '0', (33554432 - r) / 1048576))

print()
print('Re-measured on the current HEAD 04385f05 (author imported 70 overworld sprites and 94 battle pictures in between, +238,108 bytes):')
b2 = rom('baseline_newhead.time'); r2 = rom('newhead_r_level3_bt.time')
print('| step | ROM used (bytes) | saved | free of 32 MiB |')
print('|---|---:|---:|---:|')
print('| A leave as is (HEAD 04385f05) | %s | 0 | %.3f MiB |' % (format(b2, ','), (33554432 - b2) / 1048576))
print('| R recommended SKIP (apply_skip.sh 3, Battle Tower kept) | %s | %s | %.3f MiB |' % (format(r2, ','), format(b2 - r2, ','), (33554432 - r2) / 1048576))
