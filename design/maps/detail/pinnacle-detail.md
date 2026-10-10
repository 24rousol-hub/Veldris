# THE PINNACLE, detailed design (landmark, the League)

Status: **PROPOSED.** Written 2026-10-01 for the author to build from. Card this expands: [../landmarks-centre.md](../landmarks-centre.md) (teams, levels, flags, NPC roles and the wiring note are **unchanged and not repeated in full**). Teams and ids: [../../trainer-roster.md](../../trainer-roster.md). Dialogue drafts: [../../dialogue/league.inc](../../dialogue/league.inc) (labels `League_Text_*`, not wired). Arc: [../../troglodyte-arc.md](../../troglodyte-arc.md), [../../postgame.md](../../postgame.md). Roads: [routes-centre-detail.md](routes-centre-detail.md) (R20 arrives, R21 leaves). New minor names are PROPOSED. Coordinates are `x, y` tiles from the top-left tile (0,0), good to about one tile where traced from a picture.

## 0. What I measured, and what the vanilla chain is

- **Palladium renders measured.** `e4karenad5.png`, `e4willja7.png`, `e4brunoym3.png`, `e4kogard3.png` are each 240 x 360 px, no grid: **15 x 22 tiles** and a half-row margin at the top. `championlacetq2.png` is 240 x 512 px: **15 x 32**. `halloffamegscrevampzr1.png` is 160 x 263 px: **10 x 16** (7 px over). The card's sizes are right.
- **Each Palladium E4 room already contains its own vestibule** (a wall band with two Poké Ball pedestals at the bottom, a mat), so **the vanilla short halls between rooms are not needed**: the door at one room's top is a warp to the next room's mat.
- **The vanilla chain I read from `data/maps`:** League lobby `EverGrandeCity_PokemonLeague_1F` (19 x 12) top warps (9,1),(10,1) lead to `Hall5` (a short hall, 11 x 13), then `SidneysRoom` (mat (6,13), exit (6,2)), then `Hall1`, `PhoebesRoom`, `Hall2`, `GlaciasRoom`, `Hall3`, `DrakesRoom`, then `Hall4` (the **long hall**, 11 x 34), then `ChampionsRoom`, then `HallOfFame`. All four vanilla E4 rooms are 13 x 14 and use `gTileset_EliteFour`; the four short halls share one layout (`EverGrandeCity_ShortHall`, 11 x 13).
- **Tilesets.** E4 rooms, corridor and lobby: vanilla `gTileset_EliteFour` and `gTileset_PokemonCenter` (no import). Hall of Fame: vanilla `gTileset_CableClub` (the vanilla HoF) or `gTileset_HallOfFame`. **Exterior: LeoB ORAS `ever_grande` secondary** (dual-layer, 168 metatiles, same ids as vanilla `gTileset_EverGrande`, so it drops in; folder `Team-Aquas-Asset-Repo/Tilesets/The Great Tileset Exchange/Full Tilesets/LeoB ORAS/tilesets/secondary/ever_grande/`). **Needs a CREDITS row** (extend the existing leob0505 row). The Palladium rooms are credited to the Project Palladium team in the commit that traces the first one.
- **Order of fights and room naming.** The fight order is OSSIAN, HYACINTH, DUNMORE, DRAYDEN ([../../trainer-roster.md](../../trainer-roster.md)); the vanilla ids run OSSIAN (Sidney), HYACINTH (Phoebe), DRAYDEN (Glacia), DUNMORE (Drake). The wiring note in the card says to rewrite the room scripts. **I map Veldris rooms to vanilla map slots by position** (table in section 4) so the vanilla door, state var and flag chain is reused as is and only the trainer reference changes.

## 1. Description

**The approach.** The player climbs out of the long cave into **daylight on a stone landing at the top of a plateau**: a sign ('THE PINNACLE: Nine badges. Mind the steps.'), two rows of clipped lawns, flags snapping on a long low glass-and-stone building with a **copper dome**, and the sea on three sides. The building's door faces south, so the player **walks round it by the side path**, the dome and its flags overhead, to the **forecourt** in front of the lobby door. Colour: warm stone, white fences, green lawns, copper-green dome, blue sea. Sound: wind and flags; no wild Pokémon.

