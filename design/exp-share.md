# Exp. Share (Gen 6+ style)

Status: config BUILT 2026-10-08 (author: 'better Exp. Share'). **Nothing hands the item to the player yet; who gives it is an open question.**

## What changed

| Switch | Value | Effect |
|---|---|---|
| `I_EXP_SHARE_ITEM` (`include/config/item.h`) | `GEN_6` | Exp. Share becomes a **key item**. Using it from the bag (or SELECT when registered) switches it on or off |
| `I_EXP_SHARE_FLAG` (`include/config/item.h`) | `FLAG_SYS_EXP_SHARE_ON` (0x882, was `FLAG_UNUSED_0x882`) | While set, **the whole party gains Exp**, not only the Pokémon that fought |
| `B_SPLIT_EXP`, `B_EXP_CATCH`, `B_TRAINER_EXP_MULTIPLIER` | already `GEN_LATEST` | Gen 6+ rules: each participant gets full Exp; catching also gives Exp; trainer battles are not 1.5x |

The flag is saved and starts clear (off).

## Tests (mGBA, 2026-10-08)

| Check | Result |
|---|---|
| Item goes to the **Key Items** pocket with the Gen 6 description | Pass |
| Using it from the bag shows 'The Exp. Share has been turned on / off' and toggles | Pass (messages seen; Exp actually shared in a battle not checked) |

## Getting the item (PROPOSED)

The item is `ITEM_EXP_SHARE`. Any script gives it with `giveitem ITEM_EXP_SHARE`. Candidates, none built:

- **Fennick**, after the starter choice (Gen 6 convention: the professor hands it over). Inside the key lab scene, so it needs the author's yes (rule 10).
- **Mom**, in the Running Shoes scene.
- **The Route 1 guide**, with the Journal (an ordinary NPC, but he would then give three things).
- **Debug menu** (Give item) for testing.

Vanilla only gave it in Hoenn (Devon Corp 3F) and in FRLG (Route 15), neither of which a Veldris map reaches.

## Level cap note

`src/caps.c` has a level cap plan (off). An always-on Exp. Share speeds up levelling, so the cap, when it is switched on, matters more. See `design/engine-limits.md`.
