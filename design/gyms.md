# Gyms 2 to 9

Status: **Type order, level cap and town/city mix DECIDED by the author on 2026-10-01 (see Decided). Everything else below (names, leaders, gimmicks, badges, TMs, exact teams, which towns are cities beyond Crestfall) is still PROPOSED until approved (CLAUDE.md rule 9).**

**Fixed (author):** Gym 1 is Crestfall (T3), a town (changed from city by the author, 2026-10-01), Normal type, Greta (young, sassy, kind), STANDARD BADGE, silver outside and blue inside, Greta 10 and 12. Details in [characters.md](characters.md) and [teams.md](teams.md).

## Decided (author, 2026-10-01)

1. **Type order is Option B:** Normal (Greta, fixed), Bug, Ghost, Steel, Ice, Flying, Poison, Fairy, Water. **Gym 6 is Flying and gives Fly (Feather Badge).** Option A is kept only as a short appendix.
2. **Total gym level cap is 60.** Gym 1 stays at 12. The curve runs from about 17 to 19 at gym 2 up to 58 to 60 at gym 9, and **the gym 9 ace is 60**. Teams and trainers below are rescaled to it (the exact numbers are PROPOSED).
3. **The Elite Four starts at level 65**, so gym 9 at 60 leads straight into it. Details live in [postgame.md](postgame.md).
4. **Gym towns are a mix of towns and cities.** Crestfall (T3) is a town (author, 2026-10-01; it was a city before). The other city picks below are PROPOSED.
5. **No IVs or EVs, Pokemon only.**

**Level cap note:** done 2026-10-01, `src/caps.c` badge 9 row is **60** (the Champion row is 75; full table in open question 7 below). The cap is still switched off in `include/config/caps.h`.

**Not decided here:** town names (placeholders), the Goldsworth scheme per gym ([story-outline.md](story-outline.md)), trainer classes and pictures, moves (species and levels only, moves go into [teams.md](teams.md) once approved).

## Rules

- **Teams:** leaders 2 Pokemon early, rising to 5 at gym 8 and 6 at gym 9. Gym trainers sit about 3 to 4 levels below their leader's lowest Pokemon. Species are Gen 1 to 9 entries that exist in this tree (the evolved forms are used where the level warrants). Checked 2026-10-01 against this tree's evolution levels and level-up learnsets (`design/tools/teamcheck.py`): every species exists, none is under- or over-evolved for its level, and each knows at least 4 level-up moves by then. Teams mix all nine generations.
- **Trainer ids:** about 4 to 5 of the 9 brand-new ids are free (game-bible decision 6), so **every trainer here, leaders included, is meant to reuse a vanilla Hoenn entry** (CLAUDE.md, 'A new trainer', reuse route, untested).
- **Gym grass or water** is decoration only, never wild encounters.
- **Gym maps** must respect 15 live objects per map (engine-limits row 8).

## Badge family (PROPOSED)

Badge 1 is a silver ring with a blue core. Every badge keeps **the same silver ring and differs in core colour and a small motif**, so the trainer-card strip reads as one set. The card uses **one shared 15-colour palette** ([badges.md](badges.md)), so two cores may have to share a colour (the motif tells them apart). Art is being outsourced, so this is a brief. Blue stays badge 1's, so Water uses teal.


`src/field_move.c` ties each move to a badge index, so any badge can grant any move. Vanilla order is Cut 1, Flash 2, Rock Smash 3, Strength 4, Surf 5, Fly 6, Dive 7, Waterfall 8. This plan keeps **Cut, Strength, Surf, Fly and Waterfall on their vanilla numbers** (no edit) and moves three (one number each, log in [engine-edits.md](engine-edits.md)):

