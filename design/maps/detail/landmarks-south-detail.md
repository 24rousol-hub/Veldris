# SOUTH LANDMARKS: detailed design (Silverstrand, Echo Hollow, Argent Peak)

Status: **PROPOSED.** Written 2026-10-01 from [../interiors/README.md](../interiors/README.md), [../interiors/catalogue.md](../interiors/catalogue.md), [../README.md](../README.md), [../../interiors.md](../../interiors.md), [../index.md](../index.md), the cards in [../landmarks-south.md](../landmarks-south.md) (species, levels, items, flags are theirs and are kept as they are), [../../postgame.md](../../postgame.md), [../../troglodyte-arc.md](../../troglodyte-arc.md), and by looking at the Palladium images `unioncave13qx.png`, `unioncave29xw.png`, `unioncave39xd.png` (each 341 x 613, **20 x 36** tiles), `darkcave2.png` (579 x 562, **34 x 33**), `mtsilver9no.png` (732 x 545, **43 x 32**), `mtsilverentrance5uq.png` (290 x 545, **17 x 32**), `mtsilver27oa.png` (409 x 494, **24 x 29**), `mtsilberredplaceuhhhyeah6jn.png` (188 x 496, **11 x 29**), and by rendering vanilla `Route125`, the Meteor Falls and Granite Cave layouts. Roads that reach these places are in [routes-south-detail.md](routes-south-detail.md) (R29, R30, R31); the hub is [vesperhaven.md](vesperhaven.md). House template **G4-B** is in [ebbsworth.md](ebbsworth.md) section 6.0.

**New minor names and details introduced in this file are all PROPOSED:** the echo stone names (Wave, Bell, Spiral stones), the cave guide and hermit placements, the camp clerk's stall, the Troglodyte-at-the-summit staging, all coordinates.

Conventions: **(x, y) from each map's top-left (0,0)**; positions read off the Palladium images are **approximate (plus or minus 1 or 2 tiles)** because the author traces them by eye; positions I give for events (stones, trainers, items) are my design. Trainers reuse vanilla Hoenn ids, `IVs: 0`, Pokémon only. Each map keeps at most 15 live objects (I counted). **Landmarks are not fly destinations** (card; CLAUDE.md). All three open after `FLAG_SYS_GAME_CLEAR`.

---

## Findings (read first)

1. **Vanilla `Route125` is not a beach** (rendered: a sea with one big rock mountain, the Shoal Cave island, and small sandy islets). The Silverstrand card calls it 'an island-beach sea route'; the long pale beach has to be **drawn by hand**. I recommend copying the beach-spit pattern from `Route109`'s north end (sand band, dune lines) with the LeoB Dewford sand tiles.
2. **The card text and the card table disagree on B2F's trainers** (Echo Hollow): the layout says 'a Black Belt and a Psychic' on B2F, the trainer table puts Black Belt and Psychic on **B1F** and Cooltrainers on B2F. I follow the table.
3. **Argent Peak caves: the vanilla Meteor Falls tileset is the right one.** It has Waterfall metatiles, ledge stairs, grey-blue rock and boulders; the three-waterfall upper cave and the summit need no import. The card's alternatives (`MeteorFalls_1F_1R` 30 x 42) confirm it.
4. **Team Aqua's Caves Alt Primary and Secondary cannot be used**: their `metatiles.bin` is 24576 bytes each, 1024 triple-layer metatiles, over this tree's 512-per-tileset limit (engine-limits.md row 7).
5. **Image sizes are as the cards say**, with one exception: the summit image measures **11 x 29**, not 12 x 31; I plan the summit map at 12 x 31 with a wall column and rows added.

---

# 1. SILVERSTRAND (beach, post-game dead end)

## 1.1 Quick facts

