#!/usr/bin/env python3
"""resolve_undefined.py <clone_root> <log_prefix>

Experiment helper (run in a clone, after `purge_experiment.py skip-scripts`).
Loop: make; parse linker `undefined reference`s; find which Hoenn map's scripts.inc DEFINES
each missing label; un-wrap that map's include in data/event_scripts.s; repeat until the
link succeeds.  Prints the minimal set of Hoenn map scripts C code and shared scripts still
need, and the ROM bytes left.  Each round assembles one file and links, no C recompiles."""
import os, re, subprocess, sys, glob, collections, json

ROOT, PREFIX = sys.argv[1], sys.argv[2]
if os.path.realpath(ROOT) == os.path.realpath('/home/user/Veldris'):
    sys.exit('refusing to run in /home/user/Veldris')
labels = {}
for p in glob.glob(os.path.join(ROOT, 'data/maps/*/scripts.inc')):
    folder = p.split('/')[-2]
    for m in re.finditer(r'^([A-Za-z_]\w*)::?', open(p, errors='replace').read(), re.M):
        labels.setdefault(m.group(1), folder)
ev = os.path.join(ROOT, 'data/event_scripts.s')
unwrapped = []
history = []
for rnd in range(1, 40):
    r = subprocess.run('make -j2 2>&1', shell=True, cwd=ROOT, capture_output=True, text=True)
    open(f'{PREFIX}-round{rnd}.log', 'w').write(r.stdout)
    miss = set(re.findall(r"undefined reference to `([^']+)'", r.stdout))
    rom = re.search(r'ROM:\s+(\d+) B', r.stdout)
    history.append((rnd, len(miss), int(rom.group(1)) if rom else None))
    print(f'round {rnd}: {len(miss)} undefined symbols, ROM {rom.group(1) if rom else "?"}', flush=True)
    if not miss:
        break
    folders = collections.Counter()
    unknown = []
    for s in miss:
        f = labels.get(s)
        if f:
            folders[f] += 1
        else:
            unknown.append(s)
    if unknown:
        print('  labels with no defining Hoenn map (defined elsewhere / typo):', unknown[:10])
    if not folders:
        print('  nothing to unwrap, stopping')
        break
    txt = open(ev).read()
    for f in folders:
        pat = re.compile(r'\.if HOENN_MAP_SCRIPTS\n(\t\.include "data/maps/%s/scripts\.inc")\n\.endif' % re.escape(f))
        txt, n = pat.subn(r'\1', txt)
        if n:
            unwrapped.append(f)
    open(ev, 'w').write(txt)
print('\nmaps whose scripts must stay:', len(unwrapped))
print(json.dumps(sorted(unwrapped)))
json.dump({'unwrapped': sorted(unwrapped), 'history': history}, open(PREFIX + '-result.json', 'w'), indent=1)
