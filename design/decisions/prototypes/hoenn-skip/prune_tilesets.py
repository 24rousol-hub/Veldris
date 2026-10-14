#!/usr/bin/env python3
"""prune_tilesets.py - experiment: drop the C data of tilesets no live layout uses.

Usage: prune_tilesets.py <clone_root> [--dry-run] [--keep=gTileset_Cave,gTileset_Facility,...]

Run AFTER `purge_experiment.py tag-layouts` (layouts of skipped maps carry
"layout_version": "skipped").  A tileset is DEAD when
  * no live ("emerald") layout names it as primary or secondary tileset, and
  * no C file or header outside src/data/tilesets/ and src/tileset_anims.c names it
    (decoration.c needs gTileset_SecretBase*, for example, so those stay).
Then, in src/data/tilesets/{headers,graphics,metatiles}.h:
  1. the `const struct Tileset gTileset_X = {...};` block and gTilesetPointer_X line go,
  2. every top-level statement (tiles, palettes, metatiles, attributes arrays) whose
     identifier is no longer named by any remaining statement or outside file goes,
     repeated until stable.
Prints bytes of source removed and the list of dead tilesets.  It never touches
/home/user/Veldris.
"""
import json, os, re, sys, glob, collections

ROOT = sys.argv[1]
DRY = '--dry-run' in sys.argv
KEEP_TS = set()
for _a in sys.argv:
    if _a.startswith('--keep='):
        KEEP_TS |= {x for x in _a[7:].split(',') if x}   # gTileset_ names the author still wants to draw with
if os.path.realpath(ROOT) == os.path.realpath('/home/user/Veldris') and not os.environ.get('PURGE_ALLOW_REAL_REPO'):
    sys.exit('refusing to run in /home/user/Veldris (set PURGE_ALLOW_REAL_REPO=1 once the author has approved a level)')

TS = os.path.join(ROOT, 'src/data/tilesets')
files = {n: open(os.path.join(TS, n)).read() for n in ('headers.h', 'graphics.h', 'metatiles.h')}

L = json.load(open(os.path.join(ROOT, 'data/layouts/layouts.json')))['layouts']
live = set()
for l in L:
    if l and l.get('layout_version', 'emerald') == 'emerald':
        live.add(l['primary_tileset'])
        live.add(l['secondary_tileset'])

defined = re.findall(r'const struct Tileset (gTileset_\w+)\s*=', files['headers.h'])
TOK = re.compile(r'[A-Za-z_]\w*')
outside = set()
SKIP_HDR = {'include/tilesets.h', 'include/constants/metatile_labels.h'}   # these only declare / label, not use
for p in glob.glob(os.path.join(ROOT, 'src/**/*.[ch]'), recursive=True) + glob.glob(os.path.join(ROOT, 'include/**/*.h'), recursive=True):
    rel = os.path.relpath(p, ROOT)
    if rel.startswith('src/data/tilesets/') or rel == 'src/tileset_anims.c' or rel in SKIP_HDR:
        continue
    outside |= set(TOK.findall(open(p, errors='replace').read()))

dead = [t for t in defined if t not in live and t not in KEEP_TS and t not in outside and t.replace('gTileset_', 'gTilesetPointer_') not in outside]
keep = [t for t in defined if t not in dead]
print(f'{len(defined)} tilesets defined, {len(live)} live in layouts, {len(dead)} dead, {len(keep)} kept')

h = files['headers.h']
before = sum(len(v) for v in files.values())
for t in dead:
    h = re.sub(r'const struct Tileset %s\s*=\s*\{.*?\};\n\n?' % re.escape(t), '', h, flags=re.S)
    ptr = t.replace('gTileset_', 'gTilesetPointer_')
    h = re.sub(r'const struct Tileset \*const %s\s*=\s*&%s;\n' % (re.escape(ptr), re.escape(t)), '', h)
files['headers.h'] = h

def split_statements(text):
    """split into (kind, text) chunks: ('pp', line) or ('stmt', text) or ('ws', text)"""
    out = []
    i, n = 0, len(text)
    cur = []
    depth = 0
    lines = text.split('\n')
    buf = []
    for ln in lines:
        s = ln.strip()
        if depth == 0 and not buf and s.startswith('#'):
            out.append(('pp', ln + '\n'))
            continue
        if depth == 0 and not buf and (s == '' or s.startswith('//')):
            out.append(('ws', ln + '\n'))
            continue
        buf.append(ln)
        depth += ln.count('{') - ln.count('}')
        if depth == 0 and ln.rstrip().endswith(';'):
            out.append(('stmt', '\n'.join(buf) + '\n'))
            buf = []
    if buf:
        out.append(('stmt', '\n'.join(buf) + '\n'))
    return out

IDENT = re.compile(r'(?:const\s+)?(?:struct\s+\w+|u8|u16|u32|s8|s16|s32)\s+\*?(?:const\s+)?(\w+)')
chunks = {n: split_statements(files[n]) for n in files}
removed = collections.Counter()
changed = True
rounds = 0
while changed:
    changed = False
    rounds += 1
    # token sets per statement
    toks = []
    for n in chunks:
        for k, c in enumerate(chunks[n]):
            if c[0] == 'stmt':
                toks.append((n, k, set(TOK.findall(c[1]))))
    count = collections.Counter()
    for n, k, ts in toks:
        for t in ts:
            count[t] += 1
    for n, k, ts in toks:
        c = chunks[n][k]
        if c[0] != 'stmt':
            continue
        m = IDENT.search(c[1])
        if not m:
            continue
        name = m.group(1)
        # global structure refs: the Tileset structs themselves are referenced by layouts.inc (asm),
        # so only drop non-struct arrays here; struct blocks were handled above
        if c[1].lstrip().startswith('const struct'):
            continue
        if count[name] <= 1 and name not in outside:
            chunks[n][k] = ('ws', '')
            removed[name.split('_')[0]] += len(c[1])
            changed = True
after = 0
for n in files:
    txt = ''.join(c[1] for c in chunks[n])
    txt = re.sub(r'\n{3,}', '\n\n', txt)
    files[n] = txt
    after += len(txt)
print(f'source text {before} -> {after} bytes; rounds {rounds}; removed arrays by prefix: {dict(removed)}')
if not DRY:
    for n, txt in files.items():
        open(os.path.join(TS, n), 'w').write(txt)
    print('written')
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dead_tilesets.txt'), 'w').write('\n'.join(dead) + '\n')
