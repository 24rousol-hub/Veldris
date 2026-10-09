@ Hollowbrook (town exterior). Built from design/scripts/hollowbrook_scripts.inc (section 1) with real coordinates.
@ VAR_HOLLOWBROOK_STATE: 0 new game, 1 mom woke player, 2 lab scene running, 3 chose a starter, 4 beat Troglodyte here.

Hollowbrook_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, Hollowbrook_OnTransition
	map_script MAP_SCRIPT_ON_FRAME_TABLE, Hollowbrook_OnFrame
	.byte 0

@ Troglodyte's battle starts as soon as the player steps out of the lab with a starter (state 3).
@ (A coord_event outside the door does not fire on the automatic step out of a door, so this
@ uses the frame table instead, which CLAUDE.md allows for cutscenes. State 3 is only ever set
@ inside the lab, so the first Hollowbrook load in that state is the lab door.)
Hollowbrook_OnFrame:
	map_script_2 VAR_HOLLOWBROOK_STATE, 3, Hollowbrook_EventScript_TrogOutsideTrigger
	.2byte 0

Hollowbrook_OnTransition:
	setflag FLAG_VISITED_HOLLOWBROOK
	setrespawn HEAL_LOCATION_HOLLOWBROOK
	call Hollowbrook_EventScript_UpdateGrandpa
	call Hollowbrook_EventScript_UpdateTrog
	end

@ Grandfather on the bench: after the lab scene until the first badge; hidden otherwise
@ (after the League he is inside his house instead).
Hollowbrook_EventScript_UpdateGrandpa::
	goto_if_set FLAG_SYS_GAME_CLEAR, Hollowbrook_EventScript_HideGrandpa
	goto_if_set FLAG_BADGE01_GET, Hollowbrook_EventScript_HideGrandpa
	goto_if_ge VAR_HOLLOWBROOK_STATE, 3, Hollowbrook_EventScript_ShowGrandpa
	goto Hollowbrook_EventScript_HideGrandpa

Hollowbrook_EventScript_HideGrandpa::
	setflag FLAG_HIDE_HOLLOWBROOK_GRANDPA
	return

Hollowbrook_EventScript_ShowGrandpa::
	clearflag FLAG_HIDE_HOLLOWBROOK_GRANDPA
	return

@ Troglodyte waits outside the lab only while state is 3 (chosen, not yet fought).
Hollowbrook_EventScript_UpdateTrog::
	goto_if_eq VAR_HOLLOWBROOK_STATE, 3, Hollowbrook_EventScript_ShowTrog
	setflag FLAG_HIDE_HOLLOWBROOK_TROG
	return

Hollowbrook_EventScript_ShowTrog::
	clearflag FLAG_HIDE_HOLLOWBROOK_TROG
	return

@ ---- Signs ----
Hollowbrook_EventScript_TownSign::
	goto_if_set FLAG_BADGE01_GET, Hollowbrook_EventScript_TownSignAfterBadge
	msgbox Hollowbrook_Text_TownSign, MSGBOX_SIGN
	end

Hollowbrook_EventScript_TownSignAfterBadge::
	msgbox Hollowbrook_Text_SignTownAfterBadge, MSGBOX_SIGN
	end

Hollowbrook_EventScript_LabSign::
	msgbox Hollowbrook_Text_LabSign, MSGBOX_SIGN
	end

Hollowbrook_EventScript_GoldsworthSign::
	msgbox Hollowbrook_Text_GoldsworthSign, MSGBOX_SIGN
	end

Hollowbrook_EventScript_PlayerHouseSign::
	msgbox Hollowbrook_Text_PlayerHouseSign, MSGBOX_SIGN
	end

@ Locked until the League is beaten (the open-door warp comes with Hollowbrook_GoldsworthHouse).
Hollowbrook_EventScript_GoldsworthDoor::
	msgbox Hollowbrook_Text_GrandpaBefore, MSGBOX_SIGN
	end

