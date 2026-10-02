# Road cards, west group: R3 to R9

> **Open question (author, 2026-10-01): the Palladium route renders named in this file are NOT decided.** The author doubts that reusing Palladium route images will give a quality hack, so every 'source render' for a road below is a **mood and shape reference only** until the author decides how each road gets built (traced, redrawn or designed fresh). Lengths, edges, trainers, items and encounters stay as written.


Status: **PROPOSED.** Conventions, template, route numbering and level curve: [README.md](README.md). Towns: [towns/briarwick.md](towns/briarwick.md), [towns/gloomsby.md](towns/gloomsby.md), [towns/smeltham.md](towns/smeltham.md), [towns/hoarfell.md](towns/hoarfell.md). Landmarks: [landmarks-west.md](landmarks-west.md). Existing road examples: [../route1.md](../route1.md), [../route2.md](../route2.md).

## How to read these cards

- **Source renders** are Project Palladium route images in `Team-Aquas-Asset-Repo/Maps/Project Palladium/`. Sizes: `(px - 1) / 17` when the image has a 1 px grid (all route renders have it), otherwise `px / 16`. Palladium has Routes 29 to 46 minus 34 and 41. Credit Project Palladium team in `CREDITS.md` with the first map traced. The renders are Johto layouts, so each can be mirrored or rotated while tracing to fit the sketch's compass (the sketch is a diagram, not a map).
- **Level logic:** a road runs from about the ace of the gym behind it minus 3 to the ace of the gym ahead minus 3 (aces 12, 19, 25, 31, 37), nudged up for roads that can be walked in either order (R3 and R8). Gym trainers sit below that. No IVs; trainers reuse vanilla Hoenn ids (class, team and level only here).
- **Wild tables** are 12 land slots at 20/20/10/10/10/10/5/5/4/4/1/1. Water: Surf and Rock Smash use vanilla's 5 slots (60/30/5/4/1), Old Rod 2 (70/30), Good Rod 3 (60/20/20), Super Rod 5 (40/40/15/4/1). Every species named here was checked against `include/constants/species.h` (`SPECIES_*` exists). Ponds can be fished at any time; **Surf** only after badge 5 (Hoarfell), so Surf slots are for the return visit.
- **Flags** are proposed names only. Existing `FLAG_BADGE0n_GET` and `FLAG_RECEIVED_HM_*` are reused.
- **Route numbers (as the sketch is read in [README.md](README.md)):** R3 Crestfall to Briarwick; R4 Briarwick to Gloomsby; R5 Gloomsby to Smeltham; R6 Smeltham to Hoarfell (sketch 6 and 9); R7 mine spur (sketch 7 and 8); R8 Briarwick to Wendlebury; R9 Briarwick to Mothwood.

| Road | Render | Tiles | Section row (from [../region-sketch.md](../region-sketch.md)) |
|---|---|---|---|
| R3 | Route 31 | 46 x 22 | `MAPSEC_VELDRIS_ROUTE_3` |
| R4 | Route 36 | 52 x 22 | `MAPSEC_ROUTE_101` (shown as ROUTE 4) |
| R5 | Route 43 | 30 x 54 | `MAPSEC_ROUTE_102` |
| R6 | Route 42 + Route 44 (stitched) | about 131 x 25 (or Route 44 alone, 67 x 25) | `MAPSEC_ROUTE_103` |
| R7 | Route 46 | 22 x 36 | `MAPSEC_ROUTE_105` |
| R8 | Route 32 | 28 x 94 | `MAPSEC_ROUTE_107` |
| R9 | Route 35 | 28 x 32 | `MAPSEC_ROUTE_108` |

Map size checks: all under (w + 15) x (h + 14) <= 10240. The largest is R6 stitched, (131 + 15) x (25 + 14) = 5,694. R8 is (28 + 15) x (94 + 14) = 4,644.

---

## R3: Crestfall to Briarwick (land, sketch 3)

Dialogue draft: [../dialogue/route3.inc](../dialogue/route3.inc) (2026-10-01, checked, not wired).

