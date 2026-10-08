# Landmarks, west group: Mothwood, Slagwell Mine, Hoarfell Ice cave

> **Mothwood moved (author, 2026-10-08):** the maze now **branches off R8** (Wendlebury to Briarwick), not off Briarwick by R9, which is dropped. R8 opens after badge 2, so Mothwood does too. Its entrance gate needs re-placing on R8 when the maze is designed.


Status: **PROPOSED.** Names approved 2026-10-01 for Mothwood and Slagwell Mine ([../region-names.md](../region-names.md)); the Ice cave is unnamed in the sketch ("Inside Hoarfell"). Conventions, templates and the level curve: [README.md](README.md). Roads: [routes-west.md](routes-west.md). Towns: [towns/briarwick.md](towns/briarwick.md), [towns/smeltham.md](towns/smeltham.md), [towns/hoarfell.md](towns/hoarfell.md).

Sizes: Palladium images with a 1 px grid are `(px - 1) / 17`, others `px / 16`. Section ids are not decided (suggested names only). All three are **optional** for the story. Credit Project Palladium team in `CREDITS.md` with the first map traced. Trainers reuse vanilla ids (CLAUDE.md), no IVs, Pokémon only. Rates for land: 20/20/10/10/10/10/5/5/4/4/1/1. Water and rod slot counts follow vanilla: Surf and Rock Smash 5 slots (60/30/5/4/1), Old Rod 2 (70/30), Good Rod 3 (60/20/20), Super Rod 5 (40/40/15/4/1).

---

## MOTHWOOD (forest maze, off Briarwick)

### Role
An optional forest maze north-east of Briarwick, reached by R9. A Bug-type playground: bug trainers, the gym's themed grass, a shrine, a lot of items behind early HMs. It is a **return** destination: the first visit (after badge 1, with Cut) opens the maze, later visits (Strength, Surf, Waterfall) open the rest. It is nowhere on the main path, so it can be built last.

