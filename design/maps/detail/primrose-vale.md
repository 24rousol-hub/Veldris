# PRIMROSE VALE, detailed design (city, place 13, gym 8 Fairy)

Status: **PROPOSED**, written 2026-10-01. Nothing here is built; minor names are marked PROPOSED. Adds detail to [../towns/primrose-vale.md](../towns/primrose-vale.md), following [../interiors/README.md](../interiors/README.md). Style reference: [../../interiors.md](../../interiors.md). Catalogue: [../interiors/catalogue.md](../interiors/catalogue.md). Roads: [routes-east-detail.md](routes-east-detail.md). Landmark: [mirror-isle-detail.md](mirror-isle-detail.md). Sister towns: [hemlock-reach.md](hemlock-reach.md) and [brinecombe.md](brinecombe.md). House layouts follow the templates G4-A, G4-B, G4-C of [ebbsworth.md](ebbsworth.md) 6.0 and the shared Goldsworth layout of [kingsquay.md](kingsquay.md) 6.10.

**Coordinates:** `(x,y)` tiles from the top-left `(0,0)` as Porymap shows them. In an interior the top two rows are back wall and the exit mat is on the bottom row. Exterior building footprints are estimates; door tiles matter. **Pokémon only**: no real animals, even in names or jokes, and plant jokes are fine. Primrose Vale is a **Surf-only pocket on purpose** (author, 2026-10-01): its only link by land is R15, and R15 starts at a town reached by water.

## 1. Description

**First glance.**
- **From R15 (the south, the way most players arrive).** The road squeezes between two walls of trees and comes out through a low gate arch onto a paved court. A red flower bed sits to the right, benches on both sides, and an avenue of pale stone runs straight ahead, north, between two buildings, to a **fountain shaped like a cross**. Beyond it two green diamonds of meadow open out like wings. At the very top of the picture, on its own lawn, stands the gym.
- **From the lake (R17, the west).** A short wooden pier on a sandy shore, then a tree belt with one gap in it, then the ring of fenced paths. The petals reach the water.
- Everything is clipped, scented and laid out in rings, like a park that has been told it will be inspected.

**Mood and colour.** Soft morning light, pale stone, green, and rose-red. A light breath of blossom drifts on the music; there is no weather. Weather: none (`WEATHER_NONE`), because a blossom effect does not exist (open question 6).

**Sound.** Music suggestion: town `MUS_VERDANTURF` (soft and slow), gym `MUS_GYM`, Center `MUS_POKE_CENTER`, florist `MUS_PETALBURG` (as the vanilla flower shop).

**The memorable view.** From the south court, looking up the avenue to the fountain, with both diamonds of meadow spread behind it and the gym a toy at the top of the lawn.

## 2. Source, size, tilesets

| Item | Decision |
|---|---|
| Palladium render | **`nationalpark5lb.png`** (766 x 1072 px, 1 px grid, `(px-1)/17` = **45 x 63 tiles**). Credit the Project Palladium team by file name in `CREDITS.md` in the commit of the first trace ([../../map-plan.md](../../map-plan.md)). |
| Base to duplicate | Vanilla `VerdanturfTown` (`LAYOUT_VERDANTURF_TOWN`, 20 x 20, `gTileset_General` + `gTileset_Petalburg`); Verdanturf is the closest garden town. The Palladium image has no map file, so it is traced by eye. |
| Final size | **56 x 63** = the picture's 45 columns, shifted **11 columns east** (every picture `x` becomes `x + 11`), with the new west 11 columns as the lakeshore. (56 + 15) x (63 + 14) = 5467, under 10240. |
| Tilesets | `gTileset_General` (now the LeoB ORAS recolour) + `gTileset_Petalburg` (same, recoloured), the same pair Hollowbrook uses. Flowers, pale paving, round trees, fences and benches are in them. The render's pine trees do not exist; use the round trees. No new import. |
| Section | New `MAPSEC_PRIMROSE_VALE` (PROPOSED). Interiors share it. |
| Fly and heal | One row in `src/data/veldris_fly_towns.h` plus the checklist in [../../region-map.md](../../region-map.md). Heal location `HEAL_LOCATION_PRIMROSE_VALE` at `(30,47)` (in front of the Center door), `respawn_map` before `respawn_npc`, both given. `FLAG_VISITED_PRIMROSE_VALE` on transition. |

### Render landmarks, in map coordinates (picture `x` plus 11)

I read these off the render with a tile ruler; verify when tracing.

