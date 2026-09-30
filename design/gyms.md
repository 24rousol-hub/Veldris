# Gyms 2 to 9: options

Status: **PROPOSED. Every type, name, leader, gimmick, badge, TM and team below is an option, not canon, until the author approves it (CLAUDE.md rule 9).** Drafted 2026-09-30.

**Fixed (author):** Gym 1 is Crestfall (T3), Normal type, Greta (young, sassy, kind), STANDARD BADGE, silver outside and blue inside, levels up to 12. Nothing here changes it. Its details stay in [characters.md](characters.md) and [teams.md](teams.md).

**Not decided here:** town names (placeholders only), which places are cities or towns (open decision 12), the Goldsworth scheme per gym ([story-outline.md](story-outline.md)), trainer classes and pictures, moves (species and levels only, moves go into [teams.md](teams.md) once a option is approved).

## Rules every option follows

- **Teams:** leader 2 to 5 Pokemon, levels from 12 (gym 2) to about 45 (gym 9). **No IVs or EVs** on any trainer (author, 2026-09-30). Species are Gen 1 to 9 entries of this tree, and each is checked only by name and its evolution level, not yet against the learnsets.
- **Trainer ids:** about 4 to 5 of the 9 brand-new ids are still free (game-bible decision 6), so **every trainer below, leaders included, is meant to reuse a vanilla Hoenn entry** (CLAUDE.md, 'A new trainer', reuse route, untested). Costs no new id. The `Trainers` column counts gym trainers in front of the leader, and the total ids needed is in the summary.
- **Gym grass or water** is decoration only, never wild encounters (as in Crestfall).
- **Gym maps** must respect 15 live objects per map (engine-limits row 8), so 2 to 4 trainers plus the leader fits easily.

## Badge family (PROPOSED)

Badge 1 is a silver ring with a blue core. To read as a set, every badge keeps **the same silver ring and differs in core colour and a small motif in the middle**, so the trainer-card strip looks like one collection. The card uses **one shared 15-colour palette** (badges.md), so cores must be picked from colours that fit it, and two cores may have to share a colour (the motif then tells them apart). Art is being outsourced, so this is a brief, not a drawing. Blue stays badge 1's, so no later core is plain blue (Water uses teal).

## HM and field move plan (same for both orders)

`src/field_move.c` ties each move to a badge index, so any badge can grant any move. Vanilla order is Cut 1, Flash 2, Rock Smash 3, Strength 4, Surf 5, Fly 6, Dive 7, Waterfall 8. This plan keeps **Cut, Strength, Surf, Fly and Waterfall on their vanilla numbers** (no edit) and moves three (one number each, log in [engine-edits.md](engine-edits.md)):

| Badge | From | Move | Edit |
|---|---|---|---|
| 1 Standard (Greta) | Crestfall | Cut | none (author-fixed, vanilla) |
| 2 | Gym 2 | Rock Smash | was badge 3 |
| 3 | Gym 3 | Flash | was badge 2 |
| 4 | Gym 4 | Strength | none |
| 5 | Gym 5 | Surf | none |
| 6 | Gym 6 | Fly (**needs the Feather Badge in this build**, it is the 6th badge) | none |
| 7 | Gym 7 | none (TM only) | Dive moved off badge 7 |
| 8 | Gym 8 | Waterfall | none |
| 9 | Gym 9 | Dive | was badge 7 |

Why it is sensible: Surf at badge 5 is well before the sea routes (R18 to R23 lead to T16 to T18, past every gym town). Fly at gym 6 lets the player skip the long walk back from T8 to T10 (see the route note below) and is also a Flying-type gym in both options, so the **Feather Badge** fits its own name. Fly also needs the town flag set by walking in first ([region-map.md](region-map.md)). Every move is usable only when the gym in that slot is beaten, so the route design (which HM-gates which side path) stays open and the author can re-point any move.

## Town slots (both options use the same towns)

Town cells are from [region-map.md](region-map.md). The map has a fork at T6. **Suggested order:** T4, T5, T6, then the south branch T7 and T8, then back by Fly to the north branch T10, T11, T12. **T9 and T13 have no gym** (T9 leads on to T15 and T14 and a Surf route to T16, T13 is between T10 and T11). The order is open: T7 and T8 could swap with the north branch. All names are placeholders.