### Where it sits and how it is entered
- **South-west gatehouse** (a grey building at the bottom-left of the render) is the entrance from R9. The player walks in from the south.
- **North-west gatehouse** (the grey building at the top-left of the render) is the Warden's Lodge: a closed gatehouse that becomes a small reward room after the player completes the maze (see Items). It does **not** connect to another road.
- No other exits. Mothwood is a dead end (author's sketch: a green landmark with one line).

### Source and size
- Palladium **Ilex Forest** (`ilexforesttiled0ry.png`, **about 54 x 67 tiles** by `px / 16` since the grid is not 17-based; same layout as `ilexforest5dh.png`).
- Size check: (54 + 15) x (67 + 14) = 5,589 of 10,240. Fine. Map section: a new id (`MAPSEC_MOTHWOOD`, or reuse a Hoenn landmark row if the budget runs short, see [../region-sketch.md](../region-sketch.md) budget).
- Tileset: the vanilla Hoenn forest set (`Route 119`/Petalburg Woods tiles) covers the trees and short grass; the paths are plain.

### Layout
- A **tall-tree maze** in the middle. The picture shows a tight lattice of single-tile corridors, with grass pockets at junctions (that is where the wild grass goes, not everywhere).
- **Small pond** in the upper left (about 5 x 3), a little square of water. Fishing only until Surf.
- **The shrine** (a small grey pavilion with a rope) at the middle, off the main corridor. It gives the maze its centre, and holds the best item in the map. Open question 2 asks what it enshrines.
- **Three Cut trees** block shortcuts. **Two Rock Smash rocks** and **three Strength boulders** hide the side pockets.
- The route through the maze is a **spiral**: enter at the bottom-left, go right, up, left, up again, finish at the shrine. A **fence line** half-way (the red short fence at the render's upper right) is a one-way ledge for returning visitors.
- Door positions: south-west gatehouse door faces south, north-west gatehouse door faces south onto the maze.

### Wild Pokémon (levels 15 to 18; gym 2 ace is 19, minus 3 is 16)

| Slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 20% | SPINARAK | 15 to 16 |
| 2 | 20% | LEDYBA | 15 to 16 |
| 3 | 10% | PARAS | 16 |
| 4 | 10% | PINECO | 16 to 17 |
| 5 | 10% | VENIPEDE | 16 to 17 |
| 6 | 10% | SEWADDLE | 16 to 17 |
| 7 | 5% | BURMY | 17 |
| 8 | 5% | SHROOMISH | 17 |
| 9 | 4% | FOONGUS | 17 to 18 |
| 10 | 4% | JOLTIK | 17 to 18 |
| 11 | 1% | HERACROSS | 18 |
| 12 | 1% | PINSIR | 18 |

Fishing in the pond (freshwater; all slots checked): Old Rod MAGIKARP 10 (70), POLIWAG 10 (30); Good Rod POLIWAG 13 (60), MARILL 13 (20), WOOPER 13 (20); Super Rod MARILL 15 (40), WOOPER 15 (40), POLIWAG 16 (15), PSYDUCK 16 (4), CORPHISH 16 (1). Surf (after badge 5): WOOPER 14 to 18 (60), MARILL 14 to 18 (30), PSYDUCK 16 (5), POLIWAG 16 (4), CHINCHOU 18 (1).

### Trainers (6, all Bug flavour, 14 to 17; leader's lowest is 17)

| Class | Team |
|---|---|
| Bug Catcher (north-west corner) | KAKUNA 14, METAPOD 14 |
| Bug Catcher (first fork) | LEDYBA 15, SPINARAK 15 |
| Bug Catcher (pond side) | PARAS 15, VENIPEDE 16 |
| Camper (boulder pocket) | SEWADDLE 15, PINECO 16 |
| Picnicker (shrine path) | COMBEE 15, BURMY 15, SHROOMISH 16 |
| Collector (by the shrine) | VOLBEAT 16, ILLUMISE 16 |

### NPCs (6, PROPOSED)
- A lost visitor who has been in the maze 'since lunch', offers a hint (turn right at the second fence).
- The Warden (PROPOSED name Alder, in the lodge): explains the maze, gives the reward when the shrine is reached.
- A guide at the entrance with a hand-drawn map who sells it for a joke price (no real map item needed; he describes the first two turns).
- A child who has hidden an item and will not say where.
- A signpost at each junction with a different, equally useless direction ('THAT WAY. PROBABLY').
- A shrine keeper at the pavilion: tells the story (PROPOSED: a shrine for a Pokémon that watches over the wood, see Open question 2).

### Items and secrets

| Item | Where | Gate |
|---|---|---|
| POTION | entrance corridor, visible | none |
| PARALYZE HEAL | first fork, visible | none |
| NET BALL x2 | north-west pocket, visible | none |
| HONEY | hidden, a hollow tree | none |
| TINY MUSHROOM | hidden, pond side | none |
| REPEL | hidden near the first sign | none |
| ANTIDOTE | hidden, boulder pocket | Strength (badge 4) |
| SILVER POWDER | pocket behind a Cut tree | Cut (badge 1) |
| BIG MUSHROOM | pocket behind a rock | Rock Smash (badge 2) |
| REVIVE | pocket behind boulders | Strength (badge 4) |
| ELIXIR | island in the pond | Surf (badge 5) |
| TM Giga Drain | the shrine, a reward for the whole maze | none (reach the shrine) |
| Warden's gift: RARE CANDY | the Lodge, after the shrine | none |

### Gate
No gate on entry; deeper pockets need Cut, Rock Smash, Strength and Surf. No Goldsworth beat. No Troglodyte fight.

### Flags (not claimed)
`FLAG_MOTHWOOD_SHRINE_VISITED`, `FLAG_MOTHWOOD_GIFT_RECEIVED`, one `FLAG_MOTHWOOD_ITEM_*` per item, and one per trainer (the reused trainer ids carry their own). Existing `FLAG_RECEIVED_HM_*` are reused.

### Build effort
**Medium to hard.** The maze is a single large map, mostly trees (cheap to paint in Porymap, tedious to trace), but its size and the many pockets make it long. The gatehouse interiors are tiny. Build after Briarwick, R9 and the gym.

### Open questions
1. Should the Lodge door be the maze's second exit toward a later place (for example a shortcut back to Briarwick's north gate)?
2. What does the shrine enshrine? A one-off wild Pokémon, a plain shrine, or a post-game mythical? Nothing is assumed here.
3. Do you want the maze to be solvable without any guide NPC? The spiral above takes about 120 steps.

---

## SLAGWELL MINE (cave off R6, east of Smeltham)

### Role
An optional mine on the spur road R7. A real working mine gone quiet: ore, tracks, and a flooded lower chamber. Items are plentiful, and several need a later HM, so it is a **revisit** cave. No scheme beat. The cave is also where a Smeltham NPC says 'the foundry takes its ore from here', which ties the town to its mountain.

### Where it sits
- **Entrance:** a door at the top (north) of R7 (the Route 46 render's cave door). From the cave side this is the **south** exit, the bottom-centre exit of the first floor (the yellow door at the bottom of the render).
- **Two further exits** on the first floor (bottom-left and bottom-right in the Mortar renders) are **closed** (sealed with rubble, Rock Smash opens them later) and lead to short dead-end pockets with items.
- The mine has **no other road connection** (dead end).

### Source and size
- Palladium **Mt Mortar**: four views of one big cavern with a pool and a waterfall. `mtortar3xm.png` (**39 x 35**, 1 px grid) shows the first floor with item and ladder marks (yellow door at the bottom), `mtortar6bl.png` and `mtortar6bo.png` (both **39 x 35**) show the same cavern with other marks, and `mtmortar4jh.png` (**40 x 37**) shows it with darker stone and the waterfall room.
- **My reading (unclear, see Open question 1):** the four images are the same big cavern as it appears on different floors and variants in Johto, so I propose **three Veldris maps** that share this look: Mine 1F (from `mtortar3xm`), Mine Upper (the ledge level, from `mtortar6bo`, with its rock field at upper right), and the Waterfall Chamber (from `mtmortar4jh`). They share one tileset so the author can copy the 1F blocks and rework them.
- Sizes: (39 + 15) x (35 + 14) = 2,646 each; (40 + 15) x (37 + 14) = 2,805. Fine. Vanilla base: Granite Cave or Meteor Falls, which have the stone, ladders and waterfalls.
- Section: new id (`MAPSEC_SLAGWELL_MINE`).
- The cave is **dark** by header setting (requires Flash, which the player gets at Gloomsby). Without Flash the first floor stays navigable but harder. Do not make it Flash-locked.

### Layout in words
- **1F:** a big central pool with a waterfall splitting it (top to middle), ledges on both sides holding floor patches, ladders up to the upper level on the left and right ledges. The entrance at the bottom centre, with a stone path around the lower pool to the sides. A rock field on the lower right.
- **Upper:** two big plateaus either side of the waterfall, a bridge-like island in the lower pool (the platform with a ladder). Reached by ladders from 1F.
- **Waterfall Chamber:** the top pool with the waterfall dropping from the north. Reached by Surf from 1F, then **Waterfall** (badge 8) up the fall.
- **Objects:** 15 or fewer per map. Ore carts and pick-axes are decoration (tile or object).

### Wild Pokémon

Cave grass (levels 31 to 36; R6 ends near 33 and Smeltham's ace is 31, so the mine can run 3 higher):

| Slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 20% | ZUBAT | 31 to 33 |
| 2 | 20% | BOLDORE | 32 to 33 |
| 3 | 10% | GEODUDE | 31 to 32 |
| 4 | 10% | WOOBAT | 31 to 33 |
| 5 | 10% | MAGNEMITE | 32 to 33 |
| 6 | 10% | ONIX | 32 to 33 |
| 7 | 5% | GOLBAT | 34 |
| 8 | 5% | DWEBBLE | 34 |
| 9 | 4% | SKORUPI | 34 |
| 10 | 4% | GRAVELER | 34 to 35 |
| 11 | 1% | SHUCKLE | 35 |
| 12 | 1% | LARVITAR | 35 |

Surf (after badge 5, underground pool): WOOPER 30 to 34 (60), BARBOACH 30 to 34 (30), PSYDUCK 32 to 36 (5), QUAGSIRE 36 (4), CHINCHOU 34 to 36 (1). Fishing: Old Rod MAGIKARP 15 (70), BARBOACH 15 (30); Good Rod BARBOACH 25 (60), WOOPER 25 (20), GOLDEEN 25 (20); Super Rod WOOPER 30 (40), BARBOACH 30 (40), GOLDEEN 30 (15), PSYDUCK 32 (4), WHISCASH 34 (1). Rock Smash: DWEBBLE 30 to 34 (60), GEODUDE 30 to 34 (30), BOLDORE 33 (5), NOSEPASS 33 (4), SHUCKLE 33 (1).

### Trainers (6, 29 to 34)

| Class | Team | Where |
|---|---|---|
| Hiker | GEODUDE 29, ONIX 30 | 1F entrance |
| Hiker | ROGGENROLA 30, BOLDORE 31 | 1F left ledge |
| Black Belt | MACHOP 30, TIMBURR 31 | 1F right ledge |
| Collector | MAGNEMITE 31, KLINK 31 | upper left plateau |
| Guitarist | MAGNEMITE 32, KLINK 32 | upper right plateau |
| Hiker (the mine's foreman) | ONIX 32, GRAVELER 33, NOSEPASS 33 | upper, by the ladder |

### NPCs (4, PROPOSED)
- Mine clerk (outside, in Smeltham's mine office) and an old miner in the cave who talks about 'the day the lights went out'.
- A worker 'on lunch' by the first ladder (continuing Smeltham's joke).
- A hiker who has lost his torch (hint: Flash).
- A rest cot by the pool: the player may heal (NPC gives one free Potion, once).

### Items and secrets

| Item | Where | Gate |
|---|---|---|
| POTION | 1F entrance, visible | none |
| ESCAPE ROPE | 1F lower right, visible | none |
| REPEL | upper left, visible | none |
| HARD STONE | hidden, 1F rock field | none |
| ETHER | upper right, visible | none |
| TM Rock Tomb | 1F, a ladder-side pocket | none (also given by the Smeltham clerk, see town card) |
| IRON | right ledge pocket | Rock Smash (badge 2) |
| REVIVE | behind rubble, bottom-left exit pocket | Rock Smash (badge 2) |
| CARBOS | behind boulders, upper left | Strength (badge 4) |
| RARE CANDY | island platform in the lower pool | Surf (badge 5) |
| MAX ETHER | Waterfall Chamber ledge | Waterfall (badge 8) |
| NUGGET | Waterfall Chamber, hidden | Waterfall (badge 8) |
| BIG PEARL | Waterfall Chamber, hidden in the fall | Waterfall (badge 8) |

### Gate
No gate on entry. Flash makes the cave easier but is not required. The deepest items need Surf and then Waterfall, so this is the first place the player cannot finish on the first visit, deliberately.

### Flags (not claimed)
`FLAG_SLAGWELL_*` per item and per trainer reused id; `FLAG_SLAGWELL_VISITED` (set on entry, for the Smeltham clerk's hint). No story flag.

### Build effort
**Medium.** Cave tilesets exist in vanilla; the pool and waterfall are copyable from Meteor Falls. Three maps with ladders and warps. Build after Smeltham, R6 and R7.

### Open questions
1. The four Mt Mortar images look like one cavern. Are they four floors, four variants, or something else? I assumed variants and proposed three maps (1F, Upper, Waterfall Chamber).
2. Should the sealed exits (bottom-left, bottom-right) be real Rock Smash shortcuts?
3. Does the author want a legendary or a unique encounter at the Waterfall Chamber, or is item-only fine?

---

## HOARFELL ICE CAVE (optional, inside Hoarfell)

### Role
An optional frozen cave behind Hoarfell, entered from the two small doors in the cliffs of the town (see [towns/hoarfell.md](towns/hoarfell.md)). It is the place for slide puzzles and one good TM. Not required for the story.

### Where it sits
- **Entrance:** the north-centre door above the frozen lake, opening onto the first floor. The **second door** on the north-east shelf is the cave's far exit: it lets the player return to town without crossing the ice again. That gives the cave a loop.
- No road connection. When Hoarfell is reached from R6, the cave is available at once.

### Source and size
Palladium **Ice Path**, five images (all 1 px grid):

| Floor | Image | Tiles | Idea |
|---|---|---|---|
| 1F | `icepathf10va.png` | 43 x 33 | a big frozen field in the upper left, rock ledges and a spiral, a ladder in the right, two exits (bottom left and bottom right) |
| B1F | `icepathbasement112dw.png` | 26 x 23 | a maze of ice pillars with four holes (drop to the floor below) |
| B2F | `icepathbasement125fx.png` | 24 x 20 | two ledged rooms and a sliding patch in the lower right |
| B3F | `icepathbasement136kk.png` | 25 x 17 | a cramped room with two ladders and an odd green square |
| B4F | `icepathbasement216nd.png` | 26 x 24 | a huge slide floor, ladder up-right, island in the middle with an item |
| Annex | `icepathbasement229gg.png` | 16 x 22 | a small slide room, an item at the top, a ladder at the bottom |

I propose **four** maps in the build: 1F, B1F, B4F (the slide room) and the Annex, skipping B2F and B3F unless the author wants a longer cave. (B2F and B3F look like connectors.) Sizes: all are well inside the limit (the largest is (43 + 15) x (33 + 14) = 2,726).

Tileset: vanilla Hoenn has no ice-cave set except **Shoal Cave** (ice variant) and Sootopolis-like ice floors; Shoal Cave's low-tide ice room is the right base. Section: Hoarfell's own (interior reuse) or a new `MAPSEC_HOARFELL_CAVE`.

### Wild Pokémon (levels 33 to 37; gym 5 ace is 37)

| Slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 20% | SWINUB | 33 to 34 |
| 2 | 20% | SNORUNT | 33 to 34 |
| 3 | 10% | WOOBAT | 33 to 34 |
| 4 | 10% | CUBCHOO | 34 to 35 |
| 5 | 10% | VANILLITE | 34 to 35 |
| 6 | 10% | BERGMITE | 34 to 35 |
| 7 | 5% | SNEASEL | 35 to 36 |
| 8 | 5% | SMOOCHUM | 34 to 35 |
| 9 | 4% | DELIBIRD | 35 to 36 |
| 10 | 4% | PILOSWINE | 36 |
| 11 | 1% | CRYOGONAL | 37 |
| 12 | 1% | GLALIE | 37 |

Surf is not available in the cave (no water). Fishing is not possible. A Rock Smash rock set on B1F: GEODUDE 33 (60), SWINUB 33 (30), SMOOCHUM 34 (5), SNEASEL 35 (4), BERGMITE 35 (1).

### Trainers (4, 31 to 36)

| Class | Team |
|---|---|
| Hiker (1F) | SWINUB 31, SNORUNT 32 |
| Lass (B1F) | VANILLITE 32, CUBCHOO 33 |
| Fisherman (B4F, ice fishing in a hole) | SEEL 33, SPHEAL 33 |
| Hiker (Annex) | PILOSWINE 34, BERGMITE 34 |

### Items and secrets

| Item | Where | Gate |
|---|---|---|
| ICE HEAL | 1F, visible | none |
| NEVER-MELT ICE | town shelf (see Hoarfell card) | none |
| PROTEIN | B1F, visible | none |
| TM Hail | B1F, ledge behind pillars | none |
| RARE CANDY | B1F, hidden, a hole-side ledge | none |
| REVIVE | B4F island | none (slide to it) |
| TM Blizzard | Annex, at the top | slide puzzle |
| MAX ELIXIR | B4F corner | Strength (badge 4) |
| NUGGET | 1F, hidden | Rock Smash (badge 2) |

### Gate
None. Entirely optional. **Strength** opens one boulder pocket; **Rock Smash** opens one rock.

### Flags (not claimed)
`FLAG_HOARFELL_CAVE_*` per item; the reused trainer ids carry their own. No story flag.

### Build effort
**Hard**, because of tile art: ice floors that slide (the vanilla ice-floor tiles in Shoal Cave and Sootopolis do this), plus the frozen lake outside. Sliding puzzles need testing. Cut to two maps (1F and Annex) if effort is a problem.

### Open questions
1. Are the two cave doors in the Blackthorn render the intended entrance and exit, or should the north-east door be a second entrance to the same floor?
2. Should Hoarfell's cave hold any one-off Pokémon (for example a lone legendary)? None is assumed.
3. Keep B2F and B3F (a longer cave) or skip them?
