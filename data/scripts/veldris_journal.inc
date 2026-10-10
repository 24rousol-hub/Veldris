@ Veldris Journal (hack-owned script file). Opened from the bag (ITEM_JOURNAL, the old ITEM_OLD_SEA_MAP slot)
@ or from SELECT when registered. See design/journal.md. PROPOSED text, not yet approved by the author.
@ Reads existing state only, claims no flag or var. VeldrisJournal_FillVars (src/veldris_journal.c) sets
@ VAR_0x8004 = badges earned and VAR_0x8005 = TROGLODYTE fights won.

@ Gives the Journal once, from any giver. Silent if it is already in the bag (key items cannot be tossed).
Veldris_EventScript_GiveJournal::
	checkitem ITEM_JOURNAL
	goto_if_eq VAR_RESULT, TRUE, Veldris_Journal_GiveDone
	checkitemspace ITEM_JOURNAL
	goto_if_eq VAR_RESULT, FALSE, Veldris_Journal_GiveNoSpace
	giveitem ITEM_JOURNAL
Veldris_Journal_GiveDone::
	return

Veldris_Journal_GiveNoSpace::
	msgbox gText_TooBadBagIsFull, MSGBOX_DEFAULT
	return

Veldris_EventScript_Journal::
	lockall
	callnative VeldrisJournal_FillVars
	buffernumberstring STR_VAR_1, VAR_0x8004
	msgbox Veldris_Journal_Text_Badges, MSGBOX_DEFAULT
	goto_if_set FLAG_SYS_GAME_CLEAR, Veldris_Journal_HintClear
	switch VAR_0x8004
	case 0, Veldris_Journal_Hint0
	case 1, Veldris_Journal_Hint1
	case 2, Veldris_Journal_Hint2
	case 3, Veldris_Journal_Hint3
	case 4, Veldris_Journal_Hint4
	case 5, Veldris_Journal_Hint5
	case 6, Veldris_Journal_Hint6
	case 7, Veldris_Journal_Hint7
	case 8, Veldris_Journal_Hint8
	case 9, Veldris_Journal_Hint9
	goto Veldris_Journal_Troglodyte

Veldris_Journal_Hint0::
	goto_if_lt VAR_HOLLOWBROOK_STATE, 3, Veldris_Journal_Hint0Lab
	msgbox Veldris_Journal_Text_Hint0, MSGBOX_DEFAULT
	goto Veldris_Journal_Troglodyte

Veldris_Journal_Hint0Lab::
	msgbox Veldris_Journal_Text_Hint0Lab, MSGBOX_DEFAULT
	goto Veldris_Journal_Troglodyte

Veldris_Journal_Hint1::
	msgbox Veldris_Journal_Text_Hint1, MSGBOX_DEFAULT
	goto Veldris_Journal_Troglodyte

Veldris_Journal_Hint2::
	msgbox Veldris_Journal_Text_Hint2, MSGBOX_DEFAULT
	goto Veldris_Journal_Troglodyte

Veldris_Journal_Hint3::
	msgbox Veldris_Journal_Text_Hint3, MSGBOX_DEFAULT
	goto Veldris_Journal_Troglodyte

Veldris_Journal_Hint4::
	msgbox Veldris_Journal_Text_Hint4, MSGBOX_DEFAULT
	goto Veldris_Journal_Troglodyte

Veldris_Journal_Hint5::
	msgbox Veldris_Journal_Text_Hint5, MSGBOX_DEFAULT
	goto Veldris_Journal_Troglodyte

Veldris_Journal_Hint6::
	msgbox Veldris_Journal_Text_Hint6, MSGBOX_DEFAULT
	goto Veldris_Journal_Troglodyte

Veldris_Journal_Hint7::
	msgbox Veldris_Journal_Text_Hint7, MSGBOX_DEFAULT
	goto Veldris_Journal_Troglodyte

Veldris_Journal_Hint8::
	msgbox Veldris_Journal_Text_Hint8, MSGBOX_DEFAULT
	goto Veldris_Journal_Troglodyte

Veldris_Journal_Hint9::
	msgbox Veldris_Journal_Text_Hint9, MSGBOX_DEFAULT
	goto Veldris_Journal_Troglodyte

Veldris_Journal_HintClear::
	msgbox Veldris_Journal_Text_HintClear, MSGBOX_DEFAULT
	goto Veldris_Journal_Troglodyte

Veldris_Journal_Troglodyte::
	buffernumberstring STR_VAR_1, VAR_0x8005
	switch VAR_0x8005
	case 0, Veldris_Journal_TrogNone
	case 1, Veldris_Journal_TrogOnce
	msgbox Veldris_Journal_Text_TrogMany, MSGBOX_DEFAULT
	releaseall
	end

Veldris_Journal_TrogNone::
	msgbox Veldris_Journal_Text_TrogNone, MSGBOX_DEFAULT
	releaseall
	end

Veldris_Journal_TrogOnce::
	msgbox Veldris_Journal_Text_TrogOnce, MSGBOX_DEFAULT
	releaseall
	end

Veldris_Journal_Text_Badges:
	.string "{PLAYER}'s JOURNAL\n"
	.string "BADGES: {STR_VAR_1} of 9.$"

Veldris_Journal_Text_Hint0Lab:
	.string "NEXT: FENNICK's lab, in town.\n"
	.string "He phoned. He wants you there.$"

Veldris_Journal_Text_Hint0:
	.string "NEXT: CRESTFALL, east on\n"
	.string "ROUTE 1. The first gym is there.$"

Veldris_Journal_Text_Hint1:
	.string "NEXT: WENDLEBURY, then north\n"
	.string "to BRIARWICK for the second gym.$"

Veldris_Journal_Text_Hint2:
	.string "NEXT: MOTHWOOD, off ROUTE 8.\n"
	.string "Then GLOOMSBY, the foggy town.$"

Veldris_Journal_Text_Hint3:
	.string "NEXT: SMELTHAM, the foundry\n"
	.string "town. It is loud.$"

Veldris_Journal_Text_Hint4:
	.string "NEXT: HOARFELL, the snow city.\n"
	.string "Dress warmly.$"

Veldris_Journal_Text_Hint5:
	.string "NEXT: GILDHAVEN, the big city\n"
	.string "with the very tall tower.$"

Veldris_Journal_Text_Hint6:
	.string "NEXT: HEMLOCK REACH, the cliff\n"
	.string "city of apothecaries.$"

Veldris_Journal_Text_Hint7:
	.string "NEXT: PRIMROSE VALE, the garden\n"
	.string "city. Mind the flowers.$"

Veldris_Journal_Text_Hint8:
	.string "NEXT: BEACONMOUTH, the lighthouse\n"
	.string "city on the south-east coast.$"

Veldris_Journal_Text_Hint9:
	.string "NEXT: THE PINNACLE, the League,\n"
	.string "south of GILDHAVEN.$"

Veldris_Journal_Text_HintClear:
	.string "NEXT: Nothing is listed. There\n"
	.string "is a lot of coast left to see.$"

Veldris_Journal_Text_TrogNone:
	.string "TROGLODYTE has not lost to you\n"
	.string "yet. This is only temporary.$"

Veldris_Journal_Text_TrogOnce:
	.string "TROGLODYTE has lost to you\n"
	.string "once. Officially. In writing.$"

Veldris_Journal_Text_TrogMany:
	.string "TROGLODYTE has lost to you\n"
	.string "{STR_VAR_1} times. Officially.$"
