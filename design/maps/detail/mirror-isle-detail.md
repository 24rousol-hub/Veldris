# MIRROR ISLE, detailed design (landmark, lake island shrine, optional)

Status: **PROPOSED**, written 2026-10-01. Nothing here is built; minor names are marked PROPOSED. Adds detail to the landmark section in [../landmarks-east.md](../landmarks-east.md) (that card is canon for the species, levels, items and flags, and for the author's two decisions: **a static DIALGA at level 60 PROPOSED, re-offered until caught**, and **Mirror Isle is the only place to catch DITTO**). Follows [../interiors/README.md](../interiors/README.md); decisions and catalogue: [../interiors/catalogue.md](../interiors/catalogue.md). Roads: [routes-east-detail.md](routes-east-detail.md) (R16 and R17 meet this map). Waterfall comes from [Primrose Vale's gym](primrose-vale.md). **Pokémon only**: no real animals, even in names or jokes.

**Coordinates:** `(x,y)` tiles from the top-left `(0,0)` as Porymap shows them. **Sizes** for the gridded Palladium renders are `(px - 1) / 17`; I checked the four renders below by eye and by pixel size.

## 1. Description

A small island in the north-east mere, reached **only by water**. A pale shrine on a green mound, four standing stones, a jetty, and a hermit who has been waiting for someone to tell him it is late.

- **First glance from R16 (the south, the way most players arrive).** After a long cold crossing the player sees a low green mound with a stone shrine on its crown, four tall stones in a square around the steps, and a wooden jetty reaching out. Everything is still. The water around the island does not move against it.
- **First glance from R17 (the east).** A rocky stone landing, a few steps up, and the back of the shrine against the sky.
- **Mood, colour and sound.** Pale grey stone, soft green, a very pale sky. Nothing happens on the island unless the player does it. Weather: none. Music suggestion (existing Hoenn tracks): outdoor `MUS_SEALED_CHAMBER` (a hush), shrine `MUS_SEALED_CHAMBER`, Hollow `MUS_M_DUNGON`, Falls `MUS_CAVE_OF_ORIGIN`; the Dialga battle uses the static-battle default.
- **The memorable view.** The top of the Falls chamber: a stone ledge, a bright still pool, and a very large Pokémon standing in the light looking, by every sign, at its own reflection.
- **Goldsworths:** none. A shrine is the one place nobody tried to buy. No Troglodyte.

### When it opens

Reachable as soon as the player has **Surf (badge 5)** and has reached Hemlock Reach. The outer isle, the shrine hall and the whole Hollow (including **DITTO**, which needs only Surf) can be explored then. The **Falls chamber needs Waterfall (badge 8)** to reach the upper ledge, and Dialga needs the **shrine puzzle solved** as well.

## 2. The four maps at a glance

| Map (PROPOSED names) | Size | Source | Tileset |
|---|---|---|---|
| `MirrorIsle` (outdoor) | **30 x 26** | none in Palladium; hand-built | `gTileset_General` + `gTileset_Dewford` (the sea strips of vanilla Route 105 and 107) |
| `MirrorIsle_Shrine` (the hall) | **10 x 9** | Palladium `whirlislandsexit16uy.png` (171 x 154 px) | **Team Aqua `Dojo Interior Secondary`** with `gTileset_Building` (see 5) |
| `MirrorIsle_Hollow` (the cave) | **42 x 37** | Palladium `whirlislandsmain7yr.png` (715 x 630 px) | `gTileset_General` + `gTileset_Cave` (the vanilla Granite and Island Cave pair) |
| `MirrorIsle_Falls` (the chamber) | **20 x 39** | Palladium `whirlislandsmain25fz.png` (341 x 664 px) | `gTileset_General` + `gTileset_Cave`; the waterfall tiles are in `gTileset_General` (5 metatiles with the waterfall behaviour, checked in the tree) |

