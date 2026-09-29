# Game bible

**Title:** Pokémon: Piss Off Troglodyte (short form: POT)
**Region:** Veldris
**Base:** pokeemerald-expansion (personal-use GBA ROM hack; the repo is public, the ROM is never committed)

## Pitch

The player has one reason to become Champion: to humiliate Troglodyte. His real name is Beauregard Goldsworth IV. He is a sheltered, mediocre rival whose rich parents keep staging elaborate schemes to sabotage the gyms in his way. Every scheme fails. The League is just what happens to be at the end of the road.

**Author note (2026-09-29):** the Goldsworths are rich frat guys who are assholes. Every city has a Goldsworth house, and one city has their skyscraper business. Details and what is still open: [characters.md](characters.md), [story-outline.md](story-outline.md).

## Pillars

1. **The motive is petty and personal.** The player never says they want to save anything. They want Troglodyte to lose, in public, again.
2. **The schemes always fail.** Each gym has a Goldsworth scheme (see [story-outline.md](story-outline.md)). It is built up, it is obviously flawed, it collapses, and Troglodyte loses the battle that follows.
3. **Troglodyte is mediocre, not evil.** He is coddled and out of his depth. He loses because he never had to learn, not because he is a monster. The humour lands on him and his family, never on the townsfolk. *(Under review after the 2026-09-29 note on the Goldsworths: see open decision 10.)*
4. **The rest of Veldris is warm.** Gym leaders and locals are sincere and a bit weird. Greta is the model: a retired farmer who happens to be the best Normal-type trainer for miles.

## Scope (fixed by the author)

| Item | Count | Notes |
|---|---|---|
| Towns | 18 | List in [towns-and-routes.md](towns-and-routes.md) |
| Routes | 33 | Same file |
| Gyms | 9 | Gym 1 is Greta, Normal type. Others TBD. See open decision 1 (badges) |
| Elite Four | 4 members | TBD |
| Champion | not specified yet | See open decision 2 |
| Post-game | yes | Contents TBD |

## Progression skeleton (PROPOSED)

1. Intro (C-driven, `data/text/birch_speech.inc`), Prof. Fennick, starter.
2. First 3 towns and 3 routes, ending at gym 1 (Greta, Normal). Built first so all three can be flown between.
3. Gyms 2 to 9 in order, each with its own Goldsworth scheme. Every town has a Goldsworth house, and one has their skyscraper (PROPOSED details in [story-outline.md](story-outline.md)).
4. Elite Four, then the Champion.
5. Post-game.

## Who does what

- **The author** builds and edits maps in Porymap.
- **Claude** writes scripts, events, warps, trainers and dialogue, and keeps these docs current.
- Maps are fragile. No script generates map files. Claude does not hand-edit map block data or tilesets.

## Open decisions

These need the author's call. None blocks the first 3 towns.

1. **Nine gyms versus eight badges. RESOLVED 2026-09-29:** the engine now supports 9 badges through a data-driven table (option a). Details, limits and what is untested are in [badges.md](badges.md). Badge art is a placeholder set to be replaced by outsourced art.
2. **Who is the Champion?** Troglodyte, or someone else?
3. **Player and rival replacement.** Emerald's rival is May or Brendan. Troglodyte replaces them, which touches rival scripts and sprites. Which parts of the Hoenn intro and rival flow do we keep?
4. ~~**Names of towns 1 to 3.**~~ **Resolved (author, 2026-09-29):** Hollowbrook and Wendlebury approved. Crestfall comes from the author's trainer constant `TRAINER_CRESTFALL_GRETA` and is the first gym town. Marrow Bay (the bay) is still a placeholder.
5. ~~**Region map style.**~~ **Resolved (author, 2026-09-29):** the vanilla GBA town-map look. See [region-map.md](region-map.md).
6. **Trainer slots.** Only 9 new trainer IDs fit before trainer flag space overflows (`TRAINERS_COUNT` 855, `MAX_TRAINERS_COUNT` 864, upstream's own note in `include/constants/opponents.h`). A hack with a gym, Elite Four and trainers on 33 routes needs hundreds. Options: (a) reuse and rename vanilla Hoenn or FRLG trainer IDs you no longer need, or (b) raise `MAX_TRAINERS_COUNT`. Measured save headroom is about 176 bytes (roughly 1,400 flags), so a few hundred more trainers fit. It shifts every system and daily flag, which is fine on a fresh start. Untested. `TRAINER_CRESTFALL_GRETA` is the first to need a slot. Not blocking until the first new trainer is added.
7. **Does 'every city' mean all 18 towns?** The author said 'every single city'. The docs have no city/town split. Recorded as all 18, the start town included (Hollowbrook's house is then where the player first sees Goldsworth money).
8. **Which town has the skyscraper?** And does that town also get a house (17 or 18 houses)? See 'Goldsworth presence' in [story-outline.md](story-outline.md). The tower exterior needs new art or a compromise ([map-plan.md](map-plan.md)).
9. **Do Troglodyte's parents stay?** The author said 'them': make them a bunch of rich frat guys. Are the parents frat guys too, or does a wider family of brothers, cousins and uncles run the schemes?
10. **Tone limits for the Goldsworths.** The current docs say 'never swears' and 'not evil'. Can they swear now, and how cruel may they be (never to innocent townsfolk is assumed)? Until answered the old limits in [dialogue-style.md](dialogue-style.md) stay.
11. **Goldsworth house fights.** Only 9 trainer ids are spare and the 9 gym leaders use them all (decision 6). Proposed rule: the houses are NPC-only, with no trainer ids. If a house should have a fight, use one shared 'Goldsworth family' id and reset its flag with `cleartrainerflag` for repeats.

## Decision log

| Date | Decision | Who |
|---|---|---|
| 2026-09-29 | Town names Hollowbrook and Wendlebury approved. Vanilla GBA town-map look approved for the region map. | Author |
| 2026-09-29 | Badges: research public hacks with more than 8 badges, and consider a custom badge case with our own art. Plan first, no engine edits yet. | Author |
| 2026-09-29 | Fly towns: the author left it to the assistant ("whatever is best for the future"). Chosen: approach A-prime, see [region-map.md](region-map.md). | Assistant, on the author's instruction |
| 2026-09-29 | 9 gyms, Elite Four and Champion. Real 9th badge via a data-driven badge table; badge art to be outsourced (asset repo fork used for stand-ins). Assistant told to use its best judgment. | Author |
| 2026-09-29 | Region map shape approved. "Zoom out" means denser tile art (more detail in the same space), not more cells. | Author |
| 2026-09-29 | Prof. Fennick's intro tone approved (`data/text/birch_speech.inc`), including the line seeding Troglodyte's full name. | Author |
| 2026-09-29 | Maps: a mix of Project Palladium maps (Team Aqua repo, traced in Porymap as references) and vanilla bases. See [map-plan.md](map-plan.md). | Author |
| 2026-09-29 | Palladium and vanilla pairings for towns 1 to 3 approved. Hollowbrook is the first map the author builds. | Author |
| 2026-09-29 | Goldsworths: a house in every city, a skyscraper in one city as their business, and they are rich frat guys who are assholes (author's note; the reading of 'them' is open decision 9). | Author |
| 2026-09-29 | Fly-town hooks (A-prime) may be applied. Applied by the other session, table still empty. | Author |
| 2026-09-29 | New trainer card with the 9-badge strip looks good. Badge art palette question settled in the other session. | Author |
| 2026-09-29 | Repo created as a fresh start on pokeemerald-expansion. Scope fixed at 18 towns, 33 routes, 9 gyms, Elite Four, post-game. | Author |
