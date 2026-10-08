# Game bible

**Title:** Pokémon: Piss Off Troglodyte (short form: POT)
**Region:** Veldris
**Base:** pokeemerald-expansion (personal-use GBA ROM hack; the repo is public, the ROM is never committed)

## Pitch

The player has one reason to become Champion: to humiliate Troglodyte. His real name is Beauregard Goldsworth IV. He is a sheltered, mediocre rival whose rich parents keep staging elaborate schemes to sabotage the gyms in his way. Every scheme fails. The League is just what happens to be at the end of the road. **The real danger (author, 2026-10-04)** is two villain teams in a reluctant alliance against the rich, the Commons and the Drowned Crown ([factions.md](factions.md)); the player handles them as a necessary nuisance.

**Author note (2026-09-29):** the Goldsworths are rich frat guys who are assholes. Every city has a Goldsworth house (and so does Hollowbrook, the grandfather's home town, the one town exception), and one city has their skyscraper business, where Troglodyte's parents are. The parents are oblivious rather than contemptuous, unlike the rest of the family. His grandfather, a kind old man who had to step down as family head, lives in Hollowbrook's house. The Goldsworths may swear, mildly. Details and what is still open: [characters.md](characters.md), [story-outline.md](story-outline.md).

## Pillars

1. **The motive is petty and personal.** The player wants Troglodyte to lose, in public, again. **Clarified (author, 2026-10-04):** the player does care about Veldris, but feels its bigger trouble (the villain team, PROPOSED) should not be their problem. Dealing with it is a nuisance, but a necessary one. The Goldsworths are an annoyance; the team is the real danger.
2. **The schemes always fail.** Each gym has a Goldsworth scheme (see [story-outline.md](story-outline.md)). It is built up, it is obviously flawed, it collapses, and Troglodyte loses the battle that follows.
3. **Troglodyte is mediocre, not evil.** He is coddled and out of his depth. He loses because he never had to learn, not because he is a monster. The humour lands on him and his family, never on the townsfolk. *(The Goldsworths are now rich frat guys who are assholes, and can swear mildly. The humour still never lands on the townsfolk, and the grandfather is the kind exception. See [characters.md](characters.md).)*
4. **The rest of Veldris is warm.** Gym leaders and locals are sincere and a bit weird. Greta is the model: young, sassy, kind underneath, and already the best Normal-type trainer for miles (author's update 2026-09-29, replacing 'retired farmer').

## Scope (fixed by the author)

| Item | Count | Notes |
|---|---|---|
| Towns | 18 | List in [towns-and-routes.md](towns-and-routes.md). Some of the 18 are cities and the rest towns, count not final (open decision 12) |
| Routes | 33 | Same file |
| Gyms | 9 | Gym 1 is Greta, Normal type. Others TBD. See decision 1 (resolved: 9 badges) |
| Elite Four | 4 members | TBD |
| Champion | not specified yet | See open decision 2 |
| Post-game | yes | Contents TBD |

## Progression skeleton (PROPOSED)

1. Intro (C-driven, `data/text/birch_speech.inc`), Prof. Fennick, starter.
2. First 3 towns and 3 routes, ending at gym 1 (Greta, Normal). Built first so all three can be flown between.
3. Gyms 2 to 9 in order, each with its own Goldsworth scheme. Every city has a Goldsworth house (and Hollowbrook, as the one town exception), and one city has their skyscraper (PROPOSED details in [story-outline.md](story-outline.md)).
   **Alongside (author, 2026-10-04):** the villain teams, the Commons on land and the Drowned Crown at sea ([factions.md](factions.md)). Commons block Route 3 until Wendlebury; the alliance breaks between badges 5 and 7; the player and Troglodyte beat the Commons leader together.
4. **Climax (author):** after badge 9 the Elite Four and Cynthia leave to calm the region and the Drowned Crown wakes Kyogre on R19 into Gildhaven, the capital.
5. Elite Four, then the Champion.
6. Post-game (Aldermere: the Crown's refuge, Dialga's anchor, Kyogre at a random daily hour).

## Who does what

- **The author** builds and edits maps in Porymap.
- **Claude** writes scripts, events, warps, trainers and dialogue, and keeps these docs current.
- Maps are fragile. No script generates map files. Claude does not hand-edit map block data or tilesets.

## Open decisions

These need the author's call. None blocks the first 3 towns.

1. **Nine gyms versus eight badges. RESOLVED 2026-09-29:** the engine now supports 9 badges through a data-driven table (option C in badges.md). Details, limits and what is untested are in [badges.md](badges.md). Badge art is a placeholder set to be replaced by outsourced art.
2. ~~**Who is the Champion?**~~ **Resolved (author, 2026-10-01):** an **aged Cynthia** (the Sinnoh Champion, now old), the previous region's Champion and Gatsby's old friend. Not Troglodyte. She is the final fight at levels 73 to 75.
3. **Player and rival replacement.** Emerald's rival is May or Brendan. Troglodyte replaces them, which touches rival scripts and sprites. Which parts of the Hoenn intro and rival flow do we keep? **Update 2026-09-29:** the author fixed how he gets his Pokémon: he forces Fennick to give him one, at random among the starters. That replaces the Route 101 and Route 103 rival start. See 'Troglodyte's starter' in [story-outline.md](story-outline.md).
4. ~~**Names of towns 1 to 3.**~~ **Resolved (author, 2026-09-29):** Hollowbrook and Wendlebury approved. Crestfall comes from the author's trainer constant `TRAINER_CRESTFALL_GRETA` and is the first gym town. Marrow Bay (the bay) is still a placeholder.
5. ~~**Region map style.**~~ **Resolved (author, 2026-09-29):** the vanilla GBA town-map look. See [region-map.md](region-map.md).
6. **Trainer slots.** Only 9 new trainer IDs fit before trainer flag space overflows (`TRAINERS_COUNT` 855, `MAX_TRAINERS_COUNT` 864, upstream's own note in `include/constants/opponents.h`). A hack with a gym, Elite Four and trainers on 33 routes needs hundreds. Options: (a) reuse and rename vanilla Hoenn or FRLG trainer IDs you no longer need, or (b) raise `MAX_TRAINERS_COUNT`. A random Troglodyte starter needs three ids per rival battle, which makes (a) attractive: the 15 vanilla `TRAINER_BRENDAN_*` ids are the natural ones to reuse, since nothing in `src/` refers to them by name. Measured save headroom is about 176 bytes (roughly 1,400 flags), so a few hundred more trainers fit. It shifts every system and daily flag, which is fine on a fresh start. Untested. `TRAINER_CRESTFALL_GRETA` is the first to need a slot, and with her two gym trainers Crestfall needs 3 of the 9. **Clarified 2026-09-29 (author's question):** the limit only counts brand-new ids. Reusing a vanilla Hoenn trainer entry costs none, so it is not a cap. Assigned so far: Greta and two gym trainers (3 ids) plus Troglodyte, whose random starter needs 3 variants per battle (3 ids), so 6 of the 9 brand-new ids (before the pool prune, which now makes it 1 id per Troglodyte fight, so 4 at the moment, 5 once Troglodyte's Crestfall fight is added). Everything after that can reuse vanilla entries. Not blocking until the first new trainer is added.
7. ~~**Which places get a Goldsworth house?**~~ **Resolved (author, 2026-09-29):** every **city** gets one. **Towns do not, with one exception: Hollowbrook**, the grandfather's home town. The skyscraper's city gets none. Which places are cities is open decision 12.
8. **Which city has the skyscraper? PARTLY RESOLVED, still open: the city.** Resolved (author, 2026-09-29):** the skyscraper is in a **city**, not a town, and that city does **not** also get a house. Troglodyte's parents are in the tower. Which city is still TBD. The tower exterior needs new art or a compromise ([map-plan.md](map-plan.md)).
9. ~~**Do Troglodyte's parents stay?**~~ **Resolved (author, 2026-09-29):** yes. They are in the tower. They are assholes, but not on purpose like the rest of the family: they live in luxury and do not understand the lower classes, rather than disliking them. His grandfather, a kind old man who stepped down as family head because of his health, lives in Hollowbrook's Goldsworth house.
10. ~~**Tone limits for the Goldsworths.**~~ **Resolved (author, 2026-09-29):** they can swear, but nothing 4chan level. See [dialogue-style.md](dialogue-style.md) for the working limits. Not yet answered: how cruel they may be (the assumed limit: never to innocent townsfolk).
11. **Goldsworth house fights.** Only 9 trainer ids are spare and the 9 gym leaders use them all (decision 6). Proposed rule: the houses are NPC-only, with no trainer ids. If a house should have a fight, use one shared 'Goldsworth family' id and reset its flag with `cleartrainerflag` for repeats.
12. **Which of the 18 places are cities and which are towns?** The author says a city and a town are different, and there may be 7 cities with the rest towns (**7 is an example, not final**). Which places are cities, what a city has that a town does not, and whether gym towns are cities are all open. **Partly resolved (author, 2026-09-30):** Hollowbrook and Wendlebury are towns; Crestfall, the next stop, is a city. So Crestfall gets a Goldsworth house (PROPOSED, unless it turns out to hold the skyscraper). The rest is still open. Until decided, 'town' in these docs means any of the 18 settlements.
13. **Is Troglodyte like his parents or like the rest of the family? RESOLVED (author, 2026-10-01): Arc A, contemptuous then humbled** (the oblivious arc is not chosen). Earlier note, resolved (author, 2026-09-29): he starts contemptuous, like the wider family, and can change to oblivious and confused, like his parents, after certain story points. Still open: which story points trigger the change, and whether it happens at all. The story's path is undecided. The Goldsworths are one of its obstacles.
14. **Starters.** **Author, 2026-09-29:** there are **four** starters, not three. Three are on show. Troglodyte takes one of those three at random, and Fennick then reveals the fourth as an apology to the player. The player picks from what is left. **Which species: undecided. The author will tackle it once the Hollowbrook map, the lab and the houses are done.** **Confirmed by the author (2026-09-29):** four starters in total, so after Troglodyte's pick the player chooses from three (the two left on show plus the revealed fourth). The author's 'the remaining 4' was a slip. This also settles the earlier worry about the player ending up with the same species as Troglodyte: they cannot. How to build it: 'Starters and the lab scene' in [story-outline.md](story-outline.md). The vanilla starter screen is hard-wired to three balls, so the proposal is Poké Ball objects on a lab table, which needs no engine edit.

## Decision log

| Date | Decision | Who |
|---|---|---|
| 2026-10-08 | No trading: Centers have no 2F, and trade evolutions work without trading (evolution items used from the bag, the Linking Cord, Karrablast and Shelmet level up with each other in the party). The Linking Cord and the evolution items still need places in the world. | Author |
| 2026-10-08 | Mothwood is a required story event after badge 2 (ranger closure, the Drowned Crown stealing a Time Gear-like seal piece); Shedinja during it, Celebi post-game; Shaymin kept for Primrose Vale; shiny Shedinja's halo darkened. | Author |
| 2026-10-08 | Route 8 blocked until badge 2; Mothwood branches off Route 8; Route 9 dropped. Route 3 block is Commons fake road works; Teddy's Wendlebury scene is a lost Pokémon plus a chat at the inn. | Author |
| 2026-10-04 | Villains: The Commons (land routes) and THE DROWNED CROWN (sea routes, the climax after badge 9), a reluctant alliance against the rich. The player cares about Veldris but sees this as a necessary nuisance. See [factions.md](factions.md). | Author |
| 2026-09-29 | Town names Hollowbrook and Wendlebury approved. Vanilla GBA town-map look approved for the region map. | Author |
| 2026-09-29 | Badges: research public hacks with more than 8 badges, and consider a custom badge case with our own art. Plan first, no engine edits yet. | Author |
| 2026-09-29 | Fly towns: the author left it to the assistant ("whatever is best for the future"). Chosen: approach A-prime, see [region-map.md](region-map.md). | Assistant, on the author's instruction |
| 2026-09-29 | 9 gyms, Elite Four and Champion. Real 9th badge via a data-driven badge table; badge art to be outsourced (asset repo fork used for stand-ins). Assistant told to use its best judgment. | Author |
| 2026-09-29 | Region map shape approved. "Zoom out" means denser tile art (more detail in the same space), not more cells. | Author |
| 2026-09-29 | Prof. Fennick's intro tone approved (`data/text/birch_speech.inc`), including the line seeding Troglodyte's full name. | Author |
| 2026-09-29 | Maps: a mix of Project Palladium maps (Team Aqua repo, traced in Porymap as references) and vanilla bases. See [map-plan.md](map-plan.md). | Author |
| 2026-09-29 | Palladium and vanilla pairings for towns 1 to 3 approved. Hollowbrook is the first map the author builds. | Author |
| 2026-09-29 | Goldsworths: a house in every city, a skyscraper in one city as their business, and they are rich frat guys who are assholes (author's note; the reading of 'them' is settled in decision 9). | Author |
| 2026-10-01 | Level scale: gym levels run 12 (gym 1) to 60 (gym 9 ace), the Elite Four starts at 65, the Champion ends at 75. Gym type order is Option B (Normal, Bug, Ghost, Steel, Ice, Flying, Poison, Fairy, Water) with gym 6 Flying. Gym places are a mix of towns and cities. Troglodyte follows Arc A (contemptuous, then humbled). The Champion is an aged Cynthia. | Author |
| 2026-09-30 | Wendlebury is a town. The next stop, Crestfall, is a city. **Superseded 2026-10-01** | Author |
| 2026-10-01 | The cousins' nickname for Troglodyte is 'Beau'. | Author |
| 2026-10-01 | Dialga and Mew are re-offered until caught. | Author |
| 2026-10-01 | Legendaries: **DIALGA at Mirror Isle**, **MEW at Aldermere** (the ancient city). R18 construction ends at the Feather Badge (confirmed). | Author |
| 2026-10-01 | Map-card review answers: R1 to R31 numbering confirmed; Primrose Vale is a Surf-only pocket; NPC garden warden owns Scheme 8's FLORGES; scheme Pokémon are cutscene-only; Mirror Isle has a legendary encounter and is the only DITTO source; Goldsworth house split approved; Troglodyte has no Garchomp (postgame team for fights 7 and 8); all nine badges for the League; R18 is under construction; Gildhaven traced from the Goldenrod render mirrored. See [maps/index.md](maps/index.md). | Author |
| 2026-10-01 | Houses: no custom layout per house, at least 5 shared one-floor layouts ([maps/interiors/house-layouts.md](maps/interiors/house-layouts.md), six drawn up). Tilesets must look Gen 4. Assistant draws the 9 badges, author tweaks. Wendlebury Inn is in, on the Gen 4 Interior set. | Author |
| 2026-10-01 | Tilesets: the LeoB ORAS outdoor sets stay (author likes them). Pokémon sprites stay as shipped (already Gen 4/5 style); no sprite import. | Author |
| 2026-10-01 | Pokémon sprites: keep the shipped Gen 4/5-style art, not GBA-style (`P_GBA_STYLE_SPECIES_GFX` stays FALSE). Troglodyte = DP Rich Boy picture; cousins similar but not identical. Badge row spacing approved. | Author |
| 2026-10-01 | Triple-layer Team Aqua tilesets (Zelda House, Little Office, Gate Platinum, Brick Cafe) are imported with Porytiles in a separate chat that builds maps, not with the Claude-written converter. The converter and its four imports were reverted. Mock rooms rendered from the tiles were shown to check the style fit. | Author |
| 2026-10-01 | **All first-pick place names approved** ([region-names.md](region-names.md)): Briarwick, Gloomsby, Smeltham, Hoarfell, Gildhaven, Cragdale, Lingmoor, Waymeet, Hemlock Reach, Primrose Vale, Brinecombe, Ebbsworth, Kingsquay, Driftsands, Beaconmouth, Aldermere, Vesperhaven; landmarks Argent Peak, Mothwood, Slagwell Mine, Mirror Isle, The Pinnacle, Silverstrand, Echo Hollow. Gym order confirmed (Normal at Crestfall, Bug Briarwick, Ghost Gloomsby, Steel Smeltham, Ice Hoarfell, Flying Gildhaven, Poison Hemlock Reach, Fairy Primrose Vale, Water Beaconmouth). Route 34 is the post-league route. The first Goldsworth house is in Briarwick. | Author |
| 2026-10-01 | Hand-drawn region sketch ([region-sketch.md](region-sketch.md)). Route 1 is Hollowbrook to Crestfall, Route 2 is Crestfall to Wendlebury. **Crestfall is a town** (no Goldsworth house). | Author |
| 2026-09-29 | Goldsworths: Troglodyte's parents are in the tower. His grandfather, a kind old man who stepped down as family head for health reasons, lives in Hollowbrook's Goldsworth house. The Goldsworths can swear but nothing 4chan level. A city, not a town, has the skyscraper, and that city gets no separate house. Cities and towns are different (7 cities is an example, not final). | Author |
| 2026-09-29 | Goldsworth houses: cities only, with Hollowbrook (the grandfather's home town) as the one town exception. Troglodyte's parents are assholes out of obliviousness to the lower classes, not contempt like the rest of the family. | Author |
| 2026-09-29 | Troglodyte is in Hollowbrook to meet his grandfather, who was not there. He takes it out on Fennick and forces him to give him a Pokémon, random among the starters. | Author |
| 2026-09-29 | Troglodyte starts contemptuous and can change to oblivious and confused after certain undecided story points. The story path is undecided; the Goldsworths are one of the obstacles. | Author |
| 2026-09-29 | Four starters. Troglodyte takes one of the three on show at random, then Fennick reveals the fourth as an apology to the player, who picks from the rest. Species undecided until the hometown map, lab and houses are done. | Author |
| 2026-09-29 | No real animals in the game: the town's ambient creatures are common Normal-type Pokémon (hens dropped). The family does not know where the grandfather was when Troglodyte came; post-game, he was meeting the previous region's Champion, an old friend. Fennick's name for Troglodyte (BEAUREGARD) approved. | Author |
| 2026-09-29 | Hollowbrook dialogue approved except for edits: the bench old man is one text, the grandfather's name is '???' until the League is beaten, and after the League he thanks the player for setting Troglodyte straight. | Author |
| 2026-09-29 | Grandfather's name is Gatsby Goldsworth (hidden until the League is beaten); the door note is signed 'GG' and stays until the post-game. He sits outside the house after the lab scene, is gone after the first badge, and is back only in the post-game. | Author |
| 2026-09-29 | Badge 1 is the STANDARD BADGE. Crestfall's gym has 2 gym trainers. Greta is young, rising quickly in the gym hierarchy, and a tad sassy but nice (replacing 'retired farmer'). | Author |
| 2026-09-30 | No IVs or EVs on any trainer, gym leader, Elite Four member or the Champion: they belong to the player only. | Author |
| 2026-09-30 | Troglodyte's first battle is right outside the lab, with one Pokémon (his random starter). | Author |
| 2026-09-29 | Fly-town hooks (A-prime) may be applied. Applied by the other session, table still empty. | Author |
| 2026-09-29 | New trainer card with the 9-badge strip looks good. Badge art palette question settled in the other session. | Author |
| 2026-09-29 | Repo created as a fresh start on pokeemerald-expansion. Scope fixed at 18 towns, 33 routes, 9 gyms, Elite Four, post-game. | Author |