**The run.** Inside, the mood goes from **a hotel lobby** (heal, shop, a registrar with a form) to **four rooms, each a different colour and a different character**, then **a long corridor** where Troglodyte waits, then **a red-carpeted hall** with a Champion who is older than the League's paint, then **the gold Hall of Fame**. Grand, slightly ridiculous, a bit sad. **Music:** exterior `MUS_EVER_GRANDE`; lobby `MUS_POKE_CENTER` (vanilla); rooms, corridor, hall `MUS_VICTORY_ROAD` (vanilla's own for every room); battles `MUS_VS_ELITE_FOUR`, `MUS_VS_CHAMPION` (vanilla scripts), Troglodyte `MUS_VS_RIVAL`; Hall of Fame `MUS_HALL_OF_FAME_ROOM`.

**The one memorable view.** The first step onto the landing: the **whole plateau and the dome from behind**, the dome's copper green against the sea, and no door in sight, which is why the path round the building matters.

## 2. The exterior: `ThePinnacle` (28 x 24)

The card says about 28 x 26. This plan is **28 x 24**: `(28+15)*(24+14) = 1634`, well under 10240. Section: the renamed `MAPSEC_EVER_GRANDE_CITY` entry to **'THE PINNACLE'** (card; verify the fly icon, the heal rows and the type switch after the rename) or a new id. Fly point: yes (PROPOSED).

Legend: `#` cliff and sea edge, `.` cobbled ground and paths, `,` fenced lawn, `R` League roof and dome, `L` facade, `D` lobby door, `=` steps, `f` flag, `l` lamp post, `b` bench, `G` iron gate, `C` cave exit, `s` sign.

```
      x: 0000000000111111111122222222
         0123456789012345678901234567
 y 0  |############################|
 y 1  |#############C##############|   cave exit C (13,1): the warp from R20 lands (13,2)
 y 2  |###......................###|
 y 3  |###.....h....s...........###|   sign s (13,3), hopeful trainer h (8,3)
 y 4  |###......................###|
 y 5  |###....RRRRRRRRRRRRRR....###|
 y 6  |###....RRRRRRRRRRRRRR....###|
 y 7  |###....RRRRRRRRRRRRRR....###|
 y 8  |###....RRRRRRRRRRRRRR....###|
 y 9  |###....fRRRRRRRRRRRRf....###|   flags f (7,9) (20,9)
 y10  |###....LLLLLLLLLLLLLL....###|
 y11  |###....LLLLLLLLLLLLLL....###|
 y12  |###....LLLLLLDDLLLLLL....###|   lobby door D (13,12) (14,12)
 y13  |###........======........###|   steps (11..16,13)
 y14  |###...,,,,,l....l,,,,,...###|   lamp posts l (11,14) (16,14)
 y15  |###...,,,,,......,,k,,...###|   hidden Max Elixir k (19,15), behind the east bench
 y16  |###...,,b,,......,,b,,...###|   benches b (8,16) (19,16)
 y17  |###...,,,,,......,,,,,...###|
 y18  |###...,,p,,......,,,,,...###|   hidden Rare Candy p (8,18) on the west lawn
 y19  |###...,,,,,......,,,,,...###|
 y20  |###...,,,,,......,,,,,...###|
 y21  |###......................###|
 y22  |############GGGG############|   iron gate G (12..15,22), shut until the Hall of Fame
 y23  |############....############|   R21 connection (12..15,23)
```

Numbered walk:

