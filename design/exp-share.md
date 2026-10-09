# Exp. Share (Gen 6+ style)

Status: config BUILT 2026-10-08 (author: 'better Exp. Share'). **2026-10-09 (author): the item is in the bag from the start and switched on by default, so nobody has to hand it over.**

## What changed

| Switch | Value | Effect |
|---|---|---|
| `I_EXP_SHARE_ITEM` (`include/config/item.h`) | `GEN_6` | Exp. Share becomes a **key item**. Using it from the bag (or SELECT when registered) switches it on or off |
| `I_EXP_SHARE_FLAG` (`include/config/item.h`) | `FLAG_SYS_EXP_SHARE_ON` (0x882, was `FLAG_UNUSED_0x882`) | While set, **the whole party gains Exp**, not only the Pokémon that fought |
| `B_SPLIT_EXP`, `B_EXP_CATCH`, `B_TRAINER_EXP_MULTIPLIER` | already `GEN_LATEST` | Gen 6+ rules: each participant gets full Exp; catching also gives Exp; trainer battles are not 1.5x |

The flag is saved. **New games start with it set (on) and the item in the Key Items pocket** (`VeldrisNewGameDefaults()` in `src/veldris_new_game.c`, called at the end of `NewGameInitData`). The player can still switch it off from the bag, and a key item cannot be tossed or sold.

## Tests (mGBA, 2026-10-08)

| Check | Result |
|---|---|
| Item goes to the **Key Items** pocket with the Gen 6 description | Pass |
| New game (2026-10-09, headless mGBA, via title-screen quickstart): the Exp. Share is already in the Key Items pocket, and using it says 'has been turned **off**', so the flag starts set | Pass |
| Using it from the bag shows 'The Exp. Share has been turned on / off' and toggles | Pass (messages seen; Exp actually shared in a battle not checked) |

## Getting the item

**Decided 2026-10-09: it is in the bag from the first frame** (author: 'exp can be in your bag by default and also on by default'). Nothing in the story hands it over, so there is no scene to maintain and the Fennick, Mom and Route 1 guide options are dropped. Vanilla only gave it in Hoenn (Devon Corp 3F) and in FRLG (Route 15), neither of which a Veldris map reaches. Debug preset 1 ('New game') puts the state back to exactly this (item in the bag, flag set).

Note for new-game testing: a save made **before** 2026-10-09 has neither the item nor the flag; give it with the debug menu (Give item) or start a new game.

## Level cap note

`src/caps.c` has a level cap plan (off). An always-on Exp. Share speeds up levelling, so the cap, when it is switched on, matters more. See `design/engine-limits.md`.
