#!/usr/bin/env python3
"""systems.py <syms.tsv> <rom_by_map.json> : ROM cost of the Hoenn systems that hang off Hoenn maps.

Code/data objects come from the per-symbol table; script/text files from rom_by_map.json
(spans in data/event_scripts.s).  A system's number is a ceiling for what removing it could
save: some of it is shared with kept features (listed in the 'kept-code hooks' column)."""
import json, re, sys, collections, os
syms = [l.rstrip('\n').split('\t') for l in open(sys.argv[1])]
obj = collections.Counter()
for a, sz, o, sec, n in syms:
    obj[re.sub(r'^build/(emerald|emerald-release)/', '', o)] += int(sz)
shared = json.load(open(sys.argv[2]))['shared_scripts']
# trainer_slide frontier table
slide = sum(int(sz) for a, sz, o, sec, n in syms if n == 'sFrontierTrainerSlides')
SYS = collections.OrderedDict([
 ('Battle Frontier (Tower, Dome, Factory, Pike, Pyramid, Palace, Arena, Tent, Pass)',
   (['battle_tower', 'battle_dome', 'battle_factory', 'battle_factory_screen', 'battle_pike', 'battle_pyramid', 'battle_pyramid_bag',
     'battle_arena', 'battle_palace', 'battle_tent', 'battle_frontier', 'frontier_util', 'frontier_pass'],
    ['data/scripts/battle_frontier.inc', 'data/scripts/battle_pike.inc', 'data/text/battle_tent.inc'])),
 ('Contests and Pokeblocks', (['contest', 'contest_ai', 'contest_effect', 'contest_util', 'contest_painting', 'contest_link', 'contest_link_util',
                                'pokeblock', 'pokeblock_feed', 'berry_blender', 'data/contest_ai_scripts'], ['data/scripts/contest_hall.inc', 'data/scripts/berry_blender.inc'])),
 ('Secret bases and decorations', (['secret_base', 'decoration', 'decoration_inventory'], ['data/scripts/secret_base.inc', 'data/scripts/shared_secret_base.inc'])),
 ('TV, news, Mauville Old Man, Gabby and Ty, interviews, Lilycove Lady, Dewford trends',
   (['tv', 'mauville_old_man', 'dewford_trend', 'lilycove_lady'],
    ['data/scripts/tv.inc', 'data/text/tv.inc', 'data/scripts/interview.inc', 'data/scripts/gabby_and_ty.inc', 'data/text/pokemon_news.inc',
     'data/scripts/mauville_man.inc', 'data/text/mauville_man.inc', 'data/scripts/lilycove_lady.inc', 'data/scripts/profile_man.inc'])),
 ('Pokenav conditions, ribbons, Match Call', (['pokenav_match_call_list', 'pokenav_match_call_gfx', 'pokenav_match_call_data', 'match_call', 'pokenav_ribbons_summary',
     'pokenav_ribbons_list', 'pokenav_conditions', 'pokenav_conditions_gfx', 'pokenav_conditions_search_results'], ['data/text/match_call.inc'])),
 ('Apprentice, Trainer Hill, Safari Zone, Trick-house-style odds and ends', (['apprentice', 'trainer_hill', 'safari_zone', 'mirage_tower', 'lottery_corner', 'cable_car'],
     ['data/scripts/apprentice.inc', 'data/text/apprentice.inc', 'data/scripts/trainer_hill.inc', 'data/scripts/safari_zone.inc', 'data/text/lottery_corner.inc'])),
 ('Mini-games (Dodrio berry picking, Berry Crush, Pokemon Jump, Roulette, Slots)', (['dodrio_berry_picking', 'berry_crush', 'pokemon_jump', 'roulette', 'slot_machine'], ['data/scripts/roulette.inc'])),
 ('Hoenn trainer dialogue (every Hoenn trainer intro/defeat line)', ([], ['data/text/trainers.inc'])),
])
print('| System | C/data objects | script+text | total | note |')
print('|---|---:|---:|---:|---|')
tot = 0
for name, (objs, files) in SYS.items():
    a = sum(obj.get('src/' + o + '.o', obj.get(o + '.o', 0)) for o in objs)
    b = sum(shared.get(f, 0) for f in files)
    note = ''
    if name.startswith('Battle Frontier'):
        note = f'plus {slide:,} B of Frontier trainer slides inside trainer_slide.o (upstream table)'
    tot += a + b
    print(f'| {name} | {a:,} | {b:,} | {a+b:,} | {note} |')
print(f'| **sum of the above** | | | **{tot:,}** | |')
