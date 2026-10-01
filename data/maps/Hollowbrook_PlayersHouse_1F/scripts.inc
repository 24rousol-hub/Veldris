@ Hollowbrook_PlayersHouse_1F: Mom, the house ZIGZAGOON, TV, fridge, bookshelf.
@ Built from design/scripts/hollowbrook_scripts.inc (section 2) and design/dialogue/hollowbrook_houses.inc.

Hollowbrook_PlayersHouse_1F_MapScripts::
	.byte 0

@ Shared helper: {STR_VAR_1} = the player's starter (VAR_STARTER_MON 0-2 = the three on show, 3 = the fourth).
@ Stand-in species until the author picks the real four.
Hollowbrook_EventScript_BufferPlayerStarter::
	switch VAR_STARTER_MON
	case 0, Hollowbrook_EventScript_BufferPlayerStarter1
	case 1, Hollowbrook_EventScript_BufferPlayerStarter2
	case 2, Hollowbrook_EventScript_BufferPlayerStarter3
	bufferspeciesname STR_VAR_1, SPECIES_PIKACHU
	return

Hollowbrook_EventScript_BufferPlayerStarter1::
	bufferspeciesname STR_VAR_1, SPECIES_TREECKO
	return

Hollowbrook_EventScript_BufferPlayerStarter2::
	bufferspeciesname STR_VAR_1, SPECIES_TORCHIC
	return

Hollowbrook_EventScript_BufferPlayerStarter3::
	bufferspeciesname STR_VAR_1, SPECIES_MUDKIP
	return

@ Trigger on the tile next to the stairs, only while state is 0 (fresh from the intro).
Hollowbrook_PlayersHouse_1F_EventScript_MomWakeUpTrigger::
	lockall
	applymovement LOCALID_HOLLOWBROOK_MOM, Common_Movement_FacePlayer
	waitmovement 0
	msgbox Hollowbrook_Text_MomWakeUp, MSGBOX_DEFAULT
	setvar VAR_HOLLOWBROOK_STATE, 1
	releaseall
	end

Hollowbrook_PlayersHouse_1F_EventScript_Mom::
	lock
	faceplayer
	goto_if_eq VAR_HOLLOWBROOK_STATE, 0, Hollowbrook_PlayersHouse_1F_EventScript_MomWakeUp
	goto_if_le VAR_HOLLOWBROOK_STATE, 2, Hollowbrook_PlayersHouse_1F_EventScript_MomIdleBefore
	goto_if_unset FLAG_HOLLOWBROOK_MOM_GOT_MON_TOLD, Hollowbrook_PlayersHouse_1F_EventScript_MomGotPokemon
	msgbox Hollowbrook_Text_MomIdleAfter, MSGBOX_DEFAULT
	release
	end

Hollowbrook_PlayersHouse_1F_EventScript_MomWakeUp::
	msgbox Hollowbrook_Text_MomWakeUp, MSGBOX_DEFAULT
	setvar VAR_HOLLOWBROOK_STATE, 1
	release
	end

Hollowbrook_PlayersHouse_1F_EventScript_MomIdleBefore::
	msgbox Hollowbrook_Text_MomIdleBefore, MSGBOX_DEFAULT
	release
	end

Hollowbrook_PlayersHouse_1F_EventScript_MomGotPokemon::
	msgbox Hollowbrook_Text_MomGotPokemon, MSGBOX_DEFAULT
	setflag FLAG_HOLLOWBROOK_MOM_GOT_MON_TOLD
	release
	end

@ Mom's ZIGZAGOON, asleep by the kitchen.
Hollowbrook_PlayersHouse_1F_EventScript_HousePokemon::
	lock
	faceplayer
	playmoncry SPECIES_ZIGZAGOON, CRY_MODE_NORMAL
	goto_if_ge VAR_HOLLOWBROOK_STATE, 3, Hollowbrook_PlayersHouse_1F_EventScript_HousePokemonAfter
	msgbox Hollowbrook_Text_PlayerHousePokemonBefore, MSGBOX_DEFAULT
	waitmoncry
	release
	end

Hollowbrook_PlayersHouse_1F_EventScript_HousePokemonAfter::
	call Hollowbrook_EventScript_BufferPlayerStarter
	switch VAR_STARTER_MON
	case 0, Hollowbrook_PlayersHouse_1F_EventScript_HousePokemonA
	case 1, Hollowbrook_PlayersHouse_1F_EventScript_HousePokemonB
	case 2, Hollowbrook_PlayersHouse_1F_EventScript_HousePokemonC
	msgbox Hollowbrook_Text_PlayerHousePokemonAfter, MSGBOX_DEFAULT
	waitmoncry
	release
	end