**A short card, because the road is blocked at first.**

**Length and shape.** 46 x 22. A wooded lane running west to east: a gravel track along the top, a tall-grass patch in the lower left, a pond in the upper middle, and a small rocky mound in the upper right corner. The south tree line has one dirt gap (an item clearing). **Source:** Palladium `Route 31.png` (46 x 22, grid), the approved pairing in [../map-plan.md](../map-plan.md). Vanilla fallback `Route104`.

**Edges.** The render's **west end is a grey gatehouse** (Violet's gate in Johto): this becomes **Briarwick's east gatehouse** (a warp pair, one gate interior with a guard). The **east end** connects to **Crestfall's north edge** (the road turns south at the right; mirror or bend while tracing). No other exits.

**Gate (story).** **Closed until badge 1** (`FLAG_BADGE01_GET`, existing, no new flag needed). Proposal: a **road works barrier** at the Crestfall end: orange barriers, a lorry, three workers in hard hats, a sign reading 'ROAD CLOSED. RESURFACING BY GOLDSWORTH ROADWAYS'. When the player has the badge, the map script on load removes the barrier objects and the workers (the consultants' crew left after Scheme 1, see [../crestfall.md](../crestfall.md)). Alternative (author's call): a Cut tree. Both open on the same moment because Crestfall's gym gives Cut. Before badge 1, a guard says the road is shut and points to Wendlebury and R8 as the long way round.

**Wild (levels 10 to 13).** Crestfall gym ace 12, so R3 starts at 9 and runs to 16 (Briarwick's ace 19 minus 3); I use a lower band because R8 also leads to Briarwick.

| Slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 20% | KRICKETOT | 10 to 11 |
| 2 | 20% | WURMPLE | 10 to 11 |
| 3 | 10% | PIDOVE | 11 |
| 4 | 10% | SEWADDLE | 11 to 12 |
| 5 | 10% | LEDYBA | 11 to 12 |
| 6 | 10% | PATRAT | 11 to 12 |
| 7 | 5% | NINCADA | 12 |
| 8 | 5% | ODDISH | 12 to 13 |
| 9 | 4% | BELLSPROUT | 12 to 13 |
| 10 | 4% | POOCHYENA | 12 to 13 |
| 11 | 1% | COMBEE | 13 |
| 12 | 1% | MUNCHLAX | 13 |

Pond (fishing only): Old Rod MAGIKARP 10 (70), POLIWAG 10 (30); Good Rod POLIWAG 12 (60), MARILL 12 (20), WOOPER 12 (20); Super Rod MARILL 14 (40), WOOPER 14 (40), POLIWAG 14 (15), PSYDUCK 14 (4), CORPHISH 14 (1). Surf slots: skipped (the pond is tiny).

**Trainers (3).**

| Class | Team |
|---|---|
| Bug Catcher | WURMPLE 10, KRICKETOT 11 |
| Youngster | PATRAT 11, PIDOVE 12 |
| Camper | ODDISH 12, POOCHYENA 12 |

**NPCs (4).** The foreman at the barrier (before the badge), a worker on a break (after: gone), a hiker by the pond ('Briarwick has the biggest trees in Veldris'), a girl who looks for her lost net. Signs: two (Crestfall end, Briarwick end).

**Items.** POTION visible (lower left grass), PECHA BERRY hidden (by the pond), ANTIDOTE hidden in the gap clearing, GREAT BALL visible behind a Cut tree (Cut, badge 1).

**Goldsworth beat.** The road works signed 'GOLDSWORTH ROADWAYS' (foreshadows the family without a scheme). Troglodyte sighting optional: a worker says a rich boy 'went through before the cones went up, then complained about the cones'.

**Flags (not claimed).** `FLAG_R3_ROADWORKS_CLEARED` (only if the clearing should not rely on `FLAG_BADGE01_GET`), `FLAG_R3_ITEM_*`, reused trainer flags.

**Build effort.** Easy. Small, simple tiles, one gatehouse.

**Open questions.** Barrier or Cut tree? Is the 'Goldsworth Roadways' joke approved?

---

## R4: Briarwick to Gloomsby (land, sketch 4)

**Length and shape.** 52 x 22. A wide meadow road running west to east with thick tree walls north and south, a single red-berry row at the top, a ledge line in the middle, and a south gatehouse near the right end. As it nears Gloomsby it gets damper (fog weather in the east third). **Source:** Palladium `Route 36.png` (52 x 22, grid; Violet to Ecruteak in Johto, so it fits). Fallback: the tree-circle piece of `Route 37.png` (28 x 23) for a damp clearing; vanilla `Route117`.

**Edges.** **West end** meets Briarwick's west edge (the render's west gatehouse is dropped, or kept as a warp pair if the author adds a gatehouse to Briarwick). **East end** meets Gloomsby's west gatehouse. The **south gatehouse** (right end, bottom) is used as the **Marshkeeper's Lodge**, a one-room interior (the keeper gives a GREAT BALL and the fog lore); it is a dead end.

