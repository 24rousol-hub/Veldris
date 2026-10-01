# BRIARWICK (city, place 4)

Status: **PROPOSED.** Name approved 2026-10-01 ([../../region-names.md](../../region-names.md)); everything else is a brief for the author's Porymap work. Gym details: [../../gyms.md](../../gyms.md), [../../leader-names.md](../../leader-names.md), [../../trainer-roster.md](../../trainer-roster.md). Scheme 2: [../../troglodyte-arc.md](../../troglodyte-arc.md). Goldsworth houses: [../../goldsworth.md](../../goldsworth.md). Roads: [../routes-west.md](../routes-west.md). Landmark: Mothwood in [../landmarks-west.md](../landmarks-west.md).

## Role in the story

- First **city** the player reaches after Crestfall, and the second gym (Bug, HACHIMEL, HUSK BADGE, gives HM Rock Smash and TM Thief).
- Home of the **first Goldsworth house**. Crestfall is a town and has none, so the NPC-only cousin set drafted in `design/dialogue/crestfall_extra.inc` (labels `GoldCousin*`, `GoldLounger*`, `GoldPetOwner`, `GoldButler`, sign `GoldsworthHouseSign`, prefix to be renamed `Briarwick_Text_`) lives here (decision recorded in [../../crestfall.md](../../crestfall.md)).
- **Scheme 2** plays out here (Bug gym sealed in a tent, called fumigation). Details under Gym.
- No Troglodyte battle here (his fights are at gyms 1, 3, 5, 6, 7). He may be **seen** leaving town (optional sighting, see NPCs).
- The player arrives with badge 1 (level about 12 to 16) and leaves with badge 2 (about 18 to 20).

## Where it sits

Four roads meet here (sketch: the city marked 4, red, with four brown lines):

| Edge | Road | Leads to | Note |
|---|---|---|---|
| East | R3 | Crestfall (south-east on the sketch) | arrives at Briarwick's **east gatehouse** (a grey building on the Violet City render). Blocked by road works until badge 1, see R3 |
| South | R8 | Wendlebury (east on the sketch) | long lakeside road, enters at the south edge |
| West | R4 | Gloomsby (north-west) | gravel path leaving the top-left of the town |
| North-east corner | R9 | Mothwood (north-east) | a gap in the tree line past the east pond, with a small gatehouse |

Why the edges differ from the compass: the render has one real gatehouse (east) and the sketch is a diagram, not a map. The author can swap any edge; only the road card needs the same swap. (Open question 1.)

## Source and size

- Render: `Violet City` (`violetcity0ai.png`, **46 x 40 tiles**, 1 px grid, `(px - 1) / 17`). Credit Project Palladium team in `CREDITS.md` in the same commit as the map.
- Vanilla base: `FortreeCity` (tree-lined, wooden), useful for the tileset feel only. Map size check: (46 + 15) x (40 + 14) = 3,294 of 10,240, fine.
- Section: a new id (suggested constant `MAPSEC_BRIARWICK`). Not one of the reused Hoenn route rows. Fly and heal location: **yes** (a new row in `src/data/veldris_fly_towns.h` and `heal_locations.json`, `respawn_map` before `respawn_npc`, per the new-fly-town checklist in [../../region-map.md](../../region-map.md)).
- Interiors reuse the town's section (no extra ids).

## Layout

Read from the render (positions in words, relative to the picture):

- **Two long ponds** run down from the top: one left of centre, one right of centre (an L shape that turns toward the middle). They split the north half into three strips and give the town its look. Keep both, as water decoration (shallow, no Surf needed to cross because the path goes around). Fishing from them is allowed.
- **The Apiary** (the tall wooden tower at the top centre, between the ponds) is the town's showpiece. Hachimel keeps her hives there, and the player walks up a long stone path from the central square to its door. Interior: small, uses a house layout (see Buildings).
- **Central square** (paved, grey): the gym (large building in the middle, door facing south onto the square), the Mart (blue roof, just left of the gym), and a house to the right of the gym.
- **West branch:** the paved path runs west along the top-left to the R4 exit; one house sits at its far west end.
- **South-east:** the Pokémon Center (red roof) at the right, on a paved spur. A small red-berry patch (hidden items) sits just south of it.
- **South-centre:** one house in a clearing, reached by a paved loop.
- **Far east:** the grey gatehouse for R3.
- **South-west (the odd one):** the rounded, modern, slightly gaudy building on the sand patch at the bottom left is the **Goldsworth house**. It sits on pale sand, next to a small rock outcrop, so it looks like it was dropped there by crane. This is the joke: the one thing in the forest city that does not belong.
- Tree line everywhere else. Cut trees (see Items) hide one berry patch and one shortcut.

Door positions in words: gym door south side, middle of the map; Mart door south side, left of gym; Center door south side, right; Apiary door south side, top centre; west house door south; central-right house door south; south-centre house door north; Goldsworth house door east (facing the town).