1. **The cave exit (13,1)** in the north cliff. A warp tile (the vanilla exit from `VeldrisRoute20_Cave_1F` at (39,5)) lands the player at **(13,2)**. The warp back into the cave is the same tile.
2. **The landing** (cols 3-24, rows 2-4): cobbles, a **sign (13,3)**, the **hopeful trainer** at (8,3). Nothing else.
3. **The League building** (cols 7-20, rows 5-12): roof and dome rows 5-9, flags at **(7,9)** and **(20,9)**, facade rows 10-12 with the **double door at (13,12) and (14,12)** and the steps at **(11..16,13)**. The facade faces south, **so the player walks round it**.
4. **The side paths** (cols 3-6 and 21-24, rows 3-20) run down both sides of the building to the forecourt. The west path is the 'quiet' side (the retired fan), the east the 'busy' side (the photographer).
5. **The forecourt** (cols 11-16, rows 14-20) is cobbled; **fenced lawns** flank it (west cols 6-10, rows 14-20; east cols 17-21, rows 14-20). **Lamp posts (11,14), (16,14)**, **benches (8,16), (19,16)**. **Hidden Rare Candy** on the west lawn at (8,18); **hidden Max Elixir** behind the east bench at (19,15).
6. **The south wall** (row 22) with the **iron gate at (12..15,22)** (a barrier object plus two guards at (11,21) and (16,21), shut until `FLAG_SYS_GAME_CLEAR`). The gate gap meets R21 through the connection at **(12..15,23)**.
7. **Cliffs and sea** on the west (cols 0-2) and east (cols 25-27): the plateau drops to the sea. No ledges, no wild encounters.

**Palette and tile notes.** ORAS Ever Grande secondary gives the League building, stone steps, white fences and tall lawn hedges. Dome: the copper-green dome is part of the vanilla Ever Grande building; check the ORAS version. Redraw: nothing; the flags are the existing flag metatiles. The copper dome on a 14-wide roof is a **stretched** League building: the vanilla Ever Grande League front is 11 wide, so repeat the centre metatile columns to widen it.

### Exterior NPCs (5 of 15 objects)

| Role | Tile, facing | Topic |
|---|---|---|
| Hopeful trainer | (8,3) east | has lost four times and describes each room by its flaws |
| Retired Elite Four fan | (6,17) east | gossip about each member's hobby (OSSIAN's hearse, DUNMORE's naps) |
| Photographer | (22,16) west | photographs the building from three angles and the player from one |
| Flag-polisher | (21,9) up | has polished the same flag for years |
| Iron-gate guards (2) | (11,21), (16,21) | 'Not until the Hall of Fame.' They step aside once the player is Champion |

### Exterior items (positions)

| Item | Tile | Gate |
|---|---|---|
| Rare Candy (hidden) | west lawn (8,18) | none |
| Max Elixir (hidden) | behind the east bench (19,15) | none |

### Connections

| Edge or warp | Destination | Notes |
|---|---|---|
| Cave warp (13,1) | `VeldrisRoute20_Cave_1F` warp 1 at (39,5) | R20's exit |
| Door (13,12) and (14,12) | `ThePinnacle_Lobby` mats (9,11) and (10,11) | |
| South edge (12..15,23) | `VeldrisRoute21` north edge, **+4 from the Pinnacle's side** (R21's left edge at col 4) | gate shut until `FLAG_SYS_GAME_CLEAR` |

## 3. The lobby: `ThePinnacle_Lobby` (19 x 12, vanilla layout)

Use `LAYOUT_EVER_GRANDE_CITY_POKEMON_LEAGUE_1F` unchanged (`gTileset_PokemonCenter`, 19 x 12): vanilla objects are the **nurse (3,2)**, the **mart clerk (16,2)**, **door guards (8,2) and (11,2)**; warps are the **exit mats (9,11) and (10,11)** to the exterior, the **top doors (9,1) and (10,1)** to the first room, and **stairs (1,7)** to the League 2F. **Keep every one of those tiles**, because the heal and shop scripts depend on them. Veldris additions (on free floor): the **League registrar** at **(5,6)** facing right (takes the name, offers a form, 'nobody has ever filled the form in correctly'; hands over the **PP Max** and a certificate after the Hall of Fame, a card gift), a **'form desk'** sign at (5,7). The guards check **nine badges** again (so a Fly arrival cannot skip the check): the vanilla door-guard script tests one flag, replace it with `GetBadgeCount() == 9`. **This lobby is the whole League's heal point** (`HEAL_LOCATION_EVER_GRANDE_CITY_POKEMON_LEAGUE`, vanilla, respawn at the lobby). Objects 6 of 15 (nurse, clerk, 2 guards, registrar, one idle NPC).

