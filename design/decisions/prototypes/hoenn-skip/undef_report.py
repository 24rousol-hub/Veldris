#!/usr/bin/env python3
"""undef_report.py <build.log> [symbols_out.txt] : summarise linker `undefined reference` errors.

The log repeats each error (make prints the ld output twice via `| cat`), so lines are
de-duplicated by (referencing object, section offset, symbol).  `<stdin>` means an assembler
source (data/*.s through the preprocessor), i.e. data/event_scripts.s or one of its includes."""
import re, sys, collections
seen = set()
by_obj = collections.Counter()
syms = collections.defaultdict(set)
sym_objs = collections.defaultdict(set)
for line in open(sys.argv[1], errors='replace'):
    m = re.search(r'ld: (?:(\S+?\.o)|(<stdin>)):\((\S+)\): undefined reference to `([^\']+)\'', line)
    if not m:
        m = re.search(r'^(?:(\S+?\.o)|(<stdin>)):\((\S+)\): undefined reference to `([^\']+)\'', line)
    if not m:
        continue
    obj = m.group(1) or '<assembler source: data/*.s>'
    key = (obj, m.group(3), m.group(4))
    if key in seen:
        continue
    seen.add(key)
    obj = re.sub(r'^build/(emerald|emerald-release)/', '', obj)
    sym = m.group(4)
    by_obj[obj] += 1
    syms[obj].add(sym)
    sym_objs[sym].add(obj)
total = sum(by_obj.values())
print(f'{total} distinct undefined references, {len(sym_objs)} distinct symbols, {len(by_obj)} referencing objects')
print('\nby referencing object (references / distinct symbols):')
for o, n in by_obj.most_common():
    print(f'  {n:5d} / {len(syms[o]):4d}  {o}')
fam = collections.Counter()
for s in sym_objs:
    fam[re.split(r'_|(?<=[a-z])(?=[A-Z])', s)[0] if '_' not in s else s.split('_')[0]] += 1
print('\nsymbol families (text before the first underscore), distinct symbols:')
for f, n in fam.most_common(30):
    print(f'  {n:4d}  {f}')
if len(sys.argv) > 2:
    with open(sys.argv[2], 'w') as f:
        for s in sorted(sym_objs):
            f.write(f'{s}\t{",".join(sorted(sym_objs[s]))}\n')
