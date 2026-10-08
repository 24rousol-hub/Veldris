@ Veldris debug presets (hack-owned, not upstream). See design/debug-presets.md.
@ Reached from the debug menu (R+START): Scripts... slots 1 to 8 (Debug_EventScript_Script_N in debug.inc just goto the
@ Veldris_Debug_PresetN labels here) and Utilities > Cheat start (Debug_CheatStart goes to Veldris_Debug_CheatStart).
@
@ A preset only sets flags, vars, trainer flags, items and the party; no engine code. Every flag and var below is in
@ design/flags.md (or is a vanilla system flag named in running-shoes.md, exp-share.md or badges.md). When you claim a new
@ Veldris flag or var, add it to Veldris_Debug_ResetStory in the same commit.
@
@ The debug menu locks the player before it runs a script. A preset that stays put ends with release or releaseall,
@ one that moves the player ends with warp + waitstate (the new map unlocks the player).

@ ---------------------------------------------------------------------------------------------------------
@ Parts
@ ---------------------------------------------------------------------------------------------------------

Veldris_Debug_ClearBadges::
	clearflag FLAG_BADGE01_GET
	clearflag FLAG_BADGE02_GET
	clearflag FLAG_BADGE03_GET
	clearflag FLAG_BADGE04_GET
	clearflag FLAG_BADGE05_GET
	clearflag FLAG_BADGE06_GET
	clearflag FLAG_BADGE07_GET
	clearflag FLAG_BADGE08_GET
	clearflag FLAG_BADGE09_GET
	return

Veldris_Debug_AllBadges::
	setflag FLAG_BADGE01_GET
	setflag FLAG_BADGE02_GET
	setflag FLAG_BADGE03_GET
	setflag FLAG_BADGE04_GET
	setflag FLAG_BADGE05_GET
	setflag FLAG_BADGE06_GET
	setflag FLAG_BADGE07_GET
	setflag FLAG_BADGE08_GET
	setflag FLAG_BADGE09_GET
	return

@ Every story flag, var and trainer flag in design/flags.md "In use by the hack", back to its new-game value, plus the
@ things the built scripts hand out (HM CUT, TM CRUNCH). Does NOT touch the party, the bag's other items, the Running
@ Shoes, the Pokedex or the Exp. Share (Preset 1 does those).
Veldris_Debug_ResetStory::
	setvar VAR_HOLLOWBROOK_STATE, 0
	setvar VAR_TROG_STARTER, 0
	setvar VAR_STARTER_MON, 0
	clearflag FLAG_HIDE_HOLLOWBROOK_LAB_TROG
	clearflag FLAG_HIDE_HOLLOWBROOK_LAB_BALL_1
	clearflag FLAG_HIDE_HOLLOWBROOK_LAB_BALL_2
	clearflag FLAG_HIDE_HOLLOWBROOK_LAB_BALL_3
	setflag FLAG_HIDE_HOLLOWBROOK_LAB_BALL_4
	setflag FLAG_HIDE_HOLLOWBROOK_GRANDPA
	setflag FLAG_HIDE_HOLLOWBROOK_TROG
	clearflag FLAG_HOLLOWBROOK_GRANDPA_TALKED1
	clearflag FLAG_HOLLOWBROOK_GRANDPA_TALKED2
	clearflag FLAG_HOLLOWBROOK_MOM_GOT_MON_TOLD
	clearflag FLAG_VISITED_HOLLOWBROOK
	clearflag FLAG_VISITED_CRESTFALL
	clearflag FLAG_VELDRIS_ROUTE1_GUIDE_POTIONS
	clearflag FLAG_HIDDEN_ITEM_VELDRIS_ROUTE1_POTION
	clearflag FLAG_HIDDEN_ITEM_VELDRIS_ROUTE1_REPEL
	clearflag FLAG_RECEIVED_HM_CUT
	clearflag FLAG_RECEIVED_TM_CRUNCH
	clearflag FLAG_SYS_POKEMON_GET
	clearflag FLAG_ADVENTURE_STARTED
	call Veldris_Debug_ClearBadges
	cleartrainerflag TRAINER_TROGLODYTE_HOLLOWBROOK
	cleartrainerflag TRAINER_TROGLODYTE_CRESTFALL
	cleartrainerflag TRAINER_CRESTFALL_GRETA
	cleartrainerflag TRAINER_CRESTFALL_GYM_1
	cleartrainerflag TRAINER_CRESTFALL_GYM_2
	cleartrainerflag TRAINER_VELDRIS_ROUTE1_YOUNGSTER
	cleartrainerflag TRAINER_VELDRIS_ROUTE1_LASS
	cleartrainerflag TRAINER_VELDRIS_ROUTE1_FARMER
	removeitem ITEM_HM_CUT
	removeitem ITEM_TM_CRUNCH
	return