The **League 2F** (`EverGrandeCity_PokemonLeague_2F`, a Pokémon Center 2F: Union Room, Trade Center) is optional: keep it, or cut the stairs (1,7) and treat the room as a plain wall. The 'Pinnacle Lounge' of the card (a post-game Cynthia rematch room) can be this 2F re-skinned; not required.

## 4. The chain: every warp, in order

Veldris rooms and the vanilla slot each one reuses (so `VAR_ELITE_4_STATE`, the four `FLAG_DEFEATED_ELITE_4_*` flags and the room scripts stay):

| Step | Veldris map | Vanilla slot (script, flag) | State var (before to after) |
|---|---|---|---|
| 1 | `ThePinnacle_OssianRoom` | `SidneysRoom`, `FLAG_DEFEATED_ELITE_4_SIDNEY` | 0 to 1 |
| 2 | `ThePinnacle_HyacinthRoom` | `PhoebesRoom`, `FLAG_DEFEATED_ELITE_4_PHOEBE` | 1 to 2 |
| 3 | `ThePinnacle_DunmoreRoom` | `GlaciasRoom` (the third slot), `FLAG_DEFEATED_ELITE_4_GLACIA` | 2 to 3 |
| 4 | `ThePinnacle_DraydenRoom` | `DrakesRoom` (the fourth slot), `FLAG_DEFEATED_ELITE_4_DRAKE` | 3 to 4 |
| 5 | `ThePinnacle_LastCorridor` | `EverGrandeCity_Hall4` | (none) |
| 6 | `ThePinnacle_ChampionsHall` | `ChampionsRoom` | |
| 7 | `ThePinnacle_HallOfFame` | `HallOfFame` | |

In rooms 3 and 4, **change the trainer reference** (`TRAINER_DUNMORE` in the third slot, `TRAINER_DRAYDEN` in the fourth) and keep the slot's flag, so the vanilla chain is untouched. **Rewrite the vanilla room scripts' walk-in**: vanilla walks the player 2 or 3 tiles up and closes a door at (5..7,12); in the Palladium rooms the player enters at the **mat (7,21)**, so walk-in becomes about 8 tiles (to (7,13)) and the door to close is the **vestibule doorway (7,17)-(7,18)** (set a wall metatile there, as the vanilla `CloseDoor` does with its own tiles). The trainer talks from a scripted approach in vanilla (no sight line), so no trainer sight is needed.

| From (map, tile) | To (map, mat or tile) |
|---|---|
| `ThePinnacle` door (13,12) / (14,12) | `ThePinnacle_Lobby` (9,11) / (10,11) |
| `ThePinnacle_Lobby` top (9,1) / (10,1) | `ThePinnacle_OssianRoom` mat (7,21) |
| `OssianRoom` door (7,3) | `HyacinthRoom` mat (7,21) |
| `HyacinthRoom` door (7,3) | `DunmoreRoom` mat (7,21) |
| `DunmoreRoom` door (7,3) | `DraydenRoom` mat (7,21) |
| `DraydenRoom` door (7,3) | `ThePinnacle_LastCorridor` (5,33) |
| `LastCorridor` top (5,2) | `ThePinnacle_ChampionsHall` mat (7,31) |
| `ChampionsHall` door (7,3) | `ThePinnacle_HallOfFame` mat (5,15) |
| `HallOfFame` | the vanilla `GameClear` special (credits), then the respawn warp |

The **retreat** is the reverse: each room's mat (7,21) leads back to the previous room's door (7,3). Vanilla allows backtracking. No healing in the rooms or corridor (the pedestals in the vestibules are statues, not healers).

## 5. The four Elite Four rooms (Palladium, 15 x 22 each)

All four rooms share **one plan**, traced from the matching render. The only differences are the floor colour and the **side features** at cols 1-2 and 12-13 (rows 6-16).

