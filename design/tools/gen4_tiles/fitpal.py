import json, importlib, sys, numpy as np, itertools
from pathlib import Path
remap = {}
for it in range(40):
    json.dump({json.dumps(list(k)): list(v) for k, v in remap.items()}, open('remap.json', 'w'))
    for m in ['g4lib', 'hollowbrook_g4', 'route1_g4']:
        if m in sys.modules: del sys.modules[m]
    import g4lib, hollowbrook_g4 as hb, route1_g4 as r1
    sets = set(); cols = {}
    for m in (hb, r1):
        for y in range(len(m.ART)):
            for x in range(len(m.ART[0])):
                if not m.SEC[y][x]:
                    for t in g4lib.tiles8(m.ART[y][x]): sets.add(g4lib.colkey(t))
    try:
        g4lib.pack_palettes(list(sets), 6); print('fits after', len(remap), 'merges'); break
    except SystemExit:
        pass
    allc = sorted(set().union(*sets))
    best = None
    for a, b in itertools.combinations(allc, 2):
        d = sum((int(i) - int(j)) ** 2 for i, j in zip(a, b))
        if best is None or d < best[0]: best = (d, a, b)
    d, a, b = best; a = tuple(int(v) for v in a); b = tuple(int(v) for v in b)
    # map the rarer colour onto the commoner
    cnt = lambda c: sum(c in s for s in sets)
    if cnt(a) > cnt(b): a, b = b, a
    print('merge', a, '->', b, 'dist', round(d ** .5, 1))
    remap = {k: (b if v == a else v) for k, v in remap.items()}; remap[a] = b
