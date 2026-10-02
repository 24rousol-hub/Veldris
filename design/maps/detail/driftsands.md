# DRIFTSANDS: detailed design (beach town, no gym)

Status: **PROPOSED.** Written 2026-10-01 from [../interiors/README.md](../interiors/README.md), [../interiors/catalogue.md](../interiors/catalogue.md), [../README.md](../README.md), [../../interiors.md](../../interiors.md), [../index.md](../index.md), the card [../towns/driftsands.md](../towns/driftsands.md), roads R24 and R25 ([../routes-south.md](../routes-south.md)), and the Palladium renders `Route 38.png` (the gatehouse end), `Route 40.png` (sand edge mood). House templates **G4-A, G4-B, G4-C** are in [ebbsworth.md](ebbsworth.md) section 6.0. Neighbours: [kingsquay.md](kingsquay.md), [beaconmouth.md](beaconmouth.md). Road detail: [routes-south-detail.md](routes-south-detail.md).

**New minor names and details introduced in this file are all PROPOSED:** West Gate, the trainee lifeguard, the rematch Swimmer's team.

Conventions: **(x, y) from the top-left tile (0,0)**; footprints are `(x0,y0)-(x1,y1)` inclusive; a 4-wide building's door is the bottom-row tile `(x0+1, y1)` (checked on vanilla Dewford: Pokémon Center door (2,10) on footprint x1-4); mats are two tiles wide.

---

## 1. Quick facts