```
      x: 000000000011111
         012345678901234
 y 0  |###############|
 y 1  |###############|
 y 2  |###############|
 y 3  |#######D#######|   door D (7,3), the warp up to the next room
 y 4  |#######S#######|   steps (7,4) (7,5)
 y 5  |#######S#######|
 y 6  |#vvp.......pvv#|   arena rows 6-12, cols 3-11; floor lights p along cols 3 and 11
 y 7  |#vvp.EELEE.pvv#|   member L at (7,7) facing down; emblem E cols 5-9, rows 7-11
 y 8  |#vvp.EEEEE.pvv#|
 y 9  |#vvp.EEEEE.pvv#|
 y10  |#vvp.EEEEE.pvv#|
 y11  |#vvp.EEEEE.pvv#|
 y12  |#vv.........vv#|   arena foot
 y13  |#vvvvv...vvvvv#|   path cols 6-8, rows 13-16; side features v (void, pools, lava or trees)
 y14  |#vvvvv...vvvvv#|
 y15  |#vvvvv...vvvvv#|
 y16  |#vvvvv...vvvvv#|
 y17  |#######.#######|   doorway (7,17) (7,18) through the vestibule wall
 y18  |#######.#######|
 y19  |#....u...u....#|   vestibule rows 19-21: pedestal statues u (5,19) (5,20) (9,19) (9,20)
 y20  |#....u...u....#|
 y21  |#......M......#|   entry mat M (7,21), the warp from the room below
```

Legend: `#` wall, `.` floor, `D` door, `S` steps, `E` the floor emblem, `p` floor light, `L` the member, `v` side feature (see each room), `u` pedestal statue, `M` mat.

**What every room has.** The member **L at (7,7)** on the emblem's top edge, facing down (**player stops at (7,8)** and talks; the vanilla script is a scripted talk, not a sight line). The **door (7,3)** is shut (a wall metatile) until the member is beaten; the script opens it (vanilla `EverGrandeCity_*Room_EventScript_OpenDoor`-style `setmetatile`). The **vestibule** (rows 19-21) with **two pedestal statues** (signs reading 'THE LEAGUE'S STATUE OF A POKE BALL'), the **doorway (7,17)-(7,18)** and the **path (cols 6-8, rows 13-16)**. The player's walk: mat (7,21), north through the vestibule and doorway, up the path to the arena foot, to (7,8). **Objects: 3 of 15** (the member and two ambient props).

| # | Room, member | Render and colour | Side features (cols 1-2, 12-13) | Props and objects | Secret |
|---|---|---|---|---|---|
| 1 | **OSSIAN** (Dark), `ThePinnacle_OssianRoom` | `e4karenad5.png`: black and grey floor, white emblem | `v` = **black void** (impassable) | a **hearse** (an object, `OBJ_EVENT_GFX_TRUCK` in a black palette) at (1,13) in the void edge, with a **Honchkrow** (a Pokémon) perched on it (`OBJ_EVENT_GFX_SPECIES(HONCHKROW)`) at (1,12); a **candle sign** (a wall lamp) at (13,9) | none |
| 2 | **HYACINTH** (Psychic), `ThePinnacle_HyacinthRoom` | `e4willja7.png`: purple floor, white-and-rose emblem | `v` = **pools** (glass or ice tiles, impassable) | a **sideboard** sign at (12,20) in the vestibule: 'A row of snow globes. Do not touch.'; an **Espeon** (a Pokémon) object at (3,12) looking around | the snow globes (one-line joke, [../../dialogue/league.inc](../../dialogue/league.inc) `HyacinthAfter`) |
| 3 | **DUNMORE** (Fighting), `ThePinnacle_DunmoreRoom` | `e4brunoym3.png`: yellow floor, green-and-white emblem | `v` = **lava** (impassable, red-orange tiles) | a **cushion** sign at (4,12) on the arena foot, the left corner; a **Hawlucha** (a Pokémon) object at (11,12) doing push-ups (face up and down) | **DUNMORE's cushion**: examine it before the fight: 'It is still warm.' |
| 4 | **DRAYDEN** (Dragon), `ThePinnacle_DraydenRoom` | `e4kogard3.png`: green floor, purple-and-white emblem | `v` = **tall trees and ferns** (impassable, tree sprites painted as tiles) | **two Dratini** (Pokémon) objects at (3,12) and (11,12) 'like pets' (look-around); a **bonsai** sign at (12,8) | DRAYDEN's pets say a different line each time |

Per-room scripts and text come from `League_Text_{Ossian,Hyacinth,Dunmore,Drayden}{Intro,Defeat,After}` in [../../dialogue/league.inc](../../dialogue/league.inc) (not wired).

