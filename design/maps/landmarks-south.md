# Landmarks, south group (PROPOSED, started 2026-10-01)

Status: **PROPOSED.** Three post-game landmarks from the author's sketch, all unlocked after the League: **SILVERSTRAND** (beach), **ECHO HOLLOW** (cliff cave) and **ARGENT PEAK** (mountain, the toughest wild and trainer levels in the game). Names approved 2026-10-01 ([../region-names.md](../region-names.md)). Conventions: [README.md](README.md). Roads that reach them: R29, R30, R31 in [routes-south.md](routes-south.md). Hub: [towns/vesperhaven.md](towns/vesperhaven.md). Post-game list: [../postgame.md](../postgame.md).

Landmarks are not settlements, so each section is shorter than a town card but follows the same order: role, where it sits, source and size, layout, trainers and NPCs, wild tables, items, flags, effort, open questions. Species were checked against `include/constants/species.h`. Trainers reuse vanilla Hoenn ids, carry no IVs, and are Pokémon only. Palladium images live in `Team-Aquas-Asset-Repo/Maps/Project Palladium/` (sizes: `(px - 1) / 17` when the image has a 1 px grid, else `px / 16`).

Fly: **landmarks are not fly destinations** (CLAUDE.md: a new fly town needs a row and the data checklist, which is for settlements). Argent Peak's Pokémon Center needs a heal location for blackout respawn; see its section.

---

## SILVERSTRAND (beach, post-game)

### Role
A long pale beach reached by water only, from Vesperhaven (R29). It is the post-game's quiet place: no story, a treasure hunt, a few trainers, a surf shack and a dead end. 'Silver' for the sand, which is crushed shell.

### Where it sits
South-west of Vesperhaven, on the sea at the bottom of the map.

| Road | Edge | How |
|---|---|---|
| R29 from Vesperhaven | **North edge** (water) | The player surfs up to the sand. A short wooden jetty is the one dry arrival tile |
| (none) | other edges | Sea and cliff. A dead end |

### Source and size
- **Palladium:** none. The nearest mood is the sand strip of `Route 40.png` (20 x 34, sea route with a beach).
- **Vanilla base: Route 109** (`Route109_Layout`, 40 x 63, a beach road with the Seashore House). Trim to **about 44 x 30**: `(44 + 15) * (30 + 14) = 2596`.
- **Section id:** `MAPSEC_SILVERSTRAND` (name `SILVERSTRAND`, 12 chars).
- **Maps:** the beach, the Surf Shack (one house layout `LAYOUT_HOUSE1`), and an underwater cove (a copy of a vanilla `Underwater_Route*` map) for Dive items.

### Layout
- **Jetty and arrival (top).** The R29 water meets the sand. A signpost: 'SILVERSTRAND. PLEASE TAKE ONLY PHOTOGRAPHS (AND PEARLS).'
- **Dune ridge (middle).** Three dune lines with patches of dune grass (wild encounters). A cut path through them.
- **Surf Shack (middle left).** The only building. The door faces the sea, 6 tiles from the left edge.
- **Rock pools (right).** Two small pools with shining items.
- **The sandbar (bottom).** A thin sand bar leading to a tiny islet with one tree and a visible Dive spot.
- **Cliffs (left, bottom).** A dead wall of cliff, with the wreck of a wooden boat (decoration).

### Trainers (post-game, reuse vanilla ids)
| Class | Team |
|---|---|
| Swimmer male | Wailord 68, Starmie 69 |
| Swimmer female | Milotic 68, Gastrodon 69, Jellicent 70 |
| Tuber male | Floatzel 67, Sharpedo 68 |
| Beauty | Alomomola 68, Mantine 69, Walrein 70 |
| Sailor | Pelipper 68, Cloyster 69, Kingdra 70 |
| Fisherman | Whiscash 68, Gyarados 70, Seaking 69 |

