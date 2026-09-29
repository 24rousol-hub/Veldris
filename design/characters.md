# Characters

Only the facts marked **(author)** come from the author. Everything else is **PROPOSED**.

## Player

- Silent protagonist. Name is chosen at the start. **(PROPOSED)** Dialogue choices are allowed to be petty.
- Sole motivation: humiliate Troglodyte. **(author)**

## Troglodyte (Beauregard Goldsworth IV)  **(author: concept)**

- Sheltered and mediocre rival. **(author)**
- Rich parents who keep trying elaborate gym sabotage schemes that fail. **(author)**
- Voice (PROPOSED, revised 2026-09-29 after the author's note on the Goldsworths below): frat-bro entitlement and contempt, pompous, never quite understands why he lost. Refers to his family and their money. Whether he swears is open decision 10 in [game-bible.md](game-bible.md).
- Team (PROPOSED): well-bred Pokémon, poorly trained. Strong on paper, tactically naive.
- First named in Prof. Fennick's intro as BEAUREGARD GOLDSWORTH IV (PROPOSED, see Prof. Fennick below).
- In text, write **TROGLODYTE** literally. Do not use `{RIVAL}`: in this engine it expands to MAY or BRENDAN (`src/string_util.c`).

## Prof. Fennick  **(author: professor)**

- The professor who starts the player's journey.
- Replaces Prof. Birch in the intro. Intro text lives in `data/text/birch_speech.inc` (C-driven intro).
- Voice (PROPOSED): kindly, easily distracted, endlessly tolerant of the player's grudge.
- **Intro drafted 2026-09-29** in `data/text/birch_speech.inc` (text only, labels unchanged). **Tone APPROVED by the author (2026-09-29).** Beats: he lost track of the time; 'Everyone calls me the POKéMON PROFESSOR. Except my hens.'; 'So you're PLAYER. Splendid. I'll remember that. Probably.'; and he asks the player to be polite to a boy named BEAUREGARD GOLDSWORTH IV, which seeds Troglodyte.
- FENNICK is written into the text directly (there is no placeholder for it).
- **Art still to do:** the intro portrait `graphics/birch_speech/birch.png` (64x64, 16 colours) still shows Birch. His overworld sprite could be RavePossum's `prof_birch` (see [asset-inventory.md](asset-inventory.md)).

## Greta  **(author: first gym leader, Normal type, retired farmer)**

- Gym 1, in Crestfall (assumed). Normal type. Retired farmer.
- Trainer constant: **`TRAINER_CRESTFALL_GRETA`** (`TRAINER_GRETA` is already taken). **(author)**
- Voice (PROPOSED): dry, unhurried, plain-spoken farm wisdom. Sees through the Goldsworths at once.

## The Goldsworths (Troglodyte's family)

**Author note (2026-09-29), in the author's words:** every single city will have a Goldsworth house in it. Since they are uber rich they will have a skyscraper in one of the cities as their business. Make them a bunch of rich frat guys that are assholes.

**Taken as fixed (author):**
- A Goldsworth house in every city.
- A Goldsworth skyscraper in one city, as the family business.
- The Goldsworths are rich frat guys who are assholes.

**PROPOSED (my reading, easy to change):**
- 'Them' means the whole family, not only the parents. The original brief said 'rich parents' stage the schemes, so it is open whether the parents are part of the frat crowd (old money who never left the fraternity) or the schemes are run by a wider clan of brothers, cousins and uncles. See open decision 9 in [game-bible.md](game-bible.md).
- Names TBD.
- 'Every city' means all 18 towns, the start town included (open decision 7). The skyscraper's town is TBD (open decision 8).
- Voice: loud, entitled, contemptuous of the locals, still incompetent. The humour lands on them and never on innocent townsfolk. Whether they swear is open decision 10.
- Overworld sprites: the `rich_boy` family in [asset-inventory.md](asset-inventory.md) fits, picked per NPC when the houses are built.
- The houses and the skyscraper: see 'Goldsworth presence' in [story-outline.md](story-outline.md) and [map-plan.md](map-plan.md).
- Their schemes drive the plot: [story-outline.md](story-outline.md).

## Trainer constants

Every trainer constant used by the hack is recorded here when it is added.

| Constant | Who | Where | Status |
|---|---|---|---|
| `TRAINER_CRESTFALL_GRETA` | Greta, gym 1 leader | Crestfall gym (TBD) | PROPOSED, not yet added |
