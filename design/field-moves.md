# Field moves without a move slot (BUILT 2026-10-08)

**Author rule (2026-10-08):** a field move works in the open world when (1) its **badge** is earned and (2) the party has a Pokémon that **knows the move or can learn it**. The Pokémon does not need to know it, so no move slot is spent. Examples named by the author: Flash for a dark cave, Sweet Scent to attract wild Pokémon, and all the water moves.

## What it covers

| Move | Needs badge | How the player uses it |
|---|---|---|
| Cut, Rock Smash, Strength | 1, 2, 4 | Press A on the tree, rock or boulder: the usual prompt appears. Cut also works from the party menu on cuttable grass |
| Surf | 5 | Press A facing water: 'Would you like to SURF?'. Also in the party menu while facing water |
| Waterfall, Dive | 8, 9 | Press A on a waterfall (while surfing) or deep water, as in vanilla |
| Flash | 3 | In a dark cave open the party menu, pick any Pokémon, choose **Flash** |
| Fly | 6 | Outdoors, party menu, any Pokémon, choose **Fly** (opens the town map) |
| Sweet Scent | none | Party menu, any Pokémon, choose **Sweet Scent** (listed only when a party member can learn it) |

**Not covered, on purpose:** Teleport and Dig (anyone could escape any cave for free), Milk Drink and Soft-Boiled (healing), Secret Power (no secret bases here), Rock Climb and Defog (switched off). They keep the vanilla rule: a Pokémon must know the move.

## 'Can learn' means

A non-egg Pokémon whose species is in the generated teachable list (TMs, HMs, tutors) **or** whose level-up learnset contains the move at any level (needed for Sweet Scent, which is neither a TM nor a tutor move). Egg moves do not count. A Pokémon that already knows the move always works and is shown as the user first. Otherwise the first learner in the party is the user: its picture, cry and name appear in the banner ('MUDKIP used SURF!'). Rough counts from this tree's data: 263 species can learn Cut, 249 Surf, 310 Flash, 353 Strength; 275 species learn no HM at all (so a team of those still needs a knower).

## How the party menu behaves

The field move is listed in **every** party member's menu, not just the learner's, when all of these hold: the badge is earned, a party member knows or can learn it, and it is usable right where the player stands (facing water, facing a tree, in an unlit cave, outdoors for Fly). Picking it makes the knower (else the first learner) the user. Pokémon that already know the move keep the vanilla entry and the vanilla 'cannot use here' messages. A hard cap keeps room for Switch, Item and Cancel, so the menu never overflows (vanilla maximum is 8 entries).

## Code (5 upstream files, all logged in [engine-edits.md](engine-edits.md))

- **New, hack-owned:** `src/veldris_field_moves.c` and `include/veldris_field_moves.h`. The set of moves is one line, `VELDRIS_COMPAT_FIELD_MOVES` (add or remove a `COMPAT_BIT(FIELD_MOVE_...)`).
- `src/scrcmd.c`: `ScrCmd_checkfieldmove` asks `FindMonForFieldMove`. This one function serves Cut, Rock Smash, Strength, Waterfall, Dive and Surf scripts.
- `src/field_player_avatar.c`: `PartyHasMonWithSurf` asks the same helper.
- `src/party_menu.c`: two hunks (list the extra entries; point the cursor slot at the real user before the move runs).
- `include/config/pokemon.h` `P_CAN_FORGET_HIDDEN_MOVE` TRUE and `include/config/battle.h` `B_CATCH_SWAP_CHECK_HMS` FALSE: HM moves can now be forgotten and a Pokémon that knows one can be boxed, since nobody has to keep them.

No new flags, vars, save fields, assets or text. A player who never picks a Pokémon that can learn a move simply gets the vanilla 'this tree looks like it can be CUT down' text.

## Checked in mGBA (2026-10-08, party Caterpie, Treecko, Mudkip, Oddish; nobody knew a field move)

| Check | Result |
|---|---|
| A on water, Mudkip is the learner | 'Would you like to SURF?', 'Mudkip used SURF!', player ends on the surf blob |
| A on a Cut tree, Treecko is the learner | prompt, 'Treecko used Cut!', Treecko banner, tree gone, walked through |
| Dark cave, party menu on Caterpie | Flash listed, Treecko banner, cave lit |
| Tall grass, party menu | Cut and Sweet Scent listed; Sweet Scent gave a red fade and a wild Wingull |
| Outdoors with a Pidgey | Fly listed, picking it opened 'FLY to where?' |
| Badges 1, 3 and 5 cleared | no Cut prompt, no Cut/Surf/Flash entries (only Sweet Scent, which has no badge) |
| Party of Caterpie and Magikarp (no learners) | vanilla tree text, party menu shows only Summary, Switch, Item, Cancel |
| A Pokémon that knows Fly, Cut, Rock Smash and Flash | exactly the vanilla four entries plus Summary, Switch, Item, Cancel (8), no duplicates |

**Not run:** Rock Smash, Strength, Waterfall and Dive individually (they go through the same `checkfieldmove` path as Cut and Surf), a completed Fly trip, and Sweet Scent with a Pokémon that knows it.

## Optional extras, not built

- **Press A in a dark cave to light it** (a yes/no prompt) instead of using the party menu: 2 more upstream files plus a small script. Ask if you want it.
- **Dig and Teleport** could join the set with one more line, but would become free escapes for everyone.
- One-word fix in `data/scripts/surf.inc` (`EventScript_CurrentTooFast` compares to `FALSE` instead of `PARTY_SIZE`); only matters if fast-current water is ever used.
- The PC refuses to release the last Pokémon that knows Surf or Dive (`src/pokemon_storage_system.c`); harmless but now misleading.
