#!/usr/bin/env python3
"""systems_maps.py <repo_root> <deletable_maps.json> : for each Hoenn system, how many Hoenn-only maps hang off it, how many of
those maps are pinned by C/shared files (deletable_maps.py), and which C files pin them.  Read-only."""
import json, os, re, sys, collections
ROOT, DJ = sys.argv[1], json.load(open(sys.argv[2]))
VELDRIS = {'Hollowbrook','VeldrisRoute1','Crestfall','Hollowbrook_PlayersHouse_1F','Hollowbrook_PlayersHouse_2F','Hollowbrook_ProfFennickLab',
           'Hollowbrook_NeighboursHouse','Crestfall_PokemonCenter_1F','Crestfall_Mart','Crestfall_HouseA','Crestfall_HouseB','Crestfall_Gym'}
import glob
names = []
for p in glob.glob(os.path.join(ROOT, 'data/maps/*/map.json')):
    d = json.load(open(p))
    if d.get('region', 'REGION_HOENN') == 'REGION_HOENN' and d['name'] not in VELDRIS:
        names.append(d['name'])
SYS = collections.OrderedDict([
 ('Battle Frontier (Tower, Dome, Factory, Pike, Pyramid, Palace, Arena) + the three town Battle Tents', r'^(BattleFrontier_|BattlePyramid|FallarborTown_BattleTent|SlateportCity_BattleTent|VerdanturfTown_BattleTent|.*_BattleTent)'),
 ('Secret bases', r'^SecretBase_'),
 ('Contests (Lilycove contest hall and lobby, Pokeblock links)', r'^(LilycoveCity_Contest|ContestHall|LilycoveCity_ContestLobby)'),
 ('Trainer Hill', r'^TrainerHill_'),
 ('Safari Zone', r'^(SafariZone_|Route121_SafariZone)'),
 ('Mauville (Game Corner, Old Man, New Mauville)', r'^(MauvilleCity|NewMauville_)'),
 ('Lilycove (department store, museum, Lilycove Lady, harbor)', r'^LilycoveCity'),
 ('Link rooms (Pokemon Center 2F, Trade Center, Union Room, Colosseums, Record Corner)', r'^(TradeCenter|UnionRoom|BattleColosseum|RecordCorner|.*PokemonCenter_2F)'),
 ('Trick House (8 puzzle rooms)', r'^Route110_TrickHouse'),
 ('Ship / Abandoned Ship / S.S. Tidal', r'^(SSTidal|AbandonedShip)'),
 ('Legendary and puzzle dungeons (Sky Pillar, Mirage, Regi caves, Faraway, Birth, Southern Island, Navel Rock...)', r'^(SkyPillar|Route111_|MirageTower|DesertRuins|IslandCave|AncientTomb|FarawayIsland|SouthernIsland|BirthIsland|NavelRock|MarineCave|TerraCave|CaveOfOrigin|ScorchedSlab|SealedChamber|ShoalCave|MeteorFalls|GraniteCave|SeafloorCavern|MtPyre|MtChimney|JaggedPass|MagmaHideout|AquaHideout|VictoryRoad|Underwater)'),
 ('Gyms and the Elite Four rooms', r'(_Gym|EverGrande.*(Room|Hall)|Sootopolis.*Gym)'),
 ('Pokemon Centers, Marts and houses of the 16 Hoenn towns', r'(PokemonCenter_1F|_Mart|_House|Houses?$|_Lab)'),
])
out = {}
for k, pat in SYS.items():
    r = re.compile(pat)
    ms = [n for n in names if r.search(n)]
    pinned = [n for n in ms if n in DJ['pinned']]
    files = collections.Counter()
    for n in pinned:
        for f in DJ['pinned'][n]:
            files[f] += 1
    out[k] = (len(ms), len(pinned), files)
    print('| %s | %d | %d | %s |' % (k, len(ms), len(pinned), ', '.join(f.split('/')[-1] for f, c in files.most_common(5))))
