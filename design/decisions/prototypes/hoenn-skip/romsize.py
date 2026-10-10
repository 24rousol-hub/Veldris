#!/usr/bin/env python3
"""romsize.py <size -A output>... : ROM bytes (text+script_data+rodata*+data*) and delta vs the first file."""
import sys
def rom(path):
    tot=0
    for l in open(path):
        p=l.split()
        if len(p)==3 and p[0] in ('.text','script_data','.rodata.compound_string','.rodata','.data.iwram','.data.ewram'):
            tot+=int(p[1])
    return tot
base=rom(sys.argv[1])
for f in sys.argv[1:]:
    r=rom(f)
    print(f'{f.split("/")[-1]:24s} {r:12,} bytes  {r/1048576:7.3f} MiB   delta vs first {r-base:+10,}   free of 32 MiB {33554432-r:12,} ({(33554432-r)/1048576:.3f} MiB)')
