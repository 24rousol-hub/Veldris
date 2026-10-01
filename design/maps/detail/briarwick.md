# BRIARWICK: detailed city design (PROPOSED, 2026-10-01)

Status: **PROPOSED.** The build brief for the author's Porymap work. Facts come from [../towns/briarwick.md](../towns/briarwick.md) (role, roads, NPCs, items, Scheme 2), [../../dialogue/briarwick.inc](../../dialogue/briarwick.inc) (every NPC and sign), [../../gyms.md](../../gyms.md), [../../trainer-roster.md](../../trainer-roster.md), [../../goldsworth.md](../../goldsworth.md), [../../troglodyte-arc.md](../../troglodyte-arc.md) and [../interiors/README.md](../interiors/README.md). Roads: [routes-west-a.md](routes-west-a.md) (R3, R8, R9) and, outside this group, R4. The name is approved; everything else is a suggestion. New minor names are marked PROPOSED. Nothing is built.

Quick facts: **city**, place 4. Gym 2 Bug, **HACHIMEL** (`TRAINER_HACHIMEL`, Kricketune 17, Vivillon 19), HUSK BADGE, gives HM Rock Smash and TM Thief. The **first Goldsworth house** (NPC only, no battle). **Scheme 2** (the 'fumigation' tent) plays out at the gym door. The Apiary. Fly point and heal location: yes. No Troglodyte fight (an optional sighting only).

Coordinates are `(x, y)` in tiles from the top-left. They are **read off the render and right to about one tile**; confirm each with Porymap's status bar. Map size: the render is `violetcity0ai.png`, 783 x 681 px with a 1 px grid, so `(px - 1) / 17` = **46 x 40**. The east gatehouse is cropped by the render's right edge, so **make the map 50 x 40** (add four columns of pines on the right so the gate building stands whole at x 44 to 49). Size check: (50 + 15) x (40 + 14) = 3,510 of 10,240.

---

## 1. Description

**First glance from Route 8 (south edge).** You walk up a 3-wide grass lane out of a dense pine wall and onto a pale grey paved street. Straight ahead and to the right, the gym's gold-brown roof; left, the blue Mart roof. Beyond them the town climbs north in two long stripes of water, the two L-shaped ponds, and between the ponds, high above the roofs, **the Apiary**: a tall wooden tower of three storeys at the top of a long paved path.

**First glance from Route 3 (east gate).** You step out of the grey gatehouse onto a paved path at the east edge. The red Pokémon Center roof is to the north-west across a small paved square, with red berry flowers just south of it.

**First glance from Route 4 (west).** A paved strip leaves the pines at the left edge and runs east, with the Mart's blue roof below.

**Mood and colour.** The forest keeps the town in line: deep pine green, pale grey paving, the gold of the gym roof and the Apiary's wood, two bright blue ponds, a red Center roof. Dappled afternoon light, `WEATHER_SUNNY`. Civic, slightly formal, quiet, with a faint smell of honey and of lemon.

**The one gaudy thing.** The Goldsworth house, a rounded, orange-and-white pod dropped on a pale sand patch at the far south-west beside a rock outcrop, as if lowered by crane. It is the only building here that does not belong.

**Sound.** `MUS_FORTREE` (the treetop town track suits the forest city). Pokémon cries: KRICKETOT, a COMBEE hum from the Apiary, VIVILLON. No real animals: she keeps COMBEE and hives.

**The one memorable view.** From the middle of the main street at (28, 22), look north up the paved path (x 26 to 29, y 8 to 19) between the two ponds to the Apiary's door at (27, 7), with the tower filling the top of the screen. Keep the path straight and the trees along it low so the line of sight reads.

**What the player does here.** Arrives with badge 1 (level about 12 to 16), meets the sealed gym and the 'fumigation' crew, watches the SPINARAK seal the tent, battles through the web gym (two trainers and HACHIMEL), gets the HUSK BADGE, Rock Smash and Thief, visits the Apiary for HONEY, the Goldsworth house for the first cousins, and can go on west (R4), north-east (R9 to Mothwood), or back east and south.

---

## 2. Street layout in words (numbered walk)

Four roads meet here. **R8 enters the south edge** at x 16 to 18; **R3 arrives by the east gatehouse** (door (46, 28)); **R4 leaves the west edge** at y 10 to 12; **R9 leaves by the north-east gatehouse** (door (40, 4)).

