# LINGMOOR, detailed design (town, place 10, heather highland, no gym)

Status: **PROPOSED.** Written 2026-10-01 for the author to build from. Card this expands: [../towns/lingmoor.md](../towns/lingmoor.md). Rules: [../interiors/README.md](../interiors/README.md), catalogue [../interiors/catalogue.md](../interiors/catalogue.md), house style [../../interiors.md](../../interiors.md). Roads: [routes-centre-detail.md](routes-centre-detail.md). New minor names are PROPOSED. Coordinates are `x, y` tiles from the top-left tile (0,0), good to about one tile.

## 0. Facts and changes against the card

- **No Palladium render.** Vanilla base `VerdanturfTown` (20 x 20) is too small. Hand-laid **34 x 28**, `(34+15)*(28+14) = 2058`.
- **All doors face south.** The card has Center and Mart doors 'facing west onto the Green' and the Tea Rooms door 'facing north': impossible in Gen 3. Here the Center and Mart sit on the Green's **east side with their doors on a lane to the south of them**, the Tea Rooms and houses open onto the **south lane** (row 23).
- **Tilesets: LeoB ORAS `mauville` secondary** (dual-layer, 510 metatiles; in vanilla the Mauville and Verdanturf maps share this set, so Lingmoor is on the right one). Folder `Team-Aquas-Asset-Repo/Tilesets/The Great Tileset Exchange/Full Tilesets/LeoB ORAS/tilesets/secondary/mauville/`. Its README notes: the 'big trees' palette slot is not available, **use small trees**. Long grass, stone walls and flowers are in the set, which is all the heather highland needs. **Needs a CREDITS row** (extend the leob0505 row to name `mauville`).
- **Section** `MAPSEC_LINGMOOR` (new, PROPOSED). Fly destination, heal location PROPOSED `HEAL_LOCATION_LINGMOOR`, landing **(26,12)** outside the Pokémon Center.

## 1. Description

**From R11 (the west).** A **heather track** runs up onto a high plateau. Low dry-stone walls divide purple-brown moorland into small fields, the sky is huge and the wind is gentle. To the north a **ring of five standing stones** stands alone; to the east a tiny **village green** with a bench, a signpost and **a single orange stake** in the middle of the grass. Colour: purple heather (the ORAS long-grass palette, edited toward violet), grey stone walls, pale green, a dab of orange. Sound: a slow tune, nothing mechanical. **Time of day:** late afternoon, low gold light on the heather. **Music:** `MUS_VERDANTURF` (the quiet village tune) outdoors, `MUS_POKE_CENTER`, `MUS_POKE_MART`, `MUS_PETALBURG` inside the Day Care (quiet), `MUS_LITTLEROOT` in houses as in Hollowbrook.

**From R12 (the south).** The player comes through a **stone gate** in the south wall and walks north up a **farm lane** towards the Green: houses on the left, the Tea Rooms on the right, the Green at the end.

**The memorable view.** The **standing stones**: five grey stones on a heather hill at the north-west, the whole moor behind them, nothing else on the screen. A villager insists it is **'a Lunatone's seat'** (a Pokémon joke).

## 2. Street layout, in words

North at the top. `#` stone wall (the boundary), `:` moor, `,` the Green, `.` track and lanes, `o` standing stones, `m` Moon Stone (hidden), `h` the fenced hill, `y` the Day Care yard, `b` bench, `s` the orange stake, `i` signpost, `p` Pecha Berry, `c` Cut tree, `r` Revive, `k` Rock Smash rock, `x` Max Elixir. Buildings: `D` Day Care, `P` Pokémon Center, `M` Mart, `T` Tea Rooms, `A` `B` `C` houses, `S` Peat Cutter's shed; the digit in a building is its door.