| Feature in the render | Picture `(x,y)` | Map `(x,y)` | Becomes |
|---|---|---|---|
| Top signpost and fenced oval | `x 17 to 30, y 7 to 9` | `x 28 to 41, y 7 to 9` | The oval is the fence in front of the gym lawn |
| North diamond of tall grass | `x 10 to 37, y 10 to 22` | `x 21 to 48, y 10 to 22` | **Flower meadow** (decorative, no encounter), with the flags |
| Cross-shaped fountain pond | vertical arm `x 20 to 25, y 19 to 25`, horizontal arm `x 18 to 29, y 23 to 25`, stem `x 22 to 25, y 26 to 29` | vertical `x 31 to 36`, horizontal `x 29 to 40`, stem `x 33 to 36` | The fountain, decorative, no encounters |
| South diamond of ground cover | `x 10 to 36, y 26 to 37` | `x 21 to 47, y 26 to 37` | Flower beds |
| East gate building | `x 41 to 44, y 21 to 26` | `x 52 to 55, y 21 to 26` | **Goldsworth house** |
| Avenue from the fountain to the court | `x 22 to 25, y 38 to 47` | `x 33 to 36, y 38 to 47` | The central avenue, 4 tiles wide |
| South court (fenced) | `x 14 to 38, y 47 to 57` | `x 25 to 49, y 47 to 57` | South court |
| Red flower bed | `x 27 to 35, y 50 to 53` | `x 38 to 46, y 50 to 53` | Red bed, decorative |
| South gate building | `x 15 to 20, y 57 to 62` | `x 26 to 31, y 57 to 62` | **Dropped** and replaced by a gate arch (the player walks through, R15 arrives here) |
| Tree belts | the outer 3 columns, the lower west block `x 6 to 12, y 37 to 60` | `x 11 to 13`, `x 17 to 23, y 37 to 60` | Forest wall, with gaps for the paths |

## 3. Street layout, a numbered walk

North is up. The sea (lake) is west.

1. **R15 gate.** The road arrives at `x 26 to 29, y 62`, a 4-tile opening. An arch (decor, `x 25 to 30, y 60`) frames it. Trees on both sides. A sign at `(24,61)`: PRIMROSE VALE, KEEP TO THE PATHS.
2. **South court.** `x 25 to 49, y 47 to 57`, paved, fenced on three sides, benches at `x 26 to 30, y 48` and `x 38 to 46, y 48`, the red bed `x 38 to 46, y 50 to 53`. A sign at `(31,55)`: the court's name board (flavour). The Pokémon Center and the Mart stand on the north edge, either side of the avenue.
3. **Pokémon Center** at `x 27 to 31, y 42 to 46`, door `(29,46)`. **Mart** at `x 38 to 41, y 43 to 46`, door `(39,46)`. Both doors face south into the court; the card said they face north into the court, which Gen 3 buildings cannot, so they are on the court's north side facing the court (open question 5).
4. **Florist 'Petal and Pot' (PROPOSED)** at the south-east corner outside the court fence, `x 50 to 54, y 52 to 56`, door `(52,56)`, reached by a gap in the east fence at `(49,56)` and a short path along `y 57`.
5. **Central avenue north.** From the court the avenue (`x 33 to 36`) runs north through a gap in the tree line `y 38 to 46` to the ring.
6. **Central Garden, the ring.** The fenced path ring (original `x 6 to 38`, map `x 17 to 49`, `y 17 to 37`) circles the fountain. Four quarters of beds around the pond. The two diamonds of meadow are decorative. A sign at `(43,38)` (the render's red sign at the avenue's top right): CENTRAL GARDEN.
7. **Houses on the flanks.** **House A** (retired florist) at `x 18 to 21, y 31 to 34`, door `(19,34)`; **House B** (petal-press family) at `x 48 to 51, y 31 to 34`, door `(49,34)`. Both face south onto the ring path.
8. **Goldsworth house on the east edge.** `x 52 to 55, y 21 to 25`, door `(53,25)`, behind iron railings (`x 50 to 56, y 20 to 27`) with a gate gap at `(51,25)`. The path from the ring reaches it through a gap in the east fence at `(49,25)`. A gold knocker, a view of nothing. The card said the door faces west; it faces south here (open question 5).
9. **The Glade, north.** The gym stands at `x 31 to 37, y 3 to 7`, door `(34,7)`, behind the render's fenced oval. In front of it the long **lawn** `x 22 to 47, y 8 to 17` (the north diamond, as flower meadow). **This is where Scheme 8 plays out.** A gap in the ring fence at `x 32 to 37, y 18` leads up onto the lawn. Behind the gym, a quiet strip at `y 2` holds a hidden PP UP at `(34,2)`.
10. **West shore.** The tree belt (`x 11 to 13`) has one gap at `y 28 to 31`. Beyond it a **sand shore** `x 4 to 10`, **lake water** `x 0 to 3, y 14 to 46`, and a **wooden pier** `x 2 to 8, y 29 to 30`. The player steps to the pier end `(2,29)` and uses Surf for R17. The R17 connection is the 10-tile stretch `x 0, y 24 to 33`. A **NW bluff** `x 3 to 10, y 8 to 12` has a one-way ledge row `x 4 to 9, y 13` hopping down to the shore; the bluff holds a RARE CANDY at `(4,9)` behind a Strength boulder at `(6,10)`. A **Rock Smash rock** at `(8,40)` on the south-west shore hides a NUGGET.
11. **Central Garden secrets.** A Cut tree at `(20,27)` guards a TM Giga Drain at `(20,26)`; hidden MAX REPEL at `(26,30)`, hidden REVIVE at `(32,28)` on the fountain edge.