@ ---- People ----
Hollowbrook_EventScript_Farmer::
	lock
	faceplayer
	goto_if_set FLAG_BADGE01_GET, Hollowbrook_EventScript_FarmerAfterBadge
	goto_if_ge VAR_HOLLOWBROOK_STATE, 3, Hollowbrook_EventScript_FarmerAfter
	msgbox Hollowbrook_Text_FarmerBefore, MSGBOX_DEFAULT
	release
	end

Hollowbrook_EventScript_FarmerAfter::
	msgbox Hollowbrook_Text_FarmerAfter, MSGBOX_DEFAULT
	release
	end

Hollowbrook_EventScript_FarmerAfterBadge::
	msgbox Hollowbrook_Text_FarmerAfterBadge, MSGBOX_DEFAULT
	msgbox Hollowbrook_Text_BenchOldManAfterBadge, MSGBOX_DEFAULT
	release
	end

Hollowbrook_EventScript_Kid::
	lock
	faceplayer
	goto_if_set FLAG_BADGE01_GET, Hollowbrook_EventScript_KidAfterBadge
	msgbox Hollowbrook_Text_Kid, MSGBOX_DEFAULT
	release
	end

Hollowbrook_EventScript_KidAfterBadge::
	msgbox Hollowbrook_Text_KidAfterBadge, MSGBOX_DEFAULT
	release
	end

Hollowbrook_EventScript_Laundry::
	lock
	faceplayer
	goto_if_set FLAG_BADGE01_GET, Hollowbrook_EventScript_LaundryAfterBadge
	msgbox Hollowbrook_Text_Laundry, MSGBOX_DEFAULT
	release
	end

Hollowbrook_EventScript_LaundryAfterBadge::
	msgbox Hollowbrook_Text_LaundryAfterBadge, MSGBOX_DEFAULT
	release
	end

@ ---- Pokemon around town (stand-in species) ----
Hollowbrook_EventScript_HenA::
	lock
	faceplayer
	playmoncry SPECIES_ZIGZAGOON, CRY_MODE_NORMAL
	goto_if_ge VAR_HOLLOWBROOK_STATE, 3, Hollowbrook_EventScript_HenAfterTrog
	msgbox Hollowbrook_Text_HenA, MSGBOX_DEFAULT
	waitmoncry
	release
	end

@ After Troglodyte has stormed out, the same Pokemon wears his glove.
Hollowbrook_EventScript_HenAfterTrog::
	msgbox Hollowbrook_Text_HenAfterTrog, MSGBOX_DEFAULT
	waitmoncry
	release
	end

Hollowbrook_EventScript_HenB::
	lock
	faceplayer
	playmoncry SPECIES_SKITTY, CRY_MODE_NORMAL
	msgbox Hollowbrook_Text_HenB, MSGBOX_DEFAULT
	waitmoncry
	release
	end

Hollowbrook_EventScript_HenC::
	lock
	faceplayer
	playmoncry SPECIES_SLAKOTH, CRY_MODE_NORMAL
	msgbox Hollowbrook_Text_HenC, MSGBOX_DEFAULT
	waitmoncry
	release
	end

@ ---- The grandfather on the bench (state 3 until the first badge) ----
Hollowbrook_EventScript_GrandpaBench::
	lock
	faceplayer
	goto_if_unset FLAG_HOLLOWBROOK_GRANDPA_TALKED1, Hollowbrook_EventScript_GrandpaBenchFirst
	goto_if_unset FLAG_HOLLOWBROOK_GRANDPA_TALKED2, Hollowbrook_EventScript_GrandpaBenchSecond
	msgbox Hollowbrook_Text_GrandpaIdle, MSGBOX_DEFAULT
	release
	end

Hollowbrook_EventScript_GrandpaBenchFirst::
	msgbox Hollowbrook_Text_GrandpaAfter, MSGBOX_DEFAULT
	setflag FLAG_HOLLOWBROOK_GRANDPA_TALKED1
	release
	end

Hollowbrook_EventScript_GrandpaBenchSecond::
	msgbox Hollowbrook_Text_GrandpaAdvice, MSGBOX_DEFAULT
	setflag FLAG_HOLLOWBROOK_GRANDPA_TALKED2
	release
	end