```
      x: 0000000000111111111122222222223333
         0123456789012345678901234567890123
 y 0  |##################################|
 y 1  |#:::::::o:::::::::::::::::::hhhhh#|
 y 2  |#:::::o:::o:::::::::::::::::hhhhh#|
 y 3  |#:::::::m:::::::::::::::::::hhhhh#|
 y 4  |#:::::o:::o:::::::::::::::::hhhhh#|
 y 5  |.:::::::::::::::::::::::::::hhhhh#|
 y 6  |.::::::::::::::::::::::::::::::::#|
 y 7  |...............::::::::::::::::::#|
 y 8  |...............:::::::::PPPPPMMMM#|
 y 9  |#::::::::::::::,,,,i,,,:PPPPPMMMM#|
 y10  |#:::::DDDDDD:::,,,,,,,,:PPPPPMMMM#|
 y11  |#:::::DDDDDD:::,,,s,,,,:PP2PPM3MM#|
 y12  |#:::::DDDDDD::...................#|
 y13  |#:::::DD1DDD:::,,b,,,,,::::::::::#|
 y14  |#:::::yyyyyy:::,,,,,,,,::::::::::#|
 y15  |#:::::yyyyyy:::,,,,,,,,::::::::::#|
 y16  |#:::::yyyyyy:::....::::::::::::::#|
 y17  |#:r:::yyyyyy:::....::::::::::::::#|
 y18  |#:...........c:....::::::::::::::#|
 y19  |#::AAAAABBBBB::....TTTT:CCCC:SSSS#|
 y20  |#::AAAAABBBBB::....TTTT:CCCC:SSSS#|
 y21  |#::AAAAABBBBB::....TTTT:CCCC:SSSS#|
 y22  |#::AA4AABB5BB::....T6TT:C7CC:S8SS#|
 y23  |#................................#|
 y24  |#::::::::::::::....::::::::::::k:#|
 y25  |#::::::::::::::....:::::::::::::x#|
 y26  |#::::::::::::::....::::::::::::::#|
 y27  |###############....###############|
```

Numbered walk:

1. **West edge (R11).** The heather track enters at **(0,5)-(0,8)** and runs east along **rows 7-8**.
2. **The Standing Stones** (rows 1-4, cols 6-10): stones at (8,1), (10,2), (10,4), (6,4), (6,2) in a ring, the **Moon Stone** buried at the centre **(8,3)**. The track passes just south. The **guard** stands at (9,5).
3. **The Day Care** at **cols 6-11, rows 10-13, door (8,13)**, with its fenced **yard** (cols 6-11, rows 14-17), objects only (an old couple and a visitor).
4. **The Green** (cols 15-22, rows 9-15): a **bench (17,13)**, the **orange stake (18,11)**, the **signpost (19,9)**, a **Pecha Berry (16,12)**, a hidden **Hyper Potion** under the bench.
5. **The east lane** (row 12, cols 14-32) runs from the Green past the **Pokémon Center** (cols 24-28, rows 8-11, door **(26,11)**) and the **Mart** (cols 29-32, rows 8-11, door **(30,11)**).
6. **North-east:** the **fenced hill** (cols 28-32, rows 1-5), a steep grassy hill with a fence and no way up: the tease the card mentions.
7. **The farm lane** (cols 15-18, rows 16-26) runs south from the Green to the **stone gate** at **(15,27)-(18,27)** (R12).
8. **The south lane** (row 23, cols 1-32): doors of **House A (5,22)**, **House B (10,22)**, the **Tea Rooms (20,22)**, **House C (25,22)** and the **Peat Cutter's shed (30,22)**.
9. **Back path** (row 18, cols 2-12): behind Houses A and B, closed by a **Cut tree at (13,18)**; **Revive** at (2,17).
10. **The shed yard** (cols 29-32, rows 24-26): a **Rock Smash rock at (31,24)** hides a **Max Elixir** at (32,25).

