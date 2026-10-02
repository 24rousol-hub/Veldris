@ ===========================================================================
@ DRAFT, UNBUILT, not included in data/event_scripts.s.
@ Status: PROPOSED. Hand-written scripts.inc style (NOT Poryscript).
@
@ VeldrisRoute1 (Hollowbrook to Crestfall; 2026-10-01: dialogue now has surveyors and extra NPCs the script draft does not place yet). Paste into
@ data/maps/VeldrisRoute1/scripts.inc once the map is built in Porymap (close or
@ reload Porymap first). Text labels come from design/dialogue/route1.inc and are
@ appended to the same scripts.inc (each label exactly once):
@   VeldrisRoute1_Text_SignWest, SignEast, Trainer1Intro/Defeat/After,
@   Trainer2Intro/Defeat/After, Trainer3Intro/Defeat/After, GuideGive, GuideAfter,
@   TrogSighting.
@
@ PLACEHOLDER FLAGS AND VARS (proposed, NOT claimed; list in design/scripts/README.md):
@   FLAG_ROUTE1_GUIDE_POTIONS          guide's 3 POTIONs given
@   FLAG_HIDDEN_ITEM_ROUTE1_POTION     hidden POTION (bg_event, hidden item)
@   FLAG_HIDDEN_ITEM_ROUTE1_REPEL      hidden REPEL (bg_event, hidden item)
@   VAR_HOLLOWBROOK_STATE (proposed, see hollowbrook_scripts.inc): state 4 = Troglodyte
@                          beaten outside the lab, which gates the sighting NPC
@   Trainer defeated flags come from the trainer ids (0x500 + id), never hand-allocated.
@
@ PLACEHOLDER TRAINER CONSTANTS (each needs a block in src/data/trainers.party and, for a
@ reused vanilla Hoenn entry, a '#define TRAINER_VELDRIS_ROUTE1_X TRAINER_<OLD>' in
@ include/constants/opponents.h, see CLAUDE.md 'A new trainer'):
@   TRAINER_VELDRIS_ROUTE1_YOUNGSTER  (LILLIPUP L3)
@   TRAINER_VELDRIS_ROUTE1_LASS       (ZIGZAGOON L3, SKITTY L3)
@   TRAINER_VELDRIS_ROUTE1_FARMER     (ZIGZAGOON L4, SKITTY L4)
@
@ PLACEHOLDER LOCAL IDS (object local_id in Porymap):
@   LOCALID_VELDRIS_ROUTE1_GUIDE, LOCALID_VELDRIS_ROUTE1_SIGHTING
@
@ MAP EVENTS TO PLACE (by the author, or by Claude after the map is pushed):
@   3 trainer object events (trainer_type TRAINER_TYPE_NORMAL, sight range 3 to 4),
@     scripts VeldrisRoute1_EventScript_Youngster / _Lass / _Farmer
@   guide NPC, sighting NPC (flag FLAG_HIDE_... is NOT used: see note at the NPC)
@   2 bg_events (sign): west sign, east sign
@   2 bg_events (hidden_item): POTION (flag FLAG_HIDDEN_ITEM_ROUTE1_POTION) and REPEL
@   Map connections: west edge to Hollowbrook, east edge to Crestfall.
@   No triggers and no map scripts are needed.
@ ===========================================================================

VeldrisRoute1_MapScripts::
	.byte 0

@ ---- Signs ----

VeldrisRoute1_EventScript_SignWest::
	msgbox VeldrisRoute1_Text_SignWest, MSGBOX_SIGN
	end

VeldrisRoute1_EventScript_SignEast::
	msgbox VeldrisRoute1_Text_SignEast, MSGBOX_SIGN
	end

@ ---- Trainers (vanilla Route102 pattern: trainerbattle_single, then the after text) ----

VeldrisRoute1_EventScript_Youngster::
	trainerbattle_single TRAINER_VELDRIS_ROUTE1_YOUNGSTER, VeldrisRoute1_Text_Trainer1Intro, VeldrisRoute1_Text_Trainer1Defeat
	msgbox VeldrisRoute1_Text_Trainer1After, MSGBOX_AUTOCLOSE
	end

VeldrisRoute1_EventScript_Lass::
	trainerbattle_single TRAINER_VELDRIS_ROUTE1_LASS, VeldrisRoute1_Text_Trainer2Intro, VeldrisRoute1_Text_Trainer2Defeat
	msgbox VeldrisRoute1_Text_Trainer2After, MSGBOX_AUTOCLOSE
	end

VeldrisRoute1_EventScript_Farmer::
	trainerbattle_single TRAINER_VELDRIS_ROUTE1_FARMER, VeldrisRoute1_Text_Trainer3Intro, VeldrisRoute1_Text_Trainer3Defeat
	msgbox VeldrisRoute1_Text_Trainer3After, MSGBOX_AUTOCLOSE
	end

@ ---- Guide: gives 3 POTIONs once ----
@ The dialogue text GuideGive already says '{PLAYER} received 3 POTIONs!', so the gift is
@ made with giveitem_msg (which prints that text with the item fanfare) after checking
@ there is bag space. If the bag is full nothing is given and the flag stays clear, so
@ the guide offers again. (Vanilla 'giveitem' prints its own message and would repeat it.)
VeldrisRoute1_EventScript_Guide::
	lock
	faceplayer
	goto_if_set FLAG_ROUTE1_GUIDE_POTIONS, VeldrisRoute1_EventScript_GuideAfter
	checkitemspace ITEM_POTION, 3
	goto_if_eq VAR_RESULT, FALSE, VeldrisRoute1_EventScript_GuideBagFull
	giveitem_msg VeldrisRoute1_Text_GuideGive, ITEM_POTION, 3
	setflag FLAG_ROUTE1_GUIDE_POTIONS
	release
	end

VeldrisRoute1_EventScript_GuideAfter::
	msgbox VeldrisRoute1_Text_GuideAfter, MSGBOX_DEFAULT
	release
	end

VeldrisRoute1_EventScript_GuideBagFull::
	msgbox gText_TooBadBagIsFull, MSGBOX_DEFAULT
	release
	end

@ ---- Troglodyte sighting (optional, can be dropped) ----
@ A farmer who only makes sense after the first fight. Gated by state, not a hide flag:
@ before the fight he repeats the guide-style tip (GuideAfter, a stand-in). No extra flag.
VeldrisRoute1_EventScript_Sighting::
	lock
	faceplayer
	goto_if_ge VAR_HOLLOWBROOK_STATE, 4, VeldrisRoute1_EventScript_SightingTalk
	msgbox VeldrisRoute1_Text_GuideAfter, MSGBOX_DEFAULT
	release
	end

VeldrisRoute1_EventScript_SightingTalk::
	msgbox VeldrisRoute1_Text_TrogSighting, MSGBOX_DEFAULT
	release
	end
