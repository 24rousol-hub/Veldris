#!/usr/bin/env python3
"""Pick 4 moves per Pokemon from this tree's level-up learnsets (gen_9.h): up to 3 best damaging
moves (STAB-weighted, type-diverse) plus 1 useful status move when the mon knows one by that level.
Usage: python3 design/tools/pickmoves.py "Kricketune 17" "Vivillon 19" ...
Prints trainers.party move lines. Review the output: it is a starting point, not a final moveset."""
import re, sys, os
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..') + '/'
moves = {}
t = open(R + 'src/data/moves_info.h').read()
for m in re.finditer(r'\[MOVE_([A-Z0-9_]+)\] =\s*\{(.*?)\n    \},', t, re.S):
    b = m.group(2)
    nm = re.search(r'\.name = COMPOUND_STRING\("([^"]*)"\)', b)
    ty = re.search(r'\.type = (TYPE_[A-Z_]+)', b)
    pw = re.search(r'\.power = (\d+)', b)
    ca = re.search(r'\.category = (DAMAGE_CATEGORY_[A-Z]+)', b)
    moves[m.group(1)] = dict(name=nm.group(1) if nm else m.group(1), type=ty.group(1) if ty else '', power=int(pw.group(1)) if pw else 0, cat=ca.group(1) if ca else '')
# species types
types = {}
stats = {}
for g in range(1, 10):
    s = open(R + f'src/data/pokemon/species_info/gen_{g}_families.h').read()
    for m in re.finditer(r'\[SPECIES_([A-Z0-9_]+)\] =\s*\{(.*?)\n    \},', s, re.S):
        ty = re.search(r'\.types = MON_TYPES\((TYPE_[A-Z_]+)(?:,\s*(TYPE_[A-Z_]+))?', m.group(2))
        if ty: types[m.group(1)] = [x for x in ty.groups() if x]
        a = re.search(r'\.baseAttack\s*=\s*(\d+)', m.group(2)); sa = re.search(r'\.baseSpAttack\s*=\s*(\d+)', m.group(2))
        if a and sa: stats[m.group(1)] = (int(a.group(1)), int(sa.group(1)))
learn = {}
t = open(R + 'src/data/pokemon/level_up_learnsets/gen_9.h').read()
for m in re.finditer(r's([A-Za-z0-9]+)LevelUpLearnset\[\] = \{(.*?)LEVEL_UP_END', t, re.S):
    learn[re.sub(r'[^A-Z0-9]', '', m.group(1).upper())] = [(int(a), b[5:]) for a, b in re.findall(r'LEVEL_UP_MOVE\(\s*(\d+),\s*(MOVE_[A-Z0-9_]+)', m.group(2))]
teach = {}
t = open(R + 'src/data/pokemon/teachable_learnsets.h').read()
for m in re.finditer(r's([A-Za-z0-9]+)TeachableLearnset\[\] = \{(.*?)MOVE_UNAVAILABLE', t, re.S):
    teach[re.sub(r'[^A-Z0-9]', '', m.group(1).upper())] = [x[5:] for x in re.findall(r'MOVE_[A-Z0-9_]+', m.group(2))]
norm = lambda w: re.sub(r'[^A-Z0-9]', '', w.upper())
bynorm = {norm(k): k for k in types}
def resolve(sp):
    n = norm(sp)
    if n in bynorm: return bynorm[n]
    c = sorted((k for k in types if norm(k).startswith(n)), key=len)
    if c: return c[0]
    if n in OVERRIDE: return n
    return None
