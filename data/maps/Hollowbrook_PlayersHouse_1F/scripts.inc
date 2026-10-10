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
	call_if_unset FLAG_SYS_B_DASH, Hollowbrook_PlayersHouse_1F_EventScript_MomBringsShoes
	setvar VAR_HOLLOWBROOK_STATE, 1
	releaseall
	end

Hollowbrook_PlayersHouse_1F_EventScript_Mom::
	lock
	faceplayer
	goto_if_eq VAR_HOLLOWBROOK_STATE, 0, Hollowbrook_PlayersHouse_1F_EventScript_MomWakeUp
	goto_if_le VAR_HOLLOWBROOK_STATE, 2, Hollowbrook_PlayersHouse_1F_EventScript_MomIdleBefore
	goto_if_unset FLAG_HOLLOWBROOK_MOM_GOT_MON_TOLD, Hollowbrook_PlayersHouse_1F_EventScript_MomGotPokemon
	goto_if_set FLAG_BADGE01_GET, Hollowbrook_PlayersHouse_1F_EventScript_MomAfterBadge
	msgbox Hollowbrook_Text_MomIdleAfter, MSGBOX_DEFAULT
	release
	end

Hollowbrook_PlayersHouse_1F_EventScript_MomAfterBadge::
	msgbox Hollowbrook_Text_MomAfterBadge, MSGBOX_DEFAULT
	release
	end

Hollowbrook_PlayersHouse_1F_EventScript_MomWakeUp::
	msgbox Hollowbrook_Text_MomWakeUp, MSGBOX_DEFAULT
	call_if_unset FLAG_SYS_B_DASH, Hollowbrook_PlayersHouse_1F_EventScript_MomGiveRunningShoes
	setvar VAR_HOLLOWBROOK_STATE, 1
	release
	end

@ Running Shoes (design/running-shoes.md). Guarded by FLAG_SYS_B_DASH at both call sites, so it is never given twice
@ and a debug-menu shoes toggle is respected. No other flag: FLAG_SYS_B_DASH is what the engine reads.
Hollowbrook_PlayersHouse_1F_EventScript_MomGiveRunningShoes::
	msgbox Hollowbrook_Text_MomRunningShoes, MSGBOX_DEFAULT
	playfanfare MUS_OBTAIN_ITEM
	message Hollowbrook_Text_PlayerPutOnShoes
	waitfanfare
	waitmessage @ the fanfare can end before the text does, and a message() while text is printing is dropped
	waitbuttonpress
	setflag FLAG_SYS_B_DASH
	setflag FLAG_SYS_RUN_BY_DEFAULT @ run all the time; B walks, L flips it (new games start with it on)
	msgbox Hollowbrook_Text_MomShoesBox, MSGBOX_DEFAULT
	call Veldris_EventScript_GiveCostumeBox @ the Costume Box and the look picker (design/player-customization.md)
	msgbox Hollowbrook_Text_MomShoesSendOff, MSGBOX_DEFAULT
	closemessage
	return

@ Trigger path only: the player is at (10,2) and Mom is at (5,4). She walks to (10,3), hands them over, walks back and
@ faces right again. If it looks wrong in game, delete this label and the two movements and point the trigger's call at
@ MomGiveRunningShoes instead: the gift still works from a distance.
Hollowbrook_PlayersHouse_1F_EventScript_MomBringsShoes::
	closemessage
	applymovement LOCALID_HOLLOWBROOK_MOM, Hollowbrook_PlayersHouse_1F_Movement_MomToPlayer
	waitmovement 0
	call Hollowbrook_PlayersHouse_1F_EventScript_MomGiveRunningShoes
	applymovement LOCALID_HOLLOWBROOK_MOM, Hollowbrook_PlayersHouse_1F_Movement_MomBackToKitchen
	waitmovement 0
	return

Hollowbrook_PlayersHouse_1F_Movement_MomToPlayer:
	walk_right
	walk_right
	walk_right
	walk_right
	walk_right
	walk_up
	step_end

Hollowbrook_PlayersHouse_1F_Movement_MomBackToKitchen:
	walk_down
	walk_left
	walk_left
	walk_left
	walk_left
	walk_left
	face_right
	step_end

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
	goto_if_set FLAG_BADGE01_GET, Hollowbrook_PlayersHouse_1F_EventScript_TVAfterBadge
	goto_if_ge VAR_HOLLOWBROOK_STATE, 3, Hollowbrook_PlayersHouse_1F_EventScript_TVAfter
	msgbox Hollowbrook_Text_PlayerTVBefore, MSGBOX_SIGN
	end

Hollowbrook_PlayersHouse_1F_EventScript_TVAfterBadge::
	msgbox Hollowbrook_Text_PlayerTVAfterBadge, MSGBOX_SIGN
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

Hollowbrook_Text_MomRunningShoes::
	.string "Oh, and one more thing, {PLAYER}.\n"
	.string "I got you a little something.\p"
	.string "RUNNING SHOES. The shop said\n"
	.string "they're ‘terribly quick’.\p"
	.string "I said you'd be the judge.\n"
	.string "Go on. Put them on.$"

Hollowbrook_Text_PlayerPutOnShoes::
	.string "{PLAYER} put on the RUNNING SHOES.\n"
	.string "They squeak a little.$"

Hollowbrook_Text_MomShoesBox::
	.string "The box says: ‘These shoes run all\n"
	.string "the time. Hold the B Button to walk.’\p"
	.string "On the back: ‘Press the L Button\n"
	.string "to stop running all the time. Press\l"
	.string "it again to start.’$"

Hollowbrook_Text_MomShoesSendOff::
	.string "That's a lot of buttons for one\n"
	.string "pair of shoes. I read it twice.\p"
	.string "Now off you go. FENNICK is\n"
	.string "waiting, and you're ready.$"

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

@ ---- After the first badge (added 2026-10-01, FLAG_BADGE01_GET) ----
Hollowbrook_Text_MomAfterBadge::
	.string "A badge! Oh, {PLAYER}. Let me\n"
	.string "see. It's very shiny.\p"
	.string "I've put it on the fridge.\n"
	.string "...Not the badge. The drawing.$"

Hollowbrook_Text_PlayerTVAfterBadge::
	.string "The news: ‘Local trainer wins\n"
	.string "gym badge. A rich family is\l"
	.string "said to be very embarrassed.’\p"
	.string "They cut to a clean coat\n"
	.string "stomping out of a gym.$"
