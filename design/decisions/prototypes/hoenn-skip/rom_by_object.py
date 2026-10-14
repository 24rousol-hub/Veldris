#!/usr/bin/env python3
"""rom_by_object.py - ROM bytes per object file from a GNU ld map file.

Usage: rom_by_object.py <pokeemerald.map> [--top N] [--group] [--csv out.csv]

Counts only input sections placed in the ROM address window (0x08000000..0x09FFFFFF),
so RAM sections (.ewram, .iwram, .bss) are ignored. Alignment fill is attributed to
"*fill*". Prints a total (which should be close to the ROM bytes in use) and the
largest object files. With --group it adds a rollup by hack-relevant buckets:

  data/maps.o, data/map_events.o, data/layouts.o   - map headers, events, layouts
  data/event_scripts.o                              - all map scripts + their text
  src/data/tilesets, graphics/tilesets (tileset art, via src/data/tilesets/*.o if any)
  everything else by top-level directory

The linker has no per-label breakdown inside one object file, so a finer split
(per map) comes from rom_by_symbol.py (needs nm on the .elf).
"""
import re, sys, collections

def parse(path):
    objs = collections.Counter()
    secs = collections.defaultdict(collections.Counter)  # object -> section kind -> bytes
    pending = None
    started = False
    with open(path, errors='replace') as f:
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
                    m = re.match(r'^ \*fill\*\s+0x([0-9a-f]+)\s+0x([0-9a-f]+)', line)
                    if m:
                        addr, size = int(m.group(1), 16), int(m.group(2), 16)
                        if 0x08000000 <= addr < 0x0A000000:
                            objs['*fill*'] += size
                    pending = None
                    continue
            pending = None
            if size == 0:
                continue
            if not (0x08000000 <= addr < 0x0A000000):
                continue
            objs[obj] += size
            kind = name.split('.')[1] if name.startswith('.') and '.' in name[1:] else name
            secs[obj][name if name in ('.text', '.rodata', 'script_data') else ('.rodata.' + name.split('.')[2] if name.startswith('.rodata.') and name.count('.') > 1 else name)] += size
    return objs, secs

def bucket(obj):
    if obj == '*fill*':
        return 'alignment fill'
    o = obj.replace('build/emerald/', '').replace('build/emerald-release/', '')
    if o.startswith('data/') or o.startswith('src/') or o.startswith('sound/') or o.startswith('gflib/') or o.startswith('libagbsyscall') :
        parts = o.split('/')
        return parts[0] + '/' + (parts[1] if len(parts) > 2 else parts[1])
    if o.startswith('/usr'):
        return 'libc/libgcc'
    return o

def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__); sys.exit(1)
    path = args[0]
    top = 40
    group = '--group' in args
    if '--top' in args:
        top = int(args[args.index('--top') + 1])
    objs, secs = parse(path)
    total = sum(objs.values())
    print(f'ROM-resident bytes counted: {total:,} ({total/1048576:.3f} MiB)')
    print()
    print(f'{"bytes":>12}  object')
    for o, n in objs.most_common(top):
        print(f'{n:12,}  {o}')
    if group:
        print()
        g = collections.Counter()
        for o, n in objs.items():
            g[bucket(o)] += n
        print(f'{"bytes":>12}  bucket')
        for b, n in g.most_common(top):
            print(f'{n:12,}  {b}')
    if '--csv' in args:
        out = args[args.index('--csv') + 1]
        with open(out, 'w') as f:
            f.write('object,bytes\n')
            for o, n in objs.most_common():
                f.write(f'{o},{n}\n')

if __name__ == '__main__':
    main()