### Connections

| Edge | Map | Offset | Matching tiles |
|---|---|---|---|
| South | `Route15` (R15, 30 x 54) | Primrose `down` offset `+14` (R15 `x 0` sits at Primrose `x 14`) | R15 `x 12 to 15` meets Primrose `x 26 to 29` |
| West | `Route17` (R17, 56 x 20) | Primrose `left` offset `+19` (R17 row 0 sits at Primrose row 19) | R17 rows 5 to 14 meet Primrose rows 24 to 33 (lake) |
| North, East | none | | |

Recompute when the maps exist.

## 4. Palette and tile notes

- **Meadow:** both diamonds are painted with flower tiles over short grass (no tall grass, no encounters). Use three colours in a pattern, never all one.
- **Paving:** the pale stone tile of Petalburg for the ring, the avenue and the court. The fence rows are the standard fence tiles.
- **Fountain:** vanilla has no cross-shaped fountain. Paint the pond with the water tiles and a stone rim from Petalburg or Verdanturf; the four water jets of the render are decoration to skip.
- **Weather:** none. The 'drifting blossom' of the card is not available.
- **Needs redrawing:** nothing for a first playable version.

## 5. Every building

### 5.1 Pokémon Center (`PrimroseVale_PokemonCenter_1F`, `_2F`)

Shared `LAYOUT_POKEMON_CENTER_1F` and `_2F` (decision 2). Nurse `(7,2)` (needs `LOCALID_PRIMROSE_NURSE`), counter `x 4 to 9, y 2 to 3`, door mats `(6,8)` and `(7,8)`, stairs `(1,6)`. Two NPCs: a **customer** `(10,6)` facing left and a **gardener on a break** `(5,5)` wandering. Warps: `(6,8)` and `(7,8)` to `PrimroseVale` warp 0 (tile `(29,46)`).

### 5.2 Mart (`PrimroseVale_Mart`)

Shared `LAYOUT_MART` (11 x 8): clerk `(1,3)`, counter `x 2, y 2 to 4`, door mats `(3,7)` and `(4,7)`. NPCs: a shopper `(5,5)` and an old man `(9,5)`. Stock leans to Revive, Max Repel, Full Heal. Warps: `(3,7)` and `(4,7)` to `PrimroseVale` warp 1 (tile `(39,46)`).

### 5.3 Florist 'Petal and Pot' (PROPOSED, `PrimroseVale_Florist`)