- **Credits.** All three traced maps are Project Palladium renders: credit the team by file name (`whirlislandsexit16uy.png`, `whirlislandsmain7yr.png`, `whirlislandsmain25fz.png`, and `Whirl Islands.png` as the overview) in `CREDITS.md` in the commit of the first trace. The Dojo tileset needs its own row (credits file: Rejuvenation devs including Zumi, CeriseBlossome, Azeria, Soulja, Crimson, Winter, Dallas, Kyledove, Janichroma; reformat Rahtak) in the commit that imports it. **Do not use Whirl Islands UI icons or the hash-named images** (the card).
- **Section:** one new `MAPSEC_MIRROR_ISLE` (PROPOSED) shared by all four maps. **Fly:** no.
- **Whole-isle size check:** (30 + 15) x (26 + 14) = 1800; (42 + 15) x (37 + 14) = 2907; (20 + 15) x (39 + 14) = 1855. All under 10240.
- **Tileset choice for the caves.** Vanilla `gTileset_Cave` reads pale grey-white (the Regice cave `LAYOUT_ISLAND_CAVE` uses it), close to the grey-white of the Whirl Islands render, so both caves can be built with no import. The Team Aqua `Beach Cave Secondary` (grey-dark rock, sand, still blue water, cave arches, 256 or 384 metatiles, see its `example.png`) would suit the Hollow's still pool and would add a coastal look, but it needs a Porytiles conversion, a `CREDITS.md` row (Ekat, Heartlessdragoon, Vurtax, Thedeadheroalistar, Zein; reformat Rahtak) and an import in the commit that first needs it. **Not recommended for the first pass.**

## 3. Outdoor isle (`MirrorIsle`, 30 x 26)

### Plan

`~` water (Surf), `,` sand or rock shore, `.` short grass (no encounters), `H` shrine, `D` shrine door, `u` steps, `=` jetty planks, `S` standing stone, `P` plaque, `e` ELIXIR, `R` Rock Smash rock, `m` MAX REVIVE, `F` the fisherman, `L` the stone landing (R17 side).