@ ---- Troglodyte's first battle, just outside the lab (state 3, fired from the frame table) ----
@ Team: SIR BISCUIT (level 1 Lillipup) plus his random starter (Pool Prune: Rival Starter).
Hollowbrook_EventScript_TrogOutsideTrigger::
	lockall
	applymovement LOCALID_HOLLOWBROOK_TROG, Common_Movement_FacePlayer
	waitmovement 0
	playbgm MUS_ENCOUNTER_RICH, FALSE
	applymovement LOCALID_HOLLOWBROOK_TROG, Common_Movement_ExclamationMark
	waitmovement 0
	applymovement LOCALID_HOLLOWBROOK_TROG, Common_Movement_Delay48
	waitmovement 0
	msgbox Hollowbrook_Text_TrogOutside1, MSGBOX_DEFAULT
	closemessage
	call Hollowbrook_EventScript_BufferTrogSpecies
	msgbox Hollowbrook_Text_TrogPetIntro, MSGBOX_DEFAULT
	trainerbattle_no_intro TRAINER_TROGLODYTE_HOLLOWBROOK, Hollowbrook_Text_TrogOutsideDefeat
	msgbox Hollowbrook_Text_TrogOutsideAfter1, MSGBOX_DEFAULT
	msgbox Hollowbrook_Text_TrogPetAfter, MSGBOX_DEFAULT
	closemessage
	applymovement LOCALID_HOLLOWBROOK_TROG, Hollowbrook_Movement_TrogWalksAway
	waitmovement 0
	removeobject LOCALID_HOLLOWBROOK_TROG
	setflag FLAG_HIDE_HOLLOWBROOK_TROG
	setvar VAR_HOLLOWBROOK_STATE, 4
	releaseall
	end

@ From (13,13) east along the main path and out of sight past the Goldsworth house.
Hollowbrook_Movement_TrogWalksAway:
	walk_down
	walk_right
	walk_right
	walk_right
	walk_right
	walk_right
	walk_right
	walk_right
	walk_right
	walk_right
	walk_right
	step_end

Hollowbrook_Text_TownSign::
	.string "HOLLOWBROOK\n"
	.string "‘A quiet place. Mind the ZIGZAGOON.’$"

Hollowbrook_Text_LabSign::
	.string "FENNICK'S POKéMON LAB\n"
	.string "Knock. Then knock again.$"

Hollowbrook_Text_GoldsworthSign::
	.string "GOLDSWORTH HOUSE\n"
	.string "Please wipe your feet.$"

Hollowbrook_Text_PlayerHouseSign::
	.string "{PLAYER}'s house$"

Hollowbrook_Text_GrandpaBefore::
	.string "Nobody answers the door.\n"
	.string "A note is pinned to it.\p"
	.string "‘Out. Back when I'm back.\n"
	.string "Do feed the SKITTY. - GG’$"

Hollowbrook_Text_FarmerBefore::
	.string "Morning. A boy in a very clean\n"
	.string "coat went by asking for the\l"
	.string "old gentleman's house.\p"
	.string "I pointed at the big one.\n"
	.string "He didn't say thank you.$"

Hollowbrook_Text_FarmerAfter::
	.string "That clean coat stormed past\n"
	.string "again. Muttering.\p"
	.string "Didn't look where he stepped.\n"
	.string "The ZIGZAGOON saw to that.$"

Hollowbrook_Text_Kid::
	.string "I'm going to be a trainer too!\n"
	.string "When I'm older.\p"
	.string "Or when Mum says I can go past\n"
	.string "the gate. Whichever is first.$"

Hollowbrook_Text_Laundry::
	.string "I'd hang this out, but the local\n"
	.string "ZIGZAGOON think everything is\l"
	.string "a treasure.\p"
	.string "Last week they took a sock.\n"
	.string "I respect the ambition.$"

Hollowbrook_Text_HenA::
	.string "ZIGZAGOON eyes you with deep\n"
	.string "suspicion.\p"
	.string "It seems to be deciding whether\n"
	.string "you are a threat or a snack.\p"
	.string "ZIGZAGOON: Zig-zig-zag!$"