| | |
|---|---|
| Map | `Driftsands`, **32 x 24** (card: about 30 x 24; `(32+15)*(24+14) = 1786`) |
| Exterior base | Vanilla `DewfordTown` (20 x 20) enlarged, with **LeoB ORAS `secondary/dewford`** (sand ground, blue tile roofs, pines, a wooden bridge: see the repo's `7 - Dewford.png`) |
| Section / fly | `MAPSEC_DRIFTSANDS` (10 characters); fly town; `HEAL_LOCATION_DRIFTSANDS` on (14,8) outside the Center |
| Music | `MUS_DEWFORD` (vanilla Dewford; fits a sleepy beach town). Interiors the same, `MUS_POKE_CENTER`, `MUS_POKE_MART` for the shared two |
| Weather | `WEATHER_SUNNY`, `MAP_TYPE_TOWN` |
| Gym / scheme | None. One Scheme 9 **gag** (Pip and the dropped invoice). No Goldsworth house (a town gets none) |
| Roads | R24 west (through the West Gate), R25 north-east (cliff stair) |
| Objects | Town map 9; interiors well under 15 |
| Build effort | **Easy** (card). All interiors are shared or small |

---

## 2. Description

**First glance from R24 (the West Gate).** The player steps out of a plain timber gatehouse onto a pale, wide-planked boardwalk. Sun glare, the hiss of surf, a lifeguard tower on stilts, a row of blue-roofed beach huts, and in the distance two parasols and a sandcastle. After the hedges and windbreak woods of R24 the sky suddenly opens.

**From R25 (the cliff stair).** The player comes down a stone stair cut into the north cliff and sees the whole town laid out in front of them like a postcard: huts, boardwalk, beach, the sea line, and a jetty poking into it.

**Mood, colour, sound, time of day.** Sleepy, sun-bleached, faintly absurd. Palette (LeoB Dewford recolour): sand yellow ground, blue roof tiles, wood planks, white parasol canopies with red and green stripes, pines at the edges. Sound: the Dewford track, surf. **Time of day: high noon**, hot and bright (the stock sunny palette). The Pokémon Center is 'slightly too quiet' (card): an unattended deck chair on its porch.

**The one memorable view.** From the end of the jetty at (12,22) looking back up the beach: the whole row of beach huts, the stair in the cliff behind them, the lifeguard tower and, tiny at the foot of a parasol, Pip with his invoices. Keep that line of sight free of trees.

---

## 3. Street layout in words (a numbered walk)

The town is a single **beach terrace**, 32 wide, with the sea along the south. There are no ledges inside town except the north cliff.

1. **West Gate (0,10)-(3,13)**, door (1,13). A timber gatehouse on the west edge; R24's lane ends at its far door. A sign 'DRIFTSANDS' at (4,14).
2. **West boardwalk (x 1-9, y 14-15).** A 2-wide wooden walkway running east from the gate door. Wooden planks fade into sand at x 9.
3. **Lifeguard tower (6,10)-(8,12)** (decorative, on stilts) with the **Lifeguard** standing at its foot, (7,13), on the sand beside the boardwalk. The **Lifeguard's Hut** next to it, (10,10)-(13,13), door (11,13).
4. **The Lido (y 4-9).** A row of beach huts, all doors facing the sea (south) on y 7, with a sand promenade (y 8-9) in front: **house 1** (3,4)-(6,7) door (4,7); **Beachcomber's Cottage** (8,4)-(11,7) door (9,7); **Pokémon Center** (13,4)-(16,7) door (14,7); **kiosk Mart** (18,4)-(21,7) door (19,7); **Beach Hall (the Sand Museum)** (22,3)-(27,7), door (24,7).
5. **House 2 (24,10)-(27,13)**, door (25,13), east of the promenade.
6. **The beach (x 0-23, y 16-20).** Soft sand: deck chairs at (5,17),(6,17),(15,18), a sandcastle at (10,18), parasols at (21,16) and (3,19); **Pip** sits under the parasol at (21,17). A rowing boat at (18,19) tied to a post. Hidden items in the sand (section 9).
7. **The tide pool (x 24-30, y 17-20).** A shallow pool of water tiles with a visible Pearl on a rock at (27,18).
8. **The jetty (x 12-13, y 20-23).** A 2-wide wooden pier into the sea, the **Old boatman** at its end (12,22).
9. **North cliff and the R25 stair (x 28-31, y 0-3).** The cliff band (trees and rock, x 0-27, y 0-3) is solid; a stone stair at (29,0)-(30,3) climbs through it, with the **Ranger** at (30,4). It is the town's north exit and R25's start.

No tall grass in town (card): the beach carries no wild encounters, the roads carry the tables.

---

## 4. Map plan

Sketch, **1 character = 2 x 2 tiles** (16 x 12 characters for 32 x 24 tiles). Legend: `T` cliff and trees, `s` stair, `R` R25 connection band, `h` house 1, `b` Beachcomber's Cottage, `P` Pokémon Center, `k` kiosk, `H` Beach Hall, `G` West Gate, `t` lifeguard tower, `l` Lifeguard's Hut, `o` house 2, `=` boardwalk, `~` sea or tide pool, `j` jetty, `B` rowing boat, `u` Pip's parasol.

```
x:  0    1    2    3
y0  TTTTTTTTTTTTTTss
y2  TTTTTTTTTTTHHHss
y4  .hhhbbPPPkkHHH..
y6  .hhhbbPPPkkHHH..
y8  ................
y10 GG.ttll.....oo..
y12 GG.ttll.....oo..
y14 =====...........
y16 ..........u.~~~~
y18 .........B..~~~~
y20 ~~~~~~j~~~~~~~~~
y22 ~~~~~~j~~~~~~~~~
```
(The header digits mark every 10 tiles; the sketch was generated from the footprints above.)

**Connections:**

| Edge | Neighbour | How |
|---|---|---|
| North | `R25` | Map connection `up`. R25's bottom edge x 0-5 meets Driftsands x 26-31 (offset 26). The stair at x 29-30 is the player's path; the rest of x 28-31 is cliff. R25 then runs east from its south-west corner |
| West | `R24` | **No connection.** The lane ends at R24's own gatehouse; the player goes through the West Gate interior (warps) |
| South, east | none | Sea |

---

## 5. Base, tilesets, palette notes

**Exterior base.** Duplicate `DewfordTown` (20 x 20; vanilla has the Pokémon Center at x 1-4 y 7-10, a hall at top-left, a gym, a bridge over a stream) and **Change Dimensions** to 32 x 24. Keep its Pokémon Center and Hall exteriors; delete the Gym exterior and the stream and bridge. Dewford's blue-roofed house blocks supply the other huts. Draw the beach (sand tiles with the pale shell flecks), the boardwalk (wooden bridge pieces from Dewford's own bridge, laid flat), parasols and deck chairs (use the Pacifidlog or Route 109 beach objects as a pattern: **vanilla Route 109** has parasols and chairs, and its tileset is `Slateport`, so they are not in the Dewford secondary; if absent, use plain rocks and shells, decoration is optional). Delete the duplicated heal locations before saving.