## Buildings

| Building | Layout | Notes |
|---|---|---|
| Pokémon Center 1F, 2F | `LAYOUT_POKEMON_CENTER_1F`, `_2F` | shared, no painting |
| Mart | `LAYOUT_MART` | sells Poké Ball, Great Ball, Potion, Super Potion, Antidote, Paralyze Heal, Awakening, Repel, Escape Rope. No Bug-type anything |
| Gym (Bug) | custom, base `azaleagym20yp.png` (13 x 17) | see Gym |
| Apiary | `LAYOUT_HOUSE2` stand-in, or a vanilla two-floor house | 3 NPCs, a hive-shaped counter, a gift |
| Goldsworth house | the shared Goldsworth layout (stand-in `LAYOUT_HOUSE1` 10 x 9) | name `Briarwick_GoldsworthHouse`. NPC only, no trainers, no ids |
| House A (west end) | `LAYOUT_HOUSE1` | tired parent and child (Scheme 2 setup talk) |
| House B (right of gym) | `LAYOUT_HOUSE2` | retired bug-catching champion, gives a tip about Mothwood |
| House C (south-centre) | `LAYOUT_HOUSE1` | always open, a kid inside who tells the player the fumigation crew arrived with a lorry full of tent poles |
| R3 gatehouse | small gate interior (Hoenn route-gate layout) | pass-through, one guard NPC |
| R9 gatehouse | same layout | pass-through, one guard NPC |

Live objects per map must stay at 15 or fewer: the town outdoors holds about 10 of the 14 NPCs below (the rest are indoors).

## NPCs (16, all roles PROPOSED, topics only)

