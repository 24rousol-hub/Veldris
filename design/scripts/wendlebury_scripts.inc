@ ===========================================================================
@ DRAFT, UNBUILT, not included in data/event_scripts.s.
@ Status: PROPOSED. Hand-written scripts.inc style (NOT Poryscript).
@
@ Wendlebury (town 3): town exterior, Pokemon Center 1F and the Mart. Paste each
@ SECTION into the matching map's scripts.inc once the maps exist in Porymap (close or
@ reload Porymap first):
@   1. Wendlebury                 -> data/maps/Wendlebury/scripts.inc
@   2. Wendlebury_PokemonCenter_1F -> its scripts.inc (copy of vanilla Oldale's Center)
@   3. Wendlebury_Mart            -> its scripts.inc (copy of vanilla Oldale's Mart)
@ Text labels come from design/dialogue/wendlebury.inc, appended to the scripts.inc of
@ the map that uses them (each label exactly once):
@   Town: Wendlebury_Text_TownSign, CenterSign, MartSign, Trader, Kid, Gossip,
@         TravellerNorth, TravellerNorthAfter, BarricadeMan, ResidentA, ResidentB.
@   Center: Wendlebury_Text_CenterVisitor.
@   Mart: Wendlebury_Text_MartClerk.
@   NOT used: Wendlebury_Text_CenterNurse and CenterNurseDone. Vanilla's nurse is the
@   shared Common_EventScript_PkmnCenterNurse, which prints the standard 'Welcome to our
@   POKeMON CENTER' texts (gText_*). To use the Wendlebury wording the nurse would need
@   its own script; not done (engine-free, but larger). Delete those two labels or keep
@   them as spares.
@
@ PLACEHOLDER FLAGS AND VARS (NOT claimed; list in design/scripts/README.md):
@   FLAG_VISITED_WENDLEBURY  fly flag (row in src/data/veldris_fly_towns.h)
@   HEAL_LOCATION_WENDLEBURY heal location constant (src/data/heal_locations.json; write
@                            respawn_map BEFORE respawn_npc, both required, CLAUDE.md)
@   Existing vanilla: FLAG_BADGE01_GET (used by the traveller's 'after' line).
@   No other flags. No triggers.
@
@ PLACEHOLDER LOCAL IDS (object local_id in Porymap):
@   LOCALID_WENDLEBURY_NURSE (Center), LOCALID_WENDLEBURY_CLERK (Mart, optional)
@
@ MAP EVENTS TO PLACE: signs as bg_events, NPCs as object events, door warps, the Route 1
@ and Route 2 connections, the heal location. The barricade man stands in the east exit.
@ ===========================================================================

@ ===========================================================================
@ SECTION 1: Wendlebury (town exterior)
@ ===========================================================================

Wendlebury_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, Wendlebury_OnTransition
	.byte 0

Wendlebury_OnTransition:
	setflag FLAG_VISITED_WENDLEBURY
	end

Wendlebury_EventScript_TownSign::
	msgbox Wendlebury_Text_TownSign, MSGBOX_SIGN
	end

Wendlebury_EventScript_CenterSign::
	msgbox Wendlebury_Text_CenterSign, MSGBOX_SIGN
	end

Wendlebury_EventScript_MartSign::
	msgbox Wendlebury_Text_MartSign, MSGBOX_SIGN
	end

Wendlebury_EventScript_Trader::
	msgbox Wendlebury_Text_Trader, MSGBOX_NPC
	end

Wendlebury_EventScript_Kid::
	msgbox Wendlebury_Text_Kid, MSGBOX_NPC
	end

Wendlebury_EventScript_Gossip::
	msgbox Wendlebury_Text_Gossip, MSGBOX_NPC
	end

@ Traveller: warns about men in suits on Route 2 until the player has the first badge.
Wendlebury_EventScript_TravellerNorth::
	lock
	faceplayer
	goto_if_set FLAG_BADGE01_GET, Wendlebury_EventScript_TravellerNorthAfter
	msgbox Wendlebury_Text_TravellerNorth, MSGBOX_DEFAULT
	release
	end

Wendlebury_EventScript_TravellerNorthAfter::
	msgbox Wendlebury_Text_TravellerNorthAfter, MSGBOX_DEFAULT
	release
	end

Wendlebury_EventScript_BarricadeMan::
	msgbox Wendlebury_Text_BarricadeMan, MSGBOX_NPC
	end

Wendlebury_EventScript_ResidentA::
	msgbox Wendlebury_Text_ResidentA, MSGBOX_NPC
	end

Wendlebury_EventScript_ResidentB::
	msgbox Wendlebury_Text_ResidentB, MSGBOX_NPC
	end

@ ===========================================================================
@ SECTION 2: Wendlebury_PokemonCenter_1F
@ Same as Oldale's Center: sets the respawn point, runs the heal script, and keeps the
@ cable club hook (CableClub_OnResume) so the 2F link rooms work if 2F is built.
@ ===========================================================================

Wendlebury_PokemonCenter_1F_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, Wendlebury_PokemonCenter_1F_OnTransition
	map_script MAP_SCRIPT_ON_RESUME, CableClub_OnResume
	.byte 0

Wendlebury_PokemonCenter_1F_OnTransition:
	setrespawn HEAL_LOCATION_WENDLEBURY
	end

@ Vanilla heal script: the nurse object's local id goes in VAR_0x800B.
Wendlebury_PokemonCenter_1F_EventScript_Nurse::
	setvar VAR_0x800B, LOCALID_WENDLEBURY_NURSE
	call Common_EventScript_PkmnCenterNurse
	waitmessage
	waitbuttonpress
	release
	end

Wendlebury_PokemonCenter_1F_EventScript_Visitor::
	msgbox Wendlebury_Text_CenterVisitor, MSGBOX_NPC
	end

@ ===========================================================================
@ SECTION 3: Wendlebury_Mart
@ Stock (PROPOSED, wendlebury.md): POKE BALL, POTION, ANTIDOTE, PARALYZE HEAL.
@ Same pattern as Oldale's Mart: lock, faceplayer, greeting, pokemart, goodbye.
@ The vanilla 'expanded stock after ADVENTURE_STARTED' split is not needed: by the
@ time the player reaches Wendlebury the adventure has started, so there is one list.
@ ===========================================================================

Wendlebury_Mart_MapScripts::
	.byte 0

Wendlebury_Mart_EventScript_Clerk::
	lock
	faceplayer
	message Wendlebury_Text_MartClerk
	waitmessage
	pokemart Wendlebury_Mart_Pokemart
	msgbox gText_PleaseComeAgain, MSGBOX_DEFAULT
	release
	end

	.align 2
Wendlebury_Mart_Pokemart:
	.2byte ITEM_POKE_BALL
	.2byte ITEM_POTION
	.2byte ITEM_ANTIDOTE
	.2byte ITEM_PARALYZE_HEAL
	pokemartlistend