| | |
|---|---|
| Maps | `Silverstrand` (**44 x 30**, `(44+15)*(30+14) = 2596`), `Silverstrand_SurfShack` (G4-B 10 x 8), `Underwater_Silverstrand` (20 x 10, the Dive cove) |
| Section | `MAPSEC_SILVERSTRAND` (12 characters). Not a fly town; heal at Vesperhaven (card) |
| Arrival | R29 from Vesperhaven. **North edge water x 20-23** (R29's bottom edge x 22-25, offset -2). A wooden jetty at (21,3)-(22,6) is the one dry arrival tile |
| Music / weather | `MUS_DEWFORD` (the vanilla beach-town track, quiet); `WEATHER_SUNNY`; type `MAP_TYPE_ROUTE` |
| Base | Draw by hand (see Findings 1); sand and dune pieces from LeoB ORAS `secondary/dewford` (shared with Driftsands and Beaconmouth), General primary. If Dewford is not yet imported, vanilla `Dewford` secondary is the fallback |
| Gate | Post-game (R29's gate). **Dive (badge 9)** for the cove only |
| Effort | Easy to medium: one beach, one hut, one cove, no puzzles |

## 1.2 Description

**First glance.** From the jetty the player sees a long, pale, nearly white beach that looks silver in the low light: three soft dune ridges in rows, a single driftwood hut on the left with its door facing the sea, two glittering rock pools on the right, and far down the sand a thin sandbar leading to a tiny islet with one tree and a dark patch of water beside it. A wrecked wooden boat lies on its side at the foot of the left cliff. A signpost at the jetty says 'SILVERSTRAND. PLEASE TAKE ONLY PHOTOGRAPHS (AND PEARLS).'

**Mood, colour, sound, time of day.** The quiet place: sun-bleached, hushed, only the sea. Palette: pale sand with a silver-white cast (the crushed shell), turquoise shallows, grey cliff, one green tree. Sound: surf and a distant buoy; no town music, just `MUS_DEWFORD` softly. **Time of day: a bright, low late-morning**.

**The one memorable view.** The jetty's end at (22,6): the whole beach laid out below, the three dune lines leading the eye to the sandbar and the lone tree at (22,28).

## 1.3 Map plan

Sketch, **1 character = 2 x 2 tiles** (22 x 15 characters). Legend: `~` sea, `j` jetty, `d` dune ridge, `g` dune grass (wild encounters), `S` Surf Shack, `o` rock pools, `T` cliff, `w` wreck, `b` sandbar, `i` islet, `.` sand.

```
x:  0    1    2    3    4 
y0  ~~~~~~~~~~~~~~~~~~~~~~
y2  ~~~~~~~~~~jj~~~~~~~~~~
y4  ~~~~~~~~~~jj~~~~~~~~~~
y6  ~~........jj........~~
y8  ~~dggggddd..dddddddd~~
y10 ~~..............ooo.~~
y12 ~~dddddddd..dgggoood~~
y14 ~~SSSddddd..dgggdddd~~
y16 ~~SSS...............~~
y18 TTdddggggd..ddddddood.
y20 TT................oo..
y22 TT.........b.~~~~~~~~~
y24 TT..ww.....b.~~~~~~~~~
y26 TT~~~~~~~~iii~~~~~~~~~
y28 TT~~~~~~~~iii~~~~~~~~~
```
(Header digits mark every 10 tiles. The sketch is coarse; the tables give the exact positions.)

- **Jetty and arrival (x 20-23, y 0-6).** Sign at (23,4). The **child on the jetty** at (21,4).
- **Dune ridge (three lines, y 8-9, 13-14, 18-19, x 4-40) with a cut path through them at x 20-23.** Dune-grass patches (the 12-slot table, levels 66 to 72) at (6,8)-(12,9), (26,13)-(31,14), (10,18)-(16,19).
- **Surf Shack (5,14)-(8,17), door (6,17)** ('6 tiles from the left edge', card). Door faces south.
- **Rock pools (right):** (33,11)-(36,13) and (36,19)-(39,21): two small pools of shallow water with shining items.
- **Sandbar and islet:** a 2-wide sandbar (22,22)-(23,26) to a tiny **islet (20,27)-(25,29)** with one tree at (22,28) and a visible **Dive spot** at (22,26) (dark-water tile to dive from). Surf over the sandbar's edges.
- **Cliffs (left, bottom):** x 0-3, y 18-29 solid rock wall; the **wreck of a wooden boat** at (8,24)-(11,26) (decoration) with a visible **Shell Bell** in the hold at (9,25).
- **East and south:** sea.

## 1.4 Interiors

- **`Silverstrand_SurfShack` (G4-B, 10 x 8).** The **Surf Shack keeper**, a retired lifeguard, at (5,4) `FACE_DOWN`: gives **Silver Powder** once (`FLAG_RECEIVED_SILVER_POWDER`) and hints at the treasure pools ('The sand is silver. The sea took the rest.'). Plan G4-B with a surfboard rack as a wall `bg_event` (6,1) and a stack of towels. Warps: mats (3,7),(4,7) to `Silverstrand` warp 0 (door (6,17)).
- **`Underwater_Silverstrand` (20 x 10).** Dive cove under the islet: a sandy sea floor with coral. Tileset recommendation: **Underwater Reef Secondary** (Ekat, Vurtax, Heartlessdragoon; credit Rahtak for the reformat; `.../Full Tilesets/Underwater Reef Secondary`; looking at its example: golden sand floor, grey rock, coral and seaweed, shells and starfish, which is exactly the silver-sand cove with Pearl items). 6144 bytes, so probably two-layer; it has an `anim` folder (static first). Pair it with the vanilla `gTileset_Underwater` primary to avoid a second import. **Fallback (no import):** copy a vanilla `Underwater_Route*` map. Dive encounters (card): CLAMPERL 66 to 68 (60%), LUVDISC 67 to 69 (30%), HUNTAIL 68 to 70 (5%), GOREBYSS 68 to 70 (4%), LUMINEON 70 (1%). Visible items: **Pearl String** at (4,5), **Big Pearl x2** at (15,3) and (10,7).

## 1.5 Trainers, NPCs, items

**Trainers (6, post-game; reuse vanilla ids).**

| Class | Team (card) | Tile | Facing | Sight |
|---|---|---|---|---|
| Swimmer male | Wailord 68, Starmie 69 | (30,6) | `FACE_DOWN` | 4 (in the shallows) |
| Swimmer female | Milotic 68, Gastrodon 69, Jellicent 70 | (12,5) | `FACE_DOWN` | 4 |
| Tuber male | Floatzel 67, Sharpedo 68 | (38,8) | `FACE_LEFT` | 2 |
| Beauty | Alomomola 68, Mantine 69, Walrein 70 | (17,11) | `FACE_RIGHT` | 4 |
| Sailor | Pelipper 68, Cloyster 69, Kingdra 70 | (24,16) | `FACE_LEFT` | 4 |
| Fisherman | Whiscash 68, Gyarados 70, Seaking 69 | (35,15) | `FACE_UP` | 3 (by the rock pool) |

**NPCs (3 objects):** **Beachcomber** at (14,18) wading (sells information about where hidden items lie: 'three pearls, a heart, a stone'), **child on the jetty** (21,4) ('came by boat or by being brave?'), **retired Swimmer** (rematch trainer, Vesperhaven policy, [vesperhaven.md](vesperhaven.md)) at (30,16). The keeper is inside the hut. **Objects:** 6 + 3 + 2 visible items (Shell Bell, Max Revive) = **11**.

**Items (card):** Silver Powder (keeper gift); hidden **Pearl x3** at (34,12), (37,20), (26,16), **Big Pearl** at (17,19); **Heart Scale x2** at (9,9) and (30,19); **Star Piece** at (28,9); **Stardust** at (12,12); **Nugget** at (19,14); visible **Shell Bell** (9,25) in the wreck; visible **Max Revive** at the islet's tree base (22,28) (Surf over the sandbar to reach); the cove items above.

**Wild.** Dune grass 12-slot table (PELIPPER, CRAWDAUNT, SANDACONDA, PALOSSAND, CRABOMINABLE, KINGLER, SLOWBRO, CLOYSTER, GASTRODON, STARMIE, MINIOR, ARMALDO, levels 66 to 72), Surf (levels 66 to 70), Old, Good and Super Rod, Dive cove table: all per the card.

## 1.6 Warps and connections

| Map | Tile | Destination | Dest warp |
|---|---|---|---|
| `Silverstrand` | (6,17) | `Silverstrand_SurfShack` | 0 |
| `Silverstrand_SurfShack` | (3,7),(4,7) | `Silverstrand` | 0 |
| `Silverstrand` | Dive spot (22,26) | `Underwater_Silverstrand` | Porymap Dive and Emerge connection |

Connection: **north** edge water x 20-23 to `R29` bottom edge x 22-25 (Silverstrand's file `up`, offset 2; R29's file `down`, offset -2).

## 1.7 Flags (not claimed), checklist, open questions

**Flags:** `FLAG_VISITED_SILVERSTRAND` (optional), `FLAG_RECEIVED_SILVER_POWDER`, `FLAG_HIDDEN_ITEM_SILVERSTRAND_PEARL_1` to `_3`, `_BIG_PEARL`, `_HEART_SCALE_1`, `_2`, `_STAR_PIECE`, `_STARDUST`, `_NUGGET`, `FLAG_ITEM_SILVERSTRAND_MAX_REVIVE`, `FLAG_ITEM_SILVERSTRAND_SHELL_BELL`; new (PROPOSED): `FLAG_ITEM_SILVERSTRAND_PEARL_STRING`, `_BIG_PEARL_1`, `_BIG_PEARL_2` for the cove balls.

**Build checklist.** 1) Read flags.md; decide the LeoB `dewford` import (shared) and the Reef import (or the vanilla underwater fallback). 2) Create `Silverstrand` 44 x 30 from scratch (region `REGION_HOENN`, `layout_version` `emerald`): sea, three dune lines, the jetty, hut plot, pools, sandbar, islet, cliff, wreck. 3) Surf Shack (G4-B). 4) The cove (`Underwater_Silverstrand`) and the Dive and Emerge pair. 5) Warps and the north connection (R29 must exist). 6) Close and reload Porymap after Claude's event edits. 7) Claude wires trainers, items, dialogue; `make -j4`. 8) Update design docs and credits; no ROM or save staged; commit and push.