**Tilesets:**

| Where | Primary | Secondary | Source, credit |
|---|---|---|---|
| Outdoors | `gTileset_General` (LeoB, imported) | **LeoB ORAS `secondary/dewford`** | `Team-Aquas-Asset-Repo/Tilesets/The Great Tileset Exchange/Full Tilesets/LeoB ORAS/tilesets/secondary/dewford`, `graphics/door_anims/dewford.png`. Same metatile ids as vanilla. **CREDITS.md row (leob0505)**; replaces vanilla files in place, so an `engine-edits.md` entry. (Beaconmouth uses this same secondary, so import it once for both, in the first commit that needs it) |
| Houses and huts | `gTileset_Building` | `Gen4Interior` | Hollowbrook's, credited |
| Beach Hall | `gTileset_Building` | `GenericBuilding` | Vanilla `DewfordTown_Hall` (17 x 9) |
| Center, kiosk | `gTileset_Building` | `PokemonCenter`, `Shop` | Vanilla |
| West Gate | `gTileset_General` | `Shop` | Vanilla `Route110_SeasideCyclingRoadEntrance` (15 x 6) |

**Palladium:** none. `Route 38.png` supplies only R24's own gatehouse (see routes-south-detail.md). `Route 40.png` (sea route with a beach) is a mood reference for the sand edge; **not needed**, the LeoB Dewford tiles do it. **Not used:** *Desert Village Secondary* (cream plaster plaza with palms and blue water basins) looks pretty but is a triple-layer, 512-metatile set that would clash with the region's LeoB look, so it is skipped.

---

## 6. Buildings

| # | Building | Footprint | Door | Interior maps | Layout |
|---|---|---|---|---|---|
| 1 | Pokémon Center | (13,4)-(16,7) | (14,7) | `Driftsands_PokemonCenter_1F`, `_2F` | `LAYOUT_POKEMON_CENTER_1F`, `_2F` |
| 2 | Kiosk Mart | (18,4)-(21,7) | (19,7) | `Driftsands_Mart` | `LAYOUT_MART` |
| 3 | Beach Hall (Sand Museum) | (22,3)-(27,7) | (24,7) | `Driftsands_BeachHall` | `LAYOUT_DEWFORD_TOWN_HALL` (17 x 9) |
| 4 | Lifeguard's Hut | (10,10)-(13,13) | (11,13) | `Driftsands_LifeguardsHut` | G4-B (10 x 8) |
| 5 | Beachcomber's Cottage | (8,4)-(11,7) | (9,7) | `Driftsands_BeachcombersCottage` | G4-B (10 x 8), second copy |
| 6 | House 1 (a family) | (3,4)-(6,7) | (4,7) | `Driftsands_House1` | G4-A (11 x 8) |
| 7 | House 2 (a couple) | (24,10)-(27,13) | (25,13) | `Driftsands_House2` | G4-C (12 x 9) |
| 8 | West Gate | (0,10)-(3,13) | (1,13) | `Driftsands_WestGate` | vanilla gate (15 x 6) |

Eight interior maps (nine counting Center 2F).

### 6.1 Pokémon Center and kiosk Mart (shared)