| Role | Where | Topic |
|---|---|---|
| Sign: city | by the central square | 'BRIARWICK. Where the forest keeps the town in line' (deadpan welcome) |
| Sign: gym | outside the gym | 'BRIARWICK BUG GYM. Leader: HACHIMEL. Please do not shake the hives' |
| Fumigation foreman (PROPOSED name: Mr Pargeter) | before the gym, at the tent | polite, in a white suit, insists it is 'a routine hygiene treatment' (Scheme 2 setup, see Gym) |
| Fumigation junior | at the tent corner | reads from a laminated card, cannot find the exit |
| Worried gym fan | square | says the leader cannot get out and the hives are inside |
| Hiker on the east gatehouse bench | by the R3 gate | asks if the road is open yet; after badge 1 comments on the road works lifting |
| Guard (R3 gate) | gatehouse | explains the road works, names the contractor 'GOLDSWORTH ROADWAYS' (foreshadow) |
| Guard (R9 gate) | gatehouse | 'Mothwood has no map. Bring snacks' |
| Kid with a net | west path | says Mothwood is bigger inside than outside |
| Pokémon Center nurse | Center | standard |
| Visitor in the Center | Center 1F | gossip: a rich boy in a good coat was here and complained about the grass |
| Clerk | Mart | standard |
| Apiary beekeeper (HACHIMEL's assistant, PROPOSED name Wilf) | Apiary | explains honey and the gym, gives SWEET HONEY-type gift (see Items) |
| Apiary old keeper | Apiary 2F | story: the first bug-catching contest in the region was held here |
| Retired champion (PROPOSED name Tansy) | House B | after badge 2, trades one Bug TM tip, hints Mothwood shrine needs a Cut tree opened |
| Goldsworth butler | Goldsworth house door | stiff, tells the player not to breathe loudly (`GoldButler`) |
| Goldsworth cousins (3) | Goldsworth house | see the next section |

Troglodyte sighting (optional, can be cut): a Center visitor or the east-gate hiker says a rich boy went through toward Gloomsby 'in a hurry, with a dog in a jumper'. This is the only trace of him here.

### Goldsworth house (first one)

| Cousin | Type | Before (scheme not beaten) | After (Scheme 2 beaten) |
|---|---|---|---|
| BARNABY (name PROPOSED, already drafted) | Boaster | 'My family owns this street' | admits the fumigation was 'a bad line item' |
| Lounger | Lounger | 'Shh. I am resting' | 'Beau could not plan a nap' |
| Pet owner (Kip in [goldsworth.md](../../goldsworth.md)) | PERSIAN, Duchess | 'Do not pet her' | Duchess looks embarrassed |
| Butler | Staff | rules of the house | apologises on the family's behalf, a little |

Swearing: mild, only inside this house, never at townsfolk. Before/after hangs on the Scheme 2 flag, not the badge, because the fight against the tent is the story beat.

## Items and secrets

| Item | Where | Gate |
|---|---|---|
| POTION | visible, south-east berry patch | none |
| ANTIDOTE | hidden, between the two ponds | none |
| HONEY | gift from Wilf in the Apiary after the gym | badge 2 |
| TM Bullet Seed | behind a Cut tree at the north edge, past the right pond | Cut (badge 1) |
| REPEL | hidden near the R4 exit sign | none |
| ORAN BERRY x3 | berry patch (the plants) | none |
| SILVER POWDER | inside House B, a shelf the retired champion lets you take | after Scheme 2 |
| HM Rock Smash | from HACHIMEL | badge 2 |
| TM Thief | gym reward | badge 2 |
| Escape Rope | Mothwood hint reward for talking to Tansy twice | none |

Note: Cut was given at Crestfall (badge 1), so the Cut tree is a usable early reward. Rock Smash (badge 2) opens one rock in this town's south tree line, with a PP-type item behind it (placed at build time).

## Gym

- **Leader: HACHIMEL** (`TRAINER_HACHIMEL`). Young beekeeper in a veil, gentle and oddly formal, apologises to every Bug she sends out. Team: KRICKETUNE 17, VIVILLON 19 (ace). HUSK BADGE. Gives HM Rock Smash and TM Thief.
- **Interior source:** `azaleagym20yp.png` (13 x 17), the second Azalea gym image ([../../region-names.md](../../region-names.md)). Use the first Azalea gym image for Crestfall, so the two do not repeat.
- **Puzzle idea:** a garden of tall decorative grass (non-encounter) and hedge walls with **web tiles** that force a detour; the detour is the puzzle. Hint on the wall: 'Spinarak weave around the shortest way'. Needs hedge and web art (see [../../gyms.md](../../gyms.md), open question about tile art). If the author prefers no custom art, replace web tiles with plain hedge walls and use the door-swap idea from Ghost gym in reverse (doors that only open one way).
- **Gym trainers (2, levels 13 to 15, sit 3 to 4 below HACHIMEL's lowest):**

| Class | Team |
|---|---|
| Bug Catcher | KRICKETOT 13, SEWADDLE 14 |
| Aroma Lady | COMBEE 14, BURMY 15 |

- **Gym guide statue** at the door: 'Bug types hate fire, flying and rock. Brought up so far.' (placeholder).
- **Scheme 2 beat (from [../../troglodyte-arc.md](../../troglodyte-arc.md), PROPOSED):**
  1. *Setup:* a polite crew in white suits seals the gym in a tent. Fan and foreman talk outside.
  2. *Reveal:* the tent is 'fumigation'. The gym is full of Bug types, which are the point of the gym.
  3. *Collapse:* a SPINARAK seals the tent from the inside. The crew is delivered to the Pokémon Center gift-wrapped in String Shot. Use a **`coord_event` trigger** on the walkable tile in front of the gym door (elevation 3), per CLAUDE.md. Tent pieces and the crew are object events, removed by the script. Keep the scene to 6 or fewer objects.
  4. HACHIMEL steps out, apologises to the crew, and invites the player in.
- No Troglodyte fight here.

## Flags (not claimed)

All proposed names, not in [../../flags.md](../../flags.md):

| Name | Meaning |
|---|---|
| `FLAG_VISITED_BRIARWICK` | fly point, set in `MAP_SCRIPT_ON_TRANSITION` |
| `FLAG_BRIARWICK_SCHEME_DONE` | Scheme 2 resolved, switches NPC After lines |
| `VAR_BRIARWICK_SCHEME_STATE` (or the flag only) | 0 setup, 1 tent sealed, 2 done (only if the scene needs stages) |
| `FLAG_BRIARWICK_RECEIVED_HONEY` | Apiary gift |
| `FLAG_BRIARWICK_ITEM_*` | the hidden and visible items (one per item) |
| Use existing `FLAG_BADGE02_GET`, `FLAG_RECEIVED_HM_ROCK_SMASH` | no new ones |

## Build order and effort

**Medium.** A 46 x 40 city with a gym, Goldsworth house, Apiary and two gatehouses. The render is tileable from the vanilla Fortree set, but the roofs and sand patch need rework; Violet's pale paved path and tall tower are not in the vanilla set (the render's look will only be about 70 per cent matched). Order: town exterior, Center and Mart (shared layouts, instant), gym, Goldsworth house, Apiary, gatehouses, houses. Heal location and fly row last.

## Open questions

1. Which edge does each road use? The sketch is a diagram; I assumed east = R3 gatehouse, south = R8, west = R4, north-east = R9. Confirm or swap.
2. The Violet render's round building: use it as the Goldsworth house (my suggestion), or keep it for something else?
3. Scheme 2 tent crew: is the 'foreman and junior' pair enough, or should there be a third man in a hard hat for Scheme 4 to rhyme with it?
4. Does the Goldsworth house open before the gym, or only after Scheme 2? I assumed always open (the family is rude either way).
5. Is Briarwick the place for the Crestfall cousin set? [goldsworth.md](../../goldsworth.md) says the six new cousins split across the other cities; this card reuses the drafted four here and gives the other cousins to Hoarfell.