| Badge | From | Move | Edit |
|---|---|---|---|
| 1 Standard (Greta) | Crestfall | Cut | none (author-fixed, vanilla) |
| 2 | Gym 2 | Rock Smash | was badge 3 |
| 3 | Gym 3 | Flash | was badge 2 |
| 4 | Gym 4 | Strength | none |
| 5 | Gym 5 | Surf | none |
| 6 | Gym 6 | Fly (**needs the Feather Badge in this build**, it is the 6th badge) | none |
| 7 | Gym 7 | none (TM only) | Dive moved off badge 7 (**done 2026-10-01**, `src/field_move.c`) |
| 8 | Gym 8 | Waterfall | none |
| 9 | Gym 9 | Dive | was badge 7 |

Why it is sensible: Surf at badge 5 is well before the sea routes (R18 to R23 lead to T16 to T18, past every gym town). Fly at gym 6 lets the player skip the long walk back from T8 to T10 (see the route note below) and is the Flying gym, so the **Feather Badge** fits its own name. Fly also needs the town flag set by walking in first ([region-map.md](region-map.md)). Every move is usable only when the gym in that slot is beaten, so the route design (which HM-gates which side path) stays open and the author can re-point any move.

## Town slots and cities

Cells from [region-map.md](region-map.md). The map forks at T6. **Suggested order:** T4, T5, T6, then the south branch T7 and T8, then Fly to the north branch T10, T11, T12. **T9 and T13 have no gym.** Names are placeholders.