| Gym | Town slot | Section id | Reached by | Notes |
|---|---|---|---|---|
| 1 | T3 Crestfall | `MAPSEC_CRESTFALL` | R2 | Author-fixed. Greta |
| 2 | T4 | `MAPSEC_VELDRIS_TOWN_04` | R3 (from Crestfall) | Also has side path R26 |
| 3 | T5 | `MAPSEC_VELDRIS_TOWN_05` | R4 | Side path R27 |
| 4 | T6 | `MAPSEC_VELDRIS_TOWN_06` | R5 | The fork: R6 to T7, R11 to T10, side path R28 |
| 5 | T7 | `MAPSEC_VELDRIS_TOWN_07` | R6 (or R15 from Crestfall) | Loop back to Crestfall |
| 6 | T8 | `MAPSEC_VELDRIS_TOWN_08` | R7 (or R16 from Wendlebury) | Fly arrives here, so the trip back north is one flight. Side path R29 |
| 7 | T10 | `MAPSEC_VELDRIS_TOWN_10` | R11 from T6, or R17 from T5 | Side path R30 |
| 8 | T11 | `MAPSEC_VELDRIS_TOWN_11` | R13 from T13 (R12 from T10) | Side path R31 |
| 9 | T12 | `MAPSEC_VELDRIS_TOWN_12` | R14 | End of the north chain, Surf route R21 leads on to T18 |

## Summary of the two orders

| Gym | A: classic-style | B: unusual |
|---|---|---|
| 1 | Normal (Greta, fixed) | Normal (Greta, fixed) |
| 2 | Rock | Bug |
| 3 | Electric | Ghost |
| 4 | Fighting | Steel |
| 5 | Water | Ice |
| 6 | Flying | Flying |
| 7 | Psychic | Poison |
| 8 | Ice | Fairy |
| 9 | Dragon | Water |

**Shared in both options:** gym levels and team sizes, trainer counts, HM plan, town slots, and gym 6 (Flying, with its leader, gimmick, badge and team, written once below as **Gym 6 (both)**).

| Gym | Leader team | Level range | Gym trainers | Ids needed (leader plus trainers) |
|---|---|---|---|---|
| 2 | 2 | 12 to 14 | 2 (1 mon each, levels 10 to 12) | 3 |
| 3 | 3 | 16 to 18 | 2 (1 to 2 mons, 14 to 16) | 3 |
| 4 | 3 | 21 to 23 | 3 (1 to 2 mons, 19 to 21) | 4 |
| 5 | 3 | 26 to 28 | 3 (2 mons, 24 to 26) | 4 |
| 6 | 4 | 31 to 33 | 3 (2 mons, 29 to 31) | 4 |
| 7 | 4 | 36 to 38 | 4 (2 mons, 34 to 36) | 5 |
| 8 | 5 | 41 to 43 | 4 (2 to 3 mons, 39 to 41) | 5 |
| 9 | 5 | 44 to 46 | 4 (3 mons, 42 to 44) | 5 |