**Wild (levels 17 to 21).** Briarwick ace 19 minus 3 is 16; Gloomsby ace 25 minus 3 is 22.

| Slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 20% | ODDISH | 17 to 18 |
| 2 | 20% | HOOTHOOT | 17 to 18 |
| 3 | 10% | ZUBAT | 18 |
| 4 | 10% | VENIPEDE | 18 to 19 |
| 5 | 10% | SPINARAK | 18 to 19 |
| 6 | 10% | STUNKY | 19 |
| 7 | 5% | PUMPKABOO | 19 to 20 |
| 8 | 5% | DUSKULL | 20 |
| 9 | 4% | GASTLY | 19 to 20 |
| 10 | 4% | MURKROW | 20 to 21 |
| 11 | 1% | PHANTUMP | 21 |
| 12 | 1% | MISDREAVUS | 21 |

(Ghost types appear but stay rare and low, so the gym 3 theme is met on the road without a spoiler.) No pond on the render. Add a small **marsh pond** while tracing if the author wants fishing: Old Rod MAGIKARP 12 (70), POLIWAG 12 (30); Good Rod POLIWAG 17 (60), WOOPER 17 (20), BARBOACH 17 (20); Super Rod WOOPER 20 (40), BARBOACH 20 (40), POLIWAG 20 (15), CORPHISH 20 (4), SKRELP 20 (1).

**Trainers (5).**

| Class | Team |
|---|---|
| Bug Catcher | VENIPEDE 17, SPINARAK 18 |
| Picnicker | ODDISH 18, HOOTHOOT 18 |
| Hex Maniac | GASTLY 19, DUSKULL 20 |
| Bird Keeper | HOOTHOOT 19, MURKROW 20 |
| Youngster | STUNKY 19, KOFFING 20 |

**NPCs (6).** Marshkeeper (lodge), a lamp-lighter who warns of fog ahead, a film assistant with a clipboard and a van marked 'SPECTRAL PICTURES LTD' near the east end (**Scheme 3 foreshadow**: the crew's cables are laid along the road, the van's door open), a sleepy traveller on the ledge, a girl who sells 'authentic ghost stories' for a coin, a gym fan heading to Gloomsby. Signs: three (west end, mid-road, east end 'GLOOMSBY 1 KM. FOG BEYOND THIS POINT, FREE OF CHARGE').

**Items.** POTION visible (west), TM Rest visible (west meadow), REPEL hidden (ledge), AWAKENING hidden (berry row), MAX REPEL hidden (east end, near the van), GREAT BALL from the Marshkeeper, ELIXIR on an island of the optional pond (Surf, badge 5).

**Gate.** None. **Goldsworth beat:** the film van foreshadows Scheme 3; if the player looks inside the van, a script sheet reads 'Scene 14: SHEETED GUESTS ENTER. SPOOKY.' Troglodyte: optional sighting by the lamp-lighter ('a boy in a good coat demanded to know why fog is allowed').

**Flags (not claimed).** `FLAG_R4_ITEM_*`, reused trainer flags, `FLAG_R4_LODGE_GIFT`.

