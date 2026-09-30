# Characters

Only the facts marked **(author)** come from the author. Everything else is **PROPOSED**.

## Player

- Silent protagonist. Name is chosen at the start. **(PROPOSED)** Dialogue choices are allowed to be petty.
- Sole motivation: humiliate Troglodyte. **(author)**

## Troglodyte (Beauregard Goldsworth IV)  **(author: concept)**

- Sheltered and mediocre rival. **(author)**
- Rich parents who keep trying elaborate gym sabotage schemes that fail. **(author)**
- **Attitude and arc (author, 2026-09-29):** he starts out **contemptuous**, like the wider family. After certain story points he can change to **oblivious and confused**, like his parents. Which story points is undecided, because the story's path is not decided yet. All that is fixed is that the Goldsworths are one of the obstacles.
- Voice (PROPOSED): pompous and entitled, never quite understands why he lost. Refers to his family and their money. He is a Goldsworth, so he may swear a little (author). Early on he looks down on ordinary people on purpose. If the arc happens, later he is bewildered that the world does not work the way he was told. Write his lines so either mode can be swapped in.
- **Why he is in Hollowbrook (author, 2026-09-29):** he came to meet his grandfather, who was not there at the time. He takes his frustration out on Prof. Fennick and forces him to give him a Pokémon.
- **His starter is random among the three on show (author).** He never gets the fourth, which Fennick reveals afterwards. Mechanics and cost: 'Starters and the lab scene' in [story-outline.md](story-outline.md).
- Team (PROPOSED): well-bred Pokémon, poorly trained. Strong on paper, tactically naive.
- First named in Prof. Fennick's intro as BEAUREGARD GOLDSWORTH IV (APPROVED by the author with the intro tone, see Prof. Fennick below).
- In text, write **TROGLODYTE** literally. Do not use `{RIVAL}`: in this engine it expands to MAY or BRENDAN (`src/string_util.c`).

## Prof. Fennick  **(author: professor)**

- The professor who starts the player's journey.
- Replaces Prof. Birch in the intro. Intro text lives in `data/text/birch_speech.inc` (C-driven intro).
- Voice (PROPOSED): kindly, easily distracted, endlessly tolerant of the player's grudge.
- **Troglodyte bullies him into handing over a Pokémon (author, 2026-09-29).** Fennick goes along with it. He then apologises to the player by revealing a fourth starter, and the player picks from what is left (author). That is the player's first look at Troglodyte, and a reason for the grudge (PROPOSED).
- **Intro drafted 2026-09-29** in `data/text/birch_speech.inc` (text only, labels unchanged). **Tone APPROVED by the author (2026-09-29).** Beats: he lost track of the time; 'Everyone calls me the POKéMON PROFESSOR. Except my ZIGZAGOON.' (hens were dropped on 2026-09-29: the game uses Pokémon only); 'So you're PLAYER. Splendid. I'll remember that. Probably.'; and he asks the player to be polite to a boy named BEAUREGARD GOLDSWORTH IV, which seeds Troglodyte.
- FENNICK is written into the text directly (there is no placeholder for it).
- **Art still to do:** the intro portrait `graphics/birch_speech/birch.png` (64x64, 16 colours) still shows Birch. His overworld sprite could be RavePossum's `prof_birch` (see [asset-inventory.md](asset-inventory.md)).

## Greta  **(author: first gym leader, Normal type, retired farmer)**

- Gym 1, in Crestfall. Normal type. Retired farmer.
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
- Troglodyte came to Hollowbrook to meet him and he was not there at the time (author). **The family does not know where he was (author).** **Post-game payoff (author): he was meeting the previous region's Champion, an old friend of his.** Until then he stays vague about it. Before the lab scene his door is locked with a note on it; afterwards he is home (PROPOSED). What else he says and does is TBD by the author.
- **Name hidden (author, 2026-09-29): in game he is only '???' until the player beats the League.** Nobody says his name before then, and his door note is signed '???'. The real name is not chosen yet.
- **After the League (author):** he is grateful that the player set Troglodyte straight, and reveals his name. Drafted in [dialogue/hollowbrook.inc](dialogue/hollowbrook.inc) (PROPOSED wording, triggered by `FLAG_SYS_GAME_CLEAR`, the Hall of Fame flag). What the reveal means for the story is the author's.

### Lab assistants (PROPOSED)

Two aides in Fennick's lab, drafted in [dialogue/hollowbrook.inc](dialogue/hollowbrook.inc): one nervous, one deadpan. The deadpan one says the staff call Troglodyte 'TROGLODYTE' behind his back, which seeds the nickname. Unnamed for now.

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