Hollowbrook_Text_HenB::
	.string "SKITTY is sitting on a round,\n"
	.string "egg-shaped rock.\p"
	.string "It dares you to say something.\p"
	.string "SKITTY: Mew!$"

Hollowbrook_Text_HenC::
	.string "SLAKOTH is lying across the path.\n"
	.string "It has been there since dawn.\p"
	.string "It is not sorry.\p"
	.string "SLAKOTH: ...Kyu.$"

Hollowbrook_Text_HenAfterTrog::
	.string "ZIGZAGOON trots past, chest out.\p"
	.string "It is wearing a very expensive\n"
	.string "glove. It looks very pleased.\p"
	.string "ZIGZAGOON: Zig-zig!$"

Hollowbrook_Text_GrandpaAfter::
	.string "So you've met my grandson.\n"
	.string "Oh dear. I can see it on you.\p"
	.string "He gets his manners from the\n"
	.string "people who brought him up.\l"
	.string "Not from me, I hope.\p"
	.string "I should have been here when he\n"
	.string "came. I'm very sorry I wasn't.\p"
	.string "Where was I? Somewhere I had to\n"
	.string "be. That's all I can say.$"

Hollowbrook_Text_GrandpaAdvice::
	.string "Don't take him to heart.\p"
	.string "He has never been told 'no' by\n"
	.string "anyone who wasn't paid to.\p"
	.string "It makes a person very small\n"
	.string "inside. Be kind if you can.\p"
	.string "And beat him if you must.$"

Hollowbrook_Text_GrandpaIdle::
	.string "Ah, {PLAYER}. Lovely morning.\n"
	.string "I sit out here. The stairs\l"
	.string "and I are no longer friends.\p"
	.string "The view from this bench is\n"
	.string "quite good enough.$"

Hollowbrook_Text_TrogOutside1::
	.string "Not so fast, whoever you are.\n"
	.string "I want a look at that POKéMON.\p"
	.string "Honestly? I want to watch it\n"
	.string "lose. Don't look so worried.$"

Hollowbrook_Text_TrogPetIntro::
	.string "Go, {STR_VAR_2}! And stay back,\n"
	.string "SIR BISCUIT. Daddy's watching.$"

Hollowbrook_Text_TrogOutsideDefeat::
	.string "What?! That was a warm-up!\n"
	.string "A warm-up! I wasn't trying!$"

Hollowbrook_Text_TrogOutsideAfter1::
	.string "I'm not even warm yet. I skipped\n"
	.string "breakfast. That's the reason.\p"
	.string "This isn't over. Nothing ever is\n"
	.string "over with a Goldsworth.$"

Hollowbrook_Text_TrogPetAfter::
	.string "SIR BISCUIT didn't even get to\n"
	.string "play! Look what you've done!\p"
	.string "Come on, boy. We're going home.\n"
	.string "To the house with the big door.$"

@ ---- After the first badge (added 2026-10-01, FLAG_BADGE01_GET) ----
Hollowbrook_Text_FarmerAfterBadge::
	.string "Heard you took a badge off\n"
	.string "the Crestfall gym. Good.\p"
	.string "The ZIGZAGOON are quieter now.\n"
	.string "I think they're scared of you.$"

Hollowbrook_Text_BenchOldManAfterBadge::
	.string "The old gentleman's bench is\n"
	.string "empty again. Funny how a bench\l"
	.string "can look lonely.\p"
	.string "He'll be back. People like that\n"
	.string "always come home.$"

Hollowbrook_Text_KidAfterBadge::
	.string "You went past the gate!\n"
	.string "Was it scary? Was it huge?\p"
	.string "Mum says I can go when I'm\n"
	.string "twelve. I'm eleven and three\l"
	.string "quarters.$"

Hollowbrook_Text_LaundryAfterBadge::
	.string "The ZIGZAGOON brought the sock\n"
	.string "back. With a second sock.\p"
	.string "It isn't mine. I'm keeping it.$"

Hollowbrook_Text_SignTownAfterBadge::
	.string "HOLLOWBROOK\n"
	.string "‘Home of a badge holder.\l"
	.string "Still mind the ZIGZAGOON.’$"