**Open questions.** 1) A pure treasure beach (card question 1): or hide something bigger? 2) The Reef tileset import for one small cove: worth it, or copy a vanilla underwater map? 3) The sand's 'silver': a palette nudge in Porymap's tileset editor is the author's job.

---

# 2. ECHO HOLLOW (cliff cave, post-game)

## 2.1 Quick facts

| | |
|---|---|
| Maps | `EchoHollow_1F` (**20 x 36**), `EchoHollow_B1F` (20 x 36), `EchoHollow_B2F` (20 x 36), `EchoHollow_EchoChamber` (**34 x 33**, dark, needs Flash) |
| Section | `MAPSEC_ECHO_HOLLOW` (11 characters), shared by all four. Not a fly town; no Pokémon Center (card; heal at Vesperhaven, two roads away) |
| Arrival | R30's cave door (11,24) to `EchoHollow_1F` (16,33) |
| Music / weather | `MUS_CAVE_OF_ORIGIN` (vanilla Meteor Falls cave track) on the three floors, `MUS_SEALED_CHAMBER` in the Echo Chamber; no weather; type `MAP_TYPE_UNDERGROUND` |
| Tilesets | **Recommended, no import: `gTileset_General` + vanilla `gTileset_Cave`** (the Granite Cave pieces: ladders, boulders, cracked rocks, pools, ledges). **Optional upgrade:** Team Aqua **Gen 4 Cave Secondary** (Kyledove majority, Ghoulslash for the rock-climb and sideways-stair graphics, Rahtak for the north cave entrance; credit Rahtak for the reformat; 6144 bytes = 384 two-layer or 256 triple-layer metatiles, README says nothing about triple-layer so expect two-layer: check; example looked at: brown rock, wooden ladders, a pool with a rock island, boulders, stair ledges, a cave-mouth tile). **Not usable:** Caves Alt Primary and Secondary (1024 triple-layer metatiles each, over the 512 limit) |
| Dark chamber | The map flag `requires_flash` (Porymap's Map Properties) on the Echo Chamber. Flash is badge 3 |
| Credits | Palladium team for the images (first commit); Gen 4 Cave only if imported |
| Effort | Medium to hard |

## 2.2 Description

**First glance.** The player steps through a black door in a bare ridge and into a big, pale, echoing cave: pools lying in the stone like dropped mirrors, a sand bridge between two of them, a ladder in the middle of the floor. A cave guide at the mouth says the stones answer 'if asked properly'. The cave **repeats** everything: footsteps arrive a moment late.

**Mood, colour, sound.** Eerie and clean rather than dark: grey-blue rock, sand floors, bright pools; the floors below get darker, the chamber at the bottom is nearly black (needs Flash). Sound: the Meteor Falls cave track, with a deliberate half-second of silence at the three echo stones. The joke: 'It repeats everything. I have stopped talking to it.'

**The one memorable view.** B1F, the first echo stone: standing on it and seeing the long cave open out in both directions, a pool in the middle and the carved pillar to the right.

## 2.3 Floor plans

All positions are **read off the Palladium images (about +-1 or 2 tiles)** unless marked (design).

### 1F (Union Cave 1, `unioncave13qx.png`, 20 x 36)

The image shows a big cave: a **long pool** at the top (x 6-14, y 4-6), a **square pool** at the left (x 2-5, y 8-11), a middle band (y 12-17), a raised **central chamber** (x 3-7, y 18-22) with a hatched **ladder** at (5,19), a lower band (y 23-26), a **textured sand bridge** (x 9-14, y 26-27) between two **bottom pools** (x 2-5, y 28-31 and x 12-15, y 28-31), a second ladder at **(3,33)** (bottom left), and sand openings in the right wall at (16,4) and (16,32).

- **Entrance:** the opening at **(16,33)** (the lower-right sand opening) is the R30 door arrival (`EchoHollow_1F` mats (16,32),(16,33)). The other right-wall opening at (16,4) is **sealed** (solid rock; the render's top-right opening is not used).
- **Ladders:** **A** at (5,19) and **B** at (3,33), each down to B1F (the B1F render has matching up-ladders).
- **Trainers (3):** **Hiker** (Golem 68, Steelix 69, Rhyperior 70) at (11,10) `FACE_LEFT`, sight 4; **Hiker** (Gliscor 69, Golurk 70, Magcargo 69) at (13,24) `FACE_UP`, sight 4; **Ruin Maniac** (Sigilyph 69, Claydol 69, Bronzong 70) at (5,25) `FACE_RIGHT`, sight 3.
- **NPC:** **cave guide** at (15,31) `FACE_UP` just inside ('the stones answer if asked properly').
- **Pools:** Surf and fishing per the card (levels 68 to 73).
- **Items (design):** hidden **Heart Scale** at (3,3); visible nothing else. **Objects:** 3 + 1 = **4**.

### B1F (Union Cave 2, `unioncave29xw.png`, 20 x 36): the echo puzzle and the boulders

The image: a **long water channel** splitting the cave (x 6-16, y 14-17, widening into a pool at x 5-12, y 16-19 and a channel south x 9-11, y 18-24), a **side room** (x 5-9, y 18-23) holding a hatched ladder at **(7,19)**, **boulders** at about (3,7),(5,14),(15,4),(14,24),(16,24), a lower sub-room (x 1-18, y 27-35) with a pool, a ladder at **(3,32)** and a dark ladder at **(17,31)**.

- **Ladders:** **(7,19)** up to 1F ladder A; **(3,32)** up to 1F ladder B; **(17,31)** **down to B2F**.
- **Strength boulders** (3, card): (3,7), (5,14), (15,4). One blocks the nook with the **Everstone** at (9,4) (card, Strength); another is a plain obstacle on the route; the third pushes onto a switch-free spot (no puzzle needed).
- **The echo puzzle (design, from the card).** Three **echo stones** (`bg_event`s on floor tiles) and a **carved pillar** (`bg_event`):
  - Pillar at **(8,18)** next to the up-ladder (7,19): three carved shapes read **Wave, Bell, Spiral** (in that order).
  - **Wave stone** at (4,10); **Bell stone** at (15,20); **Spiral stone** at (9,28), spread over the cave so the player walks it.
  - Standing on a stone and facing it, the player 'calls out'; the cave answers with the floor tone (a different cry per stone). Call in **order**; `VAR_ECHO_HOLLOW_STONES` counts 0 to 3 (card, PROPOSED). Wrong stone: the cave sneezes dust, var back to 0. No timer.
  - When the third is called the **sealed wall** at (18,17) (a rock wall with a cracked-door look) opens (`setmetatile`) to the **Echo Chamber** (warp). Reuse the vanilla sealed-wall and Braille-door scripts for the swap (card). `FLAG_ECHO_HOLLOW_CHAMBER_OPEN` set.
- **Trainers (2):** **Black Belt** (Hariyama 70, Machamp 71, Lucario 72) at (12,12) `FACE_DOWN`, sight 4; **Psychic** (Gallade 70, Alakazam 71, Reuniclus 71) at (4,25) `FACE_UP`, sight 4.
- **Items:** **Everstone** (9,4) (Strength); hidden **Star Piece** at (6,30); the **Rock Smash side room**: a cracked rock in the wall at (3,2) opens a nook with **PP Max** at (3,1) (card, Rock Smash badge 2). **Objects:** 2 + 3 boulders + 1 item ball (Everstone) + 1 PP Max ball = **7**.

### B2F (Union Cave 3, `unioncave39xd.png`, 20 x 36)

The image: a hatched ladder at top-left **(5,3)** (up), a big **pool** across the upper third (x 2-17, y 5-9) joined to a long channel south, **stepping stones** across the water at about (8-12, 12-14), a second large pool in the lower third (x 7-17, y 27-33), rock ledges and two boulder-like rocks.

- **Ladder:** (5,3) up to B1F (17,31).
- **Hermit's nook (design):** a niche at (4,10) holding the **hermit** `FACE_RIGHT`: gives the **Max Elixir** and the order hint ('It repeats everything. I have stopped talking to it.').
- **Stepping stones:** a line of 5 stepping stones across the central pool at (8,12) to (12,12) (Strength not needed); hidden **Nugget** on the middle stone (10,12) (card).
- **Trainers (2, per the table):** **Cooltrainer male** (Tyranitar 72, Hydreigon 72, Metagross 73) at (6,15) `FACE_RIGHT`, sight 4; **Cooltrainer female** (Weavile 72, Froslass 71, Mamoswine 73) at (14,28) `FACE_UP`, sight 4.
- **Items (card):** visible **Max Revive** at (15,2); visible **Rare Candy x2** at (3,34) and (16,20). (The card also lists these 'in B2F and the chamber'; I put them on B2F and keep the Chamber's chest as the main prize.) **Objects:** 2 + 1 hermit + 3 item balls = **6**.
- **No Pokémon Center.** Heal at Vesperhaven.

### Echo Chamber (`darkcave2.png`, 34 x 33, dark; needs Flash)

The image is a square cave with a rocky outer ring, ledges, an **L-shaped pool** (x 14-29, y 10-25), stair tiles at about (11,11), (21,9), (26,25), and yellow exit marks at (24,6), (28,9), (29,23), (5,28). Design:

- **Arrival** from the sealed wall: warp lands at **(5,28)** (the bottom-left yellow mark). The path winds along the south and west ledges, around the pool, up to the far end at the **top right**.
- **Flash:** the map has `requires_flash`. With Flash (badge 3) the player lights the whole chamber (vanilla pattern). Without it they can still walk blind (not a hard gate; the card says 'Flash opens the chamber's lit path').
- **The far end (design):** **chest with TM Earthquake** (PROPOSED, card) at (29,8) (item ball), and a hidden ledge at (28,23) with a visible **Max Revive**.
- **Trainer (1):** **Expert** (Absol 73, Sableye 72, Kingambit 74) at (24,12) `FACE_DOWN`, sight 4, guarding the chest.
- **Wild (dark cave table):** levels 72 to 76 per the card (GOLEM, NOIVERN, DUSKNOIR, SABLEYE, STEELIX, GLISCOR, TYRANITAR, WEAVILE, HYDREIGON, KINGAMBIT, SPIRITOMB, METAGROSS); pool Surf (WHISCASH, GOLDUCK, LANTURN, SLOWKING, KINGDRA).
- **Exit:** the arrival tile warps back to B1F (18,17).
- **Objects:** 1 + 2 item balls = **3**.

## 2.4 Warps

| Map | Tile | Destination | Dest warp |
|---|---|---|---|
| `R30` | cave door (11,24) | `EchoHollow_1F` | arrival (16,33) |
| `EchoHollow_1F` | mats (16,32),(16,33) | `R30` | (11,24) |
| `EchoHollow_1F` | ladder A (5,19) | `EchoHollow_B1F` | (7,19) |
| `EchoHollow_1F` | ladder B (3,33) | `EchoHollow_B1F` | (3,32) |
| `EchoHollow_B1F` | (7,19) / (3,32) | `EchoHollow_1F` | (5,19) / (3,33) |
| `EchoHollow_B1F` | (17,31) | `EchoHollow_B2F` | (5,3) |
| `EchoHollow_B2F` | (5,3) | `EchoHollow_B1F` | (17,31) |
| `EchoHollow_B1F` | sealed wall (18,17) (after the puzzle) | `EchoHollow_EchoChamber` | (5,28) |
| `EchoHollow_EchoChamber` | (5,28) | `EchoHollow_B1F` | (18,17) |

## 2.5 Flags (not claimed), checklist, open questions

**Flags:** `FLAG_ECHO_HOLLOW_STONE_1`, `_2`, `_3` (called), `FLAG_ECHO_HOLLOW_CHAMBER_OPEN`, `FLAG_RECEIVED_TM_EARTHQUAKE_ECHO`, `FLAG_RECEIVED_MAX_ELIXIR_ECHO`, `FLAG_ITEM_ECHO_HOLLOW_*`, `FLAG_HIDDEN_ITEM_ECHO_HOLLOW_*`, `VAR_ECHO_HOLLOW_STONES` (0 to 3). Using `VAR_TEMP_0` would cost no spare var if the player is allowed to restart the puzzle after leaving; the card wants the progress kept.

**Build checklist.** 1) Read flags.md. 2) Trace the three Union Cave floors and the dark cave with the vanilla Cave tileset (or Gen 4 Cave if imported), `MAP_TYPE_UNDERGROUND`, section `MAPSEC_ECHO_HOLLOW`. 3) Ladders and warps. 4) Place boulders, the cracked rock nook and the stepping stones. 5) Place the pillar and the three stones, the sealed wall as a wall metatile with a pre-placed warp. 6) Set `requires_flash` on the chamber. 7) Close and reload Porymap after Claude edits events. 8) Claude wires scripts and trainers; `make -j4`; test the puzzle order and the wrong-stone reset in mGBA. 9) Update docs and credits; commit.

