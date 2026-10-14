#!/usr/bin/env python3
"""rom_symbols.py - per-symbol ROM sizes by combining an ld map file with `nm -n`.

Library + CLI.  CLI:
    rom_symbols.py <pokeemerald.map> <pokeemerald.elf> <out.tsv>

Writes a TSV: address, size, object, input-section, symbol.
Sizes come from address differences, capped at the end of the input section that
holds the symbol (taken from the ld map), so a label at the end of one object file
never swallows the next object's data.  Bytes in an input section before its first
label are written with the symbol '<unlabeled>'.
"""
import re, subprocess, sys, bisect, collections

def parse_sections(mappath):
    """Return sorted list of (start, size, obj, secname) for ROM input sections."""
    out = []
    pending = None
    started = False
    with open(mappath, errors='replace') as f:
        for line in f:
            if not started:
                if line.startswith('Linker script and memory map'):
                    started = True
                continue
            m = re.match(r'^ (\S+)\s*$', line)
            if m and not line.startswith(' *'):
                pending = m.group(1)
                continue
            m = re.match(r'^ (\S+)\s+0x([0-9a-f]+)\s+0x([0-9a-f]+)\s+(\S.*)$', line)
            if m:
                name, addr, size, obj = m.group(1), int(m.group(2), 16), int(m.group(3), 16), m.group(4).strip()
            else:
                m = re.match(r'^\s+0x([0-9a-f]+)\s+0x([0-9a-f]+)\s+(\S.*)$', line)
                if m and pending:
                    name, addr, size, obj = pending, int(m.group(1), 16), int(m.group(2), 16), m.group(3).strip()
                else:
                    pending = None
                    continue
            pending = None
            if size and 0x08000000 <= addr < 0x0A000000:
                out.append((addr, size, obj, name))
    out.sort()
    return out

def parse_nm(elfpath):
    txt = subprocess.run(['arm-none-eabi-nm', '-n', '--defined-only', elfpath], capture_output=True, text=True).stdout
    syms = []
    for line in txt.split('\n'):
        p = line.split()
        if len(p) != 3:
            continue
        a = int(p[0], 16)
        if 0x08000000 <= a < 0x0A000000 and p[1] not in 'aA':
            syms.append((a, p[2]))
    return syms

def per_symbol(mappath, elfpath):
    secs = parse_sections(mappath)
    starts = [s[0] for s in secs]
    syms = parse_nm(elfpath)
    # group symbols by section index
    bysec = collections.defaultdict(list)
    for a, n in syms:
        i = bisect.bisect_right(starts, a) - 1
        if i < 0:
            continue
        s, size, obj, name = secs[i]
        if a >= s + size:
            continue
        bysec[i].append((a, n))
    rows = []
    for i, (s, size, obj, name) in enumerate(secs):
        lst = sorted(bysec.get(i, []))
        end = s + size
        if not lst:
            rows.append((s, size, obj, name, '<unlabeled>'))
            continue
        if lst[0][0] > s:
            rows.append((s, lst[0][0] - s, obj, name, '<unlabeled>'))
        for j, (a, n) in enumerate(lst):
            nxt = lst[j + 1][0] if j + 1 < len(lst) else end
            if nxt > a:
                rows.append((a, nxt - a, obj, name, n))
            # zero-size aliases at the same address get size 0 and are skipped
    return rows

if __name__ == '__main__':
    mp, elf, out = sys.argv[1:4]
    rows = per_symbol(mp, elf)
    with open(out, 'w') as f:
        for a, sz, obj, sec, n in rows:
            f.write(f'{a:08x}\t{sz}\t{obj}\t{sec}\t{n}\n')
    print(len(rows), 'rows,', sum(r[1] for r in rows), 'bytes')
