#!/usr/bin/env python3
"""err_report.py <build.log> : count compiler/assembler errors by file and by kind (make -k logs)."""
import re, sys, collections
seen = set()
by_file = collections.Counter()
kinds = collections.Counter()
ex = {}
undecl = collections.defaultdict(set)
for line in open(sys.argv[1], errors='replace'):
    m = re.match(r'^(\S+?):(\d+)(?::\d+)?: error: (.*)$', line)
    if not m:
        m2 = re.match(r'^(<stdin>|\S+?):(\d+): Error: (.*)$', line)
        if not m2:
            continue
        m = m2
    f, ln, msg = m.group(1), m.group(2), m.group(3)
    key = (f, ln, msg)
    if key in seen:
        continue
    seen.add(key)
    by_file[f] += 1
    k = re.sub(r"'[^']*'", "'X'", msg)
    k = re.sub(r'`[^\']*\'', "`X'", k)
    kinds[k] += 1
    ex.setdefault(k, (f, ln, msg))
    mm = re.match(r"'(\w+)' undeclared", msg)
    if mm:
        undecl[mm.group(1)].add(f)
    mm = re.match(r"symbol `(\w+)' is already defined|Error: .*", msg)
print(f'{sum(by_file.values())} distinct errors in {len(by_file)} files')
print('\nby file:')
for f, n in by_file.most_common():
    print(f'  {n:5d}  {f}')
print('\nby kind:')
for k, n in kinds.most_common(15):
    print(f'  {n:5d}  {k}   e.g. {ex[k][0]}:{ex[k][1]}')
print(f'\n{len(undecl)} distinct undeclared identifiers; families:')
fam = collections.Counter(re.match(r'[A-Za-z]+_?[A-Za-z]*', i).group(0) for i in undecl)
for i, n in sorted(undecl.items(), key=lambda kv: -len(kv[1]))[:40]:
    print(f'  {i}: {sorted(n)}')
