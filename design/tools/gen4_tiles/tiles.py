from PIL import Image
import numpy as np, sys, os
P="/home/claude/24rousol-hub/team-aquas-asset-repo/Maps/Project Palladium/"
def grid(f):
    im=np.array(Image.open(P+f).convert('RGB'))
    h,w,_=im.shape
    if (w-1)%17==0 and (h-1)%17==0 and not ((w%16==0) and (h%16==0)):
        W,H=(w-1)//17,(h-1)//17
        t=[[im[1+17*y:1+17*y+16,1+17*x:1+17*x+16] for x in range(W)] for y in range(H)]
    else:
        W,H=w//16,h//16
        t=[[im[16*y:16*y+16,16*x:16*x+16] for x in range(W)] for y in range(H)]
    return W,H,t
if __name__=='__main__':
    allm={}; cols=set()
    for f in sys.argv[1:]:
        W,H,t=grid(f); u=set()
        for r in t:
            for c in r:
                k=c.tobytes(); u.add(k); allm[k]=c
                cols|=set(map(tuple,c.reshape(-1,3)))
        print(f,W,H,'unique metatiles',len(u))
    print('total unique metatiles',len(allm),'colors',len(cols))
    t8=set()
    for c in allm.values():
        for y in (0,8):
            for x in (0,8):
                b=c[y:y+8,x:x+8]
                t8.add(min(b.tobytes(),b[:,::-1].tobytes(),b[::-1].tobytes(),b[::-1,::-1].tobytes()))
    print('unique 8x8 tiles',len(t8))