@ The state the lab scene leaves: the player took ball 3 (Mudkip, VAR_STARTER_MON 2), Troglodyte took ball 1 (Treecko,
@ VAR_TROG_STARTER 0), the other two balls stay on the table, Troglodyte waits outside (the town shows him while the
@ state is 3), the grandfather sits on his bench. The Hollowbrook frame table starts the fight on the next load of the town.
Veldris_Debug_StateChosen::
	setvar VAR_TROG_STARTER, 0
	setvar VAR_STARTER_MON, 2
	setflag FLAG_HIDE_HOLLOWBROOK_LAB_TROG
	setflag FLAG_HIDE_HOLLOWBROOK_LAB_BALL_1
	clearflag FLAG_HIDE_HOLLOWBROOK_LAB_BALL_2
	setflag FLAG_HIDE_HOLLOWBROOK_LAB_BALL_3
	clearflag FLAG_HIDE_HOLLOWBROOK_LAB_BALL_4
	clearflag FLAG_HIDE_HOLLOWBROOK_GRANDPA
	setflag FLAG_SYS_B_DASH
	setflag FLAG_SYS_POKEMON_GET
	setflag FLAG_ADVENTURE_STARTED
	setflag FLAG_VISITED_HOLLOWBROOK
	setvar VAR_HOLLOWBROOK_STATE, 3
	return

@ After Troglodyte's first fight: state 4, he is gone from the town and his fight counts as won (the Journal tally).
Veldris_Debug_StateRoam::
	call Veldris_Debug_StateChosen
	setflag FLAG_HIDE_HOLLOWBROOK_TROG
	settrainerflag TRAINER_TROGLODYTE_HOLLOWBROOK
	setvar VAR_HOLLOWBROOK_STATE, 4
	return

@ What GRETA's script leaves behind (Crestfall_Gym_EventScript_GretaDefeated and GiveCut/GiveCrunch).
Veldris_Debug_StateCrestfall::
	setflag FLAG_BADGE01_GET
	setflag FLAG_RECEIVED_HM_CUT
	setflag FLAG_RECEIVED_TM_CRUNCH
	settrainerflag TRAINER_CRESTFALL_GRETA
	settrainerflag TRAINER_CRESTFALL_GYM_1
	settrainerflag TRAINER_CRESTFALL_GYM_2
	@ His second fight is not scripted yet; counted as won so the Journal tally reads 2. Drop this line when the scene exists.
	settrainerflag TRAINER_TROGLODYTE_CRESTFALL
	setflag FLAG_VISITED_CRESTFALL
	additem ITEM_HM_CUT
	additem ITEM_TM_CRUNCH
	return

@ Things the real game hands out later (Journal: Route 1 guide; Exp. Share: giver undecided) plus a few consumables.
Veldris_Debug_Stock::
	additem ITEM_JOURNAL
	additem ITEM_EXP_SHARE
	additem ITEM_POKE_BALL, 20
	additem ITEM_POTION, 10
	additem ITEM_REPEL, 5
	return

@ VAR_0x8004 = level. Six fully evolved TEST DUMMIES, not canon (change them freely). SWAMPERT can learn Surf,
@ Waterfall and Dive, TROPIUS Cut, Flash, Fly, Strength and Rock Smash (teachable lists, verified), and none of them
@ knows a field move: the field-move rule in design/field-moves.md needs only a learner in the party.
Veldris_Debug_GiveTeam::
	givemon SPECIES_SWAMPERT, VAR_0x8004
	givemon SPECIES_TROPIUS, VAR_0x8004
	givemon SPECIES_BLAZIKEN, VAR_0x8004
	givemon SPECIES_SCEPTILE, VAR_0x8004
	givemon SPECIES_RAICHU, VAR_0x8004
	givemon SPECIES_ALAKAZAM, VAR_0x8004
	special HealPlayerParty
	return

@ ---------------------------------------------------------------------------------------------------------
@ Presets (Scripts... slots 1 to 8). 1 to 6 first reset the whole story, so they do not stack on old state.
@ ---------------------------------------------------------------------------------------------------------

