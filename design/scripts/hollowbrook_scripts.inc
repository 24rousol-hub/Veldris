@ ===========================================================================
@ SUPERSEDED, built 2026-10-01 into data/maps/Hollowbrook*/scripts.inc (those are the source of truth; this draft is history
@ and differs from them). Not included in data/event_scripts.s. See design/scripts/README.md.
@ Status (when written): PROPOSED. Hand-written scripts.inc style (NOT Poryscript).
@
@ Hollowbrook: town exterior, the player's house 1F and the Goldsworth house.
@ Paste each SECTION into the matching map's scripts.inc once the author has built the
@ map in Porymap (close or reload Porymap first). Sections:
@   1. Hollowbrook            -> data/maps/Hollowbrook/scripts.inc
@   2. Hollowbrook_PlayersHouse_1F -> its own scripts.inc
@   3. Hollowbrook_GoldsworthHouse -> its own scripts.inc (post-game only)
@ The lab is in hollowbrook_lab_scripts.inc (same folder).
@
@ TEXT: the labels come from design/dialogue/hollowbrook.inc. Append the matching text
@ labels to the same scripts.inc as the script that uses them (labels are global, so
@ each must be defined exactly once in the build). Text used here:
@   Hollowbrook_Text_TownSign, LabSign, GoldsworthSign, PlayerHouseSign, FarmerBefore,
@   FarmerAfter, Kid, Laundry, BenchOldMan (unused, see note), HenA, HenB, HenC,
@   HenAfterTrog, GrandpaBefore, GrandpaAfter, GrandpaAdvice, GrandpaIdle,
@   TrogOutside1, TrogOutsideDefeat, TrogOutsideAfter1, TrogPetIntro, TrogPetAfter,
@   MomWakeUp, MomIdleBefore, MomGotPokemon, MomIdleAfter,
@   GrandpaLeague1, GrandpaLeague2, GrandpaLeagueName, GrandpaLeagueIdle.
@ Not used here: TrogOutsideIntro (replaced by TrogPetIntro while the approved level 1
@ pet exists), BenchOldMan (the bench man is the grandfather, see his scripts below;
@ BenchOldMan is a spare NPC line if the author adds a second old man).
@
@ PLACEHOLDER FLAGS AND VARS (proposed names, NOT claimed in flags.h/vars.h;
@ full list with notes in design/scripts/README.md):
@   VAR_HOLLOWBROOK_STATE  0 new game, 1 mom woke player, 2 lab scene running (Troglodyte
@                          has taken his ball, player has not chosen), 3 player chose a
@                          starter (Trog waits outside), 4 Trog beaten outside the lab
@   VAR_TROG_STARTER       ALREADY CLAIMED (0x40F7): 0, 1 or 2
@   FLAG_HIDE_HOLLOWBROOK_GRANDPA        bench grandfather hidden
@   FLAG_HIDE_HOLLOWBROOK_TROG           Troglodyte standing outside the lab hidden
@   FLAG_HOLLOWBROOK_GRANDPA_TALKED1     first talk on the bench done
@   FLAG_HOLLOWBROOK_GRANDPA_TALKED2     second topic done
@   FLAG_HOLLOWBROOK_GRANDPA_NAME_TOLD   post-game name reveal done
@   FLAG_HOLLOWBROOK_MOM_GOT_MON_TOLD    mom's 'you have a POKeMON' speech done
@   FLAG_VISITED_HOLLOWBROOK             fly flag (row in src/data/veldris_fly_towns.h)
@   Existing vanilla: FLAG_BADGE01_GET, FLAG_SYS_GAME_CLEAR.
@
@ PLACEHOLDER LOCAL IDS (set in Porymap as each object's local_id; Porymap writes
@ them to map.json, the constants are generated from there):
@   LOCALID_HOLLOWBROOK_GRANDPA (bench), LOCALID_HOLLOWBROOK_TROG (outside the lab),
@   LOCALID_HOLLOWBROOK_MOM (house 1F), LOCALID_HOLLOWBROOK_GRANDPA_HOUSE (house)
@ Placeholder trainer: TRAINER_TROGLODYTE_HOLLOWBROOK (design/teams.md, fight 1; needs
@   its block in trainers.party and a define in opponents.h first).
@
@ map.json EVENTS TO PLACE (by the author in Porymap, or by Claude, see CLAUDE.md rule 2):
@   coord_event (trigger) on the tile in front of the lab door (outside), elevation 3,
@     var VAR_HOLLOWBROOK_STATE, var_value 3, script Hollowbrook_EventScript_TrogOutsideTrigger
@   bg_event (sign) on the Goldsworth door tile, facing up: Hollowbrook_EventScript_GoldsworthDoor
@     (the door tile has NO warp event: locked until the League is beaten, see below)
@   bg_events (sign) for the four signs, object events for the NPCs/Pokemon.
@   Player house 1F: coord_event on the stair-exit tile, var VAR_HOLLOWBROOK_STATE,
@     var_value 0, script Hollowbrook_PlayersHouse_1F_EventScript_MomWakeUpTrigger.
@   Hide flags go in each object event's flag field (grandfather, Trog).
@
@ All coordinates written in this file are PLACEHOLDERS marked TODO(coords); fix them
@ against the real map. Dialogue must still pass design/tools/dialogue_check.py.
@ ===========================================================================