**Build effort.** Easy to medium. A plain tiled road; the fog is a header setting on the east third (map weather is per map, so the whole road gets fog, or use `COORD_EVENT_WEATHER_FOG_HORIZONTAL` triggers).

**Open questions.** Drop the render's west gatehouse and use edge connections? Should fog be road-wide or only east?

---

## R5: Gloomsby to Smeltham (land, sketch 5)

**Length and shape.** 30 x 54, a long north-to-south road climbing from fog into foothills: a long thin pond down the left-middle, two small ponds, tall-grass thickets, a rocky shelf on the west side, forest on the east, and a gatehouse at the far end. Smoke on the horizon (one chimney object) at the Smeltham end. **Source:** Palladium `Route 43.png` (30 x 54, grid). The render's gatehouse is at the **bottom**; that end becomes the Smeltham end (mirror vertically if the author wants Smeltham at the top).

**Edges.** One end meets **Gloomsby's east gatehouse**, the other meets **Smeltham's south edge** (via the render's gatehouse as a warp pair, or an edge connection with the building dropped).

**Wild (levels 22 to 27).** Gloomsby ace 25 minus 3 to Smeltham ace 31 minus 3 is 28; I stay at 22 to 27 so R6 can finish the climb.

| Slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 20% | MACHOP | 22 to 23 |
| 2 | 20% | GEODUDE | 22 to 23 |
| 3 | 10% | MAGNEMITE | 23 to 24 |
| 4 | 10% | ARON | 23 to 24 |
| 5 | 10% | DRILBUR | 24 |
| 6 | 10% | KLINK | 24 to 25 |
| 7 | 5% | TIMBURR | 25 |
| 8 | 5% | SANDSHREW | 25 |
| 9 | 4% | ROGGENROLA | 25 to 26 |
| 10 | 4% | NOSEPASS | 26 |
| 11 | 1% | MAWILE | 26 to 27 |
| 12 | 1% | LARVITAR | 26 to 27 |

(Steel is seeded in the wild before gym 4 on purpose, per the note in [../gyms.md](../gyms.md).) Long pond: Old Rod MAGIKARP 15 (70), BARBOACH 15 (30); Good Rod BARBOACH 22 (60), GOLDEEN 22 (20), WOOPER 22 (20); Super Rod BARBOACH 25 (40), GOLDEEN 25 (40), WOOPER 25 (15), CORPHISH 25 (4), WHISCASH 27 (1). Surf (return visit): GOLDEEN 22 to 26 (60), BARBOACH 22 to 26 (30), PSYDUCK 24 to 26 (5), WOOPER 24 (4), CHINCHOU 26 (1).

**Trainers (6).**

| Class | Team |
|---|---|
| Hiker | GEODUDE 22, ARON 23 |
| Hiker | MACHOP 24, ROGGENROLA 24 |
| Camper | TRAPINCH 24, SANDSHREW 25 |
| Black Belt | MEDITITE 25, MACHOP 25 |
| Picnicker | SHINX 24, MAREEP 25 |
| Fisherman | GOLDEEN 24, BARBOACH 25 |

**NPCs (6).** A toll-gate-style guard at the end ('Smeltham: mind the cranes'), a surveyor with a long tape measure at the foundry end (**Scheme 4 foreshadow**: he says he is 'measuring for a scrap estimate' and gives away nothing else), a hiker who recommends the Ice cave in Hoarfell, a sleepy farmhand 'who counts SKIDDO', a girl with a magnet who finds nails, a kid who throws pebbles into the pond. Signs: three.

**Items.** POTION visible, SUPER POTION visible, GREAT BALL visible, ESCAPE ROPE hidden, MAX REPEL hidden, AWAKENING hidden, HP UP on a pond islet (Surf, badge 5), IRON behind a Cut tree (Cut), TM Sandstorm visible (rocky shelf).

**Gate.** None. **Goldsworth beat:** the surveyor and a stack of rolled blueprints foreshadow Scheme 4. Troglodyte: none.

**Flags (not claimed).** `FLAG_R5_ITEM_*`, reused trainer flags.

**Build effort.** Medium (tall map, many ponds, 6 trainers).

**Open questions.** Mirror the render so Smeltham is at the bottom?

---

## R6: Smeltham to Hoarfell (land, sketch 6 and 9, with the R7 junction)

**Length and shape.** The long road across the north-west mountains: the sketch has it drawn as two segments (6 and 9) with the mine spur (7 and 8) at the join. It is one road in-game. I propose **one map, about 131 x 25**, built from **Route 42** (64 x 23: a rocky pass with ledges, small ponds and a hill to the east) for the west half and **Route 44** (67 x 25: rocky ledges, a central grove, two ponds, a cliff stair up the east side) for the east half. **Short version:** use Route 44 alone (67 x 25) with the mine junction as a gap in the north wall near the middle. **Sources:** Palladium `Route 42.png` (64 x 23, grid) and `Route 44.png` (67 x 25, grid). If one map is too long to build, split it into two maps sharing one section row (R6 West and R6 East); the junction goes on the west one.

**Edges.** **West end:** Smeltham's east edge (the Route 42 render has a west gatehouse; drop it or keep it as a warp). **East end:** Hoarfell's west gap (a cliff stair up). **Junction:** a gap in the north cliff wall, about a third of the way along, with a ledge and a sign, opening onto **R7** (the mine spur).

**Wild (levels 28 to 33).** Smeltham ace 31 minus 3 is 28; Hoarfell ace 37 minus 3 is 34.

| Slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 20% | SWINUB | 28 to 29 |
| 2 | 20% | SNORUNT | 28 to 29 |
| 3 | 10% | BOLDORE | 30 |
| 4 | 10% | BRONZOR | 29 to 30 |
| 5 | 10% | CUBCHOO | 29 to 30 |
| 6 | 10% | SKORUPI | 30 |
| 7 | 5% | SNEASEL | 30 to 31 |
| 8 | 5% | FERROSEED | 31 |
| 9 | 4% | VANILLITE | 31 to 32 |
| 10 | 4% | DELIBIRD | 31 to 32 |
| 11 | 1% | PILOSWINE | 33 |
| 12 | 1% | BERGMITE | 31 |

Ponds (two): Old Rod MAGIKARP 20 (70), GOLDEEN 20 (30); Good Rod GOLDEEN 28 (60), PSYDUCK 28 (20), SEEL 28 (20); Super Rod GOLDEEN 33 (40), SEEL 33 (40), PSYDUCK 33 (15), CHINCHOU 33 (4), LAPRAS 33 (1). Surf (after badge 5): GOLDEEN 28 to 32 (60), PSYDUCK 28 to 32 (30), SEEL 30 to 32 (5), SLOWPOKE 30 to 32 (4), LAPRAS 33 (1).

**Trainers (6).**

| Class | Team |
|---|---|
| Hiker | ROGGENROLA 28, BOLDORE 29 |
| Hiker | ONIX 29, GRAVELER 30 |
| Camper | SWINUB 29, SNORUNT 30 |
| Picnicker | CUBCHOO 30, VANILLITE 30 |
| Fisherman | SEEL 30, GOLDEEN 31 |
| Bird Keeper | STARAVIA 30, DELIBIRD 31 |

**NPCs (8).** A **lorry driver** at the roadside with a flat tyre, a lorry marked 'GOLDSWORTH SALVAGE' bound for Smeltham (**Scheme 4 foreshadow**, he is waiting for a crane); a mountaineer who tells the player about the Ice cave; a trader near the junction who sells ore samples (flavour); the old guide at the junction sign for Slagwell Mine; a boy who says he saw a rich boy shouting at a ledge (optional **Troglodyte sighting**); a kid who warns that Surf is not yet available; a cold-weather traveller offering advice about Hoarfell; a rest bench NPC who gives one Great Ball. Signs: four (west end, junction, mid-road, east end).

**Items.** POTION visible, SUPER POTION visible, GREAT BALL visible, ULTRA BALL visible (east end, first of the game), TM Dig visible (end of the pass), MAX REPEL hidden, ICE HEAL hidden, FULL HEAL hidden, EVERSTONE behind a Rock Smash rock (badge 2), CARBOS behind boulders (Strength, badge 4), RARE CANDY on a pond islet (Surf, badge 5).

**Gate.** None. The R7 spur is a side path, not a gate. **Goldsworth beat:** the Goldsworth Salvage lorry; no Troglodyte battle.

**Flags (not claimed).** `FLAG_R6_ITEM_*`, reused trainer flags, `FLAG_R6_LORRY_SEEN` (optional, only if the lorry should vanish when Scheme 4 is done: the lorry could instead be one of the vehicles folded into the cube).

**Build effort.** Hard because of its length (131 tiles). Medium if cut to Route 44 alone or split into two maps.

**Open questions.** Stitched, split or Route 44 alone? Does the lorry belong on the road or only in Smeltham?

---

## R7: Slagwell spur (land, sketch 7 and 8)

**Length and shape.** 22 x 36, a spur road leading north from R6 up a narrow rocky valley to the **mine entrance** (a dark door at the top of the render). Rocky walls on both sides, a grass floor in the lower half, ledges, a standing rock pillar in the middle with a short dirt loop around it. **Source:** Palladium `Route 46.png` (22 x 36, grid), whose top-centre cave door and south-edge entry fit exactly.

**Edges.** **South edge** meets R6's junction gap. **North:** the door at the top is the entrance to **Slagwell Mine** ([landmarks-west.md](landmarks-west.md)), a warp. No other exits (dead end).

**Wild (levels 29 to 34).**

| Slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 20% | ROGGENROLA | 29 to 30 |
| 2 | 20% | ZUBAT | 29 to 30 |
| 3 | 10% | MAGNEMITE | 30 to 31 |
| 4 | 10% | ONIX | 30 to 31 |
| 5 | 10% | BRONZOR | 30 to 31 |
| 6 | 10% | WOOBAT | 30 to 31 |
| 7 | 5% | NOSEPASS | 31 to 32 |
| 8 | 5% | DWEBBLE | 31 to 32 |
| 9 | 4% | SKORUPI | 32 |
| 10 | 4% | BOLDORE | 32 to 33 |
| 11 | 1% | MAWILE | 33 |
| 12 | 1% | LARVITAR | 33 |

Rock Smash rocks: DWEBBLE 29 to 33 (60), GEODUDE 29 to 33 (30), ROGGENROLA 30 (5), NOSEPASS 32 (4), SHUCKLE 33 (1). No water.

**Trainers (3).**

| Class | Team |
|---|---|
| Hiker | ROGGENROLA 30, MAGNEMITE 31 |
| Collector | WOOBAT 31, BRONZOR 32 |
| Black Belt | MACHOP 31, TIMBURR 32 |

**NPCs (3).** A miner at the door ('Mind the dark. Flash helps'), a boy collecting pebbles, a cart-pusher whose cart is stuck. Signs: two (junction, mine door).

**Items.** ETHER visible, ESCAPE ROPE visible, SUPER REPEL hidden, GREAT BALL behind a Rock Smash rock (badge 2), IRON behind boulders (Strength, badge 4).

**Gate.** None (the mine inside has HM-gated items). **Goldsworth beat:** after Scheme 4, one ore cart bears a sticker numbered '4001' (a gag; sets with `FLAG_SMELTHAM_SCHEME_DONE`). No Troglodyte.

**Flags (not claimed).** `FLAG_R7_ITEM_*`, reused trainer flags.

**Build effort.** Easy. A short enclosed valley, simple tiles.

**Open questions.** Is the spur an optional side road (my assumption, because the sketch draws it with an arrow each way) and not required for the story?

---

## R8: Briarwick to Wendlebury (land, no sketch number)

**Length and shape.** 28 x 94, a long lakeside road: a lake along the east side, a pier with a fisherman's cottage on the left, a wooden bridge, a small **roadside rest house** with a red roof half way (an NPC house, not a Pokémon Center), pale stone cliffs at the far end. A relaxed road with a view. **Source:** Palladium `Route 32.png` (28 x 94, grid), the longest render. **Shorter alternative:** `Route 39.png` (24 x 40, ranch and fields) if the author wants a lighter build.

**Edges.** **North end** connects to **Briarwick's south edge**. **South end** connects to **Wendlebury**: the existing card ([../wendlebury.md](../wendlebury.md)) puts R2 on the south or west edge and a barricade on the east, so I use **Wendlebury's west edge**. The render's top-left small building is Briarwick's south gatehouse (keep it as a pass-through, or drop it).

**Gate.** None. Open after badge 1 like R3 (the player can walk to Briarwick either way). The lake needs **Surf** for the water slots.

**Wild (levels 12 to 16; Crestfall ace 12, Briarwick ace 19, nudged up because it is a longer road).**

| Slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 20% | HOPPIP | 12 to 13 |
| 2 | 20% | MAREEP | 12 to 13 |
| 3 | 10% | PIDOVE | 13 |
| 4 | 10% | WURMPLE | 13 |
| 5 | 10% | BUNEARY | 13 to 14 |
| 6 | 10% | KRICKETOT | 13 |
| 7 | 5% | ODDISH | 14 |
| 8 | 5% | SKIDDO | 14 |
| 9 | 4% | SLOWPOKE | 14 to 15 |
| 10 | 4% | TEDDIURSA | 15 |
| 11 | 1% | PINECO | 15 |
| 12 | 1% | MUNCHLAX | 15 |

Lake: Surf WOOPER 12 to 16 (60), MARILL 12 to 16 (30), PSYDUCK 14 to 16 (5), SLOWPOKE 14 to 16 (4), QWILFISH 16 (1). Old Rod MAGIKARP 10 (70), POLIWAG 10 (30); Good Rod POLIWAG 13 (60), MARILL 13 (20), WOOPER 13 (20); Super Rod MARILL 15 (40), WOOPER 15 (40), POLIWAG 15 (15), PSYDUCK 16 (4), QWILFISH 16 (1).

**Trainers (6).**

| Class | Team |
|---|---|
| Fisherman (pier) | MAGIKARP 12, WOOPER 13 |
| Fisherman (lake bank) | POLIWAG 13, MARILL 14 |
| Youngster | PIDOVE 12, BUNEARY 13 |
| Lass | HOPPIP 13, MAREEP 14 |
| Camper | KRICKETOT 13, SKIDDO 14 |
| Bug Catcher | KAKUNA 13, BURMY 14 |

**NPCs (8).** The rest-house keeper (heals the party once per visit: free, flavour), a pier fisherman who talks about the lake, a girl who loses her hat in the lake, a cyclist, a boy who says Briarwick has the biggest trees, a gym fan heading to Briarwick, a surveyor measuring a billboard, a kid who counts passing PIDOVE. Signs: five including a **billboard**: 'GOLDSWORTH ESTATES: LAKESIDE LIVING. UNITS FROM TWO MILLION. NO LAKE INCLUDED.' (a deadpan foreshadow, no scheme).

**Items.** POTION visible, POKÉ BALL x3 visible, ANTIDOTE hidden, TM Double Team visible (north end), GREAT BALL visible near the rest house, ELIXIR hidden (pier end), REVIVE on the lake island (Surf, badge 5), RARE CANDY on a second island (Surf, badge 5).

**Goldsworth beat.** None. Troglodyte: optional sighting by the pier fisherman ('a boy complained to me about the MAGIKARP for ten minutes').

**Flags (not claimed).** `FLAG_R8_ITEM_*`, reused trainer flags, `FLAG_R8_REST_HEAL_USED` (a daily var only if the free heal should be limited).

**Build effort.** Medium. A big map (94 tall) but mostly tree wall and water; Surf pieces and many items. Cut to Route 39 if too long.

**Open questions.** Which edge on Wendlebury? Keep the long Route 32 or use Route 39? Is a free heal in the rest house fine?

---

## R9: Briarwick to Mothwood (land, no sketch number)

**Length and shape.** 28 x 32, a fenced, parkland lane running north from Briarwick to the forest gate: a long central sand path between fence lines, a narrow pool in the lower middle, rows of flowers, grass patches on both sides, and tree walls. A well-kept road, the mood of an avenue. **Source:** Palladium `Route 35.png` (28 x 32, grid), which has a gatehouse at each end.

**Edges.** **South end** connects to Briarwick's **north-east corner** (a gap past the east pond). **North end** is the **Mothwood gate**: the render's north gatehouse becomes a small interior, and its far door leads into **Mothwood's south-west gatehouse**, so the two are one building seen from both sides (one interior map with two door pairs). Dead end beyond.

**Gate.** None; Mothwood's inner pockets are HM-gated ([landmarks-west.md](landmarks-west.md)).

**Wild (levels 14 to 17; Briarwick ace 19 minus 3 is 16).**

| Slot | Rate | Species | Levels |
|---|---|---|---|
| 1 | 20% | LEDYBA | 14 to 15 |
| 2 | 20% | SPINARAK | 14 to 15 |
| 3 | 10% | PARAS | 15 |
| 4 | 10% | SEWADDLE | 15 to 16 |
| 5 | 10% | COMBEE | 15 to 16 |
| 6 | 10% | PINECO | 16 |
| 7 | 5% | BURMY | 16 |
| 8 | 5% | SHROOMISH | 16 |
| 9 | 4% | ODDISH | 16 to 17 |
| 10 | 4% | NYMBLE | 16 to 17 |
| 11 | 1% | HERACROSS | 17 |
| 12 | 1% | PINSIR | 17 |

Pool: Old Rod MAGIKARP 10 (70), POLIWAG 10 (30); Good Rod POLIWAG 14 (60), MARILL 14 (20), WOOPER 14 (20); Super Rod MARILL 16 (40), WOOPER 16 (40), POLIWAG 16 (15), PSYDUCK 17 (4), CORPHISH 17 (1). Surf: skip (the pool is narrow).

**Trainers (4).**

| Class | Team |
|---|---|
| Bug Catcher | LEDYBA 14, KAKUNA 14 |
| Lass | SEWADDLE 15, ODDISH 15 |
| Picnicker | SPINARAK 15, PARAS 16 |
| Youngster | PINECO 16, NYMBLE 16 |

**NPCs (6).** A gatekeeper ('Mothwood has no map. Bring snacks'), a gardener who waters the flower rows, a bug-catching kid, a retired traveller on a bench, a picnicking couple, a beekeeper's assistant carrying a hive to Briarwick. Signs: three.

**Items.** POTION visible, NET BALL x2 visible, PECHA BERRY visible, HONEY hidden (flower row), PARALYZE HEAL hidden, SUPER POTION behind a Cut tree (Cut, badge 1).

**Goldsworth beat.** None. Troglodyte: none.

**Flags (not claimed).** `FLAG_R9_ITEM_*`, reused trainer flags.

**Build effort.** Easy. Small, tidy, tile-friendly.

**Open questions.** Should Mothwood's gate be one shared interior, or two separate gatehouses?

---

## Open questions (whole group)

1. **Route directions and edges.** The sketch is a diagram; I picked edges to match the renders' gatehouses (see each card). Please confirm or swap.
2. **R3's block.** Road works that clear at badge 1 (my proposal), a Cut tree, or a different gate?
3. **R6 length.** Stitch Route 42 and Route 44 (about 131 wide), split into two maps, or use Route 44 alone?
4. **Surf slots before badge 5.** Ponds on R4, R5, R6 and R8 are fishable now and surfable after Hoarfell. Fine, or hide the Surf slots until later?
5. **Schemes vs teams.** Hagane has no MAGNEZONE and Wakasagi has no GLALIE ([towns/smeltham.md](towns/smeltham.md), [towns/hoarfell.md](towns/hoarfell.md)).
