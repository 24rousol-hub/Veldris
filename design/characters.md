# Characters

Only the facts marked **(author)** come from the author. Everything else is **PROPOSED**.

## Player

- Silent protagonist. Name is chosen at the start. **(PROPOSED)** Dialogue choices are allowed to be petty.
- Sole motivation: humiliate Troglodyte. **(author)**

## Troglodyte (Beauregard Goldsworth IV)  **(author: concept)**

- Sheltered and mediocre rival. **(author)**
- Rich parents who keep trying elaborate gym sabotage schemes that fail. **(author)**
- Voice (PROPOSED): pompous, entitled and sheltered, never quite understands why he lost. Refers to his family and their money. He is a Goldsworth, so he may swear a little (author). Whether his attitude to ordinary people is his parents' obliviousness or the wider family's contempt is open decision 13 in [game-bible.md](game-bible.md).
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

**Author notes (2026-09-29), in the author's words:**
- Every single city will have a Goldsworth house in it. Since they are uber rich they will have a skyscraper in one of the cities as their business. Make them a bunch of rich frat guys that are assholes.
- Troglodyte's parents are in the tower. His grandfather is actually a kind old man who was forced to step down from family head due to health issues, and you can find him in your home town in the Goldsworth house, living out his retirement.
- The Goldsworths can swear, but nothing 4chan level.
- A city has the skyscraper, not a town: there is a distinct difference, and there may be 7 cities with the rest towns (7 is an example, not final). The skyscraper's city does not also get a house.
- Towns do not get a house: Hollowbrook is the exception, because it is the grandfather's home town.
- Troglodyte's parents are assholes, but not on purpose like the rest of the family. They live in luxury and do not understand the lower classes. They do not dislike them, unlike the rest of the family, who do.

**Taken as fixed (author):**
- The Goldsworths are rich frat guys who are assholes, with one exception: the grandfather. The parents are a different kind of asshole (below).
- A Goldsworth house in every city, and Hollowbrook, the grandfather's home town, is the one exception: it is a town with a house. The other towns get none.
- The skyscraper is the family business, in one city, and Troglodyte's parents are in it. That city has no separate house.
- The Goldsworths may swear, mildly.

**PROPOSED (my reading, easy to change):**
- The parents run the business from the tower and now head the family, since the grandfather stepped down. Whether they also live there is not said.
- Names TBD. Troglodyte is 'IV', so the naming line would put his father at III and his grandfather at II (a possible hook, not decided).
- Voice of the wider family (the frat guys): loud, entitled, actively contemptuous of the lower classes, still incompetent, and they swear a little. The humour lands on them and never on innocent townsfolk. The limits are in [dialogue-style.md](dialogue-style.md).
- Overworld sprites: the `rich_boy` family in [asset-inventory.md](asset-inventory.md) fits the younger ones, picked per NPC when the houses are built.
- The houses and the skyscraper: see 'Goldsworth presence' in [story-outline.md](story-outline.md) and [map-plan.md](map-plan.md).
- Their schemes drive the plot: [story-outline.md](story-outline.md).

### The grandfather (author: concept)

- A kind old man, the former head of the Goldsworth family, forced to step down because of his health. Retired, and living in the Goldsworth house in the player's home town (Hollowbrook).
- He is the warm exception in a family of assholes, and the humour never lands on him (PROPOSED). His voice is gentle and dignified, with no swearing (PROPOSED).
- He is the first Goldsworth the player can meet in person (PROPOSED). What he says and does in the story is TBD by the author.
- Name TBD.

### Troglodyte's parents

- They are in the Goldsworth tower, in one of the cities (author). What the player does there is TBD.
- **Assholes by obliviousness, not by contempt (author).** They live in luxury and do not understand the lower classes. Unlike the rest of the family they do not dislike ordinary people. They just have no idea how those people live.
- Voice (PROPOSED): well-meaning and patronising, sure that money solves things, baffled when it does not. Their schemes come from not understanding what a gym or a town actually is. The humour lands on the obliviousness, not on cruelty.
- Names TBD.

## Trainer constants

Every trainer constant used by the hack is recorded here when it is added.

| Constant | Who | Where | Status |
|---|---|---|---|
| `TRAINER_CRESTFALL_GRETA` | Greta, gym 1 leader | Crestfall gym (TBD) | PROPOSED, not yet added |