**Cities (PROPOSED, except Crestfall which the author fixed):** T3 Crestfall, T5 (gym 3 Ghost), T8 (gym 6 Flying, the **skyscraper city**, no Goldsworth house because Troglodyte's parents live in the tower), T11 (gym 8 Fairy). **Towns:** T4, T6, T7, T10, T12. Every city except the skyscraper city gets a Goldsworth house: **3 houses (Crestfall, T5, T11)**. Other cities may still sit among the non-gym places (T9, T13 and further), so the total is still open (game-bible decision 12).

| Gym | Slot | Kind | Section id | Reached by | Notes |
|---|---|---|---|---|---|
| 1 | T3 Crestfall | town (author, 2026-10-01) | `MAPSEC_CRESTFALL` | R2 | No Goldsworth house (moved to Briarwick). Greta |
| 2 | T4 | town | `MAPSEC_VELDRIS_TOWN_04` | R3 | Side path R26 |
| 3 | T5 | city | `MAPSEC_VELDRIS_TOWN_05` | R4 | Goldsworth house. Side path R27 |
| 4 | T6 | town | `MAPSEC_VELDRIS_TOWN_06` | R5 | The fork: R6 to T7, R11 to T10, side path R28 |
| 5 | T7 | town | `MAPSEC_VELDRIS_TOWN_07` | R6 (or R15) | Loop back to Crestfall |
| 6 | T8 | skyscraper city | `MAPSEC_VELDRIS_TOWN_08` | R7 (or R16) | No Goldsworth house (tower). Fly arrives here. Side path R29 |
| 7 | T10 | town | `MAPSEC_VELDRIS_TOWN_10` | R11 or R17 | Side path R30 |
| 8 | T11 | city | `MAPSEC_VELDRIS_TOWN_11` | R13 (R12 from T10) | Goldsworth house. Side path R31 |
| 9 | T12 | town | `MAPSEC_VELDRIS_TOWN_12` | R14 | End of north chain, Surf route R21 to T18 |

## Levels and ids (PROPOSED)

| Gym | Type | Leader team | Leader levels | Gym trainers | Trainer levels | Ids (leader plus trainers) |
|---|---|---|---|---|---|---|
| 1 | Normal | 2 | 10 and 12 (fixed) | see teams.md | | separate |
| 2 | Bug | 2 | 17 to 19 | 2 (1 to 2 mons) | 13 to 15 | 3 |
| 3 | Ghost | 3 | 23 to 25 | 2 (1 to 2 mons) | 19 to 21 | 3 |
| 4 | Steel | 3 | 29 to 31 | 3 (2 mons) | 25 to 27 | 4 |
| 5 | Ice | 4 | 35 to 37 | 3 (2 mons) | 31 to 33 | 4 |
| 6 | Flying | 4 | 40 to 42 | 3 (2 mons) | 36 to 38 | 4 |
| 7 | Poison | 5 | 46 to 48 | 4 (2 to 3 mons) | 42 to 44 | 5 |
| 8 | Fairy | 5 | 52 to 55 | 4 (3 mons) | 48 to 50 | 5 |
| 9 | Water | 6 | 58 to 60 (ace 60) | 4 (3 mons) | 54 to 56 | 5 |

Totals: 8 leaders, 25 gym trainers, **33 ids, all reusing vanilla entries**. Gym 9 at 60 leads into the Elite Four at 65.

---

# Gym details (Option B, chosen type order)

Pitches, gimmicks, badges and TMs are PROPOSED. Teams were rescaled to the 60 cap.

Normal, Bug, Ghost, Steel, Ice, Flying, Poison, Fairy, Water. The Water gym comes last and Surf still arrives at gym 5, so the player meets the sea before its type master. A bit stranger and less predictable, but **Ghost, Steel and Fairy gyms come earlier than the matching counters are easy to catch**, so the wild encounter tables will need care.

### Gym 2: Bug (T4), Rock Smash
- **Leader pitch:** a young beekeeper in a veil, gentle and oddly formal, who apologises to every bug she sends out.
- **Gimmick:** hedge walls and a garden of tall decorative grass (not encounter grass) with web tiles that force a detour. Needs hedge and web tile art.
- **Badge:** HUSK BADGE. Silver ring, lime green core, small wing or leaf.
- **TM:** Thief (there is no Bug TM in this ROM's 50 TM list).
- **Team (2, levels 17 to 19):** Kricketune 17, Vivillon 19.

### Gym 3: Ghost (T5, city), Flash
- **Leader pitch:** a teenage mortician's apprentice, dry and unbothered, who thinks the dead are the better audience.
- **Gimmick:** a dark gym with pools of light (Flash shows more of the floor, it is also the badge's move). Some doors are fakes that loop the player back.
- **Badge:** WISP BADGE. Silver ring, violet core, small flame-like wisp. (Named to avoid Hollowbrook.)
- **TM:** Shadow Ball.
- **Team (3, levels 23 to 25):** Shuppet 23, Litwick 24, Mimikyu 25.

### Gym 4: Steel (T6), Strength
- **Leader pitch:** a middle-aged foundry foreman, exhausted and very patient. His workers are always at lunch.
- **Gimmick:** conveyor belts and crusher presses carry the player around the floor on a timing puzzle. Needs belt tiles, which may not exist yet.
- **Badge:** RIVET BADGE. Silver ring, dark slate core, small bolt or gear.
- **TM:** Iron Tail.
- **Team (3, levels 29 to 31):** Bronzor 29, Pawniard 30, Tinkatuff 31.

### Gym 5: Ice (T7), Surf
- **Leader pitch:** an old fisherman, very relaxed, who leaves the ice fishing hole for the battle and has a thermos.
- **Gimmick:** a frozen lake floor with cracked patches. The floor is slippery, and the thermos is the hint: wait by the heater tile for the ice to reset.
- **Badge:** FROST BADGE. Silver ring, pale cyan core, small snowflake. (Surf fits: the lake thaws out.)
- **TM:** Ice Beam.
- **Team (4, levels 35 to 37):** Sneasel 35, Vanillish 36, Lapras 37, Avalugg 37.

### Gym 6: Flying (T8, skyscraper city), Fly
- **Leader pitch:** a young pilot in a leather jacket, dry and a little vain, who calls the battle a flight plan and never raises his voice.
- **Gimmick:** wind-tunnel floors: arrow tiles push the player along a route over a pit-like sky bridge. Arrow tiles already exist in vanilla (Mossdeep and Sootopolis style), but check.
- **Badge:** FEATHER BADGE. Silver ring, white or sky core, small feather. The author wants Fly to need the Feather Badge in this build (src/field_move.c), so it is the natural name.
- **TM:** Aerial Ace.
- **Team (4, levels 40 to 42):** Swellow 40, Unfezant 41, Talonflame 41, Corviknight 42.

### Gym 7: Poison (T10), no HM
- **Leader pitch:** a middle-aged chemist who reads the ingredients on everything and treats battles as quality control.
- **Gimmick:** vats with coloured gas pipes. Switches shut off the gas pipes in the right order to clear a path (fixed order, hinted on the wall).
- **Badge:** VIAL BADGE. Silver ring, magenta core, small droplet.
- **TM:** Sludge Bomb.
- **Team (5, levels 46 to 48):** Weezing 46, Crobat 47, Drapion 47, Garbodor 47, Toxapex 48.

### Gym 8: Fairy (T11, city), Waterfall
- **Leader pitch:** a young florist who is much tougher than she looks and pretends not to notice that everyone underestimates her.
- **Gimmick:** a glade of flower beds. The player follows a petal trail and blooming flowers reveal the hidden door. A cute fake-out: the trainers are all enormous.
- **Badge:** CHARM BADGE. Silver ring, pink core, small flower.
- **TM:** Calm Mind (there is no Fairy TM in the 50 TM list).
- **Team (5, levels 52 to 55):** Azumarill 52, Dachsbun 52, Ribombee 53, Hatterene 54, Gardevoir 55.

### Gym 9: Water (T12), Dive
- **Leader pitch:** an old lighthouse keeper, deadpan and unhurried, the last gym leader before the coast and proud of it.
- **Gimmick:** the gym is a flooded lighthouse. The player climbs up by pumping the water level down floor by floor with valves.
- **Badge:** TIDE BADGE. Silver ring, teal core, small wave.
- **TM:** Water Pulse.
- **Team (6, levels 58 to 60):** Gyarados 58, Seismitoad 58, Araquanid 59, Barraskewda 59, Lanturn 59, Milotic 60 (ace).

---

## Remaining open questions

1. Gym leaders' names, trainer classes and pictures (not decided).
2. Tile art for the gimmicks (hedges and webs, belts, gas pipes, wind arrows, flower beds, flooded floors): check the asset repos before locking each gym in.
3. Does gym 7 keep no HM (TM only), or does the author move Dive back to 7 (no edit needed)?
4. Which non-gym places are cities (T9, T13 and others), and so how many Goldsworth houses in total (game-bible decision 12).
5. Is the order T7, T8 before T10 to T12 right, or should the north chain come first?
6. Tune levels in play: with no IVs or EVs fights run a little easier than vanilla.
7. `src/caps.c` level caps now follow the gym aces (12, 19, 25, 31, 37, 42, 48, 55, 60) and the Champion at 75. **Done 2026-10-01.** The cap is still switched off in `include/config/caps.h`, so it only matters if you turn it on.

---

## Appendix: Option A, not chosen

Normal, Rock, Electric, Fighting, Water, Flying, Psychic, Ice, Dragon. Kept so nothing is lost; its teams were not rescaled to the 60 cap.

- Gym 2 Rock (Cobble Badge, Rock Smash): quarry foreman, rail boulders.
- Gym 3 Electric (Spark Badge, Flash): retired electrician, fuse-box puzzle.
- Gym 4 Fighting (Bout Badge, Strength): polite dojo teacher, belt-order sparring rings.
- Gym 5 Water (Tide Badge, Surf): teenage ferry pilot, drain-valve pool maze.
- Gym 6 Flying: same as chosen.
- Gym 7 Psychic (Reverie Badge): old fortune teller, warp pads.
- Gym 8 Ice (Frost Badge, Waterfall): soft-spoken ice sculptor, slide puzzles.
- Gym 9 Dragon (Scale Badge, Dive): dignified champion-in-waiting, statue switches.
