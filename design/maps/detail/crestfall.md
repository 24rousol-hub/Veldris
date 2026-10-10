# CRESTFALL: detailed town design (PROPOSED, 2026-10-01)

**Superseded for the street plan (2026-10-01):** the author approved a different layout (B 'village green', 40 x 32), now built. Coordinates and the street walk below do not match the map; use [../../crestfall.md](../../crestfall.md) 'As built'. The NPC, mood and Scheme 1 notes still apply.

Status: **PROPOSED.** The build brief for the author's Porymap work. Facts come from [../../crestfall.md](../../crestfall.md) (role, buildings, Scheme 1 beats), [../../dialogue/crestfall.inc](../../dialogue/crestfall.inc) and [crestfall_extra.inc](../../dialogue/crestfall_extra.inc) (NPCs), [../../trainer-roster.md](../../trainer-roster.md) (Greta, DALE, WREN), [../../gyms.md](../../gyms.md) and the rules in [../interiors/README.md](../interiors/README.md). Roads: [routes-west-a.md](routes-west-a.md) (R1 meets the west edge, R2 the east edge, R3 the north edge). New minor names are marked PROPOSED. Nothing here is built.

Quick facts: **town**, gym 1 Normal, GRETA (`TRAINER_CRESTFALL_GRETA`, Skitty 10, Miltank 12), STANDARD BADGE, gives Cut and TM Crunch. No Goldsworth house (that moved to Briarwick). Fly point and heal location: yes. Scheme 1 (consultants, hay maze, the MILTANK eat the paperwork, Troglodyte's second fight) plays out at the gym door.

Coordinates are `(x, y)` in tiles from the top-left of the map and are read off the render, so they are right to about one tile. **Confirm every one with Porymap's status bar** before placing an event. Map size: **48 x 32** (the render is 768 x 526 px, no grid, so `px / 16` = 48 x 32.9; drop the last partial row). Size check: (48 + 15) x (32 + 14) = 2,898 of 10,240.

---

## 1. Description

**First glance from Route 1 (west edge).** You step out of the pines onto a pale sand lane at the bottom-left, under the long, flat grey roof of the grain barn. Its blue glass front and the fence in front of it run along your left shoulder. A few steps on, the lane meets a wide sand street that runs east between pines, and the roofs come into view one after another: the gym's gold-brown roof just ahead, the red Pokémon Center roof and the blue Mart roof further up the street. The town sign stands at the mouth of the lane.

**Mood and colour.** Harvest gold and fresh green. Sand paths, dark pine edges, gold gym roof, red and blue roofs, orange flowers. Warm morning light, `WEATHER_SUNNY`. Nothing is sleepy: it is a working town.

**Sound.** `MUS_PETALBURG` (calm, small-town; the quietest of the Hoenn town tracks) outdoors. Pokémon cries do the rest: a MILTANK now and then from the barn side, a ZIGZAGOON. All farm animals are Pokémon, never real animals.

**Time of day.** Late morning. The consultants say 'since nine' and the junior has been lost 'since nine'.

**The one memorable view.** From the north-west clearing (the tomato rows, about (14, 9)) you look back down over House A's green roof, across the sand street and the red Center roof to the gym roof, with the pines closing in on every side. A tidy bowl of roofs in a green bowl. Build it so that this view is clear: keep the trees between the clearing and the street low (round trees, not the tall ones) at about x 14 to 18, y 12 to 15.

**What the player does here.** Arrives at about level 7 to 9 with the first Center and Mart of the game. Meets the consultants, sees the collapse, fights Troglodyte (SIR BISCUIT 7 plus his starter 8), clears the hay maze, beats Greta, gets the STANDARD BADGE, Cut and TM Crunch. Then R2 (east) and R3 (north) open.

---

## 2. Street layout in words (numbered walk)

Roads: **R1 enters the west edge** at the two or three rows y 21 to 22; **R2 leaves the east edge** at y 20 to 22; **R3 leaves the north edge** at x 33 to 35. The sand street (y 16 to 18) is the spine.

1. **West lane (0, 21) to (12, 21).** A 2-row sand lane cut through the pine wall (the render is solid pines here, x 0 to 11, y 20 to 26: remove two rows of trees, rows y 21 and 22). It runs directly under the barn's fence (fence row y 19, trees y 20). Town sign at (10, 21)'s north side, on a cleared tile at (10, 20). `Crestfall_Text_TownSign`.
2. **The Barn (x 0 to 8, y 14 to 18).** The long grey building with glass front and brick base. **Scenery only, door locked** (decision, see Buildings). Its fence runs y 19 (x 0 to 8). A fence post group at (8 to 10, 14) with a sign at (9, 14) marks the barn yard. Rock at (8 to 9, 11 to 13).
3. **The vertical lane (x 12 to 14, y 16 to 26).** A 3-wide sand lane running north-south from the street down to the south loop. At its middle the **Gym** stands to the east (x 15 to 21, y 19 to 23), door at the bottom centre (18, 23), a gym sign at (22, 23). The south loop (sand, x 12 to 27, y 24 to 26) runs in front of the gym door.
4. **The Market square (x 22 to 26, y 19 to 24).** A 5-wide sand pocket east of the gym and west of House B, open to the street above and the south loop below. Three stalls along y 20, a square sign at (26, 19). Details below.
5. **House B (x 27 to 31, y 20 to 22).** Green roof, door (28, 22), name plate at (26, 22). A short sand spur (x 27 to 31, y 23 to 24) ties it to the loop.
6. **The sand street (x 8 to 31, y 16 to 18).** Three tiles wide. North of it, from west to east: the **tomato clearing** (x 12 to 19, y 6 to 12, see below), **House A** (x 15 to 19, y 8 to 11, door (16, 11)) with a sand stub (x 15 to 17, y 12 to 15) down to the street, the **Pokémon Center** (x 22 to 26, y 12 to 15, door (24, 15)), the **Mart** (x 28 to 31, y 7 to 10, door (30, 10)) with a sand lane (x 28 to 31, y 11 to 15) down to the street.
7. **Tomato clearing and the farm (x 12 to 19, y 6 to 12).** A grass pocket ringed by pines, closed to the south by a hop ledge (y 13: x 12 to 15 and x 17 to 19; the stub at x 16 is the gap). Tomato rows are flowers or berry-plant decoration (four short rows). This is where Grandma and the old farmer stand. A hop ledge keeps it tidy; no wild grass.
8. **The north-east hub (x 32 to 42, y 7 to 17).** The street's east end (31, 17) continues as a 3-wide sand path east along y 16 to 17 into a grass pocket beside the Mart. Here: a sign at (36, 15) ('R3 north, R2 east'), the **cave mouth** (x 38 to 41, y 12 to 15, decoration, see Buildings) and a sign at (37, 13). **R3's lane** goes north from (33 to 35, 15) to the top edge: remove the rock at (34 to 35, 9 to 12) and the pines at x 33 to 35, y 0 to 6, and lay sand. **R2's lane** goes east: sand from (36, 17) to (39, 17) through the **gap in the hop ledges at (39, 17)** (the render has two ledge pieces, x 36 to 38 and x 40 to 42, with a one-tile gap between them at x 39), then down to the lane at (39 to 47, 20 to 22) and off the east edge.
9. **Cliff and pines.** The plateau top-right (x 38 to 47, y 0 to 9) is a rocky cliff, decoration only. Pines line every other edge. Boulders (brown mounds) at (33, 3 to 5), (26, 7 to 9), (20 to 21, 7 to 9), (30, 24 to 27) are scenery.

**Water.** None. **Trees.** Round trees from the General tileset, with the two-tile-high pine look only if the LeoB recolour has it (see Palette notes). **Ledges.** The y 13 pair above the stub and the two at y 17 on the north-east path. **Palettes.** Primary `gTileset_General`, secondary `gTileset_Petalburg`, exactly as Hollowbrook.

---

## 3. Buildings

| Building | Map name | Layout / source | Size | Floors | Notes |
|---|---|---|---|---|---|
| Pokémon Center | `Crestfall_PokemonCenter_1F`, `_2F` | **`LAYOUT_POKEMON_CENTER_1F` / `_2F`, unchanged** (shared layouts) | 14 x 9, 14 x 10 | 2 | Nurse, visitor |
| Mart | `Crestfall_Mart` | **`LAYOUT_MART`, unchanged** | 11 x 8 | 1 | Clerk plus shopkeeper |
| Gym | `Crestfall_Gym` | Custom, trace `Azalea Town Gym.png` (15 x 17) | 15 x 17 | 1 | Greta, DALE, WREN, hay maze |
| House A | `Crestfall_HouseA` | Gen 4 Interior Secondary, after `Elm's House.png` | 11 x 8 | 1 | Retired couple, SKITTY on the stairs |
| House B | `Crestfall_HouseB` | Gen 4 Interior Secondary, after `Hero's House 1st Floor.png` | 10 x 8 | 1 | Young trainer, stuck |
| Barn | none | scenery | - | - | Locked, sign on the door |
| Cave mouth | none | scenery | - | - | Boulder across it |
| Market square, farm | none | exterior objects | - | - | Stalls, tomato rows |

**Building outlines on the outdoor map** (Palladium sprite sizes; match with Hoenn/LeoB building sprites of the same width, they will not be pixel-identical):

| Building | Footprint (x, y) | Door tile | Tile you stand on to enter |
|---|---|---|---|
| Pokémon Center | 22 to 26, 12 to 15 | (24, 15) | (24, 16) |
| Mart | 28 to 31, 7 to 10 | (30, 10) | (30, 11) |
| Gym | 15 to 21, 19 to 23 | (18, 23) | (18, 24) |
| House A | 15 to 19, 8 to 11 | (16, 11) | (16, 12) |
| House B | 27 to 31, 20 to 22 | (28, 22) | (28, 23) |
| Barn | 0 to 8, 14 to 18 | (4, 18) locked | none (fence row y 19) |

### 3.1 Pokémon Center (`LAYOUT_POKEMON_CENTER_1F` and `_2F`)

Do not repaint or move anything (the nurse, heal and link scripts depend on the positions). Vanilla positions, checked in `data/maps/OldaleTown_PokemonCenter_*/map.json`:

| Map | Warp | Tile | Destination |
|---|---|---|---|
| 1F | 0 and 1 | (7, 8) and (6, 8), the door mat | `Crestfall` warp 0 |
| 1F | 2 | (1, 6), stairs | 2F warp 0 |
| 2F | 0 | (1, 6) | 1F warp 2 |
| 2F | 1 | (5, 1) | `MAP_UNION_ROOM` |
| 2F | 2 | (9, 1) | `MAP_TRADE_CENTER` |

1F objects: **nurse (7, 2)** facing down (`Crestfall_Text_CenterNurse`, `CenterNurseDone`); **visitor** at (4, 4) facing right (`CenterVisitor`: 'I came here to see the gym. I stayed for the tomatoes'). Keep both away from the walkways to the stairs (1, 6) and the door (6 to 7, 8). 2F objects are the three vanilla attendants (2, 2), (6, 2), (10, 2) and the Mystery Gift man (1, 2), unchanged. Optional: the Alternative Pokecenter Secondary re-skin later (the layout positions do not change).

**Heal location and fly.** `HEAL_LOCATION_CRESTFALL` lands the player at **(24, 16)** below the Center door. In `heal_locations.json` write `respawn_map` **before** `respawn_npc` and always give both (the nurse's local id). One new row in `src/data/veldris_fly_towns.h` plus the checklist in [../../region-map.md](../../region-map.md). Town `OnTransition` sets `FLAG_VISITED_CRESTFALL` (proposed name, claim in `flags.md` when built).

### 3.2 Mart (`LAYOUT_MART`)

Unchanged. Vanilla: warps (3, 7) and (4, 7) to `Crestfall` warp 1; **clerk (1, 3)** (`MartClerk`: 'Hay is not for sale. Everything else is'); **shopkeeper** (PROPOSED second voice, `ShopkeeperBefore/After`) at (5, 5) facing up. A third object spot (9, 4) is free for a shopper. Stock (first stock): POKé BALL, POTION, ANTIDOTE, PARALYZE HEAL, plus REPEL (matches the Mart hint 'a few things for hay fever').

### 3.3 Gym: full design

**Source.** `Azalea Town Gym.png`, 15 x 17 (`px / 16`: 240 x 272). Vanilla tilesets `gTileset_Building` (primary) plus the **Petalburg Gym** secondary (Petalburg's gym is Normal type in vanilla, so the floor and wall look is right for gym 1). Do not use `PetalburgCity_Gym` as the base (9 x 112, 38 warps). Music `MUS_GYM`. Map `show_map_name` on.

**The render, read tile by tile (x, y):** a pale-green window frame fills x 0 to 1 and x 13 to 14 (the outer frame, solid) and y 0 to 2 (the back wall with four windows at x 5 to 8, y 2 and a crest at (7, 1)). The playable floor is x 2 to 12, y 3 to 15. The render has teal grass-coloured floor, two sand pads, flower planters, a centre tree, two statues and a door at (7, 16). **Use the floor, the statues, the door, the wall and the sand dais; replace the planters with hay bales and drop the centre tree** (the maze takes the centre; if the author loves the tree, it can stand as decoration at (6 to 8, 1 to 2) on the back wall).

**Theme.** The hay maze from the dialogue: 'Mind the hay. Don't trust the hay.' Greta is on a sand dais at the back, the player reaches her by a three-lane maze. A short hay maze is right for gym 1: about 35 steps door to Greta.

**New tile needed: one HAY BALE metatile** (1 x 1, blocked, collision 1). The render's flower planter is the model (a wooden box); draw it as a gold hay bale. Put it in the Petalburg gym secondary's free slots, or as a small custom secondary layered on `gTileset_Building`. The author draws it (CLAUDE.md rule 2: Claude does not edit tile files). **Fallback if no tile is drawn yet:** use any 1 x 1 blocked tile from the Petalburg gym set (a crate or a pillar) and swap it later; nothing else in this design depends on its look. Optional candidate to inspect first: `Tilesets/The Great Tileset Exchange/Individual Tiles/Oomer/bush.png` (a bush, 19 x 18; credit Oomer if used).

**The tile map** (15 x 17). `#` solid wall or frame, `H` hay bale (blocked), `.` floor, `s` sand dais (floor), `S` guide statue (blocked), `C` crest (wall), `M` door, `G` Greta, `D` DALE, `R` WREN, `I` item ball.

```
     0 1 2 3 4 5 6 7 8 9 a b c d e
y0   # # # # # # # # # # # # # # #
y1   # # # # # # # C # # # # # # #
y2   # # # # # # # # # # # # # # #
y3   # # . . . s s G s s . . . # #
y4   # # . . . . . . . . . . . # #
y5   # # H H H H H H H H H . . # #
y6   # # . . . . . . R . . . . # #
y7   # # . . H H H H H H H H H # #
y8   # # . . . . . . . . . . . # #
y9   # # H H H H H H H H H . . # #
y10  # # I . . . . . . . D . . # #
y11  # # H H H H H . H H H H H # #
y12  # # H H . S . . . S . H H # #
y13  # # H H . S . . . S . H H # #
y14  # # H H . . . . . . . H H # #
y15  # # H H . . . . . . . H H # #
y16  # # # # # # # M # # # # # # #
```

**The route (checked with a breadth-first search, 35 steps door to the tile in front of Greta):**

1. Door (7, 16), up the entrance hall (y 12 to 15), between the two guide statues (5, 12 to 13) and (9, 12 to 13). The hall is boxed by hay stacks (x 2 to 3 and x 11 to 12).
2. **Gate row y 11:** hay everywhere except the gap at (7, 11).
3. **Lane A (y 10):** step up to (7, 10), turn **east**. The west end of lane A (x 2 to 6) is a dead end with an item. East end: the gap at (11 to 12, 9).
4. **Lane B (y 8):** from the gap, turn **west** along y 8 to x 2 to 3, the gap at (2 to 3, 7).
5. **Lane C (y 6):** from the gap, turn **east** along y 6 to the gap at (11 to 12, 5).
6. **Lane D (y 4):** up the gap, turn **west** to (7, 4). Greta stands on the dais at **(7, 3)**; the player talks from (7, 4). West of (7, 4) the lane is a dead end (x 2 to 6).

**Objects** (3 live plus statues, far under the limit of 15):

| Who | Tile | Facing | Sight | Notes |
|---|---|---|---|---|
| GRETA | (7, 3) | down | none (talk) | `TRAINER_CRESTFALL_GRETA`. Copy the leader pattern in `data/maps/RustboroCity_Gym/scripts.inc` (without its rematch branch, see CLAUDE.md). Skitty 10, Miltank 12 (Oran Berry). Gives STANDARD BADGE, Cut, TM Crunch |
| DALE | (10, 10) | left | 3 | Youngster placeholder, Zigzagoon 9. Sees (7 to 9, 10) as soon as the player steps off the gap, so the first fight comes right away. `Trainer1*` |
| WREN | (8, 6) | left | 3 | Gentleman placeholder, Slakoth 10. Sees (5 to 7, 6) when the player has turned east in lane C. `Trainer2*` |
| Item ball | (2, 10) | - | - | PROPOSED: POTION at the dead end of lane A (reward for peeking) |
| Statues (bg events) | (5, 13) and (9, 13) | - | - | `GymStatueBefore` / `GymStatueAfter` (the left one; the right one can say the same) |

**Warp.** One warp at the door **(7, 16)**, to `Crestfall` warp 2. (The render's door is one tile wide with a frame.) The player arrives at (18, 24) below the gym door.

**Optional flourish, 'it moves'.** The junior says 'Nobody told me it moves.' Make it true once: after DALE is beaten, the hay bale at **(6, 9)** rolls away (`setmetatile` to floor plus `special DrawWholeMapView`), a shortcut from lane A to lane B. Needs one proposed flag (`FLAG_CRESTFALL_HAY_SHIFTED`) and no extra art beyond the hay tile and the plain floor tile.

**Statue text logic.** The left statue reads `GymStatueBefore` until `FLAG_BADGE01_GET`, then `GymStatueAfter` (the player's name). Greta's after-battle lines are `GretaBadge1`, `GretaBadge2` (Cut, Crunch), `GretaAfterBadge`; idle line `GretaIdleAfter`.

### 3.4 House A (retired couple): `Crestfall_HouseA`, 11 x 8

Gen 4 Interior Secondary, after `Elm's House.png` (13 x 10 render; the room is 11 x 8 inside the frame). Same vocabulary as Hollowbrook's neighbour's house. Cheerful, warm, a little full.

- **Back wall (y 1 to 2):** bookshelf (0 to 1), window (2), stove (3 to 4), fridge (5 to 6), TV on its cabinet (7 to 8), **stairs, decorative** (9 to 10; a stair block, no warp, no second floor).
- **Floor:** a flower table at (4 to 5, 4 to 6) with **cushions (3, 5) and (6, 5)**; a plant at (0, 6).
- **Door mat and warp:** **(8, 7)** to `Crestfall` warp 3 (mat on the right so the house is not a copy of the neighbour's). The player arrives at (16, 12).

| Who | Tile | Facing | Text |
|---|---|---|---|
| Wife | (4, 3) | up (at the stove) | `HouseAWifeBefore` / `After` ('those men in suits asked if we'd considered relocating') |
| Husband | (7, 5) | left | `HouseAHusband` (SKITTY on the warm step) |
| SKITTY | (9, 3) | up, beside the stairs | interact: cry plus a line (optional) |

bg events: TV (7 and 8, 2), bookshelf (0 and 1, 2). 3 objects.

### 3.5 House B (stuck trainer): `Crestfall_HouseB`, 10 x 8

Gen 4 Interior Secondary, after `Hero's House 1st Floor.png` (13 x 9: stove and fridge on the left, a bookshelf, a rug). One room, one occupant.

- **Back wall:** stove (1 to 2), fridge (3 to 4), window (5), bookshelf (7 to 8).
- **Floor:** a small table (4 to 5, 4 to 5) with one cushion at (3, 5) and one at (6, 5); a **bed against the east wall** at (8 to 9, 4 to 5) (the trainer 'was going to have lunch first'); a rug at (4 to 7, 6 to 7).
- **Door mat and warp:** (3, 7) to `Crestfall` warp 4. The player arrives at (28, 23).

| Who | Tile | Facing | Text |
|---|---|---|---|
| Young trainer (not a battle) | (5, 6) | up (at the table) | `HouseBTrainerBefore` / `After` |

1 object. (A one-object house is fine; vanilla houses have 1 to 2.)

### 3.6 Barn: scenery, decision

**Decision: the Barn is scenery with a locked door.** Reason: the cards give it no NPC and no scene; the farmhand's line is 'don't go in the barn with those suited men', which works as a warning about a closed building. **Door:** none that opens; put a sign on the wall at (4, 18) (`Crestfall_Text_FarmSign`, 'Pick your own. Pay on the honour system. We see you.'). If the author later wants an interior, the plan is a 12 x 9 hay barn on the Gen 4 Interior Secondary with hay stacks, a MILTANK paddock and the SLAKOTH 'who never moved'; nothing in this brief needs it.

### 3.7 Cave mouth: scenery

The dark doorway at (39, 14) with its mound (x 38 to 41, y 12 to 15) is **decoration**: a boulder or a boarded door across it, no warp. Sign at (37, 13): suggest 'HAY CELLAR. CLOSED BY ORDER OF THE MILTANK.' (new text, PROPOSED, check with `dialogue_check.py` when written). It also gives a hook for a later optional cave.

---

## 4. Market square and farm (exterior objects)

**Market square (x 22 to 26, y 19 to 24).** Three stalls along y 20, each a one-tile counter (a fence or crate tile in front of the seller, at y 21) with the seller standing behind at y 20 facing down. Keep the single tiles x 23 and x 25 open between the stalls (and all of y 19 and y 22 to 24) so the street and the south loop stay connected.

| Stall | Seller tile | Counter tile | Text (extra.inc) |
|---|---|---|---|
| Berries | (22, 20) | (22, 21) | `MarketBerryBefore` / `After` |
| Tomatoes | (24, 20) | (24, 21) | `MarketTomato` |
| Milk | (26, 20) | (26, 21) | `MarketMilk` ('MOOMOO MILK, six hundred a bottle') |

Stall art is **not** in the vanilla tilesets. Cheapest option: a 1-tile wooden fence or crate piece as the counter. If the author wants a proper stall (awning), that is new tile art (open question 4). Square sign `SquareSign` at (26, 19). A flower bed at (24, 22) in place of the render's absent fountain (Hoenn has no fountain tile in these sets).

**Tomato clearing (x 12 to 19, y 6 to 12).** Four short rows of tomato plants (decoration: use the berry-plant or flower tile in rows) at y 7, 9, 11 (x 12 to 14) and y 8 (x 17 to 19). A hidden POTION (PROPOSED) at (13, 10).

---

## 5. NPC placement (outdoors)

Object limit is per camera view (see Open questions 6): at most 16 live in view. These stay under it.

| Who | Tile | Facing / movement | Text label (prefix `Crestfall_Text_`) | When |
|---|---|---|---|---|
| Local worried | (27, 18) | face left | `LocalWorried` | before the scheme collapse |
| Farmhand (gym hint) | (14, 22) | face right | `FarmhandBefore` / `After` | always |
| Farmhand fence | (9, 15) | face up (at the fence) | `FarmhandFenceBefore` / `After` | always |
| Farmhand barn | (9, 18) | face left | `FarmhandBarnBefore` / `After` | always |
| Kid | (20, 17) | wander radius 1 | `KidBefore` / `After` | always |
| Kid at the square | (24, 22) | wander radius 1 | `KidSquareBefore` / `After` | always |
| Grandma | (14, 9) | face down | `GrandmaBefore` / `After` | always |
| Old farmer | (13, 7) | face right | `OldFarmerBefore` / `After` | always (see Open question 3) |
| Market sellers x3 | see section 4 | face down | `MarketBerry*`, `MarketTomato`, `MarketMilk` | always |
| Consultant boss | start (19, 25) | face up | `ConsultantOutside` (setup), `ConsultantBoss` (reveal) | **scheme only** (hidden by flag after) |
| Consultant junior | start (16, 25) | face right | `ConsultantJunior`, `ConsultantCollapse` | scheme only |

**Scheme-only actors (collapse scene):** Greta arrives from the east along y 25, MILTANK (object, one is enough) beside her; Troglodyte arrives from the north-east and walks to (21, 25). Their tiles are in section 6.

Persistent NPCs: 11. Scheme actors: 5. In the worst camera window (around the gym door: x 11 to 25, y 20 to 29) there are at most 9 objects live. Fine.

**Signs.** Town sign (10, 20) `TownSign`; gym sign (22, 23) `GymSign`; square sign (26, 19) `SquareSign`; farm sign (4, 18) `FarmSign` (on the Barn); hub sign (36, 15) new text, PROPOSED; cave sign (37, 13) PROPOSED; Pokémon Center sign (28, 15) and Mart sign (29, 11) use `Common_EventScript_ShowPokemonCenterSign` and the Mart equivalent; House A name plate (18, 15); House B name plate (26, 22).

---

## 6. Scheme 1 on the map (positions; the scripts are Claude's job)

The beats are in [../../crestfall.md](../../crestfall.md); this fixes where they happen. All triggers are **`coord_event`s of type trigger at elevation 3** on walkable tiles (CLAUDE.md rule: no `MAP_SCRIPT_ON_TRANSITION` for cutscenes). The player enters the gym by walking north from **(18, 24)**, so the trigger row is the three tiles below the door.

| Beat | What | Tiles |
|---|---|---|
| Setup | Boss stands outside, locals grumble, Grandma and the old farmer complain | boss at (19, 25), no trigger (he is just talked to) |
| Reveal and collapse | One scene on a trigger as the player steps to the gym door | triggers at **(17, 24), (18, 24), (19, 24)**, var `VAR_CRESTFALL_SCHEME_STATE` (PROPOSED) = 0 |
| Greta and the MILTANK arrive | from the east along the loop (y 25), stop at (22, 25) and (21, 25) | movement script |
| Troglodyte arrives | from the street, down the vertical lane, stops at (20, 25) | `TRAINER_TROGLODYTE_CRESTFALL`, SIR BISCUIT 7 plus his starter 8 |
| After the fight | Troglodyte walks off east, consultants off west, Greta says 'Gym's open. Mind the hay' | hide flags, then the gym is enterable |

Reveal needs the boss and junior at the door **before** the trigger fires, so they start at (19, 25) and (16, 25), flanking the door approach and never blocking (18, 24). Do not block (18, 23) or (18, 24).

---

## 7. Door and warp table

| Map | Warp # | Tile | Destination | Arrive at |
|---|---|---|---|---|
| `Crestfall` | 0 | (24, 15) | `Crestfall_PokemonCenter_1F` warp 0 | (6 to 7, 8) |
| `Crestfall` | 1 | (30, 10) | `Crestfall_Mart` warp 0 | (3 to 4, 7) |
| `Crestfall` | 2 | (18, 23) | `Crestfall_Gym` warp 0 | (7, 16) |
| `Crestfall` | 3 | (16, 11) | `Crestfall_HouseA` warp 0 | (8, 7) |
| `Crestfall` | 4 | (28, 22) | `Crestfall_HouseB` warp 0 | (3, 7) |
| `Crestfall_PokemonCenter_1F` | 0, 1 | (6, 8), (7, 8) | `Crestfall` warp 0 | (24, 16) |
| `Crestfall_PokemonCenter_1F` | 2 | (1, 6) | `Crestfall_PokemonCenter_2F` warp 0 | (1, 6) |
| `Crestfall_PokemonCenter_2F` | 0 | (1, 6) | `Crestfall_PokemonCenter_1F` warp 2 | (1, 6) |
| `Crestfall_PokemonCenter_2F` | 1, 2 | (5, 1), (9, 1) | Union Room, Trade Center (vanilla) | vanilla |
| `Crestfall_Mart` | 0, 1 | (3, 7), (4, 7) | `Crestfall` warp 1 | (30, 11) |
| `Crestfall_Gym` | 0 | (7, 16) | `Crestfall` warp 2 | (18, 24) |
| `Crestfall_HouseA` | 0 | (8, 7) | `Crestfall` warp 3 | (16, 12) |
| `Crestfall_HouseB` | 0 | (3, 7) | `Crestfall` warp 4 | (28, 23) |

**Map connections** (set in Porymap's Connections tab; leave 'Mirror to Connecting Maps' ticked):

| Edge | Neighbour | Opening here | Opening there | Offset on `Crestfall` |
|---|---|---|---|---|
| Left | `VeldrisRoute1` | y 21 to 22 | R1 east edge y 11 to 12 | **+10** (R1's top is 10 rows below Crestfall's top) |
| Right | `VeldrisRoute2` | y 20 to 22 | R2 west edge y 53 to 55 | **-33** (R2's top is 33 rows above Crestfall's top) |
| Up | `VeldrisRoute3` | x 33 to 35 | R3 bottom edge x 26 to 28 | **+7** (R3's left edge is 7 columns right of Crestfall's) |

Route openings are written in [routes-west-a.md](routes-west-a.md); the offsets there are the same numbers seen from the other side. Hollowbrook's own east edge is described there too.

---

## 8. Palette, tiles and what has to be redrawn

- **Outdoor tilesets:** `gTileset_General` + `gTileset_Petalburg`, which are already the LeoB ORAS recolour (replaced in place, credits in `CREDITS.md`). **No new tileset to import and no new `CREDITS.md` row for the outdoor map**, other than the Palladium credit that goes in with the first traced map ('credit the Project Palladium team naming the files used'). Files used by Crestfall: `Azalea Town.png`, `Azalea Town Gym.png`, `Elm's House.png`, `Hero's House 1st Floor.png`.
- **What the vanilla tiles do not have** (known from [../../map-plan.md](../../map-plan.md)): the tall pine look and the green roofs. The render's pines stay round trees; the green house roofs (House A, House B, the render's top-left house and bottom-right house) stay Hoenn red or brown, or recoloured if the LeoB set already has a green roof. Accept about 70 per cent of the look.
- **Palladium roof colour map:** red = Center, blue = Mart, brown-gold = gym. Keep those three because players read them as 'Center', 'Mart' and 'Gym' from far away.
- **Barn:** the long grey building. If the General set has no wide flat-roofed building, build it from a Devon Corp style block (about 9 x 5) and recolour the roof gold.
- **Interiors:** all homes on `gTileset_Gen4Interior` (the Hollowbrook tileset, already credited). Center and Mart keep their vanilla tilesets. Gym: `gTileset_Building` + the Petalburg gym secondary + **one new hay bale tile** (author art).
- **Credits needed in the commit that adds them:** Project Palladium team (the traced renders); Oomer for `bush.png` if it is used for the hay; nothing for Gen 4 Interior (already credited).

---

## 9. Items and secrets (all PROPOSED; the cards give none for Crestfall)

| Item | Where | Gate |
|---|---|---|
| POTION (hidden) | tomato clearing (13, 10) | none |
| POTION (visible) | gym lane A dead end (2, 10) | none |
| ANTIDOTE (hidden) | behind the Mart, (31, 6) | none |
| Cut tree plus ORAN BERRY x2 | a Cut tree at (31, 13) in the Mart lane's east pocket, two berries behind it | Cut (after Greta), a gentle reward for coming back |

Flags (not claimed): `FLAG_VISITED_CRESTFALL`, `VAR_CRESTFALL_SCHEME_STATE` (0 setup, 1 scene played, 2 done) or one flag only, `FLAG_CRESTFALL_ITEM_*` per hidden item, `FLAG_CRESTFALL_HAY_SHIFTED` (optional). Reused: `FLAG_BADGE01_GET`, `FLAG_RECEIVED_HM_CUT`. Claim them in [../../flags.md](../../flags.md) when the scripts are written.

---

## 10. Build checklist (in this order)

1. In Porymap: duplicate or create `Crestfall` (layout 48 x 32, `gTileset_General` + `gTileset_Petalburg`, region `REGION_HOENN`, `layout_version` emerald, section `MAPSEC_CRESTFALL`, can fly to yes).
2. Paint the outdoor map from `Azalea Town.png` in this order: pine border, grass, the sand street and lanes (including the new west lane, the north-east path to R3 and R2, the gap at (39, 17)), then buildings, then ledges, then scenery (boulders, tomato rows, barn fence).
3. Create the Center 1F, 2F and the Mart with **Add New Map with Layout** (shared vanilla layouts). **Check `data/event_scripts.s` has each `.include` exactly once.**
4. After a Duplicate Map: grep `src/data/heal_locations.json` for duplicate ids, delete extras (CLAUDE.md).
5. Paint House A, House B (Gen 4 Interior Secondary), then the gym (draw the hay tile first).
6. Place warps from section 7, then connections (R1, R2, R3 as the neighbouring maps are built).
7. Tell Claude: the NPC objects, signs, coord events, Scheme 1, the gym trainers and Greta's script are wired afterwards (and the author must close or reload Porymap first).
8. Update `design/flags.md`, `design/interiors.md` (house style), `CREDITS.md`. `make -j4`, then `python3 design/tools/dialogue_check.py` on any new text.
9. Check no ROM or save is staged (`git diff --cached --name-only | grep -Ei '\.(gba|sav|srm|sgm)$'`).

---

## Open questions

1. **R2 enters the east edge.** The Route 30 render is a south-north road, so I cut a west opening at the south end of R2 (see the route file) instead of joining R2's bottom to Crestfall's top. This keeps Wendlebury north-east of Crestfall like the sketch. The alternative is Crestfall's south edge to R2's top (Wendlebury then feels south). Confirm.
2. **R3 leaves from the north-east hub (x 33 to 35), not the north-west.** I did this to keep the north-west clearing as the farm and the memorable view. The road to Briarwick then bends west after leaving. Confirm.
3. **`OldFarmerGoldsworth`** (`crestfall_extra.inc`: 'That big house with the shiny gate? The Goldsworths') no longer fits: Crestfall has no Goldsworth house. Reword it ('Up at BRIARWICK there's a big house with a shiny gate...') or drop it.
4. **Stall art and hay art.** No stall tile exists in the Hoenn sets, and the hay bale is new art. Draw them, or use the fence and crate fallbacks.
5. **Barn:** scenery only (my decision), or an interior later?
6. **Object counting.** The engine spawns only objects within about the camera window (`TrySpawnObjectEvents`, `OBJECT_EVENTS_COUNT` 16, 64 templates per map), so the '15 per map' rule in the README is really '15 in view'. Crestfall's 16 templates are fine. Confirm that reading.
7. **Greta and the Cut tree.** Cut is given as an HM here, so the Cut tree at (31, 13) is only usable after the gym. Fine, or move it?
