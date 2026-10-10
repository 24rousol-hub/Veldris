# Extract unique metatiles from NBT + Route29 (and mirrored Route29), save contact sheet with indices
from tiles import grid
import numpy as np, json
from PIL import Image, ImageDraw
def q5(a): return (a>>3)<<3   # GBA 15-bit colour
maps={}
for name,f,mir in [('nbt','New Bark Town.png',False),('r29','Route 29.png',False)]:
    W,H,t=grid(f)
    maps[name]=(W,H,[[q5(c) for c in r] for r in t])
uniq=[]; idx={}
def key(c): return c.tobytes()
grids={}
for name,(W,H,t) in maps.items():
    g=[]
    for r in t:
        row=[]
        for c in r:
            k=key(c)
            if k not in idx: idx[k]=len(uniq); uniq.append(c)
            row.append(idx[k])
        g.append(row)
    grids[name]=g
print(len(uniq))
np.save('uniq.npy',np.array(uniq)); json.dump(grids,open('grids.json','w'))
S=3; cols=16
rows=(len(uniq)+cols-1)//cols
im=Image.new('RGB',(cols*(16*S+4),rows*(16*S+14)),(40,40,40)); d=ImageDraw.Draw(im)
for i,c in enumerate(uniq):
    x=(i%cols)*(16*S+4); y=(i//cols)*(16*S+14)
    im.paste(Image.fromarray(c.astype('uint8')).resize((16*S,16*S),Image.NEAREST),(x,y+12))
    d.text((x+1,y),str(i),fill=(255,255,0))
im.save('sheet.png'); print(im.size)