- **Layout:** the vanilla flower shop **`LAYOUT_ROUTE104_PRETTY_PETAL_FLOWER_SHOP`**, 15 x 9, Pretty Petal Flower Shop secondary, as a shared layout. Its facts (checked in the tree): shop owner `(0,3)` facing right behind a counter at `x 1, y 2 to 4`; a girl `(7,3)` wandering; a second girl `(11,6)`; door mats `(2,8)` and `(3,8)`.
- **Objects (3):** the **florist** `(0,3)` (gives the WAILMER PAIL once; talks about every flower's meaning), her **apprentice** `(7,3)` (warns that the gym leader is 'stronger than the roses'), a **customer** `(11,6)` wandering (picks a bouquet for a Pokémon). Reuse the vanilla scripts' shape (`Route104_PrettyPetalFlowerShop_EventScript_*`).
- **Item:** WAILMER PAIL (key item) once, `FLAG_RECEIVED_WAILMER_PAIL` (an existing vanilla flag may be reused).
- **Warps:** `(2,8)` and `(3,8)` to `PrimroseVale` warp 2 (tile `(52,56)`).

### 5.4 House A, the retired florist (`PrimroseVale_HouseA`)

Shares **`LAYOUT_HOLLOWBROOK_NEIGHBOURS_HOUSE`** (11 x 8, built; see [hemlock-reach.md](hemlock-reach.md) 5.6 for its free floor tiles): exit mat `(2,7)`, bookshelf bg `(7,2)` and `(8,2)`. Objects (2): the **retired florist** `(8,3)` facing up (tells the player the petal trail in the gym follows the 'language of flowers'), a Skitty `(2,4)`. Warp `(2,7)` to `PrimroseVale` warp 3 (tile `(19,34)`).

### 5.5 House B, the petal-press family (`PrimroseVale_HouseB`)

The **G4-C 'Study and lounge' template, 12 x 9** ([ebbsworth.md](ebbsworth.md) 6.0; see [hemlock-reach.md](hemlock-reach.md) 5.7 for its plan: bookshelf runs `x 0 to 2` and `x 10 to 11`, rug `x 3 to 8, y 4 to 6` with a low table `(5,5)` and `(6,5)`, plants `(1,5)` and `(10,5)`, door mats `(5,8)` and `(6,8)`). Objects (3): the **petal-press mum** `(2,4)` facing right (presses flowers into bookmarks; asks about the sea road), her **child** `(9,6)` wandering, a Slakoth `(8,3)`. **Item:** SOOTHE BELL on the right-hand shelf `(10,2)`, a reward for fetching a flower: the child asks for one (a `FLAG_PRIMROSE_SOOTHE_BELL` one-shot). Warps `(5,8)` and `(6,8)` to `PrimroseVale` warp 4 (tile `(49,34)`).

### 5.6 Goldsworth house (`PrimroseVale_GoldsworthHouse`)

Shares the **Goldsworth House layout** (13 x 11, defined once in [kingsquay.md](kingsquay.md) 6.10: bookshelf runs, TV and cabinet, a gold-and-cream rug with a low table, plants, door mats `(5,10)` and `(6,10)`). Primrose objects (4): the **Butler** `(6,3)` facing down, **Trip** (Cousin A) `(3,6)` facing right, lounging on a floor cushion ('stand out of my light', the conservatory hammock of the card has no bed in this layout), **Winston** (Cousin B) `(10,6)` facing left, phone in hand (tries to buy the garden). The cousin pair collides with other cards: Winston is also at Hoarfell, Kingsquay and Aldermere (open question 8). After Scheme 8: Trip says Beau 'couldn't plan a nap'; Winston finds 'the town is not for sale', apparently as a surprise. Light Goldsworth-only swearing is allowed here. Plus the door sign. No battle. Warps `(5,10)` and `(6,10)` to `PrimroseVale` warp 5 (tile `(53,25)`).

### 5.7 Gym 8 (full design in section 6)

14 x 19. Exterior door `(34,7)` is warp 6.

## 6. Gym 8, the Fairy gym, in full

**Leader:** SUZURAN, Fairy, ace 55 (Azumarill 52, Dachsbun 52, Ribombee 53, Hatterene 54, Gardevoir 55; `TRAINER_SUZURAN`). CHARM BADGE, TM Calm Mind, HM Waterfall. The gym's joke ([../../gyms.md](../../gyms.md)): a glade of flower beds, and all the trainers are enormous.

### 6.1 Source and size

- **Palladium:** `KantoGyms3YearsLatercorrected.png`, the **green panel** with flower beds, hedges and a tiled path (second row, left). It measures **216 x 309 px**, about **13.5 x 19.3 tiles** at 16 px. My reading is that it is the Celadon gym: a greenhouse back wall with four arched windows and a flower emblem; a row of flower boxes with the leader standing in it; a pale sand cross-shaped path through a green lawn; two blocks of round trees on the sides; two flower-box pairs; statues at the door. I round up to **14 x 19** (trim a column if the trace shows 13). (14 + 15) x (19 + 14) = 957.
- **Tilesets (recommended):** `gTileset_General` (grass, round trees, flowers, short fences, sand) as the primary, plus `gTileset_Petalburg` (a house wall with windows for the greenhouse back wall) as the secondary. A map of type `MAP_TYPE_INDOOR` may use the General primary (vanilla Contest halls do). **Use only non-encounter grass tiles** (the plain 'short grass' metatile with the normal behaviour, not the tall-grass one). Fallback if the palettes clash: `gTileset_Building` + `gTileset_PrettyPetalFlowerShop` (flower boxes and potted plants), losing the trees (open question 1).
- **No Team Aqua import.**

### 6.2 Plan and puzzle in tiles

```
 x:   0 1 2 3 4 5 6 7 8 9 A B C D          (A=10 B=11 C=12 D=13)
 y0   W W W W W W W W W W W W W W          greenhouse wall; windows at x 3-4 and 9-10; flower emblem x 6-7
 y1   W W W W W W W W W W W W W W
 y2   F F . . . . L . . . . . F F          L = SUZURAN (6,2), facing down; F = flower bed, collision
 y3   F F T T T T H T T T T T F F          T = hedge or tree, collision; H = hedge door (6,3), closed
 y4   F F . . . . : : . . . . F F          ':' = sand lane (x 6-7); '.' = lawn (short grass)
 y5   F F . . . . Q : . . . . F F          Q = Beauty (6,5), down, sight 2
 y6   T T . 1 . . : : . . 2 . T T          1 = white bud (3,6);  2 = pink bud (10,6)
 y7   T T . . . . : : . . . . T T
 y8   T T . . . . : : . . . . T T
 y9   T T . . . . : : . N . . T T          N = Black Belt (9,9), left, sight 3
 y10  T T d d d d d d d d d d T T          d = sand cross arm (x 2-11)
 y11  T T d P d d d d d d d d T T          P = Parasol Lady (3,11), down, sight 2
 y12  T T 3 . . . : : . . . 4 T T          3 = yellow bud (2,12);  4 = blue bud (11,12)
 y13  T T . . . . : : . . . . T T
 y14  T T . . . K : : . . . . T T          K = Hiker (5,14), right, sight 2
 y15  T T . . . . : : . . . 5 T T          5 = red bud (11,15)
 y16  T T a b c . : : . d e . T T          petals, left to right: a white, b pink, c yellow, d blue, e red
 y17  T T . . S . : : . S G . T T          S = statues (4,17), (9,17);  G = Gym guide (10,17), left
 y18  W W W W W W D D W W W W W W          door mats (6,18) and (7,18)
```

Letters are objects, vats or tiles named in the tables below; digits are the five buds in the order they must bloom.

**Everything in tiles:**

| What | Tile(s) |
|---|---|
| Back wall | `y 0 to 1`, all columns; windows at `x 3 to 4` and `x 9 to 10` |
| SUZURAN | `(6,2)` facing down; flower boxes `x 2 to 5` and `x 7 to 11` on `y 2` are her bed row (collision) |
| Hedge row | `x 2 to 11, y 3` (collision), **hedge door at `(6,3)`**, closed until the buds bloom |
| Side walls | `x 0 to 1` and `x 12 to 13` for `y 2 to 17`: flower beds `y 2 to 5`, round trees `y 6 to 17` (collision) |
| Sand cross path | vertical lane `x 6 to 7, y 4 to 17`, horizontal arm `x 2 to 11, y 10 to 11` |
| Lawn | the rest of `x 2 to 11, y 4 to 17`: short grass, no encounter |
| Statues | `(4,17)` and `(9,17)`, bg events with the standard gym statue text |
| Door mats | `(6,18)` and `(7,18)` |

**The puzzle (five buds, a fixed order):**

- **The order is white, pink, yellow, blue, red** (the card's order). Five **buds** are flower-bed metatiles with a bg event on each, read from the tile named 'stand':

| Order | Bud | Bud tile | Player stands | Guarded by |
|---|---|---|---|---|
| 1 | white | `(3,6)` | `(3,7)` facing north | the Beauty at `(6,5)` sees `(6,6)` and `(6,7)` only, so not guarded |
| 2 | pink | `(10,6)` | `(10,7)` facing north | not guarded |
| 3 | yellow | `(2,12)` | `(3,12)` facing west | **Parasol Lady** at `(3,11)`, down, sight 2, covers `(3,12)` and `(3,13)` |
| 4 | blue | `(11,12)` | `(10,12)` facing east | not guarded |
| 5 | red | `(11,15)` | `(10,15)` facing east | not guarded |

- **The hint** (the 'petal trail'): a row of five coloured petal tiles on the lawn at `y 16`, left to right: `(2,16)` white, `(3,16)` pink, `(4,16)` yellow, `(9,16)` blue, `(10,16)` red, with the lane `x 6 to 7` clear between. The player enters at the door, walks to `(6,17)` and sees the row in front of them. The retired florist in House A also says the trail 'follows the language of flowers'.
- **Rules** (stage var `VAR_PRIMROSE_GYM_BUDS`, 0 to 5, kept in the save):
  - Bud k only works if the stage is `k - 1`: the bed blooms (a metatile swap to a flowering variant), a soft chime, stage rises.
  - A **wrong bud** closes every bloom (all five beds revert to closed buds), stage 0, with a message ('the beds go quiet'). Nothing else is lost.
  - After **two resets** the Gym guide offers a hint ('Start where the petals start.').
  - On the **fifth** bud the hedge door at `(6,3)` is swapped for open grass, and SUZURAN stands in her bed row behind it.
- **Buds and the hedge door are metatiles** (swapped with `setmetatile`, restored on `MAP_SCRIPT_ON_LOAD` from the stage var), not objects, so they cost no object slots. The card counted five buds plus a door as six objects (12 of 15); this version uses 6 of 15. The tiles for the bud, its bloomed variant and the hedge door must exist: Pretty Petal Flower Shop tiles (pots, flower boxes in several colours) and the General tileset's flowers are the starting set (open question 1).
- **Trainers** (the joke: enormous, so use the Hiker and Black Belt sprites for the large ones):

| # | Class | Team | Position | Facing, sight | Notes |
|---|---|---|---|---|---|
| 1 | Hiker (enormous) | Clefable 48, Mawile 48, Wigglytuff 49 | `(5,14)` | right, 2 | Brandishes a garden spade; sees `(6,14)` and `(7,14)` on the lane |
| 2 | Black Belt (enormous) | Slurpuff 48, Alcremie 48, Aromatisse 49 | `(9,9)` | left, 3 | Knits; sees `(6,9)` to `(8,9)` |
| 3 | Parasol Lady | Whimsicott 48, Floette 49, Florges 49 | `(3,11)` | down, 2 | Guards the yellow bud |
| 4 | Beauty | Dedenne 48, Granbull 49, Klefki 49 | `(6,5)` | down, 2 | Last before SUZURAN; the lane tiles in front of the hedge are hers |

All reuse vanilla ids; no IVs; levels 48 to 49 are the card's (3 to 4 below SUZURAN's lowest 52).

- **Gym guide** at `(10,17)` facing left (inside, next to the right statue). Before: 'SUZURAN is smaller than the trainers; it is a fake-out.' After two resets: the hint. After the gym: TM Safeguard.
- **Objects:** SUZURAN, 4 trainers, guide = **6 of 15.**
- **Warps:** `(6,18)` and `(7,18)` to `PrimroseVale` warp 6 (tile `(34,7)`).

## 7. Scheme 8 on the north lawn, step by step

Source: [../../troglodyte-arc.md](../../troglodyte-arc.md) (Scheme 8) and [../../goldsworth.md](../../goldsworth.md). The Pokémon that wins it, **FLORGES, is a cutscene-only Pokémon owned by an NPC garden warden** (author, 2026-10-01), not SUZURAN's. All triggers are `coord_event` triggers.

**Object budget (the outdoor map must stay at 15 live objects).** I use a **pool of 2** stake or sapling objects, not 4, and the hoarding and the hedge are metatile swaps. The 'orange flag' stake has no sprite in the tree; use a small pole-like object sprite and say so (open question 4), and the sapling is a cut-tree sprite. Stakes hide when saplings appear.

| Step | Where | What |
|---|---|---|
| Setup (stage 0 to 1) | Town `MAP_SCRIPT_ON_TRANSITION` sets stage 1 on first entry (an instant setup, which is the right use of that script) | The north lawn already holds the surveyors: **chief** `(30,12)` (plants orange flags, says 'vista' twice a sentence), **assistant** `(34,13)` (tripod, lost the site plan), **agent** `(38,12)` (a brochure for 'Glade Heights'). Two stake objects at `(32,14)` and `(36,14)`. The warden stands at the fountain `(31,22)` with her **FLORGES** `(32,22)` (cutscene-only, visible all along: 'looking at the flags'). |
| Reveal (stage 1 to 2) | `coord_event` at `(32,18)` to `(37,18)` (the lawn gap), stage 1 | A **hoarding** goes up on the lawn (metatile swap at `x 30 to 38, y 11 to 12`): 'GLADE HEIGHTS, luxury condominiums with a meadow view.' The meadow is the thing the condominiums would be built on. The agent hands the player a brochure with a bouquet in the artist's impression. |
| Collapse (stage 2 to 3) | `coord_event` at `(34,12)` and `(35,12)` just in front of the hoarding, stage 2 | The warden's FLORGES walks to the lawn; the stakes become saplings (swap objects), the blueprints a hedge (the hoarding tiles swap to a hedge row). The developers buy a bouquet from a basket and leave down the lawn gap. The three surveyor objects hide. |
| After (stage 3) | The gym door | **SUZURAN steps out to `(34,8)` and invites the player in.** No Troglodyte fight (his fights fall at gyms 1, 3, 5, 6, 7). Saplings stay; the hoarding is gone. |

Foreshadowing on R15: the surveyor at its north end (see [routes-east-detail.md](routes-east-detail.md)).

**Optional Troglodyte sighting.** At the west pier `(4,29)`, after stage 3, training alone: no dialogue about Sir Biscuit, 'Work' phase, no battle (the card). He replaces the pier angler for the duration (the angler hides while he is there); `FLAG_PRIMROSE_TROG_SIGHTED`. Can be cut.

## 8. NPCs

16 roles (cities want 12 to 20). **Outdoor live objects (15 maximum, 15 at peak):**

| # | Role | Position | Behaviour | Topic |
|---|---|---|---|---|
| 1 | Surveyor, chief | `(30,12)` | faces down; hides at stage 3 | 'Vista.' |
| 2 | Surveyor, assistant | `(34,13)` | faces down; hides at stage 3 | Has lost the site plan. |
| 3 | Developer's agent | `(38,12)` | faces left; hides at stage 3 | The brochure. |
| 4 | Garden warden | `(31,22)` | faces right | Her FLORGES has been 'looking at the flags' since morning. |
| 5 | FLORGES | `(32,22)` | visible always; in the Collapse scene walks | Cutscene-only (`OBJ_EVENT_GFX_SPECIES(FLORGES)`; check the sprite exists). |
| 6 and 7 | Stake, then sapling | `(32,14)`, `(36,14)` | stage swap | |
| 8 | Child with a watering can | `(40,30)` | wanders | Waters a flower; it 'grows back faster after the surveyors stood on it'. |
| 9 | Gardener (Parasol Lady, non-trainer) | `(24,34)` | wanders | 'Glade Heights is a lovely word for a car park.' |
| 10 | Pier angler (or Troglodyte after stage 3) | `(4,31)` | faces west | The lake is 'the mere'; R17 leads to Mirror Isle. |
| 11 | Cut tree | `(20,27)` | tree | TM Giga Drain `(20,26)`. |
| 12 | TM Giga Drain ball | `(20,26)` | item | |
| 13 | Strength boulder | `(6,10)` | boulder | RARE CANDY ball at `(4,9)`. |
| 14 | RARE CANDY ball | `(4,9)` | item | |
| 15 | Rock Smash rock | `(8,40)` | rock | NUGGET. |

That is 15; the Troglodyte sighting swaps with 10 and the stake pool swaps, so it never goes over. The `FLORGES` is the most likely sprite problem: if no overworld sprite exists, use a Floette stand-in or a plain `OBJ_EVENT_GFX_...` flower sprite.

**Interior NPCs:** Center nurse, customer, gardener; Mart clerk, shopper, old man; the florist, apprentice and customer; the retired florist and Skitty; the petal-press mum, child, Slakoth; Trip, Winston; the gym's six.

## 9. Items and secrets

| Item | Where | Gate |
|---|---|---|
| WAILMER PAIL | Florist | none, once |
| SOOTHE BELL | House B shelf `(8,2)` | bring the child a flower |
| TM Giga Drain | `(20,26)` behind the Cut tree `(20,27)` | Cut (badge 1) |
| RARE CANDY | `(4,9)` behind the boulder `(6,10)` on the NW bluff | Strength (badge 4) |
| NUGGET | under the rock `(8,40)` | Rock Smash (badge 2) |
| Hidden MAX REPEL | `(26,30)` | none |
| Hidden REVIVE | `(32,28)` (fountain edge) | none |
| Hidden PP UP | `(34,2)` behind the gym | none |
| TM Safeguard | Gym guide | after gym 8 |
| CHARM BADGE, TM Calm Mind, HM Waterfall | SUZURAN | after gym 8 |
| Fly point | the city | Fly (badge 6) |

Hidden items use flags from the reserved 0x264 block ([../../flags.md](../../flags.md)). Waterfall pays off first on [Mirror Isle](mirror-isle-detail.md), a return trip.

## 10. Flags and vars (not claimed)

- `FLAG_VISITED_PRIMROSE_VALE`.
- `VAR_PRIMROSE_SCHEME8` (0 not started, 1 flags up, 2 hoarding seen, 3 collapse done).
- `FLAG_HIDE_PRIMROSE_SURVEYORS` (set at stage 3); the stake and sapling objects use `VAR_PRIMROSE_SCHEME8` read by `MAP_SCRIPT_ON_LOAD`/hide flags (`FLAG_HIDE_PRIMROSE_STAKES`, `FLAG_HIDE_PRIMROSE_SAPLINGS`).
- `VAR_PRIMROSE_GYM_BUDS` (0 to 5), plus a temp var for the reset counter.
- `FLAG_RECEIVED_WAILMER_PAIL` (reuse the vanilla one), `FLAG_PRIMROSE_SOOTHE_BELL`, `FLAG_PRIMROSE_RARE_CANDY`, `FLAG_PRIMROSE_ITEM_GIGADRAIN`, `FLAG_PRIMROSE_ITEM_NUGGET`.
- `FLAG_PRIMROSE_TROG_SIGHTED` (optional).
- Hidden items: three flags from 0x264. `FLAG_BADGE08_GET` exists. About 10 flags and 2 vars.

## 11. Door and warp table, whole town

| Map | Tile | To | Dest warp |
|---|---|---|---|
| `PrimroseVale` 0 | `(29,46)` | `PrimroseVale_PokemonCenter_1F` | 0 |
| `PrimroseVale` 1 | `(39,46)` | `PrimroseVale_Mart` | 0 |
| `PrimroseVale` 2 | `(52,56)` | `PrimroseVale_Florist` | 0 |
| `PrimroseVale` 3 | `(19,34)` | `PrimroseVale_HouseA` | 0 |
| `PrimroseVale` 4 | `(49,34)` | `PrimroseVale_HouseB` | 0 |
| `PrimroseVale` 5 | `(53,25)` | `PrimroseVale_GoldsworthHouse` | 0 |
| `PrimroseVale` 6 | `(34,7)` | `PrimroseVale_Gym` | 0 |
| PC 1F | `(6,8)`, `(7,8)` | `PrimroseVale` | 0 |
| PC 1F and 2F | `(1,6)` | each other | 0 and 2 |
| Mart | `(3,7)`, `(4,7)` | `PrimroseVale` | 1 |
| Florist | `(2,8)`, `(3,8)` | `PrimroseVale` | 2 |
| House A | `(2,7)` | `PrimroseVale` | 3 |
| House B | `(5,8)`, `(6,8)` | `PrimroseVale` | 4 |
| Goldsworth house | `(5,10)`, `(6,10)` | `PrimroseVale` | 5 |
| Gym | `(6,18)`, `(7,18)` | `PrimroseVale` | 6 |

Signs (bg events): R15 sign `(24,61)`, court board `(31,55)`, central sign `(43,38)`, gym sign `(33,8)`, Center sign `(30,46)`, Mart sign `(40,46)`, florist sign `(53,56)`, Goldsworth door sign `(54,26)`.

## 12. Build checklist, in order

1. **Credit first:** add the Project Palladium row to `CREDITS.md` naming `nationalpark5lb.png` and `KantoGyms3YearsLatercorrected.png` in the same commit as the first trace.
2. Duplicate `VerdanturfTown`, delete the two copied heal locations, set the header to `MAPSEC_PRIMROSE_VALE`, Change Dimensions to 56 x 63, repaint ground elevation 3.
3. Trace the render shifted 11 columns east: ring, fountain, diamonds (as flower meadow), court, avenue, fence lines, tree belts. Build the west shore, pier, bluff and the lake.
4. Place the building footprints and doors (section 11).
5. Build interiors: Center, Mart and Florist on shared layouts; House A on the Hollowbrook layout; House B on G4-C; Goldsworth on the shared layout from `kingsquay.md` 6.10.
6. Paint the gym (General + Petalburg, section 6): wall, beds, hedge row, sand cross, buds, petal row.
7. Claude wires: connections (offsets in section 3), warps, objects, the Scheme 8 triggers, the bud script and `MAP_SCRIPT_ON_LOAD`, trainers on reused vanilla ids, Fly row and heal location, `flags.md`, `CREDITS.md`.
8. Test: gate to gate, Scheme 8 (stages 1 to 3), the bud order, the reset and hint, Waterfall from the new HM.

## 13. Open questions

1. **Gym tileset.** General + Petalburg (outdoor tiles inside a gym) is my pick; palette clash is possible. Fallback is Building + Pretty Petal Flower Shop, which loses the trees. The bud and bloom metatiles need to exist in whichever set is chosen.
2. **Palladium licence** for the National Park trace (map-plan.md caveat) still stands.
3. **Troglodyte sighting at the pier:** keep or cut? (The card also asked.)
4. **Stake and sapling sprites** do not exist; placeholders are proposed.
5. **Building door directions.** The card put the Center and Mart 'facing north into the court' and the Goldsworth house door 'facing west'. Gen 3 buildings have south doors only, so the doors face south and the buildings are placed on the north edge of the court and at the east edge of the ring.
6. **Blossom weather.** There is no petal weather; a particle effect would be a new system (ask first).
7. **Hoarding as a metatile swap** needs a hoarding tile; the Lavaridge or General set may only have a fence. A fence plus a sign is the fallback.
8. **Cousins.** Trip and Winston are the card's allocation, and Winston appears in four cards (Hoarfell, Kingsquay, Aldermere, here). Pick one cousin set per city.