```
    012345678901234567890123456789
 0  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 1  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 2  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 3  ~~~~~~~~~~~HHHHHHHH~~~~~~~~~~~
 4  ~~~~~~~~~~,HHHHHHHH,~~~~~~~~~~
 5  ~~~~~~~~~,.HHHHHHHH.,~~~~~~~~~
 6  ~~~~~~~~~,.HHHHHHHH.,~~~~~~~~~
 7  ~~~~~~~~,..HHHHHHHH..,~~~~~~~~
 8  ~~~~~~~~,..HHHDHHHH..,~~~~~~~~
 9  ~~~~~~~,.....uuuu.....,~~~~~~~
10  ~~~~~~~,.eS..uuuu..S..,~~~~~~~
11  ~~~~~~,......uuuu......,~~~~~~
12  ~~~~~~,......uuuu......L~~~~~~
13  ~~~~~~,......P.........,~~~~~~
14  ~~~~~~,...............,~~~~~~~
15  ~~~~~~~,..............,~~~~~~~
16  ~~~~~~~,..S........S..,~~~~~~~
17  ~~~~~~~~,............R~~~~~~~~
18  ~~~~~~~~,............m~~~~~~~~
19  ~~~~~~~~~,,,,,===,,,,~~~~~~~~~
20  ~~~~~~~~~~~~~~===~~~~~~~~~~~~~
21  ~~~~~~~~~~~~~~==F~~~~~~~~~~~~~
22  ~~~~~~~~~~~~~~===~~~~~~~~~~~~~
23  ~~~~~~~~~~~~~~===~~~~~~~~~~~~~
24  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
25  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

- **The isle:** a grassy mound about 16 wide and 17 tall inside a ring of sand and low rock. No tall grass anywhere. **The surrounding water is a surf patch** with the **R16 table** (the card), and the player can fish from the jetty.
- **Shrine:** the building at `x 11 to 18, y 3 to 8`, door `(14,8)` facing south (Gen 3 doors only face south; the card said 'north-centre', which is where the building stands on the isle). A flight of **steps** `x 13 to 16, y 9 to 12` leads up to it.
- **Standing stones** (rock pillars, collision): NW `(10,10)`, NE `(19,10)`, SW `(10,16)`, SE `(19,16)`. Each has a bg sign (the puzzle's hints, section 4). A fifth plaque `P` at `(13,13)` (the shrine inscription, flavour).
- **Jetty:** planks `x 14 to 16, y 19 to 23`, ending at `(15,23)`. The player surfs to the jetty end from `(15,24)` and dismounts onto the planks. The **fisherman** `F` stands at `(16,21)` facing west.
- **East landing `L`:** a stepped rock landing at `(22,12)` to `(23,13)`; the player surfs up to `(24,12)` and dismounts at `(23,12)`. A short sand path `y 12` leads to the steps.
- **Items:** ELIXIR at `(9,10)` beside the NW stone (no gate). MAX REVIVE at `(21,18)` behind a Rock Smash rock at `(21,17)` (Rock Smash, badge 2).
- **Connections:**

| Edge | Map | Offset | Matching |
|---|---|---|---|
| South | `Route16` | isle `down` offset `-5` | the isle's `x 0 to 29` meet R16 `x 5 to 34` (all sea) |
| East | `Route17` | isle `right` offset `+4` | isle rows 9 to 18 meet R17 rows 5 to 14 |
| North, West | none | | open water |

- **Palette notes:** island grass and shore from `gTileset_General`; sand and rocks from `gTileset_Dewford`. The shrine building can be a Mossdeep or Sootopolis-style small temple front if one exists in the tileset; otherwise a grey boulder-roofed block with a stone door (the isle's silhouette is the point). The standing stones are the tall-rock tile.
- **Warps:** `MirrorIsle` warp 0 at `(14,8)` to `MirrorIsle_Shrine` warp 0.

## 4. Shrine hall (`MirrorIsle_Shrine`, 10 x 9) and the mirror puzzle

### Source and look

Palladium `whirlislandsexit16uy.png` is a **171 x 154 px** render, a small cave hall about 10 x 9 tiles with a ladder near the top and a yellow door glow at the bottom, which I take as the exit mat `(5,8)` and the stairs `(4,2)`. I read it as the footprint only; the look is replaced by the Dojo set.

- **Tileset:** Team Aqua **`Dojo Interior Secondary`** with `gTileset_Building`: a wooden hall with tatami mats, shoji screens, potted plants, altar tables with offerings and a step (its `example.png`, `example2.png`, `example3.png`). **What it adds:** the whole shrine interior look. **What it needs:** a Porytiles conversion (triple-layer, 512 metatiles, the same job Gen 4 Interior got, [../../interiors.md](../../interiors.md)), the `CREDITS.md` row above, and the import in the commit that first needs it. Fallback if the author does not want an import: vanilla `gTileset_Building` + `SootopolisGym` (it has water-floor panels), which also gives real water for the pools.
- **The three pools.** The card calls for three shallow pools that are still mirrors. The Dojo set has **no water**: use three pale **tatami panels** set into the dark wood floor (they read as still mirrors) with a small offering table beside each. If real water is wanted, use the Sootopolis fallback (open question 2).

### Plan (`x 0 to 9`, `y 0 to 8`)

```
 x:  0 1 2 3 4 5 6 7 8 9
 y0  W W W W W W W W W W
 y1  W W W W W W W W c W      c = carved door (8,1), a wall tile that opens when the beam lands
 y2  W . h . v . . t . W      h = hermit (2,2);  v = stairs down (4,2);  t = TM Light Screen ball (7,2), hidden until solved
 y3  W . . . . . . . . W
 y4  W q q . . . 2 . 3 W      2 = mirror M2 (6,4);  3 = mirror M3 (8,4);  q = pool (tatami mirror)
 y5  W q q . . . . . . W
 y6  W q q . . . 1 . s W      1 = mirror M1 (6,6);  s = skylight patch (8,6), the beam's source
 y7  W q q . . . . q q W      pools: P1 x 1-2 y 4-5, P2 x 1-2 y 6-7, P3 x 7-8 y 7
 y8  W W W W W D W W W W      D = exit mat (5,8)
