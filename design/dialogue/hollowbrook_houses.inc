@ Hollowbrook HOUSES dialogue DRAFT: the neighbour's house and the player's house extras.
@ Status: PROPOSED, not wired into any map. Companion to hollowbrook.inc (no label here repeats one there).
@ Check widths: python3 design/tools/dialogue_check.py design/dialogue/hollowbrook_houses.inc
@ Pokemon only, no real animals. Nobody here swears (only Goldsworths do). Single curly quotes for speech.
@ 'Before' = before the lab scene. 'After' = after the player has a starter.
@ Starter variants: the player's species has not been decided (the author picks later), so the text buffers it in
@ {STR_VAR_1} (bufferspeciesname from the var holding the player's starter). The three variants are kept as
@ separate labels so each can be rewritten once the species exist: A, B, C = the three on-show balls in order.
@ Stand-ins until then are Treecko (A), Torchic (B), Mudkip (C). Pick the label with a 'switch' on VAR_STARTER_MON.

@ ===================================================================
@ THE NEIGHBOUR'S HOUSE (three NPCs, next door to the player)
@ ===================================================================

@ Neighbour, a cheerful woman at the table. Before.
Hollowbrook_Text_NeighbourBefore::
	.string "Oh, hello, dear! Your mother\n"
	.string "says you're off to the lab.\p"
	.string "Bring back a POKéMON. A nice,\n"
	.string "quiet one. Mine aren't.$"

@ After, generic.
Hollowbrook_Text_NeighbourAfter::
	.string "A POKéMON of your own! Your\n"
	.string "mother will never stop talking.\p"
	.string "Not that she ever started.\n"
	.string "...Well, she did. A bit.$"

@ After, starter variants (short remark on the player's Pokemon).
Hollowbrook_Text_NeighbourStarterA::
	.string "Is that a {STR_VAR_1}? Gorgeous.\n"
	.string "It has a very trustworthy look.\p"
	.string "Mine have never had one of\n"
	.string "those. Mine are far too busy.$"

Hollowbrook_Text_NeighbourStarterB::
	.string "Is that a {STR_VAR_1}? How bold.\n"
	.string "Keep it away from the curtains.\p"
	.string "And away from the soup.\n"
	.string "Your mother's soup is sacred.$"

Hollowbrook_Text_NeighbourStarterC::
	.string "Is that a {STR_VAR_1}? Lovely.\n"
	.string "Very calm. You'll need that.\p"
	.string "It must be nice to have one\n"
	.string "around that stays put.$"

@ Neighbour's husband, reading. Before and after in one text.
Hollowbrook_Text_NeighbourHusband::
	.string "I'm reading about the Goldsworth\n"
	.string "family. It's a very long book.\p"
	.string "I'm on the chapter about their\n"
	.string "boats. They have a lot of boats.$"

@ Neighbour's child. Before.
Hollowbrook_Text_NeighbourKidBefore::
	.string "You're going to the lab? Can I\n"
	.string "come? I won't touch anything.\p"
	.string "...I'll touch one thing.$"

@ Neighbour's child. After.
Hollowbrook_Text_NeighbourKidAfter::
	.string "Show me your POKéMON! Please!\n"
	.string "Just a little look!\p"
	.string "When I'm a trainer, mine will\n"
	.string "be bigger. And louder.$"

@ The family's Pokemon, an interactable. A common Normal type stand-in (SKITTY).
Hollowbrook_Text_NeighbourPokemon::
	.string "SKITTY is chasing its own tail\n"
	.string "in a slow, serious circle.\p"
	.string "It stops. It looks at you. It\n"
	.string "starts again. Nothing is wrong.\p"
	.string "SKITTY: Nyaa!$"

@ Neighbour's bookshelf.
Hollowbrook_Text_NeighbourBookshelf::
	.string "A shelf full of cookbooks.\n"
	.string "Every page is stained.\p"
	.string "The stains are labelled.$"

@ ===================================================================
@ THE PLAYER'S HOUSE: extras (Mom is in hollowbrook.inc)
@ ===================================================================

@ TV, before the lab scene.
Hollowbrook_Text_PlayerTVBefore::
	.string "A show is on about a rich man\n"
	.string "who lost his yacht.\p"
	.string "He was found soon after. It was\n"
	.string "parked in the wrong bay.$"

@ TV, after the player has a starter.
Hollowbrook_Text_PlayerTVAfter::
	.string "The news: ‘A young man in a very\n"
	.string "clean coat has reportedly made\l"
	.string "a scene at a local lab.’\p"
	.string "They show a blurry photo.\n"
	.string "It is definitely him.$"

@ Bookshelf.
Hollowbrook_Text_PlayerBookshelf::
	.string "Your shelf. Mostly old trainer\n"
	.string "handbooks and a ‘how to lose\l"
	.string "gracefully’ pamphlet.\p"
	.string "Nobody in this house has read\n"
	.string "the pamphlet.$"

@ Fridge, before.
Hollowbrook_Text_PlayerFridgeBefore::
	.string "The fridge holds a pot of soup,\n"
	.string "a jar of pickles and a note.\p"
	.string "Note: ‘Eat something before\n"
	.string "you go. Yes, you.’$"

@ Fridge, after.
Hollowbrook_Text_PlayerFridgeAfter::
	.string "Soup, pickles and a fresh note.\n"
	.string "‘Bring your POKéMON something\l"
	.string "too. They look thin.’$"

@ A house Pokemon, an interactable (before: mom's ZIGZAGOON, asleep by the stove).
Hollowbrook_Text_PlayerHousePokemonBefore::
	.string "ZIGZAGOON is asleep by the\n"
	.string "stove. It is snoring.\p"
	.string "It looks like a rug that\n"
	.string "has made some choices.$"

@ After the player has a starter: it reacts to the new Pokemon.
Hollowbrook_Text_PlayerHousePokemonAfter::
	.string "ZIGZAGOON sniffs at your new\n"
	.string "POKéMON. A long, hard look.\p"
	.string "It goes back to sleep. Your\n"
	.string "POKéMON has been approved.$"

@ After, starter variants (the house Pokemon notices the species).
Hollowbrook_Text_PlayerHouseStarterA::
	.string "ZIGZAGOON sniffs at your {STR_VAR_1}.\n"
	.string "The {STR_VAR_1} stares back,\l"
	.string "unblinking. ZIGZAGOON yields.\p"
	.string "It was a tense moment.$"

Hollowbrook_Text_PlayerHouseStarterB::
	.string "ZIGZAGOON sniffs at your {STR_VAR_1}.\n"
	.string "It backs away from the warm\l"
	.string "glow and keeps a safe distance.\p"
	.string "You can respect that.$"

Hollowbrook_Text_PlayerHouseStarterC::
	.string "ZIGZAGOON sniffs at your {STR_VAR_1}.\n"
	.string "The {STR_VAR_1} splashes it\l"
	.string "gently. ZIGZAGOON does not mind.\p"
	.string "It has been meaning to wash.$"

@ ===================================================================
@ ADDED 2026-10-01: NEIGHBOUR'S HOUSE AFTER THE FIRST BADGE (STANDARD BADGE, FLAG_BADGE01_GET)
@ ===================================================================

Hollowbrook_Text_NeighbourAfterBadge::
	.string "A badge, dear? Your mother told\n"
	.string "me ten minutes before you did.\p"
	.string "She tells me everything. It is\n"
	.string "a lot of everything.$"

Hollowbrook_Text_NeighbourHusbandAfterBadge::
	.string "I'm still on the Goldsworth\n"
	.string "boats. Page four hundred.\p"
	.string "There's a chapter called\n"
	.string "‘Why We Do Not Swim.’$"

Hollowbrook_Text_NeighbourKidAfterBadge::
	.string "You've got a badge! Is it\n"
	.string "heavy? Can I hold it?\p"
	.string "...Can I hold it for just one\n"
	.string "second? I'll give it back.$"

Hollowbrook_Text_NeighbourPokemonAfterBadge::
	.string "SKITTY wears a ribbon now.\n"
	.string "It looks like it won something.\p"
	.string "SKITTY: Mew!$"

Hollowbrook_Text_PlayerTVAfterBadge::
	.string "The news: ‘Local trainer wins\n"
	.string "gym badge. A rich family is\l"
	.string "said to be very embarrassed.’\p"
	.string "They cut to a clean coat\n"
	.string "stomping out of a gym.$"