Vanilla layouts, unmoved: Center nurse (7,2), mats (6,8),(7,8), stairs (1,6); Mart mats (3,7),(4,7), clerk (1,3). **Center decoration:** the card says 'slightly too quiet': leave the benches empty, add one wandering Wingull at (10,6) and a retired sailor asleep at (2,4) (both ambient). **Kiosk stock:** Net Ball, Dive Ball, Super Potion, Hyper Potion, Super Repel. Paint the kiosk's counter as a striped awning if a metatile exists (cosmetic).

### 6.2 Beach Hall: the Sand Museum (`DewfordTown_Hall`, 17 x 9)

**Purpose.** A tiny museum of sand sculptures; the sculptor gives **TM Sandstorm** after the second talk (card). The vanilla hall (GenericBuilding tiles) has mats (5,8),(6,8) and nine objects; Veldris keeps them as ambient visitors. Positions from the vanilla map:

- **Sculptor** at (9,3) `FACE_UP` (the vanilla expert): the second conversation gives TM Sandstorm (`FLAG_RECEIVED_TM_SANDSTORM`).
- Visitors: girl (4,6) `FACE_UP`, woman (1,5) `FACE_RIGHT`, man (5,4) `FACE_LEFT`, twin (5,2) `FACE_UP`, little boy (14,7) wandering left and right, school kid (12,3) `FACE_RIGHT`, psychic (15,3) `FACE_LEFT`, maniac (8,6) wandering left and right. Keep five or six; the room is small.
- **Sculptures** as `bg_event`s along the back wall at (2,1),(5,1),(8,1),(11,1),(14,1): read as a Dragonair, a Wailord, a Lapras, a lighthouse, the town itself (flavour, one line each).
- **Warps:** mats (5,8),(6,8) to `Driftsands` warp 2 (door (24,7)).

### 6.3 Lifeguard's Hut (G4-B)

**Purpose.** The Net Ball seller and a first-aid shelf. Plan G4-B (10 x 8). The Lifeguard stands outside at (7,13) (card: 'at the tower foot'), so the hut holds a **trainee lifeguard** at (4,4) `FACE_DOWN` who runs the **Net Ball shop** (Net Ball, Dive Ball: a `pokemart` script). First-aid shelf `bg_event` (6,1). Warps: mats (3,7),(4,7) to `Driftsands` warp 3.

### 6.4 Beachcomber's Cottage (G4-B)

**Purpose.** **Soft Sand** on the shelf and the one-time **Heart Scale for Shell Bell** swap. The **Beachcomber** at (5,5) `FACE_LEFT` (an old man with a bucket). Soft Sand as an item ball at (7,3). Wall decoration: shells and driftwood on the shelf (bg_event (6,1)). Warps: mats (3,7),(4,7) to `Driftsands` warp 4.

### 6.5 House 1 (G4-A) and House 2 (G4-C)

- **House 1 (a family, 11 x 8).** A mother at (5,6) `FACE_UP` and a **fan** at (8,3) `FACE_UP`, a Beaconmouth-bound fan who says the lighthouse leaks ('nobody told it about the roof'). A kid on the floor at (9,5) wandering. Warps: mats (2,7),(3,7) to `Driftsands` warp 5.
- **House 2 (a sunburnt couple, 12 x 9).** A man (4,5) `FACE_RIGHT` and a woman (8,5) `FACE_LEFT`: 'We came for a day. That was nine years ago.' A suitcase `bg_event` at (1,6). Warps: mats (5,8),(6,8) to `Driftsands` warp 6.

### 6.6 West Gate (vanilla gate layout)

Vanilla `Route110_SeasideCyclingRoadEntrance`: 15 x 6, west door pair (1,5),(2,5), east door pair (12,5),(13,5), clerk at (7,2). Veldris: **west door pair to R24's gatehouse door** (the Palladium `Route 38` gatehouse at R24's east edge), **east door pair to `Driftsands` warp 0** (door (1,13)). The clerk becomes a **Gatekeeper** at (7,2) `FACE_DOWN`: 'Sand in your shoes already? Wait until you see the beach.'

---

## 7. Door and warp table

`Driftsands` outdoor warps:

| # | Tile | Destination | Dest warp |
|---|---|---|---|
| 0 | (1,13) | `Driftsands_WestGate` (east side) | 2 (the (12,5),(13,5) pair) |
| 1 | (14,7) | `Driftsands_PokemonCenter_1F` | 0 |
| 2 | (24,7) | `Driftsands_BeachHall` | 0 |
| 3 | (11,13) | `Driftsands_LifeguardsHut` | 0 |
| 4 | (9,7) | `Driftsands_BeachcombersCottage` | 0 |
| 5 | (4,7) | `Driftsands_House1` | 0 |
| 6 | (25,13) | `Driftsands_House2` | 0 |
| 7 | (19,7) | `Driftsands_Mart` | 0 |

(Interiors above refer to the exterior warp numbers in this table; follow Porymap if its numbering differs.)

| Interior | Tiles | Destination | Dest warp |
|---|---|---|---|
| `Driftsands_WestGate` | (1,5),(2,5) | `R24` gatehouse door | R24 warp (east end; see routes-south-detail.md) |
| `Driftsands_WestGate` | (12,5),(13,5) | `Driftsands` | 0 |
| `Driftsands_PokemonCenter_1F` | (6,8),(7,8) | `Driftsands` | 1 |
| `Driftsands_PokemonCenter_1F` / `_2F` | (1,6) / (1,6) | each other | |
| `Driftsands_Mart` | (3,7),(4,7) | `Driftsands` | 7 |
| `Driftsands_BeachHall` | (5,8),(6,8) | `Driftsands` | 2 |
| `Driftsands_LifeguardsHut` | (3,7),(4,7) | `Driftsands` | 3 |
| `Driftsands_BeachcombersCottage` | (3,7),(4,7) | `Driftsands` | 4 |
| `Driftsands_House1` | (2,7),(3,7) | `Driftsands` | 5 |
| `Driftsands_House2` | (5,8),(6,8) | `Driftsands` | 6 |

---

## 8. NPCs and objects outdoors (9)

