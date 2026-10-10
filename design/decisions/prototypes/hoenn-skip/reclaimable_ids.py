#!/usr/bin/env python3
"""reclaimable_ids.py - which flags, vars and trainer ids are held ONLY by Hoenn-only maps?

Usage: reclaimable_ids.py [repo_root] [out_dir]        (read-only; works on any checkout)

Why: design/flags.md counts only names called FLAG_UNUSED_* / VAR_UNUSED_* as spare.
A flag used only by a Hoenn map the player can never reach is just as free in practice,
and so is a vanilla trainer id nobody fights.  This script counts them BY VALUE
(aliases share a value), using the C preprocessor to get the real numbers.

A value counts as RECLAIMABLE when every name that has that value is referenced
only from (a) include/constants/*.h definitions, (b) Hoenn-only or FRLG map folders,
(c) src/data/trainers.party / opponents.h (trainers only), or not at all.
A value counts as IN USE when any name is referenced by C code, shared scripts or text,
tests, a Veldris map, the tracked hack files, or is in a special block.

Writes reclaimable_flags.txt, reclaimable_vars.txt, reclaimable_trainers.txt and a JSON summary.
"""
import json, os, re, subprocess, sys, glob, collections, tempfile

ROOT = sys.argv[1] if len(sys.argv) > 1 else '/home/user/Veldris'
OUT = sys.argv[2] if len(sys.argv) > 2 else '.'

VELDRIS = {'Hollowbrook', 'VeldrisRoute1', 'Crestfall', 'Hollowbrook_PlayersHouse_1F', 'Hollowbrook_PlayersHouse_2F',
           'Hollowbrook_ProfFennickLab', 'Hollowbrook_NeighboursHouse', 'Crestfall_PokemonCenter_1F', 'Crestfall_Mart',
           'Crestfall_HouseA', 'Crestfall_HouseB', 'Crestfall_Gym'}

def sh(cmd, **kw):
    return subprocess.run(cmd, shell=True, cwd=ROOT, capture_output=True, text=True, errors='replace', **kw).stdout

files = [f for f in sh('git ls-files').split('\n') if f]

# --- map classification
region = {}
for f in files:
    if f.startswith('data/maps/') and f.endswith('/map.json'):
        d = json.load(open(os.path.join(ROOT, f)))
        region[d['name']] = d.get('region', 'REGION_HOENN')
honly = {n for n, r in region.items() if r == 'REGION_HOENN' and n not in VELDRIS}
frlg = {n for n, r in region.items() if r != 'REGION_HOENN'}

def map_dir(f):
    p = f.split('/')
    return p[2] if len(p) > 3 and p[0] == 'data' and p[1] == 'maps' else None

# --- token index
TOK = re.compile(r'[A-Za-z_][A-Za-z0-9_]*')
EXT = ('.c', '.h', '.s', '.inc', '.json', '.mk', '.party', '.txt', '.py', '.sh')
index = collections.defaultdict(set)
for f in files:
    if not f.endswith(EXT) or f.startswith(('graphics/', 'tools/', 'docs/', 'migration_scripts/', 'dev_scripts/', 'design/')):
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

DEF_FILES = {'include/constants/flags.h', 'include/constants/vars.h', 'include/constants/opponents.h',
             'include/constants/flags_frlg.h', 'include/constants/vars_frlg.h', 'include/constants/rematches.h'}

def names_in(hdr, prefix):
    t = open(os.path.join(ROOT, hdr)).read()
    return re.findall(r'^#define\s+(%s[A-Za-z0-9_]*)\b' % prefix, t, re.M)

def evaluate(names, includes):
    src = ''.join('#include "%s"\n' % i for i in includes)
    src += ''.join('ZZ_%s ZZ_END %s\n' % (n, n) for n in names)
    r = subprocess.run(['arm-none-eabi-gcc', '-E', '-P', '-I', os.path.join(ROOT, 'include'), '-DEMERALD', '-DMODERN=1', '-x', 'c', '-'],
                       input=src, capture_output=True, text=True, cwd=ROOT)
    vals = {}
    for line in r.stdout.split('\n'):
        m = re.match(r'ZZ_(\w+) ZZ_END\s+(.*)$', line)
        if not m:
            continue
        expr = m.group(2).strip()
        if re.fullmatch(r'[0-9a-fA-FxX+\-*/() <>|&~]+', expr):
            try:
                vals[m.group(1)] = int(eval(expr.replace('/', '//')))
            except Exception:
                pass
    return vals

