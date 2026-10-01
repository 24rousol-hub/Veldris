@ Hollowbrook_NeighboursHouse: the neighbour, her husband, their kid and their SKITTY.
@ Built from design/dialogue/hollowbrook_houses.inc.

Hollowbrook_NeighboursHouse_MapScripts::
	.byte 0

Hollowbrook_NeighboursHouse_EventScript_Neighbour::
	lock
	faceplayer
	goto_if_ge VAR_HOLLOWBROOK_STATE, 3, Hollowbrook_NeighboursHouse_EventScript_NeighbourAfter
	msgbox Hollowbrook_Text_NeighbourBefore, MSGBOX_DEFAULT
	release
	end

@ A remark on the player's starter (three on-show variants); the fourth gets the generic line.
Hollowbrook_NeighboursHouse_EventScript_NeighbourAfter::
	call Hollowbrook_EventScript_BufferPlayerStarter
	switch VAR_STARTER_MON
	case 0, Hollowbrook_NeighboursHouse_EventScript_NeighbourA
	case 1, Hollowbrook_NeighboursHouse_EventScript_NeighbourB
	case 2, Hollowbrook_NeighboursHouse_EventScript_NeighbourC
	msgbox Hollowbrook_Text_NeighbourAfter, MSGBOX_DEFAULT
	release
	end

Hollowbrook_NeighboursHouse_EventScript_NeighbourA::
	msgbox Hollowbrook_Text_NeighbourStarterA, MSGBOX_DEFAULT
	release
	end

Hollowbrook_NeighboursHouse_EventScript_NeighbourB::
	msgbox Hollowbrook_Text_NeighbourStarterB, MSGBOX_DEFAULT
	release
	end

Hollowbrook_NeighboursHouse_EventScript_NeighbourC::
	msgbox Hollowbrook_Text_NeighbourStarterC, MSGBOX_DEFAULT
	release
	end

Hollowbrook_NeighboursHouse_EventScript_Husband::
	msgbox Hollowbrook_Text_NeighbourHusband, MSGBOX_NPC
	end

Hollowbrook_NeighboursHouse_EventScript_Kid::
	lock
	faceplayer
	goto_if_ge VAR_HOLLOWBROOK_STATE, 3, Hollowbrook_NeighboursHouse_EventScript_KidAfter
	msgbox Hollowbrook_Text_NeighbourKidBefore, MSGBOX_DEFAULT
	release
	end

Hollowbrook_NeighboursHouse_EventScript_KidAfter::
	msgbox Hollowbrook_Text_NeighbourKidAfter, MSGBOX_DEFAULT
	release
	end

Hollowbrook_NeighboursHouse_EventScript_Skitty::
	lock
	faceplayer
	playmoncry SPECIES_SKITTY, CRY_MODE_NORMAL
	msgbox Hollowbrook_Text_NeighbourPokemon, MSGBOX_DEFAULT
	waitmoncry
	release
	end

Hollowbrook_NeighboursHouse_EventScript_Bookshelf::
	msgbox Hollowbrook_Text_NeighbourBookshelf, MSGBOX_SIGN
	end

Hollowbrook_Text_NeighbourBefore::
	.string "Oh, hello, dear! Your mother\n"
	.string "says you're off to the lab.\p"
	.string "Bring back a POKéMON. A nice,\n"
	.string "quiet one. Mine aren't.$"

Hollowbrook_Text_NeighbourAfter::
	.string "A POKéMON of your own! Your\n"
	.string "mother will never stop talking.\p"
	.string "Not that she ever started.\n"
	.string "...Well, she did. A bit.$"

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

Hollowbrook_Text_NeighbourHusband::
	.string "I'm reading about the Goldsworth\n"
	.string "family. It's a very long book.\p"
	.string "I'm on the chapter about their\n"
	.string "boats. They have a lot of boats.$"

Hollowbrook_Text_NeighbourKidBefore::
	.string "You're going to the lab? Can I\n"
	.string "come? I won't touch anything.\p"
	.string "...I'll touch one thing.$"

Hollowbrook_Text_NeighbourKidAfter::
	.string "Show me your POKéMON! Please!\n"
	.string "Just a little look!\p"
	.string "When I'm a trainer, mine will\n"
	.string "be bigger. And louder.$"

Hollowbrook_Text_NeighbourPokemon::
	.string "SKITTY is chasing its own tail\n"
	.string "in a slow, serious circle.\p"
	.string "It stops. It looks at you. It\n"
	.string "starts again. Nothing is wrong.\p"
	.string "SKITTY: Nyaa!$"

Hollowbrook_Text_NeighbourBookshelf::
	.string "A shelf full of cookbooks.\n"
	.string "Every page is stained.\p"
	.string "The stains are labelled.$"