**Palette and tile notes.** Heather: tall-grass metatiles recoloured toward purple, painted as *scenery* (set their behaviour to normal, **not** encounter grass, unless the author wants wild encounters on the moor; the R11 and R12 roads carry the wild table). Stone walls: the Mauville set's fence/wall tiles. The orange stake is **one tile of orange** (a sign-post metatile in an orange palette slot, or a plain sign reading 'SURVEY'). Tree borders: small trees only.

## 3. Doors and warps (outdoor map `Lingmoor`, 34 x 28)

| # | Tile | Destination (arrival) | Notes |
|---|---|---|---|
| 0 | (8,13) | `Lingmoor_DayCare` (mat 2,8 and 3,8) | |
| 1 | (26,11) | `Lingmoor_PokemonCenter_1F` (mat 6,8) | Fly lands (26,12) |
| 2 | (30,11) | `Lingmoor_Mart` (mat 3,7) | |
| 3 | (5,22) | `Lingmoor_HouseA` (mat 2,7) | |
| 4 | (10,22) | `Lingmoor_HouseB` (mat 2,7) | |
| 5 | (20,22) | `Lingmoor_TeaRooms` (mat 2,7) | |
| 6 | (25,22) | `Lingmoor_HouseC` (mat 2,7) | |
| 7 | (30,22) | `Lingmoor_PeatShed` (mat 2,7) | |

**Connections.**

| Edge | Neighbour | Offset | Lines up |
|---|---|---|---|
| West | `VeldrisRoute11` (67 x 25) east edge | -5 | R11's east strip (rows 12-13, cut through the render's rock end, see [routes-centre-detail.md](routes-centre-detail.md)) meets the track (rows 7-8) |
| South | `VeldrisRoute12` (24 x 40) north edge | +3 | R12's stone-gate opening (cols 12-15) meets the farm lane (cols 15-18) |
| North, East | none | | stone wall, moor |

## 4. Interiors

Maps: `Lingmoor_PokemonCenter_1F/_2F`, `_Mart`, `_DayCare`, `_TeaRooms`, `_PeatShed`, `_HouseA`, `_HouseB`, `_HouseC`: **10 maps**.

### 4.1 Pokémon Center and Mart (vanilla, unchanged)

`LAYOUT_POKEMON_CENTER_1F/_2F`, `LAYOUT_MART`; same vanilla tiles as in the other towns (nurse (7,2), mats (6,8),(7,8), stairs (1,6); Mart clerk (1,3), mats (3,7),(4,7)). Center NPCs (3): a **walker** (4,4), a **gardener with a pot** (10,6), a **child with heather** (3,7). Mart stock per the card: Poké Ball, Great Ball, Super Potion, Full Heal, Repel, Pecha Berry.

### 4.2 The Day Care (12 x 9)

**Layout:** vanilla `Route117_PokemonDayCare` (`gTileset_PokemonDayCare`, 12 x 9), unchanged because the Day Care scripts (`Route117_PokemonDayCare_EventScript_DaycareWoman`, the day-care state) depend on it. Vanilla: keeper object at **(2,2)** facing down, **mats (2,8) and (3,8)**. Add (visitor) NPCs: a **visitor** at (8,5) facing left (complains her Pokémon likes it more than her), a **toy-box sign** at (10,2). The yard outside (rows 14-17) holds **two objects**: an **old man** (10,16) wandering and an **old woman** (7,15) facing down (the 'old couple'). Re-skinning to match the house style later is fine; do not move the keeper. Objects 3 of 15.

### 4.3 Houses and the Tea Rooms (Gen 4 Interior, template N)

Template **N** = `Hollowbrook_NeighboursHouse` (11 x 8, mat (2,7), bookshelf signs (7,2),(8,2), free floor x 1-9, y 3-6).