**Open questions.** 1) Union Cave plus Dark Cave (card question 1): kept. 2) The echo puzzle is mine: say if you want switches or braille. 3) No Center in the cave (card): fine two roads from Vesperhaven? 4) Vanilla Cave tileset or Gen 4 Cave for the look?

---

# 3. ARGENT PEAK (post-game mountain, the toughest levels)

## 3.1 Quick facts

| | |
|---|---|
| Maps | `ArgentPeak_BaseCamp` (**43 x 32**, outdoor), `ArgentPeak_EntranceCave` (**17 x 32**), `ArgentPeak_UpperCave` (**24 x 29**), `ArgentPeak_Summit` (**12 x 31**, the image is 11 x 29), `ArgentPeak_PokemonCenter_1F`, `_2F` |
| Section | `MAPSEC_ARGENT_PEAK` (11 characters), all maps. **Not a fly town**; `HEAL_LOCATION_ARGENT_PEAK` on the tile outside the camp Pokémon Center door (write `respawn_map` before `respawn_npc`; a blackout inside returns to the camp) |
| Arrival | R31's top edge x 24-27 to the Base Camp's bottom edge x 24-27 (a ravine you cut into the camp's southern rock wall: see 3.3) |
| Music / weather | Camp `MUS_ROUTE104` low, caves `MUS_CAVE_OF_ORIGIN`, summit `MUS_MT_PYRE_EXTERIOR` (wind); weather camp `WEATHER_SNOW` is marked **Unused** in `include/constants/weather.h` (it exists in the code but shipped nowhere): **test it in mGBA before relying on it**, otherwise `WEATHER_SHADE` or `WEATHER_SUNNY`; caves none |
| Tilesets | Camp: `gTileset_General` + **LeoB ORAS `secondary/fallarbor`** (shared with R31; pale rock, grass, cliffs). Caves and summit: **vanilla `gTileset_MeteorFalls`** (waterfalls, ledge stairs, boulders; no import). Center: vanilla. The cave interior look of the Palladium Mt Silver images is grey-blue rock, which Meteor Falls matches |
| Credits | Palladium team for the four images (first commit); LeoB `fallarbor` (CREDITS row, door anim, engine-edits) if imported |
| Objects | Camp 10, Entrance cave 8, Upper cave 6, Summit 6 (all under 15) |
| Effort | **Hard**: four maps, 11 trainers, the heaviest data, a Center and a heal location |

## 3.2 Description

**First glance, from R31.** The trail narrows into a ravine and opens onto a high green shelf on the mountain: a pond in the middle, tall pines, red-roofed Pokémon Center halfway up on the right, and at the top left the black mouth of a cave. Snow flecks the wind. The rock walls around the shelf are close and tall. A ranger at the ravine mouth says the trail is 'closed in winter', and then, 'it is open now'.

**Mood, colour, sound, time of day.** Hard, clean and a little proud: grey stone, dark pine, a Center roof of red, white snow on the high rock. This is **the toughest place in the game** (levels 70 to 85), so the palette gets colder the higher you go. Sound: wind, a low drone of the cave track. **Time of day: late afternoon, thin cold light.**

**The one memorable view.** The summit bench: the whole region laid out below under a pale sky, Troglodyte sitting at one end of it, humbled, pretending not to be.

## 3.3 Floor by floor

All coordinates are **read off the Palladium images (about +-1 or 2 tiles)** unless marked (design).

### Base Camp (`mtsilver9no.png`, 43 x 32, outdoor)

The image: a **huge rock mass** around the edges (impassable cliff tiles) with a **green plateau** inside (x 7-42, y 10-26). Rock ledges step down from the top-left. Features: a **cave door** high on the left rock face at about **(21,4)** with a small sand patch (x 19-22, y 5-8) before it; the **Pokémon Center** (red roof) at **(24,9)-(28,12)**, its door at **(26,12)**, with a sand porch (x 24-28, y 13-14); a **pond** (L-shaped, x 17-20, y 17-20 plus x 19-26, y 20-23); a column of three big pines at (17-20, 10-16); **tall-grass patches** at (19-23, 9-17), (23-29, 17-19) and the right side (36-41, 11-17); two pines at (7-10, 16-18); round shrubs along the right edge. **The bottom edge is solid rock in the render.**

- **The ravine (design, the one edit to the render).** Cut a **4-wide ravine (x 24-27) from the bottom edge (y 31) up to the plateau at y 26** through the rock wall so R31's top edge x 24-27 connects. Add a **signpost** at (28,27): 'ARGENT PEAK BASE CAMP. THE TRAILS ARE HARD.'
- **Pokémon Center** (Emerald 4-wide: (25,9)-(28,12), door (26,12)): shared `LAYOUT_POKEMON_CENTER_1F`/`_2F`; heal tile (26,13); an **old climber** and the **camp nurse** are the objects in it. Interior positions as vanilla: nurse (7,2), mats (6,8),(7,8), stairs (1,6).
- **Camp clerk** and a **stall** (Max Potion, Revive, Full Heal, Ultra Ball; card) at (30,11) `FACE_LEFT`, under an awning decoration at (29..31, 11..12).
- **Cave door** (21,4) to the Entrance Cave.
- **Cut path (optional, card HMs: Cut):** a Cut tree object at (19,14) hides a nook with a hidden Star Piece (see items).

**Trainers (5, camp; the toughest wild-adjacent trainers, 74 to 76).**

| Class | Team (card) | Tile | Facing | Sight |
|---|---|---|---|---|
| Hiker | Golem 74, Steelix 75, Rhyperior 75, Magcargo 74 | (25,24) | `FACE_DOWN` | 4 (guards the ravine top) |
| Black Belt | Hariyama 74, Machamp 75, Conkeldurr 75 | (12,19) | `FACE_RIGHT` | 4 |
| Cooltrainer female | Weavile 75, Mamoswine 75, Glaceon 74 | (30,15) | `FACE_LEFT` | 4 |
| Psychic | Alakazam 75, Gallade 75, Gardevoir 75 | (36,13) | `FACE_DOWN` | 3 |
| Cooltrainer male | Salamence 76, Metagross 76 | (21,7) | `FACE_DOWN` | 4 (guards the cave mouth) |

**NPCs and objects (camp, 10):** **Ranger at the camp gate** at (26,28) in the ravine `FACE_UP` (the trail is 'closed in winter'; after `FLAG_ARGENT_PEAK_OPEN` his lines change and he warns about the trainers; he stays on the map; the locked gate itself is R31's), **clerk** (30,11), **old climber** at (19,9) `FACE_DOWN` (Waterfall hint and the **Max Elixir**), 5 trainers, one visible **Rare Candy** on a ledge at (38,10) = **9 objects**; add a Cut tree at (19,14) for **10**.

**Wild.** Camp grass (levels 72 to 76, card), camp pond Surf (GOLDUCK, AZUMARILL, WHISCASH, LAPRAS, GYARADOS, 72 to 76), rods (card).

### Entrance Cave (`mtsilverentrance5uq.png`, 17 x 32)

The image: a winding cave with **ledges and stairs** inside, pale blue-grey walls, tan floor, boulders and shining items. The **bottom exit (yellow mat) at about (8,31)**, the **top exit (dark door) at about (14,0)**, stairs at about (4,3), (10,3), (8,8), (7,12), (13,12), (9,21), (11,28); boulders at about (3,7), (5,14), (15,4); items at about (9,4), (12,1), (13,16).

- **Warps:** bottom mat (8,31) from the camp cave door (21,4); top door (14,0) to the Upper Cave (15,28).
- **Strength boulders (3, card):** (3,7), (5,14), (15,4). **Everstone nook:** the boulder at (15,4) closes a nook with the **Everstone** at (14,3).
- **Cracked rock (Rock Smash, card):** at (3,3), opening a side nook with the **second PP Max** (card: 'PP Max x2: upper cave visible, side nook'): PP Max at (2,3).
- **Visible items:** **Rare Candy** (13,16); **Max Revive** (14,22). **Hidden:** **Star Piece** (6,26).
- **Optional dark side cave (card: Flash optional):** a small dark nook off the entrance cave at (2,20) with nothing in it but a shiny hidden **Nugget** (design).

**Trainers (2).**

| Class | Team (card) | Tile | Facing | Sight |
|---|---|---|---|---|
| Dragon Tamer | Dragonite 78, Kommo-o 78, Haxorus 79, Hydreigon 79 | (8,17) | `FACE_DOWN` | 4 |
| Expert | Tyranitar 78, Aggron 78, Lucario 79 | (10,9) | `FACE_LEFT` | 4 |

**Objects:** 2 + 3 boulders + 2 visible balls + the Everstone ball + the PP Max ball = **8**. (If you want to stay under 8, one boulder can be decoration rock, since only (15,4) is used.)
**Wild (cave, levels 75 to 80, card):** TYRANITAR, STEELIX, MAMOSWINE, WEAVILE, METANG, MACHAMP, MISMAGIUS, GOLURK, HYDREIGON, DRAGONITE, METAGROSS, SALAMENCE.

### Upper Cave (`mtsilver27oa.png`, 24 x 29): the waterfall climb

The image: **three waterfalls**: **A** top-left (x 2-5, y 0-5), **B** right (x 16-19, y 5-12), **C** bottom-left (x 3-10, y 19-27, the biggest), each with a blue pool at its base (pools at about (2-6,5-7), (14-19,12-14), (4-11,26-28)); dark door tiles at **(9,3)**, **(20,1)**, **(12,18)**; stairs at about **(9,8)**, **(18,4)**, **(16,20)**, **(8,21)**; a yellow mat at the bottom **(15,28)**. Sand paths link ledges; boulders and shining items on the ledges.

- **The climb (design, from the card: Waterfall badge 8 and Surf):** arrive at the bottom mat **(15,28)** from the Entrance Cave; surf west into **pool C** (4-11, 26-28) and **climb waterfall C** (north, tiles x 4-9, y 19-25) to the ledge (6,18); take the stair (8,21)... then follow the sand to **pool B** (14-19, 12-14), **climb waterfall B** (x 17-18, y 5-11) to the ledge (18,4), cross to **pool A** (2-6, 5-7) and **climb waterfall A** (x 3-4, y 0-4) to the top-left ledge (3,1), where **TM Hyper Beam** lies (card: 'Upper cave ledge, Waterfall'). The **stair to the summit is the dark door at (9,3)**, reached from the top of fall A along the top ledge ('at the top of the third fall').
- **Warps:** bottom mat (15,28) from the Entrance Cave top door (14,0); the dark door (9,3) up to the Summit (6,28); the other dark doors (20,1) and (12,18) are **decoration** (closed), or the optional Rock Smash side nook door at (20,1).
- **Trainers (2):** **Hiker** (Steelix 77, Golurk 77, Gliscor 78, Rhyperior 78) at (13,24) `FACE_UP`, sight 4; **Cooltrainer female** (Garchomp 79, Froslass 78, Weavile 79, Mamoswine 79) at (14,8) `FACE_LEFT`, sight 4.
- **Items:** visible **PP Max** at (19,2) (card), **Full Restore** at (20,13), **Max Revive** at (6,12), **TM Hyper Beam** at (3,1) (Waterfall); hidden **Nugget** at (11,16).
- **Pools:** Surf and fishing per the card (levels 77 to 80 for Surf; rods as the camp). **Wild (cave 75 to 80)** as the Entrance Cave.
- **Objects:** 2 + 4 item balls = **6** (+1 optional).

### Summit (`mtsilberredplaceuhhhyeah6jn.png`, 11 x 29 render; plan 12 x 31)

The image: a **top plateau** (x 1-9, y 1-7) with a stair at about **(5,8)** below it, then a **long vertical path** (x 3-7, y 9-16), a **black gap** (unreadable, y 17-23, an artefact of the stitched image), another stair at about **(5,25)** and a dark door/hole at **(5,27)** at the bottom.

- **Plan (design):** a 12 x 31 map: the **bottom door (5,28)** from the Upper Cave dark door (9,3); a long path north through rock walls (fill the black gap with rock and a short bend), a **stair (5,8)** up to the **top plateau** (x 1-9, y 1-7).
- **The stone ring and bench (design):** a ring of standing stones at the plateau (3,2),(7,2),(3,5),(7,5) (decoration, blocked), **Leftovers** (ball) in the middle at (5,3), a **bench** at (5,6) with a plaque `bg_event` (card: 'IN MEMORY OF A VERY STRONG ARGUMENT'). **Troglodyte** at (4,6) on the bench `FACE_RIGHT`, sulking and training; **SIR BISCUIT** (Stoutland, ambient `SPECIES(STOUTLAND)` object) at (6,6).
- **The fight (PROPOSED, card):** Troglodyte's post-game rematch: **Stoutland 76, Gardevoir 77, Vaporeon 77, Tyranitar 78, Pyroar 78, starter final form 80** (the finale's six raised by 8; humbled and unpretentious; reuses a vanilla id). After the win he gives the **Ability Patch** (PROPOSED), `FLAG_ARGENT_PEAK_TROG_DEFEATED`.
- **Summit approach trainer:** **Cooltrainer male** (Dragapult 82, Kingambit 82, Metagross 83, Salamence 83, Garchomp 83) at (5,14) `FACE_DOWN`, sight 4, on the long path below the plateau stair.
- **Items:** **Leftovers** at **(5,3)** in the stone ring (reaching the summit needed Waterfall, card); **Rare Candy** visible at (2,9); hidden **Star Piece** at (8,12).
- **Wild (summit corridor, levels 80 to 85):** TYRANITAR, GARCHOMP, METAGROSS, HYDREIGON, SALAMENCE, KINGAMBIT, URSALUNA, DRAGONITE, RHYPERIOR, MAMOSWINE, SPIRITOMB, DRAGAPULT (card). Set the land-encounter attribute on the corridor's floor; the plateau has none.
- **Objects:** trainer 1 + Troglodyte + Stoutland + 3 item balls = **6**.

## 3.4 Pokémon Center and heal location

Camp Pokémon Center: `ArgentPeak_PokemonCenter_1F` and `_2F`, vanilla layouts, positions as in vanilla. Add **`HEAL_LOCATION_ARGENT_PEAK`** at (26,13) (card option 1; or share Hollowbrook's). No fly point. The Center's interior objects: nurse, **old climber** is outdoors, a **tired Hiker** on the bench (10,6) (ambient).

## 3.5 Warps and connections

| Map | Tile | Destination | Dest warp |
|---|---|---|---|
| `R31` | top edge x 24-27 | `ArgentPeak_BaseCamp` bottom edge x 24-27 | connection, offset 0 |
| `ArgentPeak_BaseCamp` | (26,12) | `ArgentPeak_PokemonCenter_1F` | 0 |
| `ArgentPeak_BaseCamp` | cave door (21,4) | `ArgentPeak_EntranceCave` | (8,31) |
| `ArgentPeak_EntranceCave` | (8,31) | `ArgentPeak_BaseCamp` | (21,4) |
| `ArgentPeak_EntranceCave` | door (14,0) | `ArgentPeak_UpperCave` | (15,28) |
| `ArgentPeak_UpperCave` | mat (15,28) | `ArgentPeak_EntranceCave` | (14,0) |
| `ArgentPeak_UpperCave` | dark door (9,3) | `ArgentPeak_Summit` | (5,28) |
| `ArgentPeak_Summit` | door (5,28) | `ArgentPeak_UpperCave` | (9,3) |
| `ArgentPeak_PokemonCenter_1F` | (6,8),(7,8) | `ArgentPeak_BaseCamp` | 0 |

## 3.6 Items and secrets (card, with positions)

| Item | Where | Gate |
|---|---|---|
| Rare Candy x3 | Camp ledge (38,10), Entrance cave (13,16), Summit (2,9) | None |
| PP Max x2 | Upper cave (19,2) visible; Entrance cave side nook (2,3) | Rock Smash for the nook |
| Max Revive x2, Full Restore | Entrance (14,22), Upper (6,12), Upper (20,13) | None |
| Leftovers | Summit ring (5,3) | Waterfall (reach the summit) |
| Everstone | Entrance nook (14,3) | Strength |
| TM Hyper Beam | Upper cave ledge (3,1) | Waterfall |
| Max Elixir | Old climber | Talk |
| Ability Patch | Summit bench, after the Troglodyte fight (PROPOSED) | Beat him |
| Star Piece, Nugget | Hidden: Entrance (6,26), Summit (8,12), Upper (11,16), a Cut-tree nook at the camp | None |

## 3.7 Flags (not claimed), checklist, open questions

**Flags (card):** `FLAG_ARGENT_PEAK_OPEN` (game clear), `FLAG_ITEM_ARGENT_PEAK_RARE_CANDY_1` to `_3`, `FLAG_RECEIVED_ABILITY_PATCH_ARGENT`, `FLAG_ARGENT_PEAK_TROG_DEFEATED`, `FLAG_HIDDEN_ITEM_ARGENT_PEAK_*`; new (PROPOSED): `FLAG_ITEM_ARGENT_PEAK_PP_MAX_1`, `_2`, `_MAX_REVIVE_1`, `_2`, `_FULL_RESTORE`, `_EVERSTONE`, `_HYPER_BEAM`, `_LEFTOVERS`.

**Build checklist.** 1) Read flags.md; decide the LeoB `fallarbor` import (shared with R31). 2) Trace the Base Camp (43 x 32) and cut the ravine. 3) Place the Center, the stall and the cave door; set the heal location. 4) Trace the Entrance Cave with vanilla Meteor Falls pieces, then the Upper Cave with its three waterfalls and pools (copy Waterfall tiles from Meteor Falls), then the Summit. 5) Warps and the R31 connection (R31 must exist first). 6) Boulders, cracked rock, Cut tree. 7) Close and reload Porymap after Claude's event edits. 8) Claude wires trainers (11), Troglodyte's fight, items, dialogue; `make -j4`; test the Waterfall climb order. 9) Update design docs and credits; commit.

**Open questions.** 1) No summit boss and no legendary (card question 1): Troglodyte is the summit boss in my plan; is that enough? 2) Troglodyte's rematch is the card's proposal. 3) Is a Pokémon Center on a landmark acceptable (card question 4)? 4) The 11 x 29 summit image was stitched with a black gap; I fill it with rock: OK? 5) `WEATHER_SNOW` is marked Unused in `include/constants/weather.h`; the repo also has an `Emerald Slide` snow-tileset folder in the Team Aqua repo. Test before relying on either.