def classify(name):
    """returns (class, nrefs). class in USED, HOENN_ONLY, NONE"""
    fs = index.get(name, set()) - DEF_FILES
    if not fs:
        return 'NONE'
    for f in fs:
        d = map_dir(f)
        if d is not None and (d in honly or d in frlg):
            continue
        if f in ('src/data/trainers.party',):
            continue
        return 'USED'
    return 'HOENN_ONLY'

summary = {}
# ---------- flags
fl_names = names_in('include/constants/flags.h', 'FLAG_')
fl_vals = evaluate(fl_names, ['constants/flags.h'])
byval = collections.defaultdict(list)
for n, v in fl_vals.items():
    byval[v].append(n)

def block(v):
    if v < 0x20: return 'temp'
    if v < 0x500: return 'story/event/item'
    if v < 0x860: return 'trainer'
    if v < 0x920: return 'system'
    if v < 0x960: return 'daily'
    return 'other'

rows = []
cnt = collections.Counter()
spare_cnt = collections.Counter()
hidden = collections.Counter()
for v in sorted(byval):
    ns = byval[v]
    if v >= 0x4000:
        continue
    cls = [classify(n) for n in ns]
    all_unused_names = all(n.startswith('FLAG_UNUSED') for n in ns)
    if 'USED' in cls:
        c = 'IN_USE'
    elif 'HOENN_ONLY' in cls:
        c = 'HOENN_ONLY'
    else:
        c = 'NAMED_BUT_UNREFERENCED' if not all_unused_names else 'SPARE_BY_NAME'
    b = block(v)
    cnt[(b, c)] += 1
    rows.append((v, b, c, ns))
summary['flags'] = {f'{b}:{c}': n for (b, c), n in sorted(cnt.items())}
with open(os.path.join(OUT, 'reclaimable_flags.txt'), 'w') as f:
    f.write('# value  block  class  names   (class HOENN_ONLY = reclaimable once Hoenn is purged or declared dead)\n')
    for v, b, c, ns in rows:
        if c in ('HOENN_ONLY', 'NAMED_BUT_UNREFERENCED'):
            f.write(f'0x{v:03X}\t{b}\t{c}\t{" ".join(ns)}\n')

# ---------- vars
va_names = names_in('include/constants/vars.h', 'VAR_')
va_vals = evaluate(va_names, ['constants/vars.h'])
vby = collections.defaultdict(list)
for n, v in va_vals.items():
    vby[v].append(n)
vcnt = collections.Counter()
vrows = []
for v in sorted(vby):
    ns = vby[v]
    if not (0x4000 <= v <= 0x40FF):
        continue
    cls = [classify(n) for n in ns]
    all_unused = all(n.startswith('VAR_UNUSED') for n in ns)
    if v < 0x4010:
        c = 'TEMP'
    elif 'USED' in cls:
        c = 'IN_USE'
    elif 'HOENN_ONLY' in cls:
        c = 'HOENN_ONLY'
    else:
        c = 'SPARE_BY_NAME' if all_unused else 'NAMED_BUT_UNREFERENCED'
    vcnt[c] += 1
    vrows.append((v, c, ns))
summary['vars'] = dict(vcnt)
with open(os.path.join(OUT, 'reclaimable_vars.txt'), 'w') as f:
    f.write('# value  class  names\n')
    for v, c, ns in vrows:
        if c in ('HOENN_ONLY', 'NAMED_BUT_UNREFERENCED'):
            f.write(f'0x{v:04X}\t{c}\t{" ".join(ns)}\n')

# ---------- trainers
tr_names = [n for n in names_in('include/constants/opponents.h', 'TRAINER_') if n not in ('TRAINER_NONE',)]
tr_vals = evaluate(tr_names, ['constants/opponents.h'])
tby = collections.defaultdict(list)
for n, v in tr_vals.items():
    tby[v].append(n)
tcnt = collections.Counter()
trows = []
for v in sorted(tby):
    ns = tby[v]
    if v >= 864 or v == 0:
        continue
    cls = [classify(n) for n in ns]
    if 'USED' in cls:
        c = 'IN_USE'
    elif 'HOENN_ONLY' in cls:
        c = 'HOENN_ONLY'
    else:
        c = 'NO_MAP_REF'
    tcnt[c] += 1
    trows.append((v, c, ns))
summary['trainers'] = dict(tcnt)
with open(os.path.join(OUT, 'reclaimable_trainers.txt'), 'w') as f:
    f.write('# id  class  names\n')
    for v, c, ns in trows:
        f.write(f'{v}\t{c}\t{" ".join(ns)}\n')
json.dump(summary, open(os.path.join(OUT, 'reclaimable_summary.json'), 'w'), indent=1)
print(json.dumps(summary, indent=1))
