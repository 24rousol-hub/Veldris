# Journal (key item)

Status: BUILT 2026-10-08 at the author's request ('like the journal thing'). **All Journal wording, the hint rows and the giver are PROPOSED** until the author approves them.

## What it is

`ITEM_JOURNAL`, the old `ITEM_OLD_SEA_MAP` slot (id 731), Key Items pocket. Use it from the bag (USE) or press SELECT after REGISTER. It prints three one-box pages:

1. **Badges** of 9 (`GetBadgeCount()`, which reads the badge table).
2. **Next goal**, a one-line hint picked by badge count. One row per gym town, in `data/scripts/veldris_journal.inc` (`Veldris_Journal_Text_Hint0` to `Hint9`, plus a post-game row once `FLAG_SYS_GAME_CLEAR` is set). With 0 badges and `VAR_HOLLOWBROOK_STATE` below 3 it says to go to the lab.
3. **TROGLODYTE tally**: how many of his fights the player has won ('has not lost to you yet', 'once. Officially. In writing.', 'N times. Officially.').

## No flags, no vars

It claims nothing. It reads the badge flags, the trainer-defeated flags of the TROGLODYTE ids (0x500 + id: 0x708 and 0x709 today), `FLAG_SYS_GAME_CLEAR` and `VAR_HOLLOWBROOK_STATE`, and hands two numbers to the script in the volatile `VAR_0x8004` / `VAR_0x8005` (never saved). 'Journal already given' is `checkitem ITEM_JOURNAL`, which is safe because a key item cannot be tossed.

## Why the Old Sea Map slot

| Candidate | Verdict |
|---|---|
| **Old Sea Map** | **Used.** Referenced only by the ferry menu, a Mystery Gift script, the Hoenn Lilycove Harbor script and an unbuilt FRLG map, none of which a Veldris map can reach. Its parchment icon is the closest to a notebook |
| Eon Ticket | Tangled: record mixing, a daily special, the cable club, `.secondaryId = 1` |
| Mystic / Aurora Ticket | Free too. Kept for a possible ferry (Kingsquay) or a plot item |
| New item id | Not needed, no id spent |

The constant `ITEM_OLD_SEA_MAP` stays (other files use it); `ITEM_JOURNAL` is an alias next to it. If an 'old sea map' is ever wanted as a plot item, move the Journal to the Mystic or Aurora slot the same way.

## How to maintain it

- **Add a TROGLODYTE fight:** add one `X(TRAINER_TROGLODYTE_<PLACE>)` row to `VELDRIS_TROGLODYTE_FIGHTS` in `include/veldris_journal.h`, in story order (`design/troglodyte-arc.md` lists eight fights). Nothing warns at compile time if a fight is forgotten. Script that fight with `trainerbattle_single` or `trainerbattle_no_intro`, **never `trainerbattle_earlyrival`**, which sets the defeated flag even when the player loses (the tally would count a loss as a win). Rematches that clear the trainer flag lower the count.
- **Change a hint:** edit `Veldris_Journal_Text_Hint<N>` (N = badges earned). The rows repeat the gym order and the gym-town pairing, both still PROPOSED in `gyms.md` and `region-names.md`; if either changes the rows go stale with no build error.
- **Text limits:** bag description is 3 lines of about 109 px (the bag box is 14 tiles wide); pages are 2 lines at 216 px (`python3 design/tools/dialogue_check.py data/scripts/veldris_journal.inc`).
- **Do not** put a `giveitem` or a std script in the middle of `Veldris_EventScript_Journal`: it relies on `VAR_0x8004` / `VAR_0x8005` surviving until the pages print.

## Where the player gets it (PROPOSED)

The **Route 1 guide**, right after the three POTIONs (an ordinary NPC, so no story-beat rule applies). If the bag was full or the save is older, talking to him again hands it over. Alternatives the author can pick, each one call to `Veldris_EventScript_GiveJournal`:

- **Mom**, after 'you have a POKéMON' (overlaps the Running Shoes scene, which could simply continue into it).
- **Fennick**, right after the starter choice. Best fit for 'field notes', but it sits inside the key lab scene, so it needs the author's yes first (rule 10).

## Code map

| Piece | Where |
|---|---|
| Item entry | `src/data/items.h` (`[ITEM_OLD_SEA_MAP]`, `ITEM_USE_FIELD`, `fieldUseFunc = ItemUseOutOfBattle_Journal`) |
| Use from bag or SELECT | `src/item_use.c` (`Task_OpenJournal`, `ItemUseOutOfBattle_Journal`, modelled on the Pokémon Box Link) |
| Script, pages, hints | `data/scripts/veldris_journal.inc` (hack-owned) |
| Numbers for the pages | `src/veldris_journal.c` `VeldrisJournal_FillVars`, list in `include/veldris_journal.h` (hack-owned) |
| Giver | `data/maps/VeldrisRoute1/scripts.inc` (`GuideJournal`) |

The item type must stay `ITEM_USE_FIELD`: `ITEM_USE_BAG_MENU` (the Town Map's type) indexes past the field-use table when the item is used from SELECT (`src/item_use.c`).

## Open questions for the author

1. Giver: Route 1 guide (built), Mom, or Fennick?
2. Name 'Journal', and spending the Old Sea Map slot on it?
3. Hint rows that touch the story: badge 1 says 'WENDLEBURY, then north to BRIARWICK' (hints the north road is shut), badge 2 assumes MOTHWOOD comes before GLOOMSBY (no design file says so), badge 9 says 'THE PINNACLE' and skips the Drowned Crown climax. Keep them vague, or react to story steps once those flags exist?
4. Are the gym towns in the hint rows final (still PROPOSED in `gyms.md`)?
5. Tally wording ('Officially.'), and whether to show 'N of 8' or hide the total.
6. Post-game row: a placeholder ('Nothing is listed. There is a lot of coast left to see.').
7. Icon: the parchment is kept. A hand-drawn notebook icon would need art, a `CREDITS.md` row and two more logged upstream lines.

## Tests (mGBA, headless, 2026-10-08)

| Check | Result |
|---|---|
| Item shows in Key Items as 'Journal' with the parchment icon; description fits 3 lines | Pass |
| USE from the bag: bag closes, three pages (badges, next goal, TROGLODYTE), controls released | Pass |
| REGISTER, then SELECT in the field: same pages, controls released | Pass |
| 0 badges, `VAR_HOLLOWBROOK_STATE` 0: lab row ('FENNICK's lab') | Pass |
| 3 badges: 'SMELTHAM' row; count reads '3 of 9' | Pass |
| TROGLODYTE tally: none ('has not lost to you yet') and one (flag 0x708 set: 'once. Officially. In writing.') | Pass |
| Route 1 guide gives the Journal after the POTIONs, then the repeat line, no second Journal | Pass (first talk and a repeat talk) |
| Tally at 2 or more, 9 badges, post-game row, bag-full second chance, a 7-letter wide player name | Not run |
| Losing a TROGLODYTE fight leaves the tally unchanged | Not run (fight 1 is scripted with `trainerbattle_no_intro`, which only sets the flag on a win) |
