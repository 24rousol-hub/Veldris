Crestfall_Gym_MapScripts::
	map_script MAP_SCRIPT_ON_LOAD, Crestfall_Gym_OnLoad
	.byte 0

@ The centre gates stay shut until Greta is beaten (author, 2026-10-08).
Crestfall_Gym_OnLoad:
	call_if_set FLAG_BADGE01_GET, Crestfall_Gym_EventScript_OpenGates
	end

Crestfall_Gym_EventScript_OpenGates::
	setmetatile 6, 11, 513, FALSE
	setmetatile 7, 11, 513, FALSE
	setmetatile 8, 11, 513, FALSE
	setmetatile 6, 16, 513, FALSE
	setmetatile 7, 16, 513, FALSE
	setmetatile 8, 16, 513, FALSE
	setmetatile 5, 11, 736, TRUE
	setmetatile 9, 11, 736, TRUE
	setmetatile 5, 16, 736, TRUE
	setmetatile 9, 16, 736, TRUE
	return

Crestfall_Gym_EventScript_Greta::
	trainerbattle_single TRAINER_CRESTFALL_GRETA, Crestfall_Gym_Text_GretaIntro, Crestfall_Gym_Text_GretaDefeat, Crestfall_Gym_EventScript_GretaDefeated, NO_MUSIC
	goto_if_unset FLAG_RECEIVED_HM_CUT, Crestfall_Gym_EventScript_GiveCut
	goto_if_unset FLAG_RECEIVED_TM_CRUNCH, Crestfall_Gym_EventScript_GiveCrunch
	msgbox Crestfall_Gym_Text_GretaAfterBadge, MSGBOX_DEFAULT
	release
	end

Crestfall_Gym_EventScript_GretaDefeated::
	message Crestfall_Gym_Text_ReceivedBadge
	waitmessage
	call Common_EventScript_PlayGymBadgeFanfare
	msgbox Crestfall_Gym_Text_GretaBadgeInfo, MSGBOX_DEFAULT
	setflag FLAG_BADGE01_GET
	settrainerflag TRAINER_CRESTFALL_GYM_1
	settrainerflag TRAINER_CRESTFALL_GYM_2
	call Crestfall_Gym_EventScript_OpenGates
	special DrawWholeMapView
	goto Crestfall_Gym_EventScript_GiveCut
	end

Crestfall_Gym_EventScript_GiveCut::
	giveitem ITEM_HM_CUT
	goto_if_eq VAR_RESULT, FALSE, Common_EventScript_ShowBagIsFull
	setflag FLAG_RECEIVED_HM_CUT
	goto Crestfall_Gym_EventScript_GiveCrunch
	end

Crestfall_Gym_EventScript_GiveCrunch::
	giveitem ITEM_TM_CRUNCH
	goto_if_eq VAR_RESULT, FALSE, Common_EventScript_ShowBagIsFull
	setflag FLAG_RECEIVED_TM_CRUNCH
	msgbox Crestfall_Gym_Text_GretaGifts, MSGBOX_DEFAULT
	release
	end

@ Gym trainers. Beating Greta marks both as beaten, so an unbeaten one just chats afterwards (author: one required).
Crestfall_Gym_EventScript_Dale::
	trainerbattle_single TRAINER_CRESTFALL_GYM_1, Crestfall_Gym_Text_DaleIntro, Crestfall_Gym_Text_DaleDefeat
	msgbox Crestfall_Gym_Text_DaleAfter, MSGBOX_AUTOCLOSE
	end

Crestfall_Gym_EventScript_Wren::
	trainerbattle_single TRAINER_CRESTFALL_GYM_2, Crestfall_Gym_Text_WrenIntro, Crestfall_Gym_Text_WrenDefeat
	msgbox Crestfall_Gym_Text_WrenAfter, MSGBOX_AUTOCLOSE
	end

Crestfall_Gym_EventScript_Statue::
	lockall
	goto_if_set FLAG_BADGE01_GET, Crestfall_Gym_EventScript_StatueCertified
	msgbox Crestfall_Gym_Text_Statue, MSGBOX_DEFAULT
	releaseall
	end

Crestfall_Gym_EventScript_StatueCertified::
	msgbox Crestfall_Gym_Text_StatueCertified, MSGBOX_DEFAULT
	releaseall
	end

@ Greta's lines are the earlier drafts in design/dialogue/crestfall.inc (PROPOSED); the gym trainers' lines are
@ reworded from that draft because the hay maze is gone.
Crestfall_Gym_Text_GretaIntro:
	.string "Well, hello. You must be {PLAYER}.\n"
	.string "The whole town has been talking.\p"
	.string "I'm GRETA. Crestfall's gym leader.\n"
	.string "Yes, I know. I look too young.\p"
	.string "I get that a lot. Usually right\n"
	.string "before I win.\p"
	.string "Normal types. Don't look so\n"
	.string "disappointed. Normal is reliable.\p"
	.string "Flashy gets you a cool entrance.\n"
	.string "Reliable gets you badges.\p"
	.string "Try to keep up. No pressure.$"

Crestfall_Gym_Text_GretaDefeat:
	.string "Wow. Okay. That was good.\n"
	.string "Really good.$"

Crestfall_Gym_Text_ReceivedBadge:
	.string "{PLAYER} received the STANDARD\n"
	.string "BADGE from GRETA!$"

Crestfall_Gym_Text_GretaBadgeInfo:
	.string "That badge means you've met the\n"
	.string "standard to start the gym\l"
	.string "challenge. The real work begins.\p"
	.string "It also lets you use CUT. Here,\n"
	.string "take these as well.$"

Crestfall_Gym_Text_GretaGifts:
	.string "CUT clears small trees. CRUNCH\n"
	.string "bites hard. Use both wisely.\p"
	.string "And the gates are open now, so\n"
	.string "come back any time.$"

Crestfall_Gym_Text_GretaAfterBadge:
	.string "That Goldsworth boy? Bit of a\n"
	.string "mess, honestly. Not wicked.\p"
	.string "He's just never been told ‘no.’\n"
	.string "So you'd be doing the region a\l"
	.string "favour, every time you beat him.$"

Crestfall_Gym_Text_DaleIntro:
	.string "Pick a side, pick a fight!\n"
	.string "You picked mine. Come on, then!$"

Crestfall_Gym_Text_DaleDefeat:
	.string "Fair's fair. Go on through.$"

Crestfall_Gym_Text_DaleAfter:
	.string "GRETA's tougher than she looks.\n"
	.string "Also tougher than she sounds.$"

Crestfall_Gym_Text_WrenIntro:
	.string "Ah, a challenger! This side of\n"
	.string "the hall is mine. Shall we?$"

Crestfall_Gym_Text_WrenDefeat:
	.string "Splendid. Truly splendid.$"

Crestfall_Gym_Text_WrenAfter:
	.string "I've watched GRETA climb the\n"
	.string "ranks. She'll go far. So may you.$"

Crestfall_Gym_Text_Statue:
	.string "CRESTFALL POKéMON GYM$"

Crestfall_Gym_Text_StatueCertified:
	.string "CRESTFALL POKéMON GYM\p"
	.string "GRETA'S CERTIFIED TRAINERS:\n"
	.string "{PLAYER}$"