| Object | Tile | Move | Topic |
|---|---|---|---|
| Lifeguard | (7,13) | `FACE_DOWN` | Warns about the tide and the deep sea beyond (the way to Aldermere is Dive-only) |
| **Pip** (PROPOSED, the junior clerk from Kingsquay) | (21,17) | `FACE_DOWN` | Sunburnt, reading invoices under the parasol. 'One went. Wind.' Optional: hand back the loose invoice found at (23,16) (`FLAG_DRIFTSANDS_PIP_MET`; no item, no reward) |
| Old boatman | (12,22) | `FACE_UP` | The sunken town of Aldermere is north-west; a Dive-able trainer can enter the old streets |
| Kid with bucket | (9,17) | `WANDER_AROUND` | Sand-in-the-pail joke, no items |
| Swimmer (post-game rematch, trainer) | (25,19) | `FACE_DOWN` | In the tide-pool shallows. Hidden until `FLAG_SYS_GAME_CLEAR`; **PROPOSED team** Floatzel 65, Lanturn 66, Gastrodon 66 (class Swimmer, reuses a vanilla id, `cleartrainerflag` per fight, `IVs: 0` lines) |
| Tuber and Tuber (not trainers) | (4,19) and (7,20) | `FACE_UP` | Float on tubes in the surf, talk about the heat. They are objects on water tiles (shallow edge) |
| Ranger | (30,4) | `FACE_DOWN` | Warns that the cliff road 'has a water problem' (R25's stream) |

Bg events: town sign (4,14), stair sign (28,4) ('BEACONMOUTH: NORTH ALONG THE CLIFF'), jetty sign (11,20), Pokémon Center board.

**Fishing (PROPOSED).** The jetty (12,22),(13,22) and the shore at (18,20): Old Rod, Good Rod, Super Rod with **R23's tables** (levels 53 to 56, see routes-south-detail.md). Surf is allowed in the open sea south of the beach but there are no Surf encounters in town waters (the card: no wild encounters in town).

---

## 9. Items and hidden items (positions)

| Item | Where | Gate |
|---|---|---|
| TM Sandstorm | Beach Hall sculptor | Speak to him twice |
| Soft Sand | Beachcomber's Cottage, ball (7,3) | None |
| Shell Bell | Beachcomber trade (one Heart Scale) | A Heart Scale |
| Pearl | Tide pool rock, ball (27,18), visible | None |
| Big Pearl (hidden) | Sand dune at (17,16) | None |
| Heart Scale x2 (hidden) | (9,18) and (21,18) | None |
| Stardust (hidden) | Behind the lifeguard tower, (7,9) | None |
| Max Elixir | Rowing boat, ball (18,19), visible | After the League (hide the ball until `FLAG_SYS_GAME_CLEAR`) |

---

## 10. Scripts and events the build needs

- `Driftsands_MapScripts`: `ON_TRANSITION` sets `FLAG_VISITED_DRIFTSANDS` and the heal location; hides the rematch Swimmer and shows the Max Elixir ball after game clear.
- Pip: a once-only talk that sets `FLAG_DRIFTSANDS_PIP_MET`; the loose invoice `bg_event` (23,16).
- Sculptor: two-step talk for the TM. Beachcomber: Heart Scale trade (once) via `checkitem`/`removeitem`/`giveitem`.
- No battles inside town except the post-game Swimmer rematch.

**Flags (not claimed, from the card):** `FLAG_VISITED_DRIFTSANDS`, `FLAG_RECEIVED_TM_SANDSTORM`, `FLAG_RECEIVED_SHELL_BELL`, `FLAG_DRIFTSANDS_PIP_MET`, `FLAG_HIDDEN_ITEM_DRIFTSANDS_BIG_PEARL`, `_HEART_SCALE_1`, `_HEART_SCALE_2`, `_STARDUST`; new (PROPOSED): `FLAG_ITEM_DRIFTSANDS_SOFT_SAND`, `FLAG_ITEM_DRIFTSANDS_PEARL`, `FLAG_ITEM_DRIFTSANDS_MAX_ELIXIR`, `FLAG_DRIFTSANDS_INVOICE_RETURNED` (optional).

---

## 11. Build checklist (in order)

1. Read flags.md, engine-edits.md. Decide the LeoB `dewford` import (it serves Beaconmouth too).
2. Duplicate `DewfordTown`, Change Dimensions to 32 x 24, delete the gym exterior and bridge, set `MAPSEC_DRIFTSANDS`, delete duplicated heal locations before the first save.
3. Paint the cliff band and stair, the beach, the boardwalk, the jetty, the tide pool.
4. Place the eight building exteriors (section 6). Move or recopy the Dewford PC and Hall to their new footprints.
5. Interiors: Center and Mart (shared), Beach Hall (duplicate `DewfordTown_Hall`), G4 houses and huts, West Gate (vanilla gate layout).
6. Warps (section 7) and connection (north R25, offset 26). Check R25 and R24 exist before saving the connections.
7. Close and reload Porymap after Claude edits events.
8. Claude wires scripts and dialogue; dialogue_check; `make -j4`.
9. Update design docs and credits; check no ROM or save is staged; commit and push.

---

## 12. Open questions

1. **R24 reaches the town through a gate, not a map connection.** I did this so the gatehouse in the Palladium R24 render stays a real building. If the author prefers a plain edge connection, drop the West Gate and connect R24's east edge to Driftsands' west edge at y 14-15.
2. **R25 connects over the north edge at x 26-31.** That makes R25's south-west corner the start of the road. If R25 is built horizontally with its west edge facing the town, the stair should become a warp pair instead.
3. **Pip and the invoice.** Welcome, or should Driftsands stay silent on Scheme 9 (card question 2)?
4. **Beach objects.** The LeoB Dewford tileset may lack parasols and deck chairs; they are decoration only and can be skipped.
5. **The rematch Swimmer's team** is my proposal (the card only says a post-game rematch trainer).
