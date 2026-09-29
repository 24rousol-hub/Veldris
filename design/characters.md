# Characters

Only the facts marked **(author)** come from the author. Everything else is **PROPOSED**.

## Player

- Silent protagonist. Name is chosen at the start. **(PROPOSED)** Dialogue choices are allowed to be petty.
- Sole motivation: humiliate Troglodyte. **(author)**

## Troglodyte (Beauregard Goldsworth IV)  **(author: concept)**

- Sheltered and mediocre rival. **(author)**
- Rich parents who keep trying elaborate gym sabotage schemes that fail. **(author)**
- Voice (PROPOSED): pompous, entitled, never quite understands why he lost. Refers to his parents and their money. Never swears.
- Team (PROPOSED): well-bred Pokémon, poorly trained. Strong on paper, tactically naive.
- In text, write **TROGLODYTE** literally. Do not use `{RIVAL}`: in this engine it expands to MAY or BRENDAN (`src/string_util.c`).

## Prof. Fennick  **(author: professor)**

- The professor who starts the player's journey.
- Replaces Prof. Birch in the intro. Intro text lives in `data/text/birch_speech.inc` (C-driven intro).
- Voice (PROPOSED): kindly, easily distracted, endlessly tolerant of the player's grudge.

## Greta  **(author: first gym leader, Normal type, retired farmer)**

- Gym 1, in Crestfall (assumed). Normal type. Retired farmer.
- Trainer constant: **`TRAINER_CRESTFALL_GRETA`** (`TRAINER_GRETA` is already taken). **(author)**
- Voice (PROPOSED): dry, unhurried, plain-spoken farm wisdom. Sees through the Goldsworths at once.

## The Goldsworths (Troglodyte's parents)

- Names TBD. **(PROPOSED)** Two people who mistake money for competence. Their schemes drive the plot. See [story-outline.md](story-outline.md).

## Trainer constants

Every trainer constant used by the hack is recorded here when it is added.

| Constant | Who | Where | Status |
|---|---|---|---|
| `TRAINER_CRESTFALL_GRETA` | Greta, gym 1 leader | Crestfall gym (TBD) | PROPOSED, not yet added |