Hollowbrook_PlayersHouse_1F_EventScript_HousePokemonA::
	msgbox Hollowbrook_Text_PlayerHouseStarterA, MSGBOX_DEFAULT
	waitmoncry
	release
	end

Hollowbrook_PlayersHouse_1F_EventScript_HousePokemonB::
	msgbox Hollowbrook_Text_PlayerHouseStarterB, MSGBOX_DEFAULT
	waitmoncry
	release
	end

Hollowbrook_PlayersHouse_1F_EventScript_HousePokemonC::
	msgbox Hollowbrook_Text_PlayerHouseStarterC, MSGBOX_DEFAULT
	waitmoncry
	release
	end

Hollowbrook_PlayersHouse_1F_EventScript_TV::
	goto_if_ge VAR_HOLLOWBROOK_STATE, 3, Hollowbrook_PlayersHouse_1F_EventScript_TVAfter
	msgbox Hollowbrook_Text_PlayerTVBefore, MSGBOX_SIGN
	end

Hollowbrook_PlayersHouse_1F_EventScript_TVAfter::
	msgbox Hollowbrook_Text_PlayerTVAfter, MSGBOX_SIGN
	end

Hollowbrook_PlayersHouse_1F_EventScript_Fridge::
	goto_if_ge VAR_HOLLOWBROOK_STATE, 3, Hollowbrook_PlayersHouse_1F_EventScript_FridgeAfter
	msgbox Hollowbrook_Text_PlayerFridgeBefore, MSGBOX_SIGN
	end

Hollowbrook_PlayersHouse_1F_EventScript_FridgeAfter::
	msgbox Hollowbrook_Text_PlayerFridgeAfter, MSGBOX_SIGN
	end

Hollowbrook_PlayersHouse_1F_EventScript_Bookshelf::
	msgbox Hollowbrook_Text_PlayerBookshelf, MSGBOX_SIGN
	end

Hollowbrook_Text_MomWakeUp::
	.string "Oh, you're up! FENNICK phoned.\n"
	.string "He wants you at the lab.\p"
	.string "Be polite if you meet the\n"
	.string "Goldsworth boy. He's been\l"
	.string "stomping around town all morning.\p"
	.string "And take a clean handkerchief.\n"
	.string "You never know.$"

Hollowbrook_Text_MomIdleBefore::
	.string "Off to the lab, {PLAYER}.\n"
	.string "FENNICK doesn't like to wait.\p"
	.string "Well. He doesn't notice waiting.\n"
	.string "But he'd feel bad afterwards.$"

Hollowbrook_Text_MomGotPokemon::
	.string "You have a POKéMON! Let me see.\p"
	.string "Oh, what a face. You two are\n"
	.string "going to get into trouble.\p"
	.string "I heard about the Goldsworth\n"
	.string "boy. FENNICK told me everything.\p"
	.string "Don't let him get to you.\n"
	.string "...Or do. A little.$"

Hollowbrook_Text_MomIdleAfter::
	.string "Come home when you're hungry.\n"
	.string "Or when you're losing.\p"
	.string "I've made soup either way.$"

Hollowbrook_Text_PlayerHousePokemonBefore::
	.string "ZIGZAGOON is asleep by the\n"
	.string "stove. It is snoring.\p"
	.string "It looks like a rug that\n"
	.string "has made some choices.$"

Hollowbrook_Text_PlayerHousePokemonAfter::
	.string "ZIGZAGOON sniffs at your new\n"
	.string "POKéMON. A long, hard look.\p"
	.string "It goes back to sleep. Your\n"
	.string "POKéMON has been approved.$"

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

Hollowbrook_Text_PlayerTVBefore::
	.string "A show is on about a rich man\n"
	.string "who lost his yacht.\p"
	.string "He was found soon after. It was\n"
	.string "parked in the wrong bay.$"

Hollowbrook_Text_PlayerTVAfter::
	.string "The news: ‘A young man in a very\n"
	.string "clean coat has reportedly made\l"
	.string "a scene at a local lab.’\p"
	.string "They show a blurry photo.\n"
	.string "It is definitely him.$"

Hollowbrook_Text_PlayerFridgeBefore::
	.string "The fridge holds a pot of soup,\n"
	.string "a jar of pickles and a note.\p"
	.string "Note: ‘Eat something before\n"
	.string "you go. Yes, you.’$"

Hollowbrook_Text_PlayerFridgeAfter::
	.string "Soup, pickles and a fresh note.\n"
	.string "‘Bring your POKéMON something\l"
	.string "too. They look thin.’$"

Hollowbrook_Text_PlayerBookshelf::
	.string "Your shelf. Mostly old trainer\n"
	.string "handbooks and a ‘how to lose\l"
	.string "gracefully’ pamphlet.\p"
	.string "Nobody in this house has read\n"
	.string "the pamphlet.$"
