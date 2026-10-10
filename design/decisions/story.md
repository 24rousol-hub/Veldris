## Quick answers (one word each)

These are the small calls from the 2026-10-09 work. Answer with the number and a letter, for example '1 B'. Defaults are what is built today.

| # | Question | Options | Built today / my pick |
|---|---|---|---|
| Q1 | Who gives the **Journal**? | A the Route 1 guide (ordinary NPC, after the Potions) / B Mom, right after 'you have a Pokémon', in the shoes scene / C Prof. Fennick, after the starter choice (a key lab scene, so it needs your yes) | **A is built.** I would pick **B**: Mom already hands over the shoes, and 'she gives you a notebook' is warm and quick. One call to `Veldris_EventScript_GiveJournal` |
| Q2 | **Game-day length** of the fake clock | A 72 real minutes (20x, now) / B real time (1:1) / C 24 real minutes (60x) | **A is built.** Pick B if you want night to feel like real night, C if you want it to change fast enough to notice on one route |
| Q3 | Rich jingle in **Crestfall's** Troglodyte fight (Scheme 1) | yes / no | Not there yet; one line (`playbgm MUS_ENCOUNTER_RICH, FALSE`) in the other session's scene. Pick **yes** |
| Q4 | **Victory tune** after beating Troglodyte | A gym-leader tune (built) / B Elite Four tune (35 s) / C ordinary trainer tune | **A is built** |
| Q5 | **Wall clock** spot in the player's room | A x=3, between the bed and the PC (built event) / B x=6, between the PC and the TV | **A is built.** You paint the clock picture in Porymap either way |
| Q6 | Clock **hours** | A standard: Morning 6-10, Day 10-19, Evening 19-20, Night 20-6 (now) / B Gen 4 style: Morning 4-10, Day 10-20, Night 20-4, no Evening | **A is built** |
| Q7 | **Route 1 night species** | keep Hoothoot, Rattata, Spinarak, Murkrow / change | Kept as PROPOSED |
| Q8 | **Furniture** lines | keep the 17 neutral village lines / rewrite them richer or poorer | Kept as PROPOSED |

## Story and world calls still open in the game bible

### Starters (open decision 14): which four species?

You said you would tackle this once the Hollowbrook map, the lab and the houses were done: they are. Today the lab uses stand-ins (Treecko, Torchic, Mudkip, and Pikachu as the fourth). Rules from you: four starters; three on show; Troglodyte takes one of the three at random; Fennick then reveals the fourth as an apology; the player picks from the three left. So **each of the three must be a believable thing for Troglodyte to grab, and the fourth should feel like a gift**.

| Set | The three on show | The fourth (the apology) | Why it fits | Watch out for |
|---|---|---|---|---|
| **A: Johto** | Chikorita, Cyndaquil, Totodile | Togepi (an egg in Johto lore; becomes Togetic, then Togekiss with a Shiny Stone) | The Palladium map art is Johto and Kanto: Hollowbrook is New Bark Town, Fennick is Prof. Elm. The Togepi egg is exactly what Elm hands over | Chikorita's line (Grass) is weak into gyms 2, 5, 6 and 7 (Bug, Ice, Flying, Poison). Fairy fourth is strong into gym 7 (Poison), weak into gym 4 (Steel) |
| **B: Sinnoh** | Turtwig, Chimchar, Piplup | Riolu (Lucario needs high friendship in the daytime: the fake clock now makes that real) | Cynthia, the old Champion, is from Sinnoh and is Gatsby's old friend: the starters could come from her through Fennick. Matches the Gen 4 look of the hack's trainer art and tiles | A Riolu gift hints at Cynthia early, which is your story beat to time. Chimchar's line (Fire/Fighting) is strong into gyms 1, 2, 4, 5 and weak into 6 and 8 |
| **C: Unova** | Snivy, Tepig, Oshawott | Eevee (a rare one Fennick could not afford to part with) | Plain triangle, all three evolve at the same levels (17 and 36), so easy to balance; Eevee gives the player a choice later | No story link; Gen 5 sprites are the newest style in the tree |
| **D: Hoenn (stand-ins)** | Treecko, Torchic, Mudkip | your pick (Pikachu is the stand-in) | Already built and tested in battle, pool-prune tested | It is the vanilla Emerald trio, so the least original |

How the answer is used: one batch edit of `sStarterMon` in `src/starter_choose.c`, the lab text and the three starter variants inside each Troglodyte block in `src/data/trainers.party` (his later fights use the evolved forms). Nothing else depends on the species. The evolution lines of the chosen four would also have to be added to the level plan in `design/teams.md`. Troglodyte keeps his Lillipup (SIR BISCUIT) in every set. I would pick **A**, because Hollowbrook is already New Bark Town in everything but name; B is the strongest story pick if you want Cynthia seeded from minute one.

### Which of the 18 places are cities (open decision 12), and the skyscraper (open decision 8)

Your own sketch labels already say City for seven of them. Reading those labels literally gives a clean answer:

| Place | Sketch label | Gym | Goldsworth house? | Notes |
|---|---|---|---|---|
| Briarwick | City 4 | 2 Bug | yes (the first one, approved) | |
| Hoarfell | City 7 | 5 Ice | yes | |
| Gildhaven | Central City | 6 Flying | **no: the skyscraper** (the city that has the tower gets no house) | The names table already calls it 'the Goldsworth skyscraper hub' |
| Hemlock Reach | City east | 7 Poison | yes | |
| Primrose Vale | City far NE | 8 Fairy | yes | |
| Kingsquay | City SE | none | yes | Big harbour city, no gym |
| Beaconmouth | City far SE | 9 Water | yes | |
| Vesperhaven, Aldermere | South City, Lost City | none | post-game only | Treat as post-game places; no house |

Everything else (Hollowbrook, Crestfall, Wendlebury, Gloomsby, Smeltham, Cragdale, Lingmoor, Waymeet, Brinecombe, Ebbsworth, Driftsands) is a town, with Hollowbrook the one town that keeps a Goldsworth house. That gives **six Goldsworth city houses** (Briarwick, Hoarfell, Hemlock Reach, Primrose Vale, Kingsquay, Beaconmouth), one skyscraper (Gildhaven) and the grandfather's house in Hollowbrook. Answer: **adopt the sketch labels** / or tell me which place changes.

### Goldsworth house fights (open decision 11)

All six city houses are NPC-only today (no trainer ids). A: keep them NPC-only. B: one shared 'Goldsworth family' trainer id whose flag is cleared with `cleartrainerflag` after each fight, so every house can have a cousin to beat (flag space is not an issue: it reuses one id). My pick: **B for at most two or three houses**, the loud ones (Chad, Biff), because the player is here to humiliate them; the lounger and the wine snob stay NPC-only.

### Tone limit: how cruel may a Goldsworth be (open decision 10)

You settled that they may swear lightly. Still open: cruelty. A: never to innocent townsfolk (the assumed limit; the cruelty is aimed at the player, at Troglodyte and at each other). B: they may be rude to townsfolk but never cruel to children or animals. Pick **A** unless you want sharper villains.
