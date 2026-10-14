import sys, numpy as np, importlib
from PIL import Image
def render(mod, out, S=2, coll=False):
    m = importlib.import_module(mod)
    H, W = len(m.ART), len(m.ART[0])
    img = np.zeros((H*16, W*16, 3), np.uint8)
    for y in range(H):
        for x in range(W):
            t = m.ART[y][x].copy()
            if coll and m.COLL[y][x] == 0x3400: t = (t*0.6 + np.array([255,0,0])*0.4).astype(np.uint8)
            img[y*16:y*16+16, x*16:x*16+16] = t
    Image.fromarray(img).resize((W*16*S, H*16*S), Image.NEAREST).save(out)
render(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv)>3 else 2, len(sys.argv)>4)
