"""Render a map layout (any primary/secondary) to PNG. Usage: python3 mrender.py LAYOUT_ID out.png [scale] [ids]"""
import json, sys, re
import numpy as np
from pathlib import Path
from PIL import Image, ImageDraw
V=Path('/home/claude/veldris')
def tsdir(name):
    h=(V/'src/data/tilesets/headers.h').read_text()
    m=re.search(r'const struct Tileset '+name+r' =\s*\{(.*?)\};',h,re.S); body=m.group(1)
    tiles=re.search(r'\.tiles = (\w+)',body).group(1)
    g=(V/'src/data/tilesets/graphics.h').read_text()
    p=re.search(tiles+r'\[\] = INCGFX_U32\("([^"]+)/tiles.png"',g)
    return V/p.group(1)
def read_pal(p):
    t=Path(p).read_text().split(); n=int(t[2]); return [tuple(int(x) for x in t[3+i*3:6+i*3]) for i in range(n)]
class TS:
    def __init__(s,prim,sec):
        s.pd,s.sd=tsdir(prim),tsdir(sec)
        def tl(d):
            a=np.array(Image.open(d/'tiles.png'))&15
            return [a[y*8:y*8+8,x*8:x*8+8] for y in range(a.shape[0]//8) for x in range(a.shape[1]//8)]
        s.pt,s.st=tl(s.pd),tl(s.sd)
        s.pals={}
        for i in range(13):
            for d in ((s.pd,) if i<6 else (s.sd,)):
                f=d/f'palettes/{i:02d}.pal'
                if f.exists(): s.pals[i]=read_pal(f)
        s.pm=np.frombuffer((s.pd/'metatiles.bin').read_bytes(),'<u2'); s.sm=np.frombuffer((s.sd/'metatiles.bin').read_bytes(),'<u2')
        s.cache={}
    def meta(s,mid):
        if mid in s.cache: return s.cache[mid]
        src=s.pm if mid<512 else s.sm; base=(mid if mid<512 else mid-512)*8
        img=np.zeros((16,16,3),np.uint8); img[:]=(0,0,0)
        if base+8>len(src): s.cache[mid]=img; return img
        ent=src[base:base+8]
        for g in range(2):
            for k in range(4):
                e=int(ent[g*4+k]); idx,hf,vf,pal=e&0x3FF,(e>>10)&1,(e>>11)&1,e>>12
                t=s.pt[idx] if idx<512 else (s.st[idx-512] if idx-512<len(s.st) else np.zeros((8,8),np.uint8))
                if hf:t=t[:,::-1]
                if vf:t=t[::-1]
                ox,oy=(k%2)*8,(k//2)*8
                P=s.pals.get(pal,[(255,0,255)]*16)
                for y in range(8):
                    for x in range(8):
                        c=t[y,x]
                        if c or g==0: 
                            if c: img[oy+y,ox+x]=P[c]
                            elif g==0: img[oy+y,ox+x]=P[0]
        s.cache[mid]=img; return img
def render(grid,ts,scale=2,ids=False,coll=False):
    H,W=grid.shape; img=np.zeros((H*16,W*16,3),np.uint8)
    for y in range(H):
        for x in range(W): img[y*16:y*16+16,x*16:x*16+16]=ts.meta(int(grid[y,x])&0x3FF)
    im=Image.fromarray(img).resize((W*16*scale,H*16*scale),Image.NEAREST); d=ImageDraw.Draw(im)
    if ids or coll:
        for y in range(H):
            for x in range(W):
                v=int(grid[y,x])
                if coll and (v>>10)&3: d.rectangle([x*16*scale,y*16*scale,x*16*scale+16*scale-1,y*16*scale+16*scale-1],outline=(255,0,0))
                if ids: d.text((x*16*scale+1,y*16*scale+1),str(v&0x3FF),fill=(255,255,0))
    return im
def layout(lid):
    L={l['id']:l for l in json.load(open(V/'data/layouts/layouts.json'))['layouts']}[lid]
    g=np.frombuffer((V/L['blockdata_filepath']).read_bytes(),'<u2').reshape(L['height'],L['width'])
    return g,TS(L['primary_tileset'],L['secondary_tileset'])
if __name__=='__main__':
    g,ts=layout(sys.argv[1]); sc=int(sys.argv[3]) if len(sys.argv)>3 else 2
    render(g,ts,sc,'ids' in sys.argv,'coll' in sys.argv).save(sys.argv[2])