1. **The south lane (x 16 to 18, y 23 to 39).** A 3-wide grass lane between tree blocks, paved at its top end (y 22 to 23) and left grass below. R8 arrives at the bottom edge; remove the pines at x 16 to 18, y 35 to 39 (the render's grass lane is closed at the bottom by a tree row).
2. **The main street (y 20 to 22, x 9 to 35).** The paved spine, three rows wide. It runs from the west branch to the PC spur.
3. **The central square (x 12 to 38, y 16 to 22).** The three roofs on the street's north edge: the **Mart** (x 12 to 15, y 16 to 19, door (14, 19)), the **Gym** (x 20 to 25, y 16 to 20, door (23, 20)), and **House B** (x 32 to 37, y 16 to 19, door (34, 19)). A sign at (31, 19) is House B's name plate; a sign at (26, 20) is the gym's.
4. **The Apiary Walk (x 26 to 29, y 8 to 19).** A 4-wide paved path from the square north between the two ponds to the Apiary's front door at (27, 7). A sign at (28, 10) ('The Apiary... a very long staircase. Knock softly'). Trees fill both sides (x 23 to 25 and x 30 to 33, y 8 to 15).
5. **The Apiary (x 25 to 30, y 0 to 7).** The three-storey wooden tower at the top centre; door at the bottom of the ground floor, (27, 7).
6. **The two ponds.** Left pond: a top arm (x 14 to 21, y 2 to 4) and a long stem (x 18 to 21, y 5 to 17), with a small fenced bridge or fence at (14 to 17, 5). Right pond: a stem (x 34 to 37, y 4 to 11) and a foot (x 30 to 37, y 12 to 15). Water decoration, shallow, **no Surf needed** (the path goes around). Fishing is allowed.
7. **The west branch (x 0 to 11, y 10 to 12; x 9 to 11, y 12 to 22).** A paved strip from the west edge east to x 11, then a paved column south at x 9 to 11 down to the main street. This is R4's exit. House A (x 4 to 8, y 15 to 18, door (5, 18)) sits just west of the column. A sign at (3, 13) is the R4 sign.
8. **The PC spur (x 30 to 35, y 22 to 34).** A 6-wide paved column running south from the street's east end, with the **Pokémon Center** (x 33 to 37, y 25 to 28, door (35, 28)) on its east side and the **South Loop** (a paved ring at x 24 to 33, y 33 to 34) at its bottom.
9. **House C (x 24 to 28, y 30 to 32, door (25, 32)).** On a clearing south of the street, reached by the loop; door faces the loop at (25, 33).
10. **The berry patch (x 33 to 37, y 31 to 34).** Red berry flowers just south of the Center: berry trees and a visible POTION.
11. **The east lane (x 38 to 41, y 5 to 25) and the NE gate.** A grass lane between the right pond and the pine wall, running north from the east end of the town to the **R9 gatehouse** (x 38 to 43, y 0 to 4, door (40, 4)). The render has a clump of four trees at (38 to 41, 12 to 17): remove them to open the lane. A Cut-tree nook on its east side at (42 to 43, 7 to 8).
12. **The east gate path (x 40 to 46, y 26 to 31).** From the PC spur a paved path runs east along y 29 to 31 to x 42, up x 40 to 42 (y 26 to 28), and on east along y 29 to x 46 to the **R3 gatehouse** (x 44 to 49, y 24 to 28, door (46, 28)). Bench at (44 to 45, 30).
13. **The sand patch and the Goldsworth house (x 0 to 8, y 25 to 39).** Pale sand at the far south-west, a rock outcrop (x 0 to 5, y 25 to 30) with a brick doorway at (2, 29) (**decoration**, see 3.12), and the round **Goldsworth house** (x 3 to 7, y 32 to 34, door (5, 34)) with a sign at (7, 34). No path leads to it from the street: a dirt track (sand, 2 wide) runs from the south lane's west side along y 36 to 37, x 8 to 15, so the house is reachable but sits 'off the grid'.

**Water.** The two ponds only. **Ledges.** None in the render. **Trees.** Everywhere not paved: solid pine walls; leave round trees along the Apiary Walk. **Cut trees:** one (TM Bullet Seed nook). **Rock Smash rock:** one (south tree line, see Items). **Palettes.** `gTileset_General` + `gTileset_Petalburg`, as Hollowbrook (see Palette notes for the paving).

---

## 3. Buildings

| Building | Map name | Layout / source | Size | Floors | Notes |
|---|---|---|---|---|---|
| Pokémon Center | `Briarwick_PokemonCenter_1F`, `_2F` | **`LAYOUT_POKEMON_CENTER_1F` / `_2F`, unchanged** | 14 x 9, 14 x 10 | 2 | Nurse, visitor, the tent crew after Scheme 2 |
| Mart | `Briarwick_Mart` | **`LAYOUT_MART`, unchanged** | 11 x 8 | 1 | Clerk, no bug sprays |
| Gym | `Briarwick_Gym` | Custom, trace `azaleagym20yp.png` (13 x 17) | 13 x 17 | 1 | HACHIMEL, two trainers, the web gates |
| The Apiary | `Briarwick_Apiary_1F`, `_2F` | Gen 4 Interior Secondary | 12 x 9, 12 x 8 | 2 | WILF, the old keeper, COMBEE |
| Goldsworth house | `Briarwick_GoldsworthHouse` | Gen 4 Interior Secondary, after `Gold's House.PNG` | 13 x 10 | 1 | Butler, 3 cousins, DUCHESS |
| House A | `Briarwick_HouseA` | Gen 4 Interior Secondary, after `Elm's House.png` | 10 x 8 | 1 | Tired parent and child |
| House B | `Briarwick_HouseB` | Gen 4 Interior Secondary, after `Gold's House.PNG` (lower room) | 11 x 8 | 1 | Tansy, the retired champion |
| House C | `Briarwick_HouseC` | Gen 4 Interior Secondary, after `Elm's House.png` | 9 x 8 | 1 | A kid, always open |
| R3 gatehouse | `Briarwick_R3Gatehouse` | **Gate Platinum Secondary** (Team Aqua repo) | 9 x 12 | 1 | Pass-through, one guard |
| R9 gatehouse | `Briarwick_R9Gatehouse` | Gate Platinum Secondary | 9 x 12 | 1 | Pass-through, one guard |
| Brick doorway (cave) | none | scenery | - | - | Boarded, sign |

**Building outlines on the outdoor map:**

| Building | Footprint (x, y) | Door tile | Tile you stand on to enter |
|---|---|---|---|
| Pokémon Center | 33 to 37, 25 to 28 | (35, 28) | (35, 29) |
| Mart | 12 to 15, 16 to 19 | (14, 19) | (14, 20) |
| Gym | 20 to 25, 16 to 20 | (23, 20) | (23, 21) |
| Apiary | 25 to 30, 0 to 7 | (27, 7) | (27, 8) |
| Goldsworth house | 3 to 7, 32 to 34 | (5, 34) | (5, 35) |
| House A | 4 to 8, 15 to 18 | (5, 18) | (5, 19) |
| House B | 32 to 37, 16 to 19 | (34, 19) | (34, 20) |
| House C | 24 to 28, 30 to 32 | (25, 32) | (25, 33) |
| R3 gatehouse | 44 to 49, 24 to 28 | (46, 28) | (46, 29) |
| R9 gatehouse | 38 to 43, 0 to 4 | (40, 4) | (40, 5) |

All doors face south, per the door rule. (The render's two gatehouses are cropped or show a side view, so the doors above are my choices; the existing cards allow the author to swap.)

### 3.1 Pokémon Center (`LAYOUT_POKEMON_CENTER_1F` and `_2F`)

Unchanged. Vanilla warps and positions, from `OldaleTown_PokemonCenter_*/map.json`:

| Map | Warp | Tile | Destination |
|---|---|---|---|
| 1F | 0 and 1 | (7, 8), (6, 8), door mat | `Briarwick` warp 0 |
| 1F | 2 | (1, 6), stairs | 2F warp 0 |
| 2F | 0 | (1, 6) | 1F warp 2 |
| 2F | 1, 2 | (5, 1), (9, 1) | Union Room, Trade Center |

1F objects: **nurse (7, 2)**; **visitor** at (4, 4) facing right (`CenterVisitor`, the Troglodyte sighting: 'a rich boy... a LILLIPUP in a little jumper'; `CenterVisitorAfter` after the scheme). **After Scheme 2** the foreman at (11, 5) facing left and the junior at (12, 6) facing left stand in the lobby, wrapped in a ribbon and eating biscuits (`ForemanAfter`, `JuniorAfter`); both are hidden before the scheme. **Heal location and fly:** `HEAL_LOCATION_BRIARWICK` lands at **(35, 29)** below the Center door. `respawn_map` **before** `respawn_npc`, give both. A new row in `src/data/veldris_fly_towns.h` and the checklist in [../../region-map.md](../../region-map.md). `OnTransition` sets `FLAG_VISITED_BRIARWICK`.

### 3.2 Mart (`LAYOUT_MART`)

Unchanged. Warps (3, 7) and (4, 7) to `Briarwick` warp 1; **clerk (1, 3)** (`Clerk`: 'We sell no bug sprays. House rule. HACHIMEL asked'). Stock: POKé BALL, GREAT BALL, POTION, SUPER POTION, ANTIDOTE, PARALYZE HEAL, AWAKENING, REPEL, ESCAPE ROPE; **no Bug-type item** (the card says so). A free spot at (5, 5) for a shopper.

### 3.3 Gym: full design

**Source.** `azaleagym20yp.png`, the second Azalea gym image (13 x 17; 208 x 276 px, `px / 16`, drop the partial last row). The first image is Crestfall's, so the two gyms do not repeat. Vanilla tilesets `gTileset_Building` plus a gym secondary (**Fortree Gym** or **Rustboro Gym**, whichever has the plainest green-ish floor; Fortree's gym is the Flying gym in vanilla and Rustboro's the Rock gym, so neither says 'Bug', which is fine). Music `MUS_GYM`.

**The render, read tile by tile:** a pale-green frame at x 0 and x 12 and a window wall at y 1 to 2 (four windows at x 4 to 7, a ladybug crest at (6, 1)). The room floor is x 1 to 11, y 3 to 15. A row of **11 hedge planters** along y 3 (alternating blue-flowered and green), a ring of single planters around a centre tree, two statues at (4 to 8, 13 to 14) and a door at (6, 16). I keep the planter row, the statues, the door and the wall, **replace the planter ring with a hedge garden maze and drop the centre tree** (if the author loves it, it can stand on the back wall at (5 to 7, 1 to 2); it is optional).

**Theme and puzzle (from the card).** Hedge walls and **web tiles** that force a detour: the detour is the puzzle. 'Spinarak weave around the shortest way.' The shortest way, straight up the middle, is webbed shut. Each trainer guards a side alcove; beating them cuts the web in front of the corridor ('the web moves, though').

**New tiles needed (the card allows them; the author draws them, CLAUDE.md rule 2): a HEDGE metatile (1 x 1, blocked) and a WEB metatile (1 x 1, blocked, a corridor tile with a silk web across it).** Both go in the chosen gym secondary's free metatile slots. **Fallback if no art is drawn yet:** a hedge is any 1 x 1 blocked tile; a web is a different blocked tile (any rope or boulder tile). The web must be a **separate metatile id from the hedge** so a script can replace it with the plain floor tile. Candidate sources to inspect first: `Tilesets/The Great Tileset Exchange/Individual Tiles/Oomer/bush.png` (a bush, 19 x 18) as the hedge; the web is new (credit Oomer if the bush is used).

**The tile map** (13 x 17). `#` solid wall or frame, `h` hedge (blocked), `W` web (blocked until its trainer is beaten), `.` floor, `S` guide statue (blocked), `C` crest (wall), `M` door, `L` HACHIMEL, `B` bug catcher, `A` aroma lady.

```
     0 1 2 3 4 5 6 7 8 9 a b c
y0   # # # # # # # # # # # # #
y1   # # # # # # C # # # # # #
y2   # # # # # # # # # # # # #
y3   # h h h h h h h h h h h #
y4   # . . . . . L . . . . . #
y5   # . . . . . . . . . . . #
y6   # h h h h h . h h h h h #
y7   # h h h h h W h h h h h #
y8   # h h h h h . . . . A h #
y9   # h h h h h . h h h h h #
y10  # h h h h h W h h h h h #
y11  # h B . . . . h h h h h #
y12  # h h h h h . h h h h h #
y13  # . . . S . . . S . . . #
y14  # . . . S . . . S . . . #
y15  # . . . . . . . . . . . #
y16  # # # # # # M # # # # # #
```

**The route in three stages** (checked with a breadth-first search; stage 0 reaches only the hall, the corridor to y 10 and the west alcove; stage 1 reaches y 8 and the east alcove; stage 2 reaches the dais):

1. **Stage 0.** Door (6, 16), up the hall past the two statues to the gate row gap (6, 12), then the corridor (6, 11). The next corridor tile **(6, 10) is the first web**. The only open side is **west**: the alcove along y 11, x 2 to 5. 'Left at the hedge.'
2. **West alcove.** The **Bug Catcher** stands at (2, 11) facing east (sight 3: he sees (3 to 5, 11) but not the corridor tile (6, 11), so the player must step in). Beat him: **web (6, 10) disappears** (`setmetatile` to floor, then `special DrawWholeMapView`).
3. **Stage 1.** Up the corridor to (6, 8). The next tile **(6, 7) is the second web**. The only open side is **east**: the alcove along y 8, x 7 to 10. 'Right at the web.'
4. **East alcove.** The **Aroma Lady** stands at (10, 8) facing west (sight 3: sees (7 to 9, 8), so she triggers the moment the player steps off the corridor). Beat her: **web (6, 7) disappears**.
5. **Stage 2.** Up (6, 7), (6, 6), onto the dais. **HACHIMEL stands at (6, 4)** facing down; the player talks from (6, 5). The two dais rows (y 4 to 5) are open the full width (x 1 to 11) for the leader's flowers and the gym guide.

**Objects** (3 live plus 2 statues, far under 15):

| Who | Tile | Facing | Sight | Notes |
|---|---|---|---|---|
| HACHIMEL | (6, 4) | down | none (talk) | `TRAINER_HACHIMEL`; copy the leader pattern of `RustboroCity_Gym/scripts.inc`; Kricketune 17, Vivillon 19 (ace). Apologises to every Pokémon. Gives HUSK BADGE, HM Rock Smash, TM Thief |
| Bug Catcher | (2, 11) | right | 3 | Kricketot 13, Sewaddle 14. `Trainer1*`. 'Left at the hedge, then right at the web. The web moves, though' |
| Aroma Lady | (10, 8) | left | 3 | Combee 14, Burmy 15. `Trainer2*` |
| Statues (bg events) | (4, 14) and (8, 14) | - | - | `GymStatue` before the badge, `GymStatueWin` after (the player's name) |
| Hint plaque (bg event) | (5, 12) on a hedge tile | - | - | PROPOSED text: 'Spinarak weave around the shortest way.' (new, check with `dialogue_check.py`) |

**Web state.** On map load a `MAP_SCRIPT_ON_LOAD` script places each web again unless its trainer's defeated flag is set (the reused trainer ids carry their own flags). The two webs need no new flag. **Warp:** one, at the door **(6, 16)**, to `Briarwick` warp 2.

**Optional item.** A hidden POTION behind the Bug Catcher at (2, 11), the alcove's dead end (PROPOSED; leave out if unwanted).

### 3.4 The Apiary: `Briarwick_Apiary_1F` (12 x 9) and `_2F` (12 x 8)

Gen 4 Interior Secondary (already imported). The hive is the **dome machine** from Fennick's lab (metatiles 326/327, 334/335, 342/343 in `design/interiors.md`), left as is or recoloured honey-gold: a hive-shaped centrepiece that costs no new art. Legend: `#` wall, `W` window (wall), `B` bookshelf (2 x 2), `K` honey counter (blocked), `H` the hive-dome (2 wide, 3 tall), `S` stair block, `R` rug, `P` plant, `m` door mat, `n` NPC spot.

**1F** (ground floor, entered from the front door, 12 x 9):

```
      0 1 2 3 4 5 6 7 8 9 a b
y1    # B B . W . . H H . S S
y2    # B B n . . . H H . S S      WILF at (3, 2), behind the counter
y3    # . K K K K . H H . . .      honey counter (2 to 5, 3), the dome runs y 1 to 3
y4    # . . . . . . . . . . .
y5    # . . R R R R . . P . .      rug (3 to 6, 5 to 6)
y6    # . . R R R R . . . . .
y7    # . . . . . . . . . . .
y8    # # # # # m # # # # # #
```

- **Door mat and warp:** (5, 8) to `Briarwick` warp 3. The player arrives at (27, 8).
- **Stairs up:** the stair block (10 to 11, 1 to 2); its bottom step **(10, 2) is an east-arrow warp** to 2F (copy the metatile used at `Hollowbrook_PlayersHouse_1F` (11, 2)), walking east from (9, 2).
- **Objects:** **WILF** (3, 2) facing down across the counter: `WilfBefore` (before badge 2), `WilfAfter` and **HONEY** gift (`FLAG_BRIARWICK_RECEIVED_HONEY`) after the gym, `WilfIdle`. **COMBEE x2** (Pokémon objects, wander radius 1) at (8, 5) and (9, 6): ambient hum, no battle. 3 objects.

**2F** (12 x 8, the old keeper's room, reached only by the stairs):

```
      0 1 2 3 4 5 6 7 8 9 a b
y1    # T T . W . W B B . . .      trophy cabinet (1 to 2), bookshelf (7 to 8)
y2    # T T . . . . B B . D .      stairwell D at (10, 2), entered walking west from (11, 2)
y3    # . . . . k . . . . . .      OLD KEEPER k at (5, 3)
y4    # . . . t t . . . . c .      low table t (4 to 5, 4 to 5)
y5    # . . c t t c . . P . .
y6    # . . . . . . . . . . .
y7    # # # # # # # # # # # #
```

- **Stairwell down:** (10, 2), arrive on 2F at (11, 2); walking west onto (10, 2) warps to 1F warp 1 (the Hollowbrook 2F pair, mirrored). **No door on this floor.**
- **Objects:** **old keeper** at (5, 3) facing down (`ApiaryKeeper`: 'The first bug-catching contest in the region was held right here'); **COMBEE** at (8, 5). 2 objects. The trophy cabinet (1 to 2, 1 to 2) can be a bg event with a PROPOSED line about a plain net.

### 3.5 Goldsworth house: `Briarwick_GoldsworthHouse`, 13 x 10

**Cold, tidy, rich.** Gen 4 Interior Secondary, after `Gold's House.PNG` (the tall two-room house: use its lower, kitchen-and-rug room as the size reference, then widen to 13). Palette goal: cooler than the other homes (use the blue-grey floor variant and the brown armchairs from the set), a tidy symmetrical room with matching plants. NPC only: no trainers, no ids, 5 objects.

```
      0 1 2 3 4 5 6 7 8 9 a b c
y1    # B B . W T T . W . B B .      trophy cabinets (1 to 2) and (10 to 11), TV (5 to 6)
y2    # B B . . T T . . . B B .
y3    # . . . . . . . . . . . .
y4    # . s s . . . . . s s . .      armchairs (2 to 3, 4 to 5) and (9 to 10, 4 to 5) facing the TV
y5    # . s s R R R R R s s . .      rug (4 to 8, 5 to 7)
y6    # . . . R R R R R . . . .
y7    # P . . R R R R R . . . P
y8    # . . . . . . . . . . . .
y9    # # # # # # m # # # # # #
```

- **Back wall:** two display cabinets (the bookshelf tiles dressed as trophy cases), a TV between two windows, a plant pair at the front corners (0 and 12 on y 7).
- **Door mat and warp:** (6, 9) to `Briarwick` warp 4. Arrive at (5, 35). Outside, a sign at (7, 34): `GoldsworthHouseSign` ('Deliveries to the side gate. Visitors: don't').
- **Objects:**

| Who | Tile | Facing | Label | Notes |
|---|---|---|---|---|
| Butler | (6, 7) | down | `ButlerDoor` / `ButlerAfter` | stands two tiles inside the door; 'Please do not touch anything. Or breathe loudly' |
| BARNABY (boaster) | (3, 6) | up | `BarnabyBefore`, `BarnabyBoast`, `BarnabyBoast2` / `BarnabyAfter` | name PROPOSED already drafted; mild swearing only here |
| Lounger | (9, 6) | up | `LoungerBefore` / `LoungerAfter` | beside the right armchair, 'Shh. I'm resting' |
| Pet owner (KIP, in goldsworth.md) | (10, 3) | down | `PetOwnerBefore` / `PetOwnerAfter` | |
| DUCHESS (PERSIAN, object) | (11, 3) | left | `PetOwner*` or silent | 'Do not pet her. She bites. With contempt' |

Before/after switches on the **Scheme 2 flag**, not the badge. Residents swear mildly and are rude to the player and never cruel to townsfolk. The house is always open (the family is rude either way). The 'Beau' nickname is the cousins' (see `characters.md`).

### 3.6 House A (tired parent and child): `Briarwick_HouseA`, 10 x 8

Gen 4 Interior Secondary, after `Elm's House.png` (trim to 10 x 8). The street smells of lemon (the fumigation).

- **Back wall (y 1 to 2):** window (1), stove (2 to 3), fridge (4 to 5), bookshelf (7 to 8).
- **Floor:** a flower table (3 to 4, 4 to 5) with cushions (2, 5) and (5, 5); a rug (2 to 5, 4 to 6); a plant (9, 6).
- **Door mat and warp:** (4, 7) to `Briarwick` warp 5. Arrive at (5, 19).
- **Objects:** parent at (3, 3) facing up (`HouseAParent` / `HouseAParentAfter`); child at (7, 5) facing left (`HouseAChild`, 'forty tent poles and a lorry'). 2 objects.

### 3.7 House B (Tansy, the retired champion): `Briarwick_HouseB`, 11 x 8

Gen 4 Interior Secondary, after the **lower room** of `Gold's House.PNG` (a kitchen at top-left, a green rug with a table and two plants). A cosy house of someone who won one contest forty years ago and kept the trophy.

- **Back wall:** stove (1 to 2), fridge (3 to 4), a window (5), a **trophy shelf** (7 to 8, 1 to 2; the plain net trophy, a bg event).
- **Floor:** a rug (3 to 7, 4 to 6) with a table (4 to 6, 4 to 5); two plants at (1, 6) and (9, 6).
- **Door mat and warp:** (5, 7) to `Briarwick` warp 6. Arrive at (34, 20).
- **Objects:** **Tansy** (name PROPOSED) at (5, 6) facing up. `TansyBefore`; `TansyHint` (the Mothwood tip) on the second talk; after Scheme 2 `TansyAfter` and the **SILVER POWDER** ('off the shelf'); ESCAPE ROPE on the second talk of the hint. 1 object.

### 3.8 House C (a kid who saw the lorry): `Briarwick_HouseC`, 9 x 8

Gen 4 Interior Secondary, a small one-room house.

- **Back wall:** window (1), stove (2 to 3), fridge (4 to 5), TV (6 to 7).
- **Floor:** a cushion at (3, 4), a plant at (7, 6).
- **Door mat and warp:** (4, 7) to `Briarwick` warp 7. Arrive at (25, 33). Always open.
- **Object:** the kid at (4, 4) facing down (`HouseCKid`, 'One of them is scared of the ponds. I saw him jump'). 1 object.

### 3.9 Gatehouses: `Briarwick_R3Gatehouse` and `Briarwick_R9Gatehouse`, 9 x 12 each

**One interior per gate, two doors each**, joining a building in Briarwick to a building in the road map. **Tileset: Gate Platinum Secondary** (folder `Tilesets/The Great Tileset Exchange/Full Tilesets/Gate Platinum Secondary/`, credit **blloop**; 80 tiles, 128 metatiles; README: based on expanded and triple-layer metatiles). Its `example.png` shows exactly a route gate: a pale tiled corridor, a window row, a wood-framed arch at the north end, stone steps at the south end, and two columns of pink-potted plants. **Important:** the catalogue's `Gatehouse Secondary` tileset is **not** a gate: its `example.png` is a counter lobby (a Center-style lobby with a U-shaped counter). Use **Gate Platinum**, not 'Gatehouse'.

Credits row needed, in the commit that first imports it: `data/tilesets/secondary/gate_platinum/` (or the folder name chosen), creator blloop, source `24rousol-hub/Team-Aquas-Asset-Repo`, `Tilesets/The Great Tileset Exchange/Full Tilesets/Gate Platinum Secondary`, licence 'Please credit blloop for use' (its README).

```
      0 1 2 3 4 5 6 7 8
y0    # # # # # # # # #
y1    # # # # a # # # #      north arch, one warp tile at (4, 1)
y2    # . . . . . . . #
y3    # . P . . . P . #
y4    # . P . . . P . #
y5    # . P . . g P . #      GUARD at (5, 5) in the right half of the corridor
y6    # . P . . . P . #
y7    # . P . . . P . #
y8    # . P . . . P . #
y9    # . . . . . . . #
y10   # . . . . . . . #
y11   # # # # m # # # #      south steps/door mat, one warp tile at (4, 11)
```

- Corridor 3 wide (x 3 to 5), plants (pink pots) at x 2 and x 6 from y 3 to 8.
- **The north arch is on the centre line:** the single warp tile is **(4, 1)** (`a` above). South warp tile **(4, 11)** (`m`).
- **Guard** at (5, 5) facing left. R3 gate: `R3GuardBefore` / `R3GuardAfter` (the road works). R9 gate: `R9Guard` ('Mothwood has no map. Bring snacks and a friend').
- **R3 gate warps:** (4, 11) to `Briarwick` warp 8 (the building at the east edge); (4, 1) to `VeldrisRoute3` warp 0 (R3's west gate building, door (3, 9)). Entering from R3 the player arrives at (4, 1) and walks south.
- **R9 gate warps:** (4, 11) to `Briarwick` warp 9; (4, 1) to the R9 map's **south arrow warp** (see [routes-west-a.md](routes-west-a.md)).
- **Arrival animation:** the exit warps use door/arrow tile behaviour; test in mGBA that the player walks out facing the right way (open question 4).

**Outside the R3 gate:** the bench at (44 to 45, 30) with the **hiker** sitting at (44, 30) facing up (`R3HikerBefore` / `R3HikerAfter`: 'Is the road open yet?'). A sign at (43, 28) (`R3GateSign`). **Outside the R9 gate:** an optional sign at (39, 6), new text, PROPOSED (the card has none).

### 3.10 Brick doorway: scenery

The brick-faced doorway at (2, 29) in the rock outcrop (x 0 to 5, y 25 to 30) with a sign at (4, 30). **Decoration, no warp.** Suggested sign (new text, PROPOSED): 'ROOT CELLAR. LOCKED.' It leaves a hook for a later optional cellar. The rest of the outcrop is a rock face.

---

## 4. NPC placement (outdoors) and the Scheme 2 scene

Text labels use the prefix `Briarwick_Text_`. The cards give 16 NPCs; 8 are outdoors, the rest are in the buildings above.

| Who | Tile | Facing / movement | Label | When |
|---|---|---|---|---|
| Fan (worried gym fan) | (19, 21) | face right | `FanWorried` / `FanAfter` | always |
| Fumigation foreman (Mr Pargeter, PROPOSED) | (21, 22) | face right | `ForemanBefore`, `ForemanAsk`, `ForemanReveal` / `ForemanWrapped` | **scheme only**; after: in the Center |
| Fumigation junior | (25, 22) | face left | `JuniorBefore` / `JuniorAfter` | scheme only; after: in the Center |
| Kid with a net | (6, 11) | wander radius 1 (west strip) | `KidNet` | always |
| Hiker (R3 gate) | (44, 30) | face up | `R3HikerBefore` / `After` | always |
| Berry trees x3 | (34, 32), (36, 32), (35, 33) | - | ORAN BERRY | always |
| Item ball (POTION) | (38, 33) | - | visible | always |

**Signs.** City sign `TownSign` at (27, 23); gym sign `GymSign` at (26, 20) (`GymSignSealed` while the tent stands); Apiary sign `ApiarySign` at (28, 10); R3 gate sign `R3GateSign` at (43, 28); R4 sign `R4Sign` at (3, 13); House B name plate at (31, 19); Goldsworth sign (7, 34); cellar sign (4, 30). Center and Mart signs: the usual pairs beside each door, PROPOSED at (32, 28) and (37, 28) for the Center and (11, 19) and (16, 19) for the Mart.

### Scheme 2 on the map

The beats are in [../towns/briarwick.md](../towns/briarwick.md); this fixes where they happen. All triggers are **`coord_event` triggers at elevation 3** (CLAUDE.md rule). **Keep the scene to 6 objects.**

| Piece | What | Tile |
|---|---|---|
| Tent | 2 objects (each a 32 x 32 sprite) covering the gym door approach | (22, 21) and (24, 21) |
| Foreman, junior, fan | the three standing NPCs above | as in the table |
| Reveal trigger | the player steps up to the tent flap | **(22, 22), (23, 22), (24, 22)**, state 0 |
| Collapse | a SPINARAK (object, species graphics) seals the tent from inside; the crew is wrapped; tent objects removed by the script | at (23, 21) |
| HACHIMEL steps out | she appears at (23, 21) and walks to (23, 22) | 6th object, then `HachimelOut`, `HachimelToCrew`, `HachimelInvite` |
| After | the crew walks to the Center (hide flags; they re-appear inside as in 3.1) | gym door unblocked |

**Assets this scene needs and the repo does not have** (author, open question 3): a **tent** overworld sprite (2 objects, 32 x 32 each) and a **wrapped crew** sprite (the foreman and junior swapped via `OBJ_EVENT_GFX_VAR_n`). Fallback with no art: SPINARAK objects (`OBJ_EVENT_GFX_SPECIES(SPINARAK)`) standing in a ring around the two men, no tent, and the dialogue carries the joke.

---

## 5. Door and warp table

| Map | Warp # | Tile | Destination | Arrive at |
|---|---|---|---|---|
| `Briarwick` | 0 | (35, 28) | `Briarwick_PokemonCenter_1F` warp 0 | (6 to 7, 8) |
| `Briarwick` | 1 | (14, 19) | `Briarwick_Mart` warp 0 | (3 to 4, 7) |
| `Briarwick` | 2 | (23, 20) | `Briarwick_Gym` warp 0 | (6, 16) |
| `Briarwick` | 3 | (27, 7) | `Briarwick_Apiary_1F` warp 0 | (5, 8) |
| `Briarwick` | 4 | (5, 34) | `Briarwick_GoldsworthHouse` warp 0 | (6, 9) |
| `Briarwick` | 5 | (5, 18) | `Briarwick_HouseA` warp 0 | (4, 7) |
| `Briarwick` | 6 | (34, 19) | `Briarwick_HouseB` warp 0 | (5, 7) |
| `Briarwick` | 7 | (25, 32) | `Briarwick_HouseC` warp 0 | (4, 7) |
| `Briarwick` | 8 | (46, 28) | `Briarwick_R3Gatehouse` warp 0 | (4, 11) |
| `Briarwick` | 9 | (40, 4) | `Briarwick_R9Gatehouse` warp 0 | (4, 11) |
| `Briarwick_PokemonCenter_1F` | 0, 1 | (6, 8), (7, 8) | `Briarwick` warp 0 | (35, 29) |
| `Briarwick_PokemonCenter_1F` | 2 | (1, 6) | `Briarwick_PokemonCenter_2F` warp 0 | (1, 6) |
| `Briarwick_PokemonCenter_2F` | 0 | (1, 6) | `Briarwick_PokemonCenter_1F` warp 2 | (1, 6) |
| `Briarwick_PokemonCenter_2F` | 1, 2 | (5, 1), (9, 1) | Union Room, Trade Center | vanilla |
| `Briarwick_Mart` | 0, 1 | (3, 7), (4, 7) | `Briarwick` warp 1 | (14, 20) |
| `Briarwick_Gym` | 0 | (6, 16) | `Briarwick` warp 2 | (23, 21) |
| `Briarwick_Apiary_1F` | 0 | (5, 8) | `Briarwick` warp 3 | (27, 8) |
| `Briarwick_Apiary_1F` | 1 | (10, 2) | `Briarwick_Apiary_2F` warp 0 | (11, 2) |
| `Briarwick_Apiary_2F` | 0 | (10, 2) | `Briarwick_Apiary_1F` warp 1 | (9, 2) |
| `Briarwick_GoldsworthHouse` | 0 | (6, 9) | `Briarwick` warp 4 | (5, 35) |
| `Briarwick_HouseA` | 0 | (4, 7) | `Briarwick` warp 5 | (5, 19) |
| `Briarwick_HouseB` | 0 | (5, 7) | `Briarwick` warp 6 | (34, 20) |
| `Briarwick_HouseC` | 0 | (4, 7) | `Briarwick` warp 7 | (25, 33) |
| `Briarwick_R3Gatehouse` | 0 | (4, 11) | `Briarwick` warp 8 | (46, 29) |
| `Briarwick_R3Gatehouse` | 1 | (4, 1) | `VeldrisRoute3` warp 0 | (3, 10) |
| `Briarwick_R9Gatehouse` | 0 | (4, 11) | `Briarwick` warp 9 | (40, 5) |
| `Briarwick_R9Gatehouse` | 1 | (4, 1) | `VeldrisRoute9` warps 1 to 3 (arrow tiles) | (14, 30) |

**Map connections** (leave 'Mirror to Connecting Maps' ticked):

| Edge | Neighbour | Opening here | Opening there | Offset on `Briarwick` |
|---|---|---|---|---|
| Down | `VeldrisRoute8` | x 16 to 18 | R8 top edge x 13 to 15 | **+3** (R8's left edge is 3 columns right of Briarwick's) |
| Left | R4 | y 10 to 12 | R4's east end | set when R4 is designed (open question 2) |

R3 and R9 are **gate warps, not edge connections**; the road maps do not need a connection back.

---

## 6. Items and secrets (card items, with positions)

| Item | Where | Gate |
|---|---|---|
| POTION | visible, SE berry patch, (38, 33) | none |
| ANTIDOTE | hidden between the two ponds, (24, 8) | none |
| REPEL | hidden by the R4 sign, (4, 13) | none |
| ORAN BERRY x3 | berry patch, trees at (34, 32), (36, 32), (35, 33) | none |
| TM Bullet Seed | behind a Cut tree: tree at (42, 8) on the east lane's east wall, ball at (43, 8) in a 2 x 2 nook | Cut (badge 1) |
| HONEY | gift from Wilf, Apiary 1F | badge 2 |
| SILVER POWDER | from Tansy | after Scheme 2 |
| ESCAPE ROPE | Tansy, second talk | none |
| HM Rock Smash and TM Thief | HACHIMEL | badge 2 |
| PP-type item behind a Rock Smash rock | south tree line, rock at (19, 37), item at (19, 38) (PROPOSED: PP UP) | Rock Smash |

Flags (not claimed): `FLAG_VISITED_BRIARWICK`, `FLAG_BRIARWICK_SCHEME_DONE`, `VAR_BRIARWICK_SCHEME_STATE` (0 setup, 1 tent sealed, 2 done) if the scene needs stages, `FLAG_BRIARWICK_RECEIVED_HONEY`, `FLAG_BRIARWICK_ITEM_*` per item. Reused: `FLAG_BADGE02_GET`, `FLAG_RECEIVED_HM_ROCK_SMASH`. Claim them in [../../flags.md](../../flags.md) when built.

---

## 7. Palette, tiles and what has to be redrawn

- **Outdoor tilesets:** `gTileset_General` + `gTileset_Petalburg` (the LeoB ORAS recolour already in the tree), as Hollowbrook, so Briarwick matches. **No new outdoor import.** The Palladium credit goes in with the first traced map; files used by Briarwick: `violetcity0ai.png`, `azaleagym20yp.png`, `Elm's House.png`, `Gold's House.PNG`.
- **The paved grey path** (the Violet city look): the town's identity. Look in Porymap's metatile picker for a grey paving or plaza tile in `gTileset_Petalburg` or the General set; if none, use the sand path tile and the grey paving only for the Apiary Walk. Nothing to import yet. (open question 5)
- **The Apiary.** No tall wooden tower exists in the Hoenn sets. Cheapest honest version: a 6 x 5 wood-roofed block (the Fortree-style building) with a second and third storey painted as a stack of balconies. Needs new building art; keep the footprint (x 25 to 30, y 0 to 7).
- **The Goldsworth pod.** A rounded orange-and-white building (x 3 to 7, y 32 to 34) is not in the sets. Compromise if no art is drawn: a flat-roofed modern block in white and orange on a sand patch; the joke still works because it is the only building here that does not look like it grew.
- **Gatehouse buildings** (two, 6 x 5 each): the grey roof and glass front. Use a Devon-style or school-style block recoloured grey.
- **Ponds:** General water, shallow, plus a small fence or bridge at (14 to 17, 5).
- **Interiors:** homes and the Apiary on `gTileset_Gen4Interior` (already imported and credited). Center and Mart vanilla. **Gate interiors: Gate Platinum Secondary, a new import** (credits in 3.9). **Gym: `gTileset_Building` + a gym secondary + a hedge tile and a web tile (author art).**
- **Credits needed in the commit that adds them:** Project Palladium team; blloop (Gate Platinum Secondary); Oomer if `bush.png` is used. Nothing for Gen 4 Interior.

---

## 8. Build checklist (in this order)

1. In Porymap create `Briarwick`: layout **50 x 40**, `gTileset_General` + `gTileset_Petalburg`, region `REGION_HOENN`, `layout_version` emerald, section `MAPSEC_BRIARWICK`, can fly to yes.
2. Paint the outdoor map from `violetcity0ai.png`: pine walls, ponds, paved streets and the Apiary Walk, then the lanes (south lane, east lane, the dirt track to the Goldsworth house), then the buildings (the two gatehouses last), then scenery (berry patch, the sand patch, the outcrop).
3. Create the Center 1F, 2F and the Mart with **Add New Map with Layout**. **Check `data/event_scripts.s` has each `.include` exactly once.**
4. After any Duplicate Map: grep `src/data/heal_locations.json` for duplicate ids and delete the extras.
5. Paint the homes (Houses A, B, C, the Goldsworth house, the Apiary 1F and 2F) on Gen 4 Interior.
6. Draw the hedge and web tiles, then paint the gym.
7. In its own commit, import Gate Platinum Secondary (credit row), then paint the two gate interiors.
8. Place warps from section 5, then the connection to R8 (and R4 when it exists).
9. Tell Claude: objects, signs, trainers, the tent scene triggers, the web `setmetatile` scripts, the Goldsworth lines and the heal-location traps are wired afterwards. The author must close or reload Porymap first.
10. Update `design/flags.md`, `design/interiors.md` and `CREDITS.md`; `make -j4`; `python3 design/tools/dialogue_check.py` on any new text.
11. Check no ROM or save is staged.

---

## Open questions

1. **Doors of the gatehouses and the Goldsworth house.** The existing card put the Goldsworth door on the **east** side and House C's door on the **north**; the render shows both facing **south**, which also obeys the door rule, so I used south. The gatehouses are cropped or side-on in the render; I gave them south doors with a short path to each. Confirm.
2. **R4's connection.** R4's card says its west end meets Briarwick's west edge, but a left edge only joins a right edge. Either R4 is mirrored so its east end meets Briarwick, or the connection is made another way. Needs R4's author.
3. **Custom art this design needs:** hedge tile, web tile, hay-like pieces on the other gym, a **tent** sprite and **wrapped crew** sprite, the Apiary tower and the Goldsworth pod. Which are drawn, which use the fallbacks?
4. **Gate interiors.** Both gates have one interior with two doors in different maps, and the far doors use arch or arrow tiles. The player's arrival direction needs a test in mGBA. Alternatively make each gate a plain edge connection and drop the gate interiors.
5. **Paving.** Does the set have the pale grey paving, or does the town use sand paths and a recoloured tile for the Apiary Walk only?
6. **Scheme 2 crew in the Center after.** I assumed the foreman and junior appear in the Center lobby (the 'biscuits' lines). If the author does not want two more objects in the Center, drop them and keep only the visitor's line.
7. **Third man for Scheme 4** (the card's question 3): my tent scene allows only 6 objects, so a third man would need the fan to move out.