```

- A **clock face** (3 x 3 pale mat pattern, decor, walkable) is centred at `(4,5)`; the hall hints at the Dialga link (time standing still).
- **Warps:** `(5,8)` to `MirrorIsle` warp 0 (the shrine door tile `(14,8)`); `(4,2)` stairs to `MirrorIsle_Hollow` warp 0 (tile `(36,3)`).

### The mirror puzzle in tiles

- **The beam.** A skylight patch at `s (8,6)` sends light **west** along row 6. Three brass mirrors `1 2 3` are objects, each with four facing positions: **N, E, S, W**. Each position is where the beam leaves that mirror. The beam goes: `(8,6)` west to M1 `(6,6)`, which must send it **north**; north along column 6 to M2 `(6,4)`, which must send it **east**; east along row 4 to M3 `(8,4)`, which must send it **north**; north along column 8 through `(8,3)` and `(8,2)` to the carved door `c (8,1)`. **Solution: M1 = N, M2 = E, M3 = N.**
- **Objects:** hermit 1, mirrors 3, TM ball 1 (hidden until solved) = 5 of 15. No object sprite for a brass mirror exists; use the Trick House statue sprite (`OBJ_EVENT_GFX_TRICK_HOUSE_STATUE`) as the stand, or a small boulder sprite. Placeholder graphic is fine (open question 3).
- **Interaction:** press A on a mirror: it turns clockwise (N, E, S, W, N, ...); a text line names the new facing. After each turn, a script checks all three; if the solution is made: a flash (screen palette fade), the carved door tile swaps to its open variant (`setmetatile`), the TM ball appears, `FLAG_MIRRORISLE_PUZZLE_SOLVED` is set (the card). If not solved, nothing. State is kept in `VAR_MIRRORISLE_MIRRORS` (a temp var of three 2-bit fields, so the puzzle resets each time the hall is entered; solved state is the flag).
- **The hint (the standing stones).** The card says the stones' evening shadows show the three bearings; I assign them:

| Stone (outdoor) | Bg sign text topic | Gives |
|---|---|---|
| SW `(10,16)` | 'At evening my shadow points north.' | M1 = **N** |
| NW `(10,10)` | 'At evening my shadow points east.' | M2 = **E** |
| NE `(19,10)` | 'At evening my shadow points north.' | M3 = **N** |
| SE `(19,16)` | 'I cast no shadow. Nothing here is late.' | no bearing; a flavour hint at the clock and at Dialga |

  Order the player walks the stones (south-west, north-west, north-east) is the order of the mirrors. The hermit says it once: 'Read them as the sun leaves: left to right.' (topics only, not final text).
- **Reward:** TM Light Screen at `(7,2)` (the card).
- **NPC:** the **hermit** at `(2,2)`, facing down, in the north-west corner on a mat (card: the pools only show what is above them, and the sky is free; explains the mirror puzzle once). He also says the shrine keeper 'has been waiting to be told it is late' (the Dialga hook).

## 5. The Hollow (`MirrorIsle_Hollow`, 42 x 37)

### Source and look

Palladium `whirlislandsmain7yr.png` is **715 x 630 px** (42 x 37 tiles): a big pale cave with nested ring corridors, several raised rooms, **six ladders** (yellow icons), **two holes** (black discs), a black arch in the middle, six stairs (white steps), and open gaps at the bottom edge. **Overview sheet:** `Whirl Islands.png` (1424 x 1035 px) shows it with its eight neighbours.

- **Tileset:** `gTileset_General` + `gTileset_Cave` (vanilla, pale grey-white), traced by eye. **Music:** `MUS_M_DUNGON`. **Weather:** none.
- **What the Veldris version changes from the render:** it is **one map**, so the render's ladders to other maps become **same-map ladder pairs** (a warp pair within the map), and the render's holes are painted as dark floor decor. The render has no still pool; one is added.

### Zones (all coordinates are the render's, as I read them)

| Zone | Tiles | What is there |
|---|---|---|
| **North-east landing** | `x 29 to 40, y 1 to 10` | **Arrival from the shrine stairs** at the ladder `(36,3)` (Hollow warp 0). A second ladder `(30,9)` and a long top corridor (`y 2 to 3`) running west to the North Hall. |
| **North Hall** | `x 13 to 24, y 5 to 13` | A raised room with stairs `(22,8)` and `(16,14)`. **The Falls tunnel** is a cave-door tile in its north wall at `(18,5)` (Hollow warp 1; the card says 'a dark tunnel at the north end'). |
| **Outer west ring** | `x 2 to 8, y 2 to 24` | A corridor around the west side with a ladder `(6,5)` and stairs `(7,8)` and `(7,22)`. |
| **Central Basin** | `x 9 to 33, y 14 to 27` | The open middle. The render's black arch at `(18,21)` becomes a **dark alcove** (decor, collision) with a hidden PP MAX at `(18,22)` in front of it. A **still pool** (decor, collision, no encounters, no Surf) at `x 21 to 26, y 16 to 18`, a 6 x 3 mirror of the cave roof, with a bg plaque at `(23,19)`. The **wanderer** stands on a ledge at `(23,15)`. |
| **South-west rooms** | `x 8 to 15, y 22 to 34` | A hole (decor) at `(14,28)`, a ladder `(10,31)`, stairs `(11,24)`. |
| **South-east rooms** | `x 24 to 40, y 20 to 34` | A hole (decor) at `(26,22)`, ladders `(32,29)` and `(24,31)`, stairs `(35,31)`. The **tall ledge**: a plateau `x 33 to 38, y 24 to 29` reached by stairs at `(35,30)`; a Strength boulder at `(35,26)` and the **RARE CANDY** at `(36,24)` (Strength, badge 4). |

**Ladder pairs (same-map warps).** `(6,5)` and `(24,31)`; `(30,9)` and `(10,31)`; `(32,29)` back to `(36,3)` (a shortcut to the arrival). Painted as the Cave tileset's ladder metatile. The pairing is mine; the render's ladders pair with other maps. I have not walked every route in the render; **check reachability while painting** and move a ladder if a pocket is cut off.

- **Items:** RARE CANDY `(36,24)` (Strength), PP MAX hidden `(18,22)` (hidden-item range 0x264). The card says two item spots. No Rock Smash encounters (card).
- **Wild Pokémon:** the card's cave table (levels 49 to 53, 12 slots). **DITTO is in slots 3 and 4 (20 percent) and nowhere else in the game** (author, 2026-10-01). Every walkable cave-floor tile encounters (the Cave tileset's floor behaviour); the stone ledges and the plateau top are included.
- **NPCs (card):** the wanderer on the ledge at `(23,15)`, facing down: Strength is easier than it looks, 'push it twice'.
- **Objects:** wanderer 1, boulder 1, RARE CANDY ball 1 = 3 of 15.
- **Warps (7 in all):**

| # | Tile | To | Dest warp |
|---|---|---|---|
| 0 | `(36,3)` ladder | `MirrorIsle_Shrine` | 1 |
| 1 | `(18,5)` tunnel | `MirrorIsle_Falls` | 0 |
| 2 and 3 | `(6,5)` and `(24,31)` | each other | 3 and 2 |
| 4 and 5 | `(30,9)` and `(10,31)` | each other | 5 and 4 |
| 6 | `(32,29)` | `MirrorIsle_Hollow` | 0 |

## 6. The Falls chamber (`MirrorIsle_Falls`, 20 x 39)

### Source and look

Palladium `whirlislandsmain25fz.png` is **341 x 664 px** (20 x 39 tiles): a tall cave room with a long water channel, a **three-tile-wide waterfall** (the render's `x 12 to 14, y 17 to 28`), a top basin with a ladder, a mid-level island with a ladder, and a lower pool with a ladder and a hole. It is the right-hand panel of `Whirl Islands.png`. **Tileset:** `gTileset_General` + `gTileset_Cave`; the waterfall tiles come from `gTileset_General` (checked in the tree). **Music:** `MUS_CAVE_OF_ORIGIN`. **Weather:** none.

### Zones

| Zone | Tiles | What is there |
|---|---|---|
| **South strip (arrival)** | floor `x 9 to 13, y 33 to 34` | The ladder `(13,33)` (Falls warp 0, from the Hollow's tunnel). The player starts here, on the south edge. |
| **Lower pool** | water `x 4 to 15, y 29 to 37` | A surf patch (no wild table, no encounters). West ledge `x 4 to 8, y 29 to 30` with a dark hole (decor) at `(8,28)`. |
| **The waterfall** | `x 12 to 14, y 17 to 28` | Waterfall tiles, 12 tall. **Waterfall (badge 8)** to climb it. Start from the pool at `(13,29)` facing north. |
| **The channel** | water `x 12 to 14, y 7 to 16` | A surf patch above the falls. |
| **Mid-level island** | floor `x 4 to 10, y 13 to 15` | **MAX ELIXIR** ball at `(6,14)`; a ladder `(7,14)` (a one-way drop back, Falls warp 2). Dismount from the channel at `(10,14)`. |
| **Top ledge** | floor `x 5 to 11, y 7 to 9` | **MIRROR HERB** ball at `(6,7)`; the **wanderer** at `(10,8)`; **DIALGA** at `(8,8)` (hidden unless the puzzle is solved); a ladder at `(11,7)` (a one-way drop back, Falls warp 1). Dismount from the channel at `(11,8)`. |
| Rock | everything else | Wall tiles (collision) with the cave's edge shapes. |

- **How the player moves:** from the south strip they surf north across the pool to `(13,29)`, climb the falls with Waterfall to the channel, and surf north to the top ledge (with the mid island as a side stop). The **ladders at `(11,7)` and `(7,14)` are one-way drops** to the south strip, so the player is never stranded above; they leave by the tunnel door from the south strip: that door is the same ladder `(13,33)`, back to the Hollow.
- **Objects:** wanderer 1, MIRROR HERB 1, MAX ELIXIR 1, DIALGA 1 = 4 of 15.
- **Warps (3):**

| # | Tile | To | Dest warp |
|---|---|---|---|
| 0 | `(13,33)` ladder | `MirrorIsle_Hollow` | 1 |
| 1 | `(11,7)` ladder | `MirrorIsle_Falls` | 0 |
| 2 | `(7,14)` ladder | `MirrorIsle_Falls` | 0 |

### DIALGA, the static encounter

- **Species and level:** DIALGA, **level 60 PROPOSED** (matching MIZZLE's ace, a stiff fight after gym 8). `SPECIES_DIALGA` exists (`P_FAMILY_DIALGA`, Gen 4). The Origin forme is not planned.
- **Visibility:** the object (`OBJ_EVENT_GFX_SPECIES(DIALGA)`, the expansion's per-species overworld sprite; check it exists, else use a placeholder) shows only when `FLAG_MIRRORISLE_PUZZLE_SOLVED` is set and `FLAG_MIRRORISLE_DIALGA` is not. The hide flag is set on transition from those two.
- **Re-offered until caught (author):** `setwildbattle` and a wild battle on interaction. If the player faints, runs, or defeats it without catching, the object **stays**, and talking to it again starts the battle again. `FLAG_MIRRORISLE_DIALGA` is set **only on a catch**, and that hides the object. Claude's script pattern follows how another legend is wired in this tree (not designed here).
- **Theme:** a mirror of the still lake, and time standing still. The shrine puzzle (mirrors, a clock face on the floor) wakes it. The deadpan joke: the shrine keeper has 'been waiting to be told it is late'.
- **Gate:** Surf (badge 5), Waterfall (badge 8), puzzle solved. Not required for the main story.

## 7. NPCs (card roles with positions)

| Role | Where | Topic |
|---|---|---|
| Hermit | Shrine hall `(2,2)` | The pools show only what is above them; the sky is 'free'. Explains the mirror puzzle once. |
| Fisherman | Jetty `(16,21)`, faces west | The mere is quieter in the evening, and the catches are better than R16's. |
| Plaque (bg event) | Steps `(13,13)` | A one-line shrine inscription. |
| Standing-stone signs (4, bg events) | `(10,10)`, `(19,10)`, `(10,16)`, `(19,16)` | The bearing hints (section 4). |
| Wanderer | Hollow ledge `(23,15)` | Strength is easier than it looks, 'push it twice'. |
| Wanderer, after the falls | Falls top ledge `(10,8)` | Asks where the way back is (points at the ladder). |

**Trainers:** none on the isle (two swimmers on the approach roads, see [routes-east-detail.md](routes-east-detail.md)).

## 8. Items and secrets

| Item | Where | Gate |
|---|---|---|
| ELIXIR | outdoor `(9,10)` beside the NW stone | none |
| MAX REVIVE | outdoor `(21,18)` behind the rock `(21,17)` | Rock Smash (badge 2) |
| TM Light Screen | shrine hall `(7,2)` | solve the mirror puzzle |
| RARE CANDY | Hollow `(36,24)` behind the boulder `(35,26)` | Strength (badge 4) |
| PP MAX | Hollow hidden `(18,22)` | none (hidden-item flag, reserved 0x264 range) |
| MAX ELIXIR | Falls mid island `(6,14)` | Waterfall (badge 8) |
| MIRROR HERB | Falls top ledge `(6,7)` | Waterfall (badge 8) |
| DIALGA | Falls top ledge `(8,8)` | Waterfall (badge 8) and the puzzle |
| DITTO | Hollow cave floor | Surf; the **only** place in the game |

## 9. Flags and vars (not claimed)

- `FLAG_MIRRORISLE_PUZZLE_SOLVED`, `VAR_MIRRORISLE_MIRRORS` (temp var, three 2-bit fields).
- `FLAG_MIRRORISLE_DIALGA` (set only on a catch), a hide flag `FLAG_HIDE_MIRRORISLE_DIALGA` (set and cleared on transition from the two flags above).
- One-shot flags: `FLAG_MIRRORISLE_TM_LIGHT_SCREEN`, `FLAG_MIRRORISLE_ELIXIR`, `FLAG_MIRRORISLE_MAX_REVIVE`, `FLAG_MIRRORISLE_RARE_CANDY`, `FLAG_MIRRORISLE_MIRROR_HERB`, `FLAG_MIRRORISLE_MAX_ELIXIR`.
- One hidden-item flag (PP MAX) from 0x264. The card says two hidden flags; I count one hidden item.
- About 10 flags and 1 temp var from the spare pool.

## 10. Door and warp table, whole landmark

| Map | Tile | To | Dest warp |
|---|---|---|---|
| `MirrorIsle` 0 | `(14,8)` | `MirrorIsle_Shrine` | 0 |
| `MirrorIsle_Shrine` 0 | `(5,8)` | `MirrorIsle` | 0 |
| `MirrorIsle_Shrine` 1 | `(4,2)` | `MirrorIsle_Hollow` | 0 |
| `MirrorIsle_Hollow` 0 | `(36,3)` | `MirrorIsle_Shrine` | 1 |
| `MirrorIsle_Hollow` 1 | `(18,5)` | `MirrorIsle_Falls` | 0 |
| `MirrorIsle_Hollow` 2 to 6 | ladder pairs (section 5) | same map | |
| `MirrorIsle_Falls` 0 | `(13,33)` | `MirrorIsle_Hollow` | 1 |
| `MirrorIsle_Falls` 1, 2 | `(11,7)`, `(7,14)` | `MirrorIsle_Falls` | 0 (one-way drops) |

## 11. Build checklist, in order

1. **Isle outdoor.** Create `MirrorIsle` (a new map, not a duplicate: the outdoor isle is hand-built), 30 x 26, `gTileset_General` + `gTileset_Dewford`, region `REGION_HOENN`, layout version `emerald`. Paint the sea, the mound, the shrine front, the jetty and the landing (section 3). Add the section `MAPSEC_MIRROR_ISLE`.
2. **Shrine hall.** Import and convert the Dojo set (CREDITS row, in this commit), or use the fallback. Paint section 4's plan. Credit `whirlislandsexit16uy.png`.
3. **Hollow.** Trace `whirlislandsmain7yr.png` (credit it) in `gTileset_General` + `gTileset_Cave`, place the ladders, the still pool, the plateau and the hole decor. Check reachability.
4. **Falls.** Trace `whirlislandsmain25fz.png` (credit it), place the waterfall tiles (`gTileset_General`) and the three zones.
5. **Claude wires:** connections to R16 and R17 (offsets in section 3), warps (section 10), objects, bg events (stones, plaque, valves are not here), the mirror script and flags, wild tables (the card's cave table in the Hollow and the R16 table in the outdoor water), the Waterfall gate, DIALGA's script, `flags.md`, `CREDITS.md`, `engine-edits.md` if any.
6. **Test:** DITTO in the Hollow with only Surf; the mirror puzzle (all 64 combinations are three mirrors, 4 states each: a quick check that only M1 = N, M2 = E, M3 = N solves it); Waterfall; DIALGA's fainted-and-return case.

Effort: **medium to hard.** Four maps; the outdoor isle is easy but takes painting time, the Hollow and Falls are traced from Palladium, the mirror puzzle is a small script.

## 12. Open questions

1. **Hollow ladder pairs** are my invention (the render's ladders pair with other maps); reachability needs a check while painting.
2. **Pools.** Tatami panels as 'mirrors' (Dojo) or real water (Sootopolis fallback)?
3. **Mirror sprite.** No brass-mirror object exists. A placeholder (statue or boulder sprite) is proposed.
4. **Whirlpool decor.** The Whirl Islands render has none outdoors, but R14 uses rock pairs; nothing to decide here.
5. **Section id:** a new `MAPSEC_MIRROR_ISLE` costs one of the tight free ids (about 8 left, [../../setup-budget.md](../../setup-budget.md)); borrowing a Hoenn cave id saves it but puts the wrong name on the Pokénav. The card asked this; I recommend the new id.
6. **Shrine door direction.** Gen 3 doors face south; the card said the door is 'north-centre'. The shrine stands at the north of the isle and its door faces south onto the steps.
7. **Optional or on the main path?** The card treats it as optional. R16 and R17 are also Primrose Vale's only ways in, so the isle is passed on the way, but nothing forces the player onto it.
8. **DITTO before badge 8.** The isle needs only Surf, so DITTO is catchable from badge 5 on (the card says 'post-badge-8 by design'); this is a conflict. If DITTO must wait for badge 8, gate the Hollow's stairs (the shrine hall's stairs) on `FLAG_BADGE08_GET`.
