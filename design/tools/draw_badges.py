#!/usr/bin/env python3
"""Draws the 9 Veldris badges into graphics/trainer_card/badges.png (128x32, 16x16 per slot).
Slots 0-8 = badges, slot 15 = empty socket. One shared 16-colour palette (index 0 = background).
Tweak a shape or the PAL list and re-run from the repo root. The author can also just edit the PNG
in any indexed-colour editor, keeping this palette."""
from PIL import Image, ImageDraw
import math, sys
PAL = [(136,96,112),(40,40,56),(248,248,248),(208,208,216),(152,152,168),(96,96,112),
       (136,208,248),(56,128,224),(24,56,152),(152,224,72),(40,144,56),(248,216,56),
       (192,128,224),(112,48,152),(248,128,176),(200,48,104)]
K,W,S,G,D,LB,MB,DB,LG,DG,Y,LP,DP,PK,PD = range(1,16)
sheet = Image.new('P',(128,32),0)
p=[]
for c in PAL: p+=list(c)
sheet.putpalette(p+[0]*(768-len(p)))
def slot(i):
    return (i%8)*16,(i//8)*16
def tile():
    im=Image.new('P',(16,16),0); im.putpalette(sheet.getpalette()); return im, ImageDraw.Draw(im)
def poly_ring(n,r,cx=7.5,cy=7.5,rot=0):
    return [(cx+r*math.cos(rot+2*math.pi*k/n),cy+r*math.sin(rot+2*math.pi*k/n)) for k in range(n)]
def outlined(d,pts,fill):
    d.polygon(pts,fill=K); 
def b_standard():  # silver ring, blue centre, white glint
    im,d=tile(); d.ellipse([1,1,14,14],fill=K); d.ellipse([2,2,13,13],fill=G); d.ellipse([3,3,12,12],fill=D)
    d.ellipse([4,4,11,11],fill=K); d.ellipse([5,5,10,10],fill=MB); d.ellipse([6,6,9,9],fill=LB)
    d.point([3,3],fill=W);d.point([4,2],fill=W);d.point([2,4],fill=W);d.point([6,6],fill=W); return im
def b_bug():  # briar: green hexagon, yellow honeycomb centre, thorn points
    im,d=tile(); pts=poly_ring(6,7.2,rot=math.pi/6); d.polygon(pts,fill=K)
    d.polygon(poly_ring(6,6,rot=math.pi/6),fill=DG); d.polygon(poly_ring(6,4.2,rot=math.pi/6),fill=LG)
    d.polygon(poly_ring(6,2.4,rot=math.pi/6),fill=Y); d.point([7,7],fill=W)
    for x,y in [(1,7),(14,7),(7,1),(8,14)]: d.point([x,y],fill=DG)
    return im
def b_ghost():  # purple flame wisp with eyes
    im,d=tile()
    body=[(8,0),(11,4),(14,8),(13,12),(10,15),(5,15),(2,12),(1,8),(4,5),(6,3)]
    d.polygon(body,fill=K); inner=[(8,2),(10,5),(12,8),(11,12),(9,14),(6,14),(4,12),(3,8),(5,6),(7,4)]
    d.polygon(inner,fill=DP); d.polygon([(8,4),(10,7),(10,11),(8,13),(6,13),(5,9),(6,6)],fill=LP)
    d.rectangle([6,8,6,9],fill=K); d.rectangle([9,8,9,9],fill=K); d.point([6,8],fill=W); d.point([9,8],fill=W); return im
def b_steel():  # cog
    im,d=tile()
    for k in range(8):
        a=k*math.pi/4; cx=7.5+6*math.cos(a); cy=7.5+6*math.sin(a)
        d.rectangle([cx-2,cy-2,cx+2,cy+2],fill=K)
    d.ellipse([1,1,14,14],fill=K)
    for k in range(8):
        a=k*math.pi/4; cx=7.5+6*math.cos(a); cy=7.5+6*math.sin(a)
        d.rectangle([cx-1,cy-1,cx+1,cy+1],fill=G)
    d.ellipse([2,2,13,13],fill=G); d.ellipse([3,3,12,12],fill=D); d.ellipse([5,5,10,10],fill=K); d.ellipse([6,6,9,9],fill=LB)
    d.point([3,4],fill=W);d.point([4,3],fill=W);return im
def b_ice():  # snowflake in blue disc
    im,d=tile(); d.ellipse([0,0,15,15],fill=K); d.ellipse([1,1,14,14],fill=DB)
    for k in range(6):
        a=k*math.pi/3
        d.line([7.5,7.5,7.5+6*math.cos(a),7.5+6*math.sin(a)],fill=W,width=1)
        mx,my=7.5+3.5*math.cos(a),7.5+3.5*math.sin(a)
        for s in (-1,1):
            b=a+s*math.pi/3
            d.line([mx,my,mx+2*math.cos(b),my+2*math.sin(b)],fill=LB,width=1)
    d.rectangle([6,6,9,9],fill=W); return im
def b_flying():  # feather: white-blue wing sweeping up right
    im,d=tile()
    f=[(2,14),(1,9),(3,5),(7,2),(12,1),(14,2),(14,6),(12,10),(8,13),(4,15)]
    d.polygon(f,fill=K); g=[(3,13),(2,9),(4,6),(7,3),(12,2),(13,3),(13,6),(11,9),(8,12),(5,14)]
    d.polygon(g,fill=W); d.polygon([(4,12),(4,8),(7,5),(11,3),(12,5),(10,8),(7,11)],fill=LB)
    d.line([3,14,12,3],fill=MB,width=1); d.line([3,13,11,3],fill=DB,width=1); return im
def b_poison():  # drop, green, purple bubbles
    im,d=tile(); drop=[(8,0),(11,4),(13,8),(13,11),(11,14),(8,15),(5,14),(3,11),(3,8),(5,4)]
    d.polygon(drop,fill=K); d.polygon([(8,2),(10,5),(12,8),(12,11),(10,13),(8,14),(6,13),(4,11),(4,8),(6,5)],fill=DG)
    d.polygon([(8,4),(9,6),(11,9),(10,12),(8,13),(6,12),(5,9)],fill=LG)
    d.ellipse([6,8,8,10],fill=LP); d.point([7,8],fill=W); d.ellipse([9,10,10,11],fill=PK); d.point([5,6],fill=W); return im
def b_fairy():  # pink heart with white star
    im,d=tile(); d.ellipse([0,1,8,9],fill=K); d.ellipse([7,1,15,9],fill=K)
    d.polygon([(0,6),(15,6),(8,15)],fill=K)
    d.ellipse([1,2,7,8],fill=PD); d.ellipse([8,2,14,8],fill=PD); d.polygon([(1,6),(14,6),(8,14)],fill=PD)
    d.ellipse([2,3,6,7],fill=PK); d.ellipse([9,3,13,7],fill=PK); d.polygon([(2,6),(13,6),(8,12)],fill=PK)
    d.line([7.5,3,7.5,9],fill=W); d.line([5,6,10,6],fill=W); d.point([3,4],fill=W); return im
def b_water():  # blue wave in a ring
    im,d=tile(); d.ellipse([0,0,15,15],fill=K); d.ellipse([1,1,14,14],fill=DB)
    for y,c in ((5,MB),(8,LB),(11,MB)):
        for x in range(2,14):
            yy=y+int(round(1.5*math.sin((x-2)*0.9))); d.point([x,yy],fill=c); d.point([x,yy+1],fill=c)
    d.point([4,3],fill=W); d.point([5,2],fill=W); d.point([11,12],fill=LB); return im
def b_socket():
    im,d=tile(); d.ellipse([1,1,14,14],fill=D); d.ellipse([2,2,13,13],fill=G); d.ellipse([3,3,12,12],fill=D)
    d.ellipse([4,4,11,11],fill=G); return im
B=[b_standard,b_bug,b_ghost,b_steel,b_ice,b_flying,b_poison,b_fairy,b_water]
for i,f in enumerate(B): sheet.paste(f(),slot(i))
sheet.paste(b_socket(),slot(15))
out=sys.argv[1] if len(sys.argv)>1 else 'graphics/trainer_card/badges.png'
sheet.save(out)
big=sheet.convert('RGB').resize((768,192),Image.NEAREST); big.save(out.replace('.png','_preview.png') if len(sys.argv)>1 else '/tmp/badges_preview.png')