### NPCs
- **Surf Shack keeper**: a retired lifeguard. Gives Silver Powder once. Hints at the treasure pools. Topic: 'The sand is silver. The sea took the rest.'
- **Beachcomber**: wades the shallows and sells information about where hidden items lie ('three pearls, a heart, a stone').
- **Child on the jetty**: asks if the player came by boat or by 'being brave'. Gag.
- **Retired Swimmer (rematch)**: one post-game rematch trainer (see Vesperhaven's rematch policy).
- No shop. Heal at Vesperhaven.

### Wild Pokémon
Dune grass, levels 66 to 72. Standard rates.

| Slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 20% | PELIPPER | 66 to 67 |
| 2 | 20% | CRAWDAUNT | 66 to 67 |
| 3 | 10% | SANDACONDA | 67 to 68 |
| 4 | 10% | PALOSSAND | 67 to 68 |
| 5 | 10% | CRABOMINABLE | 68 |
| 6 | 10% | KINGLER | 68 to 69 |
| 7 | 5% | SLOWBRO | 69 |
| 8 | 5% | CLOYSTER | 69 |
| 9 | 4% | GASTRODON | 70 |
| 10 | 4% | STARMIE | 70 |
| 11 | 1% | MINIOR | 71 |
| 12 | 1% | ARMALDO | 72 |

Surf (levels 66 to 70), rates 60/30/5/4/1: TENTACRUEL 66 to 70, MANTINE 67 to 70, STARMIE 68 to 70, ALOMOMOLA 69 to 70, DONDOZO 70.
Old Rod (70/30): MAGIKARP 25 to 30, TENTACOOL 25 to 30. Good Rod (60/20/20): SHELLDER 45 to 50, CORSOLA 45 to 50, STARYU 45 to 50. Super Rod (40/40/15/4/1): SEADRA 66 to 70, OCTILLERY 66 to 70, CLOYSTER 67 to 70, KINGDRA 69 to 70, GYARADOS 70.
Dive cove, levels 66 to 70: CLAMPERL 66 to 68 (60%), LUVDISC 67 to 69 (30%), HUNTAIL 68 to 70 (5%), GOREBYSS 68 to 70 (4%), LUMINEON 70 (1%).

### Items and secrets
| Item | Where | Gate |
|---|---|---|
| Silver Powder | Surf Shack gift | None |
| Pearl x3, Big Pearl | Rock pools and sand (hidden) | None |
| Heart Scale x2, Star Piece, Stardust | Hidden in the dunes | None |
| Shell Bell | The wreck's hold (visible) | None |
| Max Revive | Islet tree base | Surf over the sandbar |
| Pearl String, Big Pearl x2 | Underwater cove | **Dive** (badge 9) |
| Nugget | Dune ridge (hidden) | None |

### Flags (not claimed)
`FLAG_VISITED_SILVERSTRAND` (optional), `FLAG_RECEIVED_SILVER_POWDER`, `FLAG_HIDDEN_ITEM_SILVERSTRAND_PEARL_1` to `_3`, `_BIG_PEARL`, `_HEART_SCALE_1`, `_2`, `_STAR_PIECE`, `_STARDUST`, `_NUGGET`, `FLAG_ITEM_SILVERSTRAND_MAX_REVIVE`, `FLAG_ITEM_SILVERSTRAND_SHELL_BELL`.

### Build order and effort
**Easy to medium.** One beach, one house, one cove. No puzzles. The wild and trainer data are the bulk.

### Open questions
1. Is a pure treasure beach what you want for the south landmark, or should it hide something bigger?
2. Dive cove: the Underwater maps in Hoenn are tied to a route above; this one needs its own pair with a dive connection in Porymap.

---

## ECHO HOLLOW (cliff cave, post-game)

### Role
A dark cliff-side cave south-east of Vesperhaven, reached by land (R30). The post-game's puzzle cave: the walls answer back, and three echo stones open a hidden chamber. Mid-hard trainers and a reward chamber.

### Where it sits
South-east of Vesperhaven. R30 ends at a cave mouth on a cliff.

| Road | Edge | How |
|---|---|---|
| R30 from Vesperhaven | The cave entrance (a door on R30's north-east end) | A warp into Echo Hollow 1F |
| (none) | other | Cave only, a dead end |

### Source and size
- **Palladium (images only):**
  - **1F:** `unioncave13qx.png` (341 x 613, gridded, **20 x 36**): a three-pool cave with a stair in the middle.
  - **B1F:** `unioncave29xw.png` (**20 x 36**).
  - **B2F:** `unioncave39xd.png` (**20 x 36**).
  - **The Echo Chamber (dark):** `darkcave2.png` (579 x 562, **34 x 33**), or `darkcave.png` (766 x 681, **45 x 40**) if the author wants a larger one. Dark Cave in Johto needs Flash; here Flash (badge 3) opens the chamber's lit path.
- **Vanilla alternative:** `GraniteCave_B1F` (32 x 26) or `ShoalCave_LowTideEntranceRoom` (35 x 35) as the 1F, `AlteringCave` (32 x 24) for the chamber.
- **Section id:** `MAPSEC_ECHO_HOLLOW` (name `ECHO HOLLOW`, 11 chars). Interiors share it.

### Layout
- **1F (Union Cave 1).** A big cave, three pools in a row, a middle stair down. Two Hiker trainers and a Ruin Maniac.
- **B1F.** A long cave split by a water channel, boulders to push (Strength, badge 4). The echo stones are here.
- **B2F.** A shorter floor, a bridge of stepping stones across a pool. A Black Belt and a Psychic.
- **Echo Chamber (dark cave).** Behind a sealed wall that opens when the three echo stones have been called in order. Needs **Flash** to light the map. The reward chest and a hidden ledge lie at the far end.
- **The puzzle.** Three **echo stones** (bg_events) on B1F: wall markings that answer in a deep voice. Stand on the stone, 'call out', and the cave answers with the opposite floor tone. The order is carved on a nearby pillar as three shapes (a wave, a bell, a spiral). Call in that order: the sealed wall opens. A wrong call just makes the cave sneeze dust. No time limit. No new tiles: reuse the vanilla sealed-wall and Braille-door scripts for the swap.
- **HMs used:** Strength (boulders on B1F), Surf (the pools), Flash (chamber), Rock Smash (a cracked wall to a side room with an item). Waterfall is not used here.

### Trainers (post-game, reuse vanilla ids)
| Floor | Class | Team |
|---|---|---|
| 1F | Hiker | Golem 68, Steelix 69, Rhyperior 70 |
| 1F | Hiker | Gliscor 69, Golurk 70, Magcargo 69 |
| 1F | Ruin Maniac | Sigilyph 69, Claydol 69, Bronzong 70 |
| B1F | Black Belt | Hariyama 70, Machamp 71, Lucario 72 |
| B1F | Psychic | Gallade 70, Alakazam 71, Reuniclus 71 |
| B2F | Cooltrainer male | Tyranitar 72, Hydreigon 72, Metagross 73 |
| B2F | Cooltrainer female | Weavile 72, Froslass 71, Mamoswine 73 |
| Chamber | Expert | Absol 73, Sableye 72, Kingambit 74 |

### NPCs
- A **cave guide** at the mouth: tells the player the stones answer if 'asked properly'.
- A **hermit** in a nook on B2F: gives the order hint and a Max Elixir. Topic: 'It repeats everything. I have stopped talking to it.'
- No shop, no Center.

### Wild Pokémon
Cave (1F, B1F, B2F), levels 68 to 74:

| Slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 20% | GOLEM | 68 to 70 |
| 2 | 20% | NOIVERN | 68 to 70 |
| 3 | 10% | SWOOBAT | 69 to 70 |
| 4 | 10% | SABLEYE | 69 to 70 |
| 5 | 10% | STEELIX | 70 to 71 |
| 6 | 10% | GLISCOR | 70 to 71 |
| 7 | 5% | DUSKNOIR | 71 to 72 |
| 8 | 5% | ABSOL | 72 |
| 9 | 4% | TYRANITAR | 73 |
| 10 | 4% | WEAVILE | 73 |
| 11 | 1% | HYDREIGON | 74 |
| 12 | 1% | KINGAMBIT | 74 |

Echo Chamber (dark cave), levels 72 to 76: same table shifted: GOLEM 72 to 73 (20%), NOIVERN 72 to 73 (20%), DUSKNOIR 73 to 74 (10%), SABLEYE 73 to 74 (10%), STEELIX 74 (10%), GLISCOR 74 (10%), TYRANITAR 75 (5%), WEAVILE 75 (5%), HYDREIGON 75 to 76 (4%), KINGAMBIT 75 to 76 (4%), SPIRITOMB 76 (1%), METAGROSS 76 (1%).
Cave pools, Surf (60/30/5/4/1): WHISCASH 68 to 72, GOLDUCK 68 to 72, LANTURN 70 to 72, SLOWKING 71 to 73, KINGDRA 72.
Old Rod (70/30): MAGIKARP 25 to 30, BARBOACH 25 to 30. Good Rod (60/20/20): GOLDEEN 45 to 50, BARBOACH 45 to 50, CARVANHA 45 to 50. Super Rod (40/40/15/4/1): WHISCASH 68 to 72, SEAKING 68 to 72, GYARADOS 70 to 72, SHARPEDO 70 to 72, MILOTIC 72.

### Items and secrets
| Item | Where | Gate |
|---|---|---|
| TM Earthquake | Echo Chamber chest (PROPOSED) | Echo stones solved, Flash |
| Max Revive, Rare Candy x2 | B2F and the chamber (visible) | None |
| Max Elixir | Hermit | Talk |
| PP Max | Side room (cracked wall) | **Rock Smash** (badge 2) |
| Everstone | B1F boulder nook | **Strength** (badge 4) |
| Heart Scale, Star Piece | Hidden in the cave | None |
| Nugget | B2F stepping stones (hidden) | None |

### Flags (not claimed)
`FLAG_ECHO_HOLLOW_STONE_1`, `_2`, `_3` (called), `FLAG_ECHO_HOLLOW_CHAMBER_OPEN`, `FLAG_RECEIVED_TM_EARTHQUAKE_ECHO`, `FLAG_RECEIVED_MAX_ELIXIR_ECHO`, `FLAG_ITEM_ECHO_HOLLOW_*` (visible items), `FLAG_HIDDEN_ITEM_ECHO_HOLLOW_*` (hidden), plus a var `VAR_ECHO_HOLLOW_STONES` (0 to 3 ordered progress).

### Build order and effort
**Medium to hard.** Four cave floors from Palladium art, each a straight trace (no new tileset features if Porymap has the cave tileset). The echo puzzle is three bg_events and a var. Build after R30.

### Open questions
1. Union Cave or Dark Cave as the main body? I used both: Union Cave for the three floors, Dark Cave (Flash) for the last chamber.
2. The 'echo' puzzle is mine: say if you want something different (switches, braille, a sliding-block floor).
3. The cave has no Center. Fine for a post-game landmark with a hub two roads away?

---

## ARGENT PEAK (post-game mountain; the toughest wild and trainer levels in the game, 70 to 85)

### Role
A tall snow-streaked mountain south-west of Hollowbrook, reached by R31. It is the post-game's hardest place: levels 70 to 85 for wild Pokémon and trainers, a base camp with a Pokémon Center, a cave with a waterfall climb and a summit. **It is where Troglodyte trains**, and where his post-game rematch happens (PROPOSED: 'one per region area', postgame.md). No named boss. The summit has a bench and a view of the whole region.

Gate: opens after the League. The R31 gate on Hollowbrook's south-west edge is held by a **ranger** (hide flag at game clear), see R31.

### Where it sits
South-west of Hollowbrook (the sketch's green landmark at the bottom left). One road in (R31), nothing else.

| Road | Edge | How |
|---|---|---|
| R31 from Hollowbrook | **Base Camp, south edge** | The mountain trail ends at the camp gate |
| (none) | other | A dead end by design |

### Source and size
Four Palladium Mt Silver images (the files exist in the asset repo; sizes measured from the PNGs):

| Map | Image | Size in tiles | Use |
|---|---|---|---|
| Base Camp (outdoor) | `mtsilver9no.png` (732 x 545, gridded) | **43 x 32** | A grassy mountainside with a Pokémon Center, a pond, trees, a cave mouth at the top |
| Entrance cave (1F) | `mtsilverentrance5uq.png` (290 x 545, gridded) | **17 x 32** | The first cave, ledges and stairs |
| Upper cave (2F) | `mtsilver27oa.png` (409 x 494, gridded) | **24 x 29** | Cave with three waterfalls (Waterfall to climb), a pond |
| Summit corridor | `mtsilberredplaceuhhhyeah6jn.png` (188 x 496) | about **12 x 31** | A long summit path, a bench and a rock ring at the end |

- **Vanilla alternative:** `MeteorFalls_1F_1R` (30 x 42) and `MtPyre_Exterior` (38 x 51) for the base camp and cave; `Route 45.png` (22 x 91) is R31.
- **Section id:** `MAPSEC_ARGENT_PEAK` (name `ARGENT PEAK`, 11 chars). All four maps share it.
- **Heal location:** the camp's Pokémon Center is a normal `LAYOUT_POKEMON_CENTER_1F` and `_2F`. A blackout from inside Argent Peak must have a respawn: add `HEAL_LOCATION_ARGENT_PEAK` (write `respawn_map` before `respawn_npc`), or let it share Hollowbrook's. It is not a Fly spot.

### Layout
- **Base Camp.** The R31 trail enters at the bottom. A grassy mountainside with a pond in the middle, trees, three trainers on ledges, and the **Pokémon Center** halfway up on the right (about 5 tiles from the right edge). A cave mouth at the top left leads to the entrance cave.
- **Entrance cave (17 x 32).** A winding cave with ledges, three boulders for Strength, a cracked rock for Rock Smash (a side nook), two trainers.
- **Upper cave (24 x 29).** The **waterfall climb**: three waterfalls need **Waterfall (badge 8)** to ascend, a pond needs Surf. Two trainers on the ledges. The stair to the summit is at the top of the third fall.
- **Summit corridor (12 x 31).** A long path with a stone ring at the top. A bench at the end. **Troglodyte** stands at the bench (PROPOSED), training and sulking.
- **HMs used:** Cut (a tree on the camp path), Strength, Rock Smash, Surf, Waterfall. Flash is optional (a dark side cave off the entrance cave).

### Trainers (post-game, the toughest in the game, 74 to 85; reuse vanilla ids; no IVs)
| Place | Class | Team |
|---|---|---|
| Camp | Hiker | Golem 74, Steelix 75, Rhyperior 75, Magcargo 74 |
| Camp | Black Belt | Hariyama 74, Machamp 75, Conkeldurr 75 |
| Camp | Cooltrainer female | Weavile 75, Mamoswine 75, Glaceon 74 |
| Camp | Psychic | Alakazam 75, Gallade 75, Gardevoir 75 |
| Camp | Cooltrainer male | Salamence 76, Metagross 76 |
| Entrance cave | Dragon Tamer | Dragonite 78, Kommo-o 78, Haxorus 79, Hydreigon 79 |
| Entrance cave | Expert | Tyranitar 78, Aggron 78, Lucario 79 |
| Upper cave | Hiker | Steelix 77, Golurk 77, Gliscor 78, Rhyperior 78 |
| Upper cave | Cooltrainer female | Garchomp 79, Froslass 78, Weavile 79, Mamoswine 79 |
| Summit approach | Cooltrainer male | Dragapult 82, Kingambit 82, Metagross 83, Salamence 83, Garchomp 83 |
| Summit bench | **TROGLODYTE (post-game rematch, PROPOSED)** | Stoutland 76, Gardevoir 77, Vaporeon 77, Tyranitar 78, Pyroar 78, starter final form 80 |

Troglodyte's team is the finale's six (postgame.md and troglodyte-arc.md fight 8: Stoutland 68, Gardevoir 69, Vaporeon 70, Tyranitar 70, Pyroar 70, starter final 72) raised by 8. He plays humbled and unpretentious. Not a new id; reuses a vanilla one.

### NPCs
- **Ranger at the camp gate**: the summit trail is 'closed in winter'. Opens at game clear. Warns of the trainers.
- **Camp nurse** and **camp clerk**: the Center and a stall (Max Potion, Revive, Full Heal, Ultra Ball).
- **Old climber**: gives the Waterfall hint and a Max Elixir.
- **Summit view sign**: a bench plaque, 'IN MEMORY OF A VERY STRONG ARGUMENT' (a deadpan joke).

### Wild Pokémon
Base Camp grass, levels 72 to 76. Standard rates.

| Slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 20% | GOLEM | 72 to 73 |
| 2 | 20% | URSARING | 72 to 73 |
| 3 | 10% | MISMAGIUS | 73 to 74 |
| 4 | 10% | MACHAMP | 73 to 74 |
| 5 | 10% | MAMOSWINE | 74 |
| 6 | 10% | MAGCARGO | 74 |
| 7 | 5% | STEELIX | 75 |
| 8 | 5% | WEAVILE | 75 |
| 9 | 4% | DRAGONAIR | 75 |
| 10 | 4% | GABITE | 75 to 76 |
| 11 | 1% | TYRANITAR | 76 |
| 12 | 1% | HYDREIGON | 76 |

Entrance cave and upper cave (cave), levels 75 to 80:

| Slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 20% | TYRANITAR | 75 to 77 |
| 2 | 20% | STEELIX | 75 to 77 |
| 3 | 10% | MAMOSWINE | 76 to 78 |
| 4 | 10% | WEAVILE | 76 to 78 |
| 5 | 10% | METANG | 77 to 78 |
| 6 | 10% | MACHAMP | 77 to 78 |
| 7 | 5% | MISMAGIUS | 78 to 79 |
| 8 | 5% | GOLURK | 78 to 79 |
| 9 | 4% | HYDREIGON | 79 to 80 |
| 10 | 4% | DRAGONITE | 79 to 80 |
| 11 | 1% | METAGROSS | 80 |
| 12 | 1% | SALAMENCE | 80 |

Summit corridor (cave or rough), levels 80 to 85:

| Slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 20% | TYRANITAR | 81 to 83 |
| 2 | 20% | GARCHOMP | 81 to 83 |
| 3 | 10% | METAGROSS | 82 to 84 |
| 4 | 10% | HYDREIGON | 82 to 84 |
| 5 | 10% | SALAMENCE | 82 to 84 |
| 6 | 10% | KINGAMBIT | 83 to 85 |
| 7 | 5% | URSALUNA | 83 to 85 |
| 8 | 5% | DRAGONITE | 83 to 85 |
| 9 | 4% | RHYPERIOR | 84 |
| 10 | 4% | MAMOSWINE | 84 |
| 11 | 1% | SPIRITOMB | 85 |
| 12 | 1% | DRAGAPULT | 85 |

Camp pond, Surf (60/30/5/4/1): GOLDUCK 72 to 76, AZUMARILL 72 to 76, WHISCASH 73 to 76, LAPRAS 74 to 76, GYARADOS 76. Upper cave pond (Surf): same species, levels 77 to 80.
Fishing, all ponds: Old Rod (70/30) MAGIKARP 25 to 30, BARBOACH 25 to 30. Good Rod (60/20/20) GOLDEEN 45 to 50, PSYDUCK 45 to 50, BARBOACH 45 to 50. Super Rod (40/40/15/4/1) GOLDUCK, WHISCASH, SEAKING at 72 to 76, GYARADOS 76 to 78, MILOTIC 78.

No legendaries are used. The summit's wild levels (up to 85) exceed the Champion's ace (75), which is the point of the post-game.

### Items and secrets
| Item | Where | Gate |
|---|---|---|
| Rare Candy x3 | Camp ledge, entrance cave, summit (visible) | None |
| PP Max x2 | Upper cave (visible), side nook | Rock Smash for one |
| Max Revive x2, Full Restore | Caves (visible) | None |
| Leftovers | Summit rock ring | Waterfall (reach the summit) |
| Everstone | Entrance cave nook | **Strength** |
| TM Hyper Beam | Upper cave ledge | Waterfall |
| Max Elixir | Old climber | Talk |
| Ability Patch | Summit bench, after the Troglodyte fight (PROPOSED) | Beat him |
| Star Piece, Nugget | Hidden in caves | None |

### Flags (not claimed)
`FLAG_ARGENT_PEAK_OPEN` (game clear, hides the ranger), `FLAG_ITEM_ARGENT_PEAK_RARE_CANDY_1` to `_3`, `FLAG_RECEIVED_ABILITY_PATCH_ARGENT`, `FLAG_ARGENT_PEAK_TROG_DEFEATED`, hidden item flags `FLAG_HIDDEN_ITEM_ARGENT_PEAK_*`.

### Build order and effort
**Hard.** Four maps from Palladium images, the heaviest wild and trainer data (11 trainers, 36 wild slots), a Pokémon Center and a heal location. Build last.

### Open questions
1. Argent Peak is meant to be 'the toughest place'. I added no boss and no legendaries. Do you want a summit boss (an old trainer, or Cynthia herself)?
2. Troglodyte's rematch here is mine, from 'one per region area' in postgame.md.
3. Mt Silver's Johto location is south-west of Johto; here it is south-west of Hollowbrook, so it matches the sketch.
4. Is a Pokémon Center on a landmark acceptable, or only the hub's Center?