### Tile notes for the four rooms

- The **vanilla `gTileset_EliteFour`** has only the grey-blue League floor and walls (palettes 6 to 11 are blue-grey colourways), so black, purple, yellow and green floors are **palette edits** in Porymap (a recolour of the floor and emblem palette slot per room). The side features need **new metatiles** that this set does not have: **black void** (any impassable all-black tile; the engine's empty tile works), **pool tiles** (a blue glass or ice floor, 2 metatiles), **lava** (an orange glowing floor, 2 metatiles) and **trees** (a pair of tree metatiles; copy from `gTileset_General` into a copy of the E4 tileset, since a map has only one secondary). **Cheapest first pass:** build all four rooms as vanilla rooms (13 x 14, zero new tiles, colours by palette), get the whole chain playable, then upgrade one Palladium room at a time. This follows the card's 'the vanilla set builds almost for free'.
- **About the 70 per cent match** noted in [../../map-plan.md](../../map-plan.md): the arena, steps, emblem, path and vestibule are the same tiles in all four; only the four side-feature sets differ.

## 6. The Last Corridor: `ThePinnacle_LastCorridor` (11 x 34, vanilla `EverGrandeCity_Hall4`)

Use the vanilla layout (`gTileset_EliteFour`, music `MUS_VICTORY_ROAD`). From the collision map: a **3-wide corridor at cols 4-6, rows 5-33**, a **wide landing at rows 3-4 (cols 0-10)** below the top door, pillar niches at **cols 1 and 9** on rows 7, 9, 11, 14, 18, 23 (decor alcoves). **Warps: bottom (5,33) from `DraydenRoom`; top (5,2) to the Champion's Hall.**

**Troglodyte, the final fight (Arc A).** He waits at the **far end**, in front of the Champion's door, at **(5,4)** facing down. **Trigger:** `coord_event` tiles at **(4,24), (5,24), (6,24)** across the corridor (CLAUDE.md: a trigger, not `OnTransition`; the elevation must match the corridor floor). When the player crosses row 24 he calls out, walks **south 17 tiles to (5,21)** and stops facing the player (so the player is never ambushed in the narrow part). Beats (`League_Text_TrogArcA1`, `TrogArcA2`, battle, `TrogArcADefeat`, `TrogArcAHumbled`, `TrogArcAHumbled2`): 'the help', the money-and-breeding boast, battle, denial, a real admission, and 'I'll be back, properly'. **Team:** Stoutland 'Sir Biscuit' 68, Gardevoir 69, Vaporeon 70, Tyranitar 70, Pyroar 70, plus one starter final form at 72 (Party Size 6, `Pool Prune: Rival Starter`, no held items; **no Garchomp**, fixed by the author). After the fight he walks to **(3,3)** and stands aside, then is hidden when the player steps through (5,2). He appears nowhere else in the League. Flags (not claimed): `TRAINER_TROGLODYTE_PINNACLE` alias, `FLAG_DEFEATED_TROGLODYTE_FINAL`. Objects 1.

## 7. The Champion's Hall: `ThePinnacle_ChampionsHall` (15 x 32)

Trace `championlacetq2.png` (a long red carpet, dragon-horn statues on both sides, a raised dais). **Swap the statues for plain columns** (the render's statues are dragon horns, a Lance joke; the card says plain columns). Tileset `gTileset_EliteFour` plus palette edits (teal floor, purple wall band).

```
      x: 000000000011111
         012345678901234
 y 0  |###############|
 y 1  |###############|
 y 2  |###############|
 y 3  |#######D#######|   door D (7,3) to the Hall of Fame
 y 4  |###.........###|   dais rows 4-8, cols 3-11; emblem E (6..8,5..7)
 y 5  |###...EEE...###|
 y 6  |###...ELE...###|   CYNTHIA L at (7,6) facing down
 y 7  |###...EEE...###|
 y 8  |###.........###|
 y 9  |#.....rrr.....#|   red carpet r, cols 6-8, rows 9-27
 y10  |#..c..rrr..c..#|   columns c (where the render has dragon-horn statues): rows 10-11, 13-14, 16-17, 19-20, 22-23 at cols 3 and 11
 y11  |#..c..rrr..c..#|
 y12  |#.....rrr.....#|
 y13  |#..c..rrr..c..#|
 y14  |#..c..rrr..c..#|
 y15  |#.....rrr.....#|
 y16  |#..c..rrr..c..#|
 y17  |#..c..rrr..c..#|
 y18  |#.....rrr.....#|
 y19  |#..c..rrr..c..#|
 y20  |#..c..rrr..c..#|
 y21  |#.....rrr.....#|
 y22  |#..c..rrr..c..#|
 y23  |#..c..rrr..c..#|
 y24  |#.....rrr.....#|
 y25  |#.....rrr.....#|
 y26  |######rrr######|   wall gap, the carpet passes (6..8,26..27)
 y27  |######rrr######|
 y28  |#....u...u....#|   vestibule rows 28-30: pedestal statues u (5,28) (5,29) (9,28) (9,29)
 y29  |#....u...u....#|
 y30  |#.............#|
 y31  |#######M#######|   entry mat M (7,31)
```

Legend: `#` wall, `.` floor, `D` door, `E` dais emblem, `L` CYNTHIA, `r` red carpet, `c` column (impassable), `u` pedestal statue, `M` mat.

- **CYNTHIA** stands at **(7,6)** on the dais facing down; the **player stops at (7,8)**, in front of the dais steps, and talks (`League_Text_ChampIntro`, `ChampSendOut`, `ChampDefeat`, `ChampAfter`, `ChampPraise`). Team: Spiritomb 73, Roserade 73, Togekiss 74, Lucario 74, Milotic 74, Garchomp 75 ([../../trainer-roster.md](../../trainer-roster.md)). **Music** `MUS_VS_CHAMPION`.
- The **door (7,3)** at the top of the dais is the warp to the Hall of Fame; the script opens it after the fight.
- **Vanilla ends this room with a cutscene:** the rival and Birch walk in at (6,12) (vanilla objects with hide flags). **PROPOSED:** skip it; Cynthia says her praise and the door opens. (The Fennick call comes later: `League_Text_HofFennickCall`.)
- **Objects 1 of 15** (plus two hidden vanilla cutscene slots deleted).
- Pacing: the carpet is **17 tiles long (rows 9-25)** so the walk up from the vestibule feels long and quiet, with the columns on both sides. No music change until the fight starts.

## 8. The Hall of Fame: `ThePinnacle_HallOfFame` (10 x 16)

Trace `halloffamegscrevampzr1.png` (a gold diamond floor, a record machine in the top wall, a small terminal, an entry notch at the bottom). Tileset `gTileset_CableClub` or `gTileset_HallOfFame` (vanilla), music `MUS_HALL_OF_FAME_ROOM`.

```
      x: 0000000000
         0123456789
 y 0  |##########|
 y 1  |###mmmm###|   the record machine m, cols 3-6, rows 1-3 (impassable)
 y 2  |#..mmmm..#|
 y 3  |#..mmmm..#|
 y 4  |#........#|
 y 5  |#........#|
 y 6  |#.....t..#|   terminal t (6,6)
 y 7  |#........#|
 y 8  |#........#|
 y 9  |#........#|
 y10  |#........#|
 y11  |#........#|
 y12  |#........#|
 y13  |#........#|
 y14  |#........#|   gold diamond floor rows 2-14, cols 1-8
 y15  |####.M####|   entry notch (4,15) and mat M (5,15)
```

Legend: `#` wall, `.` floor, `m` the record machine, `t` terminal, `M` entry mat.

- The vanilla HoF script (`EverGrandeCity_HallOfFame_EnterHallOfFame`) walks the player and the Champion up the hall in two movements, then plays `FLDEFF_HALL_OF_FAME_RECORD` and sets the game-clear flags. **Rewrite its movement lists** for this room: the player arrives at the **mat (5,15)** (vanilla arrives at (7,11) in a 15 x 17 room); walk up **9 tiles to (5,6)** and then stand at **(5,5) facing up** at the machine; the walking partner is **CYNTHIA** instead of Wallace (a vanilla object `LOCALID_HALL_OF_FAME_WALLACE`, becomes Cynthia's graphic), who walks beside the player at (4,y). The machine's recess is the impassable `m` block (cols 3-6, rows 1-3).
- **Attendant:** the **Hall of Fame attendant** (`League_Text_HofAttendant`) stands at **(8,6)** facing left; gives the Nugget after the Hall of Fame (card). 
- After the record the vanilla script calls `special GameClear` and `setrespawn HEAL_LOCATION_LITTLEROOT_TOWN_*`. **Replace the respawn with Hollowbrook's** (`HEAL_LOCATION_HOLLOWBROOK`, a script edit only): the player wakes at home, ready for the grandfather's scene ([../../postgame.md](../../postgame.md)). Check `special GameClear`'s credits path for `VAR_STARTER_MON` (the fourth starter, postgame.md).
- Objects 2 of 15 (attendant, Cynthia as a walking object).

## 9. Maps, sizes and counts

| Map | Size | Source | Objects |
|---|---|---|---|
| `ThePinnacle` | 28 x 24 | new, ORAS Ever Grande | 5 + 2 guards |
| `ThePinnacle_Lobby` | 19 x 12 | vanilla League 1F | 6 |
| `ThePinnacle_OssianRoom` | 15 x 22 | Palladium Karen room | 3 |
| `ThePinnacle_HyacinthRoom` | 15 x 22 | Palladium Will room | 3 |
| `ThePinnacle_DunmoreRoom` | 15 x 22 | Palladium Bruno room | 3 |
| `ThePinnacle_DraydenRoom` | 15 x 22 | Palladium Koga room | 3 |
| `ThePinnacle_LastCorridor` | 11 x 34 | vanilla `Hall4` | 1 |
| `ThePinnacle_ChampionsHall` | 15 x 32 | Palladium Lance room | 1 |
| `ThePinnacle_HallOfFame` | 10 x 16 | Palladium HoF | 2 |
| `ThePinnacle_Lounge` (optional) | 14 x 10 | vanilla League 2F, re-skinned | 4 |

**Nine required maps, ten with the Lounge.** All use the Pinnacle's section.

## 10. Build checklist (in order)

1. Decide room source (vanilla first pass or Palladium) and import ORAS `ever_grande` (CREDITS row).
2. Build `ThePinnacle` (28 x 24, section 2), the lobby (vanilla layout, no painting), then the **chain with vanilla rooms** (13 x 14) so every warp, door and state var works.
3. Wire the scripts: the nine-badge guards, the new fight order (rooms 3 and 4 trainer references), the Hall of Fame respawn.
4. Replace rooms one by one with the Palladium traces (new metatiles for side features), then the Champion's Hall and the Hall of Fame.
5. The Last Corridor trigger and Troglodyte's fight; the iron gate and `FLAG_SYS_GAME_CLEAR`.
6. Dialogue (`python3 design/tools/dialogue_check.py`), `design/` updates (`flags.md`, `engine-edits.md` if the section rename touches C), CREDITS, `make -j4`, check no ROM staged.

## 11. Open questions

1. **Palladium rooms or vanilla rooms?** The card (and README decision 5) chose Palladium; the side features need three or four new metatiles in a copy of the E4 tileset. I recommend vanilla first, then upgrade.
2. **Is The Pinnacle a fly point?** Renaming `MAPSEC_EVER_GRANDE_CITY` keeps its fly flag and heal locations but is unchecked for fly icon and type switch; a new section is the safer alternative.
3. **The Champion's post-fight cutscene.** Vanilla has the rival and Birch walk in; I proposed skipping it. Or have Fennick walk in instead?
4. **The Lounge:** keep the vanilla 2F (Union Room and Trade Center links) as a re-skinned lounge, or cut it?
5. **Hall of Fame partner.** Wallace's object becomes Cynthia in the vanilla script. Does the author want Cynthia (the defeated Champion) as the walking partner, or the League registrar?
6. **Respawn after the credits.** `HEAL_LOCATION_HOLLOWBROOK` is proposed; check the player's house door or the bench (the grandfather scene).
7. **Gate guard line vs gatehouse** on the iron gate: a guard line again (see [routes-centre-detail.md](routes-centre-detail.md) open question 2).