@ 1 "New game (bedroom)": the very start. Mom's wake-up scene is the coord event at (10,2) on the 1F; walk down the stairs.
Veldris_Debug_Preset1::
	call Veldris_Debug_ResetStory
	clearflag FLAG_SYS_B_DASH
	clearflag FLAG_SYS_RUN_BY_DEFAULT
	clearflag FLAG_SYS_POKEDEX_GET
	clearflag FLAG_SYS_EXP_SHARE_ON
	removeitem ITEM_JOURNAL
	removeitem ITEM_EXP_SHARE
	callnative ZeroPlayerPartyMons
	warp MAP_HOLLOWBROOK_PLAYERS_HOUSE_2F, 2, 4
	waitstate
	end

@ 2 "Lab scene (Trog 1)": state 1 (Mom's scene done, shoes given), no Pokemon. Stand on the door mat of the lab and press
@ Up once: the trigger tiles are (6,10) and (7,10).
Veldris_Debug_Preset2::
	call Veldris_Debug_ResetStory
	setflag FLAG_SYS_B_DASH
	setvar VAR_HOLLOWBROOK_STATE, 1
	callnative ZeroPlayerPartyMons
	warp MAP_HOLLOWBROOK_PROF_FENNICK_LAB, 6, 11
	waitstate
	end

@ 3 "Trog fight 1 (door)": the starter is chosen (Mudkip L5, the only party member) and the player arrives on the lab
@ door tile outside, which fires Troglodyte's first fight from the town's frame table.
Veldris_Debug_Preset3::
	call Veldris_Debug_ResetStory
	call Veldris_Debug_StateChosen
	callnative ZeroPlayerPartyMons
	givemon SPECIES_MUDKIP, 5
	warp MAP_HOLLOWBROOK, 1
	waitstate
	end

@ 4 "After Trog fight": free roam, state 4, Mudkip L8, the key items and a few consumables, in front of the player's house.
Veldris_Debug_Preset4::
	call Veldris_Debug_ResetStory
	call Veldris_Debug_StateRoam
	call Veldris_Debug_Stock
	callnative ZeroPlayerPartyMons
	givemon SPECIES_MUDKIP, 8
	warp MAP_HOLLOWBROOK, 9, 21
	waitstate
	end

@ 5 "Crestfall: redo gym": gym 1 untouched (no badge, GRETA, DALE and WREN unbeaten, no HM CUT / TM CRUNCH), team L11,
@ standing at the gym door inside. The gates are shut again because the gym map loads without the badge flag.
Veldris_Debug_Preset5::
	call Veldris_Debug_ResetStory
	call Veldris_Debug_StateRoam
	call Veldris_Debug_Stock
	setflag FLAG_VISITED_CRESTFALL
	callnative ZeroPlayerPartyMons
	setvar VAR_0x8004, 11
	call Veldris_Debug_GiveTeam
	warp MAP_CRESTFALL_GYM, 7, 22
	waitstate
	end

@ 6 "Crestfall done": gym 1 as GRETA leaves it (badge 1, HM CUT, TM CRUNCH), team L12, outside the Center.
Veldris_Debug_Preset6::
	call Veldris_Debug_ResetStory
	call Veldris_Debug_StateRoam
	call Veldris_Debug_StateCrestfall
	call Veldris_Debug_Stock
	callnative ZeroPlayerPartyMons
	setvar VAR_0x8004, 12
	call Veldris_Debug_GiveTeam
	warp MAP_CRESTFALL, 9, 15
	waitstate
	end

@ 7 "Next badge + team": gives the next badge in table order (1 also runs Greta's rewards), makes sure the story is at
@ least in free roam, and REPLACES the party with six test dummies at that gym's ace level (src/caps.c:
@ 12, 19, 25, 31, 37, 42, 48, 55, 60). Press again for the next one. Badge 7 has no field move.
Veldris_Debug_Preset7::
	call_if_lt VAR_HOLLOWBROOK_STATE, 4, Veldris_Debug_StateRoam
	goto_if_unset FLAG_BADGE01_GET, Veldris_Debug_Badge1
	goto_if_unset FLAG_BADGE02_GET, Veldris_Debug_Badge2
	goto_if_unset FLAG_BADGE03_GET, Veldris_Debug_Badge3
	goto_if_unset FLAG_BADGE04_GET, Veldris_Debug_Badge4
	goto_if_unset FLAG_BADGE05_GET, Veldris_Debug_Badge5
	goto_if_unset FLAG_BADGE06_GET, Veldris_Debug_Badge6
	goto_if_unset FLAG_BADGE07_GET, Veldris_Debug_Badge7
	goto_if_unset FLAG_BADGE08_GET, Veldris_Debug_Badge8
	goto_if_unset FLAG_BADGE09_GET, Veldris_Debug_Badge9
	msgbox Veldris_Debug_Text_AllBadges, MSGBOX_DEFAULT
	releaseall
	end

Veldris_Debug_Badge1::
	call Veldris_Debug_StateCrestfall
	setvar VAR_0x8005, 1
	setvar VAR_0x8004, 12
	goto Veldris_Debug_BadgeDone

Veldris_Debug_Badge2::
	setflag FLAG_BADGE02_GET
	setvar VAR_0x8005, 2
	setvar VAR_0x8004, 19
	goto Veldris_Debug_BadgeDone

Veldris_Debug_Badge3::
	setflag FLAG_BADGE03_GET
	setvar VAR_0x8005, 3
	setvar VAR_0x8004, 25
	goto Veldris_Debug_BadgeDone

Veldris_Debug_Badge4::
	setflag FLAG_BADGE04_GET
	setvar VAR_0x8005, 4
	setvar VAR_0x8004, 31
	goto Veldris_Debug_BadgeDone

Veldris_Debug_Badge5::
	setflag FLAG_BADGE05_GET
	setvar VAR_0x8005, 5
	setvar VAR_0x8004, 37
	goto Veldris_Debug_BadgeDone

Veldris_Debug_Badge6::
	setflag FLAG_BADGE06_GET
	setvar VAR_0x8005, 6
	setvar VAR_0x8004, 42
	goto Veldris_Debug_BadgeDone

Veldris_Debug_Badge7::
	setflag FLAG_BADGE07_GET
	setvar VAR_0x8005, 7
	setvar VAR_0x8004, 48
	goto Veldris_Debug_BadgeDone

Veldris_Debug_Badge8::
	setflag FLAG_BADGE08_GET
	setvar VAR_0x8005, 8
	setvar VAR_0x8004, 55
	goto Veldris_Debug_BadgeDone

Veldris_Debug_Badge9::
	setflag FLAG_BADGE09_GET
	setvar VAR_0x8005, 9
	setvar VAR_0x8004, 60
	goto Veldris_Debug_BadgeDone

@ VAR_0x8004 = level, VAR_0x8005 = badges now held.
Veldris_Debug_BadgeDone::
	callnative ZeroPlayerPartyMons
	call Veldris_Debug_GiveTeam
	buffernumberstring STR_VAR_1, VAR_0x8005
	buffernumberstring STR_VAR_2, VAR_0x8004
	msgbox Veldris_Debug_Text_BadgeSet, MSGBOX_DEFAULT
	releaseall
	end

@ 8 "All field moves": all nine badges (Cut 1, Rock Smash 2, Flash 3, Strength 4, Surf 5, Fly 6, Waterfall 8, Dive 9;
@ src/field_move.c) and two learners ADDED to the party at L30. Press once; the party is not cleared.
Veldris_Debug_Preset8::
	call Veldris_Debug_AllBadges
	givemon SPECIES_SWAMPERT, 30
	givemon SPECIES_TROPIUS, 30
	msgbox Veldris_Debug_Text_FieldMoves, MSGBOX_DEFAULT
	releaseall
	end

@ ---------------------------------------------------------------------------------------------------------
@ Utilities > Cheat start: everything unlocked, for walking around the built maps and any new one.
@ The C side (DebugAction_Util_CheatStart) has already set the clock up.
@ ---------------------------------------------------------------------------------------------------------
Veldris_Debug_CheatStart::
	call Veldris_Debug_StateRoam
	call Veldris_Debug_StateCrestfall
	call Veldris_Debug_AllBadges
	setflag FLAG_SYS_POKEDEX_GET
	special SetUnlockedPokedexFlags
	setflag FLAG_SYS_NATIONAL_DEX
	special EnableNationalPokedex
	call Veldris_Debug_Stock
	callnative ZeroPlayerPartyMons
	setvar VAR_0x8004, 50
	call Veldris_Debug_GiveTeam
	release
	end

Veldris_Debug_Text_BadgeSet:
	.string "Badges: {STR_VAR_1} of 9.\n"
	.string "Party: six test mons at L{STR_VAR_2}.$"

Veldris_Debug_Text_AllBadges:
	.string "All nine badges are already set.$"

Veldris_Debug_Text_FieldMoves:
	.string "All nine badges set. SWAMPERT and\n"
	.string "TROPIUS added: they can learn them all.$"