Totals: 8 leaders, 25 gym trainers, **33 ids, all reusing vanilla entries** (Crestfall's 3 are separate). Level caps (`caps.h`) have a badge 9 row at 50, a placeholder.

---

# Option A: classic-style order

Normal, Rock, Electric, Fighting, Water, Flying, Psychic, Ice, Dragon. Familiar rhythm and broad type coverage, so a player who knows Pokemon can plan a team. Fire and Grass are left for the wild and for Troglodyte.

### Gym 2: Rock (T4), Rock Smash
- **Leader pitch:** a young quarry foreman in a hard hat, blunt and unbothered. Treats battles as site inspections and every Goldsworth stunt as a safety violation.
- **Gimmick:** loose boulders sit on rails in the floor and block lanes. Stepping on marked plates slides them (no Strength needed, Strength comes at badge 4). Needs a rail or cracked-floor look in the tileset.
- **Badge:** COBBLE BADGE. Silver ring, amber core, small chipped-stone shape.
- **TM:** Rock Tomb.
- **Team (2, levels 12 to 14):** Geodude 12, Nosepass 14.

### Gym 3: Electric (T5), Flash
- **Leader pitch:** an elderly retired electrician, calm and literal. Speaks in flat, warm one-liners and is never shocked, whatever happens.
- **Gimmick:** a fuse-box puzzle: floor switches light panels and open the gates in order, in the style of the vanilla electric gym's locked doors but with our own layout.
- **Badge:** SPARK BADGE. Silver ring, yellow core, small zigzag.
- **TM:** Shock Wave (Thunderbolt is a later-game reward elsewhere).
- **Team (3, levels 16 to 18):** Pachirisu 16, Magnemite 17, Luxio 18.

### Gym 4: Fighting (T6), Strength
- **Leader pitch:** a middle-aged dojo teacher, very polite, extremely fit, and completely without irony. Bows at everything.
- **Gimmick:** a ladder of sparring rings. The trainers stand on mats and the player must fight them in belt colour order to open the next door (visible clue, not hidden).
- **Badge:** BOUT BADGE. Silver ring, red core, small fist or knot.
- **TM:** Brick Break.
- **Team (3, levels 21 to 23):** Meditite 21, Makuhita 22, Timburr 23.

### Gym 5: Water (T7), Surf
- **Leader pitch:** a teenage ferry pilot, cheerful but deadpan, who talks about drowning like the weather.
- **Gimmick:** the gym floor is half pool. Walkways are laid out as a maze and drain valves (switches) change which path is open. The player does not need Surf to finish it.
- **Badge:** TIDE BADGE. Silver ring, teal core (blue is badge 1's), small wave.
- **TM:** Water Pulse.
- **Team (3, levels 26 to 28):** Lombre 26, Wailmer 27, Quagsire 28.

### Gym 6 (both): Flying (T8), Fly
See **Gym 6 (both)** at the end of Option B. It is identical in both orders.

### Gym 7: Psychic (T10), no HM
- **Leader pitch:** an old fortune teller who predicts nothing that hasn't already happened and acts disappointed when she is right.
- **Gimmick:** warp pads link rooms in a fixed pattern. A painted floor hint shows the route, so it reads as a puzzle rather than a maze.
- **Badge:** REVERIE BADGE. Silver ring, pink core, small eye or spiral.
- **TM:** Calm Mind.
- **Team (4, levels 36 to 38):** Xatu 36, Kadabra 37, Girafarig 37, Claydol 38.

### Gym 8: Ice (T11), Waterfall
- **Leader pitch:** a young, soft-spoken ice sculptor who apologises to her Pokemon, and to you, before the battle.
- **Gimmick:** slippery ice floors, slide-until-blocked puzzles, broken up by patches of rough floor. Vanilla has ice rooms (for example in Shoal Cave), so check their tiles before promising it.
- **Badge:** FROST BADGE. Silver ring, pale cyan core, small snowflake or crystal.
- **TM:** Ice Beam.
- **Team (5, levels 41 to 43):** Glalie 41, Dewgong 41, Piloswine 42, Jynx 42, Abomasnow 43.

### Gym 9: Dragon (T12), Dive
- **Leader pitch:** an old, dignified champion-in-waiting whose reputation is bigger than her temper. She has been expecting you and is mildly annoyed you are late.
- **Gimmick:** a hall of statues with four dragon-scale switches. Fight the gym trainers to find the clue for each, then press them in order to open the last door (dialogue hints, no lookup needed).
- **Badge:** SCALE BADGE. Silver ring, purple core, small scale or claw.
- **TM:** Dragon Claw.
- **Team (5, levels 44 to 46):** Altaria 44, Dragonair 44, Flygon 45, Fraxure 45, Gabite 46.

---

# Option B: unusual order

Normal, Bug, Ghost, Steel, Ice, Flying, Poison, Fairy, Water. The Water gym comes last and Surf still arrives at gym 5, so the player meets the sea before its type master. A bit stranger and less predictable, but **Ghost, Steel and Fairy gyms come earlier than the matching counters are easy to catch**, so the wild encounter tables will need care.

### Gym 2: Bug (T4), Rock Smash
- **Leader pitch:** a young beekeeper in a veil, gentle and oddly formal, who apologises to every bug she sends out.
- **Gimmick:** hedge walls and a garden of tall decorative grass (not encounter grass) with web tiles that force a detour. Needs hedge and web tile art.
- **Badge:** HUSK BADGE. Silver ring, lime green core, small wing or leaf.
- **TM:** Thief (there is no Bug TM in this ROM's 50 TM list).
- **Team (2, levels 12 to 14):** Ledyba 12, Kricketune 14.

### Gym 3: Ghost (T5), Flash
- **Leader pitch:** a teenage mortician's apprentice, dry and unbothered, who thinks the dead are the better audience.
- **Gimmick:** a dark gym with pools of light (Flash shows more of the floor, it is also the badge's move). Some doors are fakes that loop the player back.
- **Badge:** WISP BADGE. Silver ring, violet core, small flame-like wisp. (Named to avoid Hollowbrook.)
- **TM:** Shadow Ball.
- **Team (3, levels 16 to 18):** Shuppet 16, Duskull 17, Misdreavus 18.

### Gym 4: Steel (T6), Strength
- **Leader pitch:** a middle-aged foundry foreman, exhausted and very patient. His workers are always at lunch.
- **Gimmick:** conveyor belts and crusher presses carry the player around the floor on a timing puzzle. Needs belt tiles, which may not exist yet.
- **Badge:** RIVET BADGE. Silver ring, dark slate core, small bolt or gear.
- **TM:** Iron Tail.
- **Team (3, levels 21 to 23):** Bronzor 21, Aron 22, Mawile 23.

### Gym 5: Ice (T7), Surf
- **Leader pitch:** an old fisherman, very relaxed, who leaves the ice fishing hole for the battle and has a thermos.
- **Gimmick:** a frozen lake floor with cracked patches. The floor is slippery, and the thermos is the hint: wait by the heater tile for the ice to reset.
- **Badge:** FROST BADGE. Silver ring, pale cyan core, small snowflake. (Surf fits: the lake thaws out.)
- **TM:** Ice Beam.
- **Team (3, levels 26 to 28):** Sneasel 26, Delibird 27, Lapras 28.

### Gym 6 (both): Flying (T8), Fly
- **Leader pitch:** a young pilot in a leather jacket, dry and a little vain, who calls the battle a flight plan and never raises his voice.
- **Gimmick:** wind-tunnel floors: arrow tiles push the player along a route over a pit-like sky bridge. Arrow tiles already exist in vanilla (Mossdeep and Sootopolis style), but check.
- **Badge:** FEATHER BADGE. Silver ring, white or sky core, small feather. The author wants Fly to need the Feather Badge in this build (src/field_move.c), so it is the natural name.
- **TM:** Aerial Ace.
- **Team (4, levels 31 to 33):** Swellow 31, Pelipper 32, Fearow 32, Tropius 33.

### Gym 7: Poison (T10), no HM
- **Leader pitch:** a middle-aged chemist who reads the ingredients on everything and treats battles as quality control.
- **Gimmick:** vats with coloured gas pipes. Switches shut off the gas pipes in the right order to clear a path (fixed order, hinted on the wall).
- **Badge:** VIAL BADGE. Silver ring, magenta core, small droplet.
- **TM:** Sludge Bomb.
- **Team (4, levels 36 to 38):** Weezing 36, Swalot 37, Seviper 37, Muk 38.

### Gym 8: Fairy (T11), Waterfall
- **Leader pitch:** a young florist who is much tougher than she looks and pretends not to notice that everyone underestimates her.
- **Gimmick:** a glade of flower beds. The player follows a petal trail and blooming flowers reveal the hidden door. A cute fake-out: the trainers are all enormous.
- **Badge:** CHARM BADGE. Silver ring, pink core, small flower.
- **TM:** Calm Mind (there is no Fairy TM in the 50 TM list).
- **Team (5, levels 41 to 43):** Azumarill 41, Granbull 41, Ribombee 42, Dedenne 42, Gardevoir 43.

### Gym 9: Water (T12), Dive
- **Leader pitch:** an old lighthouse keeper, deadpan and unhurried, the last gym leader before the coast and proud of it.
- **Gimmick:** the gym is a flooded lighthouse. The player climbs up by pumping the water level down floor by floor with valves.
- **Badge:** TIDE BADGE. Silver ring, teal core, small wave.
- **TM:** Water Pulse.
- **Team (5, levels 44 to 46):** Lanturn 44, Wailord 44, Gyarados 45, Swampert 45, Milotic 46.

---

## Recommendation (PROPOSED)

**Option A.** Its type order is the easier one to read, and it needs fewer tiles that may not exist (Option B wants hedges, belts and gas pipes, three new tile sets). Its HM fits are tighter (Rock Smash from Rock, Flash from Electric, Strength from Fighting, Surf from Water, Fly from Flying) and it ends on a Dragon finale before the Elite Four. The trade-off is that it is the most predictable. If the author wants a stranger mix, take B and keep Flying as gym 6 either way.

Mixing the two is fine. The town slots, HM plan and team sizes do not depend on the type order.

## Open questions

1. Which option, or a mix? Each type swap only changes the leader's team and the gimmick.
2. Gym towns or cities? Every city gets a Goldsworth house and one city has the skyscraper (game-bible decision 12), so which slots are cities is still open.
3. Is the gym order in T7 and T8 before T10 to T12 right, or should the north chain come first?
4. Should gym 7 (no HM) keep no HM, or should the author move Dive back to 7 (no edit needed)?
5. Do the gimmicks need tile art not in the asset repos? Check before locking a gym in.
6. Levels: leader ranges are the target, and with no IVs or EVs the fights will play a little easier than vanilla, so tune in play.