@ ===========================================================================
@ SECTION 1: Hollowbrook (town exterior)
@ ===========================================================================

Hollowbrook_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, Hollowbrook_OnTransition
	.byte 0

@ Instant setup only (cutscenes use coord_events, per CLAUDE.md).
Hollowbrook_OnTransition:
	setflag FLAG_VISITED_HOLLOWBROOK
	call Hollowbrook_EventScript_UpdateGrandpa
	call Hollowbrook_EventScript_UpdateTrog
	end

@ Grandfather timeline (story-outline.md, 'The grandfather's whereabouts'):
@   start .. lab scene              hidden (door locked, note)
@   lab scene .. first badge        on the bench
@   first badge .. League           hidden again
@   after the League                hidden here (he is inside the open house instead)
@ The lab scene also clears the flag, so he is already on the bench when the player
@ walks out, even before this script next runs.
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

@ Troglodyte stands outside the lab only while state is 3 (chosen, not yet fought).
@ No new-game flag reset is needed: this decides it on every map load.
Hollowbrook_EventScript_UpdateTrog::
	goto_if_eq VAR_HOLLOWBROOK_STATE, 3, Hollowbrook_EventScript_ShowTrog
	setflag FLAG_HIDE_HOLLOWBROOK_TROG
	return

Hollowbrook_EventScript_ShowTrog::
	clearflag FLAG_HIDE_HOLLOWBROOK_TROG
	return

@ Shared helper (also called by the lab): buffers Troglodyte's species into STR_VAR_2.
@ Stand-in species (Treecko/Torchic/Mudkip) until the author picks the real starters;
@ keep the order the same as the lab's three balls (ball 1, 2, 3) and as Tag6/Tag7/Tag8
@ in trainers.party.
Hollowbrook_EventScript_BufferTrogSpecies::
	switch VAR_TROG_STARTER
	case 0, Hollowbrook_EventScript_BufferTrogSpecies1
	case 1, Hollowbrook_EventScript_BufferTrogSpecies2
	case 2, Hollowbrook_EventScript_BufferTrogSpecies3
	return

Hollowbrook_EventScript_BufferTrogSpecies1::
	bufferspeciesname STR_VAR_2, SPECIES_TREECKO
	return

Hollowbrook_EventScript_BufferTrogSpecies2::
	bufferspeciesname STR_VAR_2, SPECIES_TORCHIC
	return

Hollowbrook_EventScript_BufferTrogSpecies3::
	bufferspeciesname STR_VAR_2, SPECIES_MUDKIP
	return

@ ---- Signs ----

Hollowbrook_EventScript_TownSign::
	msgbox Hollowbrook_Text_TownSign, MSGBOX_SIGN
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

@ ---- NPCs ----

@ Farmer: one line before the lab scene (state < 3), another afterwards.
Hollowbrook_EventScript_Farmer::
	lock
	faceplayer
	goto_if_ge VAR_HOLLOWBROOK_STATE, 3, Hollowbrook_EventScript_FarmerAfter
	msgbox Hollowbrook_Text_FarmerBefore, MSGBOX_DEFAULT
	release
	end

Hollowbrook_EventScript_FarmerAfter::
	msgbox Hollowbrook_Text_FarmerAfter, MSGBOX_DEFAULT
	release
	end

Hollowbrook_EventScript_Kid::
	msgbox Hollowbrook_Text_Kid, MSGBOX_NPC
	end

Hollowbrook_EventScript_Laundry::
	msgbox Hollowbrook_Text_Laundry, MSGBOX_NPC
	end

@ ---- Interactable Pokemon (MSGBOX_NPC would turn them to face the player, which is
@ fine. Add playmoncry here if the author wants cries; species are stand-ins) ----

Hollowbrook_EventScript_HenA::
	lock
	faceplayer
	goto_if_ge VAR_HOLLOWBROOK_STATE, 3, Hollowbrook_EventScript_HenAfterTrog
	playmoncry SPECIES_ZIGZAGOON, CRY_MODE_NORMAL
	msgbox Hollowbrook_Text_HenA, MSGBOX_DEFAULT
	waitmoncry
	release
	end

@ After Troglodyte has stormed out, the same Pokemon wears his glove.
Hollowbrook_EventScript_HenAfterTrog::
	playmoncry SPECIES_ZIGZAGOON, CRY_MODE_NORMAL
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
@ Talk 1: GrandpaAfter. Talk 2: GrandpaAdvice. Afterwards: GrandpaIdle.
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

@ ---- The Goldsworth door ----
@ No warp on this tile. Locked with a note until FLAG_SYS_GAME_CLEAR (Hall of Fame),
@ then it opens and warps inside. The note text is GrandpaBefore (signed 'GG').
Hollowbrook_EventScript_GoldsworthDoor::
	lockall
	goto_if_set FLAG_SYS_GAME_CLEAR, Hollowbrook_EventScript_GoldsworthDoorOpen
	msgbox Hollowbrook_Text_GrandpaBefore, MSGBOX_DEFAULT
	releaseall
	end

@ TODO(coords): door tile x,y and the interior warp target (MAP_HOLLOWBROOK_GOLDSWORTH_HOUSE,
@ x, y) depend on the built maps. Note the post-game house is the only way in.
Hollowbrook_EventScript_GoldsworthDoorOpen::
	opendoor 0, 0
	waitdooranim
	applymovement LOCALID_PLAYER, Hollowbrook_Movement_EnterDoorUp
	waitmovement 0
	warpdoor MAP_HOLLOWBROOK_GOLDSWORTH_HOUSE, 0, 0
	waitstate
	releaseall
	end

Hollowbrook_Movement_EnterDoorUp:
	walk_up
	set_invisible
	step_end

@ ---- Troglodyte's first battle, right outside the lab (author, 2026-09-30) ----
@ Fired by a coord_event at the lab's outside door tile, only while state is 3.
@ Team: one random starter (Pool Prune: Rival Starter reads VAR_TROG_STARTER) plus the
@ approved level 1 pet SIR BISCUIT. trainerbattle_no_intro is the vanilla rival pattern
@ (Route103): intro is a plain msgbox first, then the battle with only a defeat text.
@ No battle has been run yet; the Trog object is hidden by FLAG_HIDE_HOLLOWBROOK_TROG.
@ Without the pet: swap TrogPetIntro for TrogOutsideIntro and drop the TrogPetAfter line.
Hollowbrook_EventScript_TrogOutsideTrigger::
	lockall
	applymovement LOCALID_HOLLOWBROOK_TROG, Common_Movement_FacePlayer
	waitmovement 0
	applymovement LOCALID_HOLLOWBROOK_TROG, Common_Movement_ExclamationMark
	waitmovement 0
	applymovement LOCALID_HOLLOWBROOK_TROG, Common_Movement_Delay48
	waitmovement 0
	msgbox Hollowbrook_Text_TrogOutside1, MSGBOX_DEFAULT
	closemessage
	@ playbgm MUS_ENCOUNTER_xxx, TRUE   @ TODO: rival battle music not chosen (teams.md: Music TBD)
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
	fadedefaultbgm
	releaseall
	end

@ TODO(coords): walk toward the map edge or the Goldsworth house; length depends on the map.
Hollowbrook_Movement_TrogWalksAway:
	walk_down
	walk_down
	walk_down
	walk_down
	step_end

@ ===========================================================================
@ SECTION 2: Hollowbrook_PlayersHouse_1F (mom)
@ ===========================================================================

Hollowbrook_PlayersHouse_1F_MapScripts::
	.byte 0

@ Trigger on the stair-exit tile, only while state is 0 (fresh from the intro). It runs
@ the wake-up speech unprompted, then sets state 1 so the lab is the next goal.
Hollowbrook_PlayersHouse_1F_EventScript_MomWakeUpTrigger::
	lockall
	applymovement LOCALID_HOLLOWBROOK_MOM, Common_Movement_FacePlayer
	waitmovement 0
	msgbox Hollowbrook_Text_MomWakeUp, MSGBOX_DEFAULT
	setvar VAR_HOLLOWBROOK_STATE, 1
	releaseall
	end

@ Mom by state: 0 (trigger missed) wake-up; 1 and 2 idle before; 3 and up: the
@ 'you have a POKeMON' speech once, then idle after.
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

@ ===========================================================================
@ SECTION 3: Hollowbrook_GoldsworthHouse (post-game only)
@ One NPC, the grandfather. Reachable only after FLAG_SYS_GAME_CLEAR (see the door).
@ ===========================================================================

Hollowbrook_GoldsworthHouse_MapScripts::
	.byte 0

@ First talk: League1, League2, then the name (GATSBY GOLDSWORTH). After that, idle.
Hollowbrook_GoldsworthHouse_EventScript_Grandpa::
	lock
	faceplayer
	goto_if_set FLAG_HOLLOWBROOK_GRANDPA_NAME_TOLD, Hollowbrook_GoldsworthHouse_EventScript_GrandpaIdle
	msgbox Hollowbrook_Text_GrandpaLeague1, MSGBOX_DEFAULT
	msgbox Hollowbrook_Text_GrandpaLeague2, MSGBOX_DEFAULT
	msgbox Hollowbrook_Text_GrandpaLeagueName, MSGBOX_DEFAULT
	setflag FLAG_HOLLOWBROOK_GRANDPA_NAME_TOLD
	release
	end

Hollowbrook_GoldsworthHouse_EventScript_GrandpaIdle::
	msgbox Hollowbrook_Text_GrandpaLeagueIdle, MSGBOX_DEFAULT
	release
	end
