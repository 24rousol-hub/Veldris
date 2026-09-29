# Game bible

**Title:** Pokémon: Piss Off Troglodyte (short form: POT)
**Region:** Veldris
**Base:** pokeemerald-expansion (personal-use GBA ROM hack; the repo is public, the ROM is never committed)

## Pitch

The player has one reason to become Champion: to humiliate Troglodyte. His real name is Beauregard Goldsworth IV. He is a sheltered, mediocre rival whose rich parents keep staging elaborate schemes to sabotage the gyms in his way. Every scheme fails. The League is just what happens to be at the end of the road.

## Pillars

1. **The motive is petty and personal.** The player never says they want to save anything. They want Troglodyte to lose, in public, again.
2. **The schemes always fail.** Each gym has a Goldsworth scheme (see [story-outline.md](story-outline.md)). It is built up, it is obviously flawed, it collapses, and Troglodyte loses the battle that follows.
3. **Troglodyte is mediocre, not evil.** He is coddled and out of his depth. He loses because he never had to learn, not because he is a monster. The humour lands on him and his parents, never on the townsfolk.
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
3. Gyms 2 to 9 in order, each with its own Goldsworth scheme.
4. Elite Four, then the Champion.
5. Post-game.

## Who does what

- **The author** builds and edits maps in Porymap.
- **Claude** writes scripts, events, warps, trainers and dialogue, and keeps these docs current.
- Maps are fragile. No script generates map files. Claude does not hand-edit map block data or tilesets.

## Open decisions

These need the author's call. None blocks the first 3 towns.

1. **Nine gyms versus eight badges.** The engine is built for 8 badges: `NUM_BADGES` is derived from `FLAG_BADGE08_GET`, and `gBadgeFlags`, the trainer card, the main menu and the shop criteria all loop over that range. The 9th slot cannot sit next to the others because `SYSTEM_FLAGS + 0xF` is already `FLAG_VISITED_LITTLEROOT_TOWN`. The list of places is in [engine-limits.md](engine-limits.md). Options: (a) extend the engine to 9 badges (multi-file edit plus trainer card art), or (b) 8 real badges and the 9th gym gives something else, such as a key item and a flag the League gate checks. Not blocking until gym 8. Needs a decision before we build gym 8. **Direction (author, 2026-09-29):** first look at how public ROM hacks with more than 8 badges did it, and consider our own badge case with our own badge art so badges can be mixed and matched instead of using Emerald's defaults. Research and a written plan come first (`design/badges.md`), with no engine edits until the author approves.
2. **Who is the Champion?** Troglodyte, or someone else?
3. **Player and rival replacement.** Emerald's rival is May or Brendan. Troglodyte replaces them, which touches rival scripts and sprites. Which parts of the Hoenn intro and rival flow do we keep?
4. ~~**Names of towns 1 to 3.**~~ **Resolved (author, 2026-09-29):** Hollowbrook and Wendlebury approved. Crestfall comes from the author's trainer constant `TRAINER_CRESTFALL_GRETA` and is the first gym town. Marrow Bay (the bay) is still a placeholder.
5. ~~**Region map style.**~~ **Resolved (author, 2026-09-29):** the vanilla GBA town-map look. See [region-map.md](region-map.md).
6. **Trainer slots.** Only 9 new trainer IDs fit before trainer flag space overflows (`TRAINERS_COUNT` 855, `MAX_TRAINERS_COUNT` 864, upstream's own note in `include/constants/opponents.h`). A hack with a gym, Elite Four and trainers on 33 routes needs hundreds. Options: (a) reuse and rename vanilla Hoenn or FRLG trainer IDs you no longer need, or (b) raise `MAX_TRAINERS_COUNT`. Measured save headroom is about 176 bytes (roughly 1,400 flags), so a few hundred more trainers fit. It shifts every system and daily flag, which is fine on a fresh start. Untested. `TRAINER_CRESTFALL_GRETA` is the first to need a slot. Not blocking until the first new trainer is added.

## Decision log

| Date | Decision | Who |
|---|---|---|
| 2026-09-29 | Town names Hollowbrook and Wendlebury approved. Vanilla GBA town-map look approved for the region map. | Author |
| 2026-09-29 | Badges: research public hacks with more than 8 badges, and consider a custom badge case with our own art. Plan first, no engine edits yet. | Author |
| 2026-09-29 | Fly towns: the author left it to the assistant ("whatever is best for the future"). Chosen: approach A-prime, see [region-map.md](region-map.md). | Assistant, on the author's instruction |
| 2026-09-29 | Region map shape approved. "Zoom out" means denser tile art (more detail in the same space), not more cells. | Author |
| 2026-09-29 | Prof. Fennick's intro tone approved (`data/text/birch_speech.inc`), including the line seeding Troglodyte's full name. | Author |
| 2026-09-29 | Maps: a mix of Project Palladium maps (Team Aqua repo, traced in Porymap as references) and vanilla bases. See [map-plan.md](map-plan.md). | Author |
| 2026-09-29 | Repo created as a fresh start on pokeemerald-expansion. Scope fixed at 18 towns, 33 routes, 9 gyms, Elite Four, post-game. | Author |