OVERRIDE = {'VIVILLON': (['TYPE_BUG', 'TYPE_FLYING'], (52, 90)), 'TOGEKISS': (['TYPE_FAIRY', 'TYPE_FLYING'], (50, 120))}  # species whose .types use macros
BAD = {'SELF_DESTRUCT', 'EXPLOSION', 'LAST_RESORT', 'HYPER_BEAM', 'GIGA_IMPACT', 'FOCUS_PUNCH', 'BELCH', 'STRUGGLE', 'MIND_BLOWN', 'MISTY_EXPLOSION', 'ENDEAVOR', 'REVERSAL', 'FLAIL', 'COVET', 'RETURN', 'FRUSTRATION', 'SPIT_UP', 'DREAM_EATER', 'FAKE_OUT', 'FIRST_IMPRESSION', 'SNORE', 'SUCKER_PUNCH', 'ASSURANCE', 'WATER_SPORT', 'ROCK_SMASH', 'THIEF'}
UTIL = ['SWORDS_DANCE', 'CALM_MIND', 'NASTY_PLOT', 'DRAGON_DANCE', 'BULK_UP', 'IRON_DEFENSE', 'TOXIC', 'WILL_O_WISP', 'THUNDER_WAVE', 'SLEEP_POWDER', 'RECOVER', 'ROOST', 'SYNTHESIS', 'MOONLIGHT', 'SLACK_OFF', 'HEAL_PULSE', 'TOXIC_SPIKES', 'SPIKES', 'STEALTH_ROCK', 'PROTECT', 'DETECT', 'AGILITY', 'HYPNOSIS', 'CONFUSE_RAY', 'SCREECH', 'LEECH_SEED', 'AQUA_RING', 'COIL', 'WORK_UP', 'HELPING_HAND']
def pick(sp, lv):
    key = resolve(sp)
    if not key: return None, f'unknown species {sp}'
    if key in OVERRIDE: own, st = OVERRIDE[key]
    else: own, st = types[key], stats.get(key, (80, 80))
    special = st[1] > st[0] * 1.15
    physical = st[0] > st[1] * 1.15
    PHYS = {'SWORDS_DANCE', 'BULK_UP', 'DRAGON_DANCE', 'WORK_UP_PHYS'}; SPEC = {'CALM_MIND', 'NASTY_PLOT'}
    L = learn.get(norm(key)) or learn.get(norm(sp)) or []
    known = []
    for l, m in L:
        if l <= lv and m not in known: known.append(m)
    if lv >= 40:  # late game: TM/tutor moves are fair game
        for m in teach.get(norm(key)) or teach.get(norm(sp)) or []:
            if m not in known: known.append(m)
    dmg = []
    for m in known:
        d = moves.get(m)
        if not d or m in BAD or d['cat'] == 'DAMAGE_CATEGORY_STATUS' or d['power'] < 40: continue
        score = d['power'] * (1.5 if d['type'] in own else 1.0)
        pref = 'DAMAGE_CATEGORY_SPECIAL' if special else ('DAMAGE_CATEGORY_PHYSICAL' if physical else None)
        if pref and d['cat'] != pref: score *= 0.55
        dmg.append((score, m, d['type']))
    dmg.sort(reverse=True)
    chosen, seen = [], {}
    pool = list(dmg)
    while pool and len(chosen) < 3:
        best = max(pool, key=lambda x: x[0] * (0.75 ** seen.get(x[2], 0)))
        pool.remove(best); chosen.append(best[1]); seen[best[2]] = seen.get(best[2], 0) + 1
    def okutil(u):
        if u in PHYS and special: return False
        if u in SPEC and physical: return False
        return u in known
    util = next((u for u in UTIL if okutil(u)), None)
    if util: chosen.append(util)
    elif pool: chosen.append(pool[0][1])
    if len(chosen) < 4:
        for m in known[::-1]:
            if m not in chosen and m not in BAD: chosen.append(m)
            if len(chosen) == 4: break
    return [moves[m]['name'] if m in moves else m for m in chosen], None
if __name__ == '__main__':
    for a in sys.argv[1:]:
        if ' ' not in a:
            sys.exit('usage: pickmoves.py "Species LEVEL" ...')
        sp, lv = a.rsplit(' ', 1)
        mv, err = pick(sp, int(lv))
        print(f'## {sp} {lv}', err or '')
        for m in mv or []: print('-', m)