| Map | Door | Interior in words | NPCs (tile, facing) |
|---|---|---|---|
| `Lingmoor_TeaRooms` | (20,22) | counter and kettle top-left, three small tables, a window onto the Green, jars of dried heather | **host** (3,3) facing right (a berry for a chat, **Soothe Bell** on the second talk); a **customer** (7,5) facing left; a **scone-eater** (9,6) facing up |
| `Lingmoor_PeatShed` | (30,22) | peat blocks stacked to the ceiling, a cutting spade, a stove | **peat cutter** (5,4) facing down (gives **TM Secret Power** for a Pecha Berry) |
| `Lingmoor_HouseA` | (5,22) | a weaver's loom by the window | **weaver** (4,4) facing right; her **Skitty** (8,5) looking around |
| `Lingmoor_HouseB` | (10,22) | a boy's room: toy boats, a heather collection in jars | **child** (6,5) wandering (collects heather, hides from the Day Care keeper) |
| `Lingmoor_HouseC` | (25,22) | an old man's house, a barometer and a pipe rack | **old man** (8,3) facing up (the road to Waymeet, the trains that do not run) |

## 5. NPCs outdoors (7 of 15 live objects)

| Role | Tile | Movement | Topic |
|---|---|---|---|
| Villager at the stake | (17,11) | face right | 'That stake's been there since before I got here. Nobody pulls it.' |
| Stone-ring guard | (9,5) | face up | a Lunatone's seat, do not sit |
| Walker | (3,8) | face right, R11 gate | warns about R11's long ledges |
| Child | (21,16) | wander, lanes | collects heather |
| Old man on the bench | (17,12) | face down (sits at the bench) | the road to Waymeet, the trains |
| Gardener | (14,25) | face up, near the gate | tends a flower box by the stone gate |
| Day Care visitor | (7,16) | look around | outside, see 4.2 |

Signs: town sign at (1,9) ('LINGMOOR, heather highland'), the Green's signpost (19,9), the Tea Rooms (19,23), the Day Care (7,14), the stake's survey note at (18,12), R12 gate sign (14,25).

## 6. Items and secrets (positions)

| Item | Where | Gate |
|---|---|---|
| **TM Secret Power** | the peat cutter, inside the shed | a Pecha Berry from the Mart (the Green's berry at (16,12) is free) |
| **Soothe Bell** | Tea Rooms host | talk twice |
| Pecha Berry (visible) | the Green (16,12) | none |
| Moon Stone (hidden) | the standing stones (8,3) | none |
| Revive | back path (2,17) | Cut tree (13,18) |
| Max Elixir | shed yard (32,25) | Rock Smash rock (31,24) |
| Hyper Potion (hidden) | under the Green bench (17,13) | none |

## 7. Build checklist (in order)

1. Import ORAS `mauville` (CREDITS row) in the first commit that uses it. Build `Lingmoor` 34 x 28 (walls, lanes, the Green, ring, hill), doors per section 3. Save; check `event_scripts.s` once and `heal_locations.json`.
2. Add `MAPSEC_LINGMOOR` and the fly row.
3. Shared Center and Mart, then the Day Care (vanilla layout, check its scripts are included), then the Tea Rooms and shed, then the three houses.
4. Connections to R11 and R12 when they exist; the Cut tree and rock.
5. Scripts (TMs, the berry errand, bell), dialogue (`python3 design/tools/dialogue_check.py`), `design/` updates, CREDITS, `make -j4`, no ROM staged.

## 8. Open questions

1. **Is the Day Care wanted here?** (the card asks). It is the only reason the town exists. If it moves to Waymeet or Wendlebury, Lingmoor becomes a pure rest stop.
2. The **orange stake**: keep as a joke, or cut (card question 2)? It costs one tile and one sign.
3. **TM Secret Power** is a weak TM; confirm or swap.
4. The **fenced hill**: leave as a tease or hide a post-game item on it?
5. **Heather as encounter grass?** I assumed scenery only. If the author wants wild Pokémon in the village, the heather tiles need encounter behaviour and a wild table (not in the card).
