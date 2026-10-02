import re,glob,sys,json
R='/home/user/Veldris/'
species={}   # name -> dict(gen, evos[(lvl,target)], pre)
for g in range(1,10):
    t=open(R+f'src/data/pokemon/species_info/gen_{g}_families.h').read()
    for m in re.finditer(r'\[SPECIES_([A-Z0-9_]+)\] =\s*\{(.*?)\n    \},',t,re.S):
        n=m.group(1); body=m.group(2)
        ev=re.search(r'\.evolutions = EVOLUTION\((.*?)\),\n',body,re.S)
        evos=[]
        if ev:
            for e in re.finditer(r'\{(EVO_[A-Z_]+),\s*([^,]+),\s*SPECIES_([A-Z0-9_]+)',ev.group(1)):
                evos.append((e.group(1),e.group(2).strip(),e.group(3)))
        species[n]={'gen':g,'evos':evos}
pre={}
for n,d in species.items():
    for k,a,tg in d['evos']: pre.setdefault(tg,[]).append((n,k,a))
learn={}
t=open(R+'src/data/pokemon/level_up_learnsets/gen_9.h').read()
for m in re.finditer(r's([A-Za-z0-9]+)LevelUpLearnset\[\] = \{(.*?)LEVEL_UP_END',t,re.S):
    learn[m.group(1).upper()]=[(int(a),b) for a,b in re.findall(r'LEVEL_UP_MOVE\(\s*(\d+),\s*(MOVE_[A-Z0-9_]+)',m.group(2))]
def norm(w): return re.sub(r'[^A-Z0-9]','',w.upper())
bynorm={norm(n):n for n in species}
files=sys.argv[1:]
for f in files:
    print('==',f)
    for ln,line in enumerate(open(R+f),1):
        if not re.search(r'Team|\| \d|^\| [A-Z]',line) : continue
        pairs=re.findall(r"([A-Z][A-Za-z'.\-]+)(?: ['A-Z]*)? (\d{1,3})\b",line)
        gens=[];bad=[]
        for w,l in pairs:
            n=bynorm.get(norm(w))
            if not n: continue
            l=int(l)
            if l<2 or l>100: continue
            d=species[n]; gens.append(d['gen'])
            for k,a,tg in d['evos']:
                if k=='EVO_LEVEL' and a.isdigit() and 0<int(a)<=l: bad.append(f'{w} {l}: should be {tg} (evolves at {a})')
            for p,k,a in pre.get(n,[]):
                if k=='EVO_LEVEL' and a.isdigit() and int(a)>l: bad.append(f'{w} {l}: below evolution level {a} of {p}')
            lm=learn.get(norm(n)) or learn.get(n)
            if lm is None: bad.append(f'{w}: no learnset found')
            else:
                known=[m for lv,m in lm if lv<=l]
                if len(set(known))<4: bad.append(f'{w} {l}: only {len(set(known))} level-up moves by then')
        if bad or len(set(gens))>=1 and len(gens)>=2:
            print(f'{f}:{ln} gens={sorted(set(gens))}'+('' if not bad else ' | '+'; '.join(bad)))
if len(sys.argv)==1:
    pass
