@ Hollowbrook_ProfFennickLab: Prof. Fennick's lab and the four-starter scene.
@ Built from design/scripts/hollowbrook_lab_scripts.inc (coordinates filled in for this map).
@ Species are stand-ins until the author picks: Treecko, Torchic, Mudkip on show, Pikachu
@ (VELDRIS_FOURTH_STARTER in src/starter_choose.c) as the revealed fourth.
@
@ Layout: Fennick (7,4) behind the 4-wide table (5..8,5), counter row (5..8,6), balls on (5..8,5).
@ Troglodyte starts at (4,7). Door mats (6,11)/(7,11); scene trigger and exit blocker on (6,10)/(7,10).
@ VAR_HOLLOWBROOK_STATE: 0 new game, 1 mom woke player, 2 Trog has his ball (player choosing),
@ 3 player chose (Trog waits outside), 4 Trog beaten outside.

Hollowbrook_ProfFennickLab_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, Hollowbrook_ProfFennickLab_OnTransition
	.byte 0

@ The fourth ball is revealed mid-scene, so it starts hidden until the scene has run.
Hollowbrook_ProfFennickLab_OnTransition:
	call_if_lt VAR_HOLLOWBROOK_STATE, 2, Hollowbrook_ProfFennickLab_EventScript_HideBall4
	end

Hollowbrook_ProfFennickLab_EventScript_HideBall4::
	setflag FLAG_HIDE_HOLLOWBROOK_LAB_BALL_4
	return

@ Shared helper: {STR_VAR_2} = Troglodyte's species. (Also used by the town scripts later;
@ define it only here.)
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

@ ===========================================================================
@ THE TROGLODYTE SCENE (coord_event at the door, state 0 or 1)
@ ===========================================================================

Hollowbrook_ProfFennickLab_EventScript_TrogScene::
	lockall
	applymovement LOCALID_PLAYER, Hollowbrook_ProfFennickLab_Movement_PlayerWalkIn
	waitmovement 0
	msgbox Hollowbrook_Text_LabTrogScene1, MSGBOX_DEFAULT
	closemessage
	applymovement LOCALID_HOLLOWBROOK_LAB_FENNICK, Common_Movement_FacePlayer
	waitmovement 0
	msgbox Hollowbrook_Text_LabTrogScene2, MSGBOX_DEFAULT
	closemessage
	applymovement LOCALID_HOLLOWBROOK_LAB_TROG, Common_Movement_FacePlayer
	waitmovement 0
	msgbox Hollowbrook_Text_LabTrogScene3, MSGBOX_DEFAULT
	msgbox Hollowbrook_Text_LabTrogScene4, MSGBOX_DEFAULT
	msgbox Hollowbrook_Text_LabTrogScene5, MSGBOX_DEFAULT
	msgbox Hollowbrook_Text_LabTrogScene6, MSGBOX_DEFAULT
	closemessage
	@ His random pick: 0, 1 or 2. VAR_TROG_STARTER is read by every Troglodyte battle
	@ (trainer pool prune in src/trainer_pools.c).
	random 3
	copyvar VAR_TROG_STARTER, VAR_RESULT
	call Hollowbrook_EventScript_BufferTrogSpecies
	switch VAR_TROG_STARTER
	case 0, Hollowbrook_ProfFennickLab_EventScript_TrogWalksToBall1
	case 1, Hollowbrook_ProfFennickLab_EventScript_TrogWalksToBall2
	case 2, Hollowbrook_ProfFennickLab_EventScript_TrogWalksToBall3
	end

Hollowbrook_ProfFennickLab_EventScript_TrogWalksToBall1::
	applymovement LOCALID_HOLLOWBROOK_LAB_TROG, Hollowbrook_ProfFennickLab_Movement_TrogToBall1
	waitmovement 0
	removeobject LOCALID_HOLLOWBROOK_LAB_BALL_1
	setflag FLAG_HIDE_HOLLOWBROOK_LAB_BALL_1
	call Hollowbrook_ProfFennickLab_EventScript_TrogTakesBall
	applymovement LOCALID_HOLLOWBROOK_LAB_TROG, Hollowbrook_ProfFennickLab_Movement_TrogLeavesFromBall1
	goto Hollowbrook_ProfFennickLab_EventScript_TrogGone
	end

Hollowbrook_ProfFennickLab_EventScript_TrogWalksToBall2::
	applymovement LOCALID_HOLLOWBROOK_LAB_TROG, Hollowbrook_ProfFennickLab_Movement_TrogToBall2
	waitmovement 0
	removeobject LOCALID_HOLLOWBROOK_LAB_BALL_2
	setflag FLAG_HIDE_HOLLOWBROOK_LAB_BALL_2
	call Hollowbrook_ProfFennickLab_EventScript_TrogTakesBall
	applymovement LOCALID_HOLLOWBROOK_LAB_TROG, Hollowbrook_ProfFennickLab_Movement_TrogLeavesFromBall2
	goto Hollowbrook_ProfFennickLab_EventScript_TrogGone
	end

Hollowbrook_ProfFennickLab_EventScript_TrogWalksToBall3::
	applymovement LOCALID_HOLLOWBROOK_LAB_TROG, Hollowbrook_ProfFennickLab_Movement_TrogToBall3
	waitmovement 0
	removeobject LOCALID_HOLLOWBROOK_LAB_BALL_3
	setflag FLAG_HIDE_HOLLOWBROOK_LAB_BALL_3
	call Hollowbrook_ProfFennickLab_EventScript_TrogTakesBall
	applymovement LOCALID_HOLLOWBROOK_LAB_TROG, Hollowbrook_ProfFennickLab_Movement_TrogLeavesFromBall3
	goto Hollowbrook_ProfFennickLab_EventScript_TrogGone
	end

@ {STR_VAR_2} is already buffered with his species.
Hollowbrook_ProfFennickLab_EventScript_TrogTakesBall::
	playse SE_PIN
	msgbox Hollowbrook_Text_LabTrogTakes, MSGBOX_DEFAULT
	applymovement LOCALID_HOLLOWBROOK_LAB_TROG, Common_Movement_FacePlayer
	waitmovement 0
	msgbox Hollowbrook_Text_LabTrogSneer, MSGBOX_DEFAULT
	closemessage
	return

Hollowbrook_ProfFennickLab_EventScript_TrogGone::
	waitmovement 0
	playse SE_EXIT
	removeobject LOCALID_HOLLOWBROOK_LAB_TROG
	setflag FLAG_HIDE_HOLLOWBROOK_LAB_TROG
	delay 30
	msgbox Hollowbrook_Text_LabTrogLeaves, MSGBOX_DEFAULT
	@ Until the player picks a ball the exit is blocked (see ExitBlocker).
	setvar VAR_HOLLOWBROOK_STATE, 2
	applymovement LOCALID_HOLLOWBROOK_LAB_FENNICK, Common_Movement_FacePlayer
	waitmovement 0
	msgbox Hollowbrook_Text_LabApology1, MSGBOX_DEFAULT
	msgbox Hollowbrook_Text_LabApology2, MSGBOX_DEFAULT
	closemessage
	@ The fourth ball appears.
	clearflag FLAG_HIDE_HOLLOWBROOK_LAB_BALL_4
	addobject LOCALID_HOLLOWBROOK_LAB_BALL_4
	playse SE_PIN
	delay 30
	msgbox Hollowbrook_Text_LabApology3, MSGBOX_DEFAULT
	@ TODO: clearflag FLAG_HIDE_HOLLOWBROOK_GRANDPA once the town and that flag exist.
	releaseall
	end

@ Player steps from the door trigger row (10) up to row 9.
Hollowbrook_ProfFennickLab_Movement_PlayerWalkIn:
	walk_up
	step_end

@ Troglodyte starts at (4,7), left of the table front. Ball k is at (4+k,5), behind the
@ counter row, so he stands at (4+k,7) facing up.
Hollowbrook_ProfFennickLab_Movement_TrogToBall1:
	walk_right
	face_up
	step_end

Hollowbrook_ProfFennickLab_Movement_TrogToBall2:
	walk_right
	walk_right
	face_up
	step_end

Hollowbrook_ProfFennickLab_Movement_TrogToBall3:
	walk_right
	walk_right
	walk_right
	face_up
	step_end

@ Out along column 5 (left of where the player stands), then onto the door mat.
Hollowbrook_ProfFennickLab_Movement_TrogLeavesFromBall1:
	walk_down
	walk_down
	walk_down
	walk_down
	walk_right
	step_end

Hollowbrook_ProfFennickLab_Movement_TrogLeavesFromBall2:
	walk_left
	walk_down
	walk_down
	walk_down
	walk_down
	walk_right
	step_end

Hollowbrook_ProfFennickLab_Movement_TrogLeavesFromBall3:
	walk_left
	walk_left
	walk_down
	walk_down
	walk_down
	walk_down
	walk_right
	step_end

@ While state is 2 the player may not leave without a starter.
Hollowbrook_ProfFennickLab_EventScript_ExitBlocker::
	lockall
	applymovement LOCALID_HOLLOWBROOK_LAB_FENNICK, Common_Movement_FacePlayer
	waitmovement 0
	msgbox Hollowbrook_Text_LabExitBlocked, MSGBOX_DEFAULT
	closemessage
	applymovement LOCALID_PLAYER, Hollowbrook_ProfFennickLab_Movement_StepBackIn
	waitmovement 0
	releaseall
	end

Hollowbrook_ProfFennickLab_Movement_StepBackIn:
	walk_up
	step_end

@ ===========================================================================
@ THE FOUR POKE BALLS (talk across the counter row). VAR_0x8008 = ball number.
@ ===========================================================================

Hollowbrook_ProfFennickLab_EventScript_Ball1::
	lock
	goto_if_ge VAR_HOLLOWBROOK_STATE, 3, Hollowbrook_ProfFennickLab_EventScript_BallGone
	goto_if_lt VAR_HOLLOWBROOK_STATE, 2, Hollowbrook_ProfFennickLab_EventScript_BallNotYet
	setvar VAR_0x8008, 1
	bufferspeciesname STR_VAR_1, SPECIES_TREECKO
	showmonpic SPECIES_TREECKO, 10, 3
	msgbox Hollowbrook_Text_LabBallAsk, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Hollowbrook_ProfFennickLab_EventScript_BallDeclined
	setvar VAR_TEMP_TRANSFERRED_SPECIES, SPECIES_TREECKO
	setvar VAR_STARTER_MON, 0
	givemon SPECIES_TREECKO, 5
	goto Hollowbrook_ProfFennickLab_EventScript_BallGiven
	end

Hollowbrook_ProfFennickLab_EventScript_Ball2::
	lock
	goto_if_ge VAR_HOLLOWBROOK_STATE, 3, Hollowbrook_ProfFennickLab_EventScript_BallGone
	goto_if_lt VAR_HOLLOWBROOK_STATE, 2, Hollowbrook_ProfFennickLab_EventScript_BallNotYet
	setvar VAR_0x8008, 2
	bufferspeciesname STR_VAR_1, SPECIES_TORCHIC
	showmonpic SPECIES_TORCHIC, 10, 3
	msgbox Hollowbrook_Text_LabBallAsk, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Hollowbrook_ProfFennickLab_EventScript_BallDeclined
	setvar VAR_TEMP_TRANSFERRED_SPECIES, SPECIES_TORCHIC
	setvar VAR_STARTER_MON, 1
	givemon SPECIES_TORCHIC, 5
	goto Hollowbrook_ProfFennickLab_EventScript_BallGiven
	end

Hollowbrook_ProfFennickLab_EventScript_Ball3::
	lock
	goto_if_ge VAR_HOLLOWBROOK_STATE, 3, Hollowbrook_ProfFennickLab_EventScript_BallGone
	goto_if_lt VAR_HOLLOWBROOK_STATE, 2, Hollowbrook_ProfFennickLab_EventScript_BallNotYet
	setvar VAR_0x8008, 3
	bufferspeciesname STR_VAR_1, SPECIES_MUDKIP
	showmonpic SPECIES_MUDKIP, 10, 3
	msgbox Hollowbrook_Text_LabBallAsk, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Hollowbrook_ProfFennickLab_EventScript_BallDeclined
	setvar VAR_TEMP_TRANSFERRED_SPECIES, SPECIES_MUDKIP
	setvar VAR_STARTER_MON, 2
	givemon SPECIES_MUDKIP, 5
	goto Hollowbrook_ProfFennickLab_EventScript_BallGiven
	end

@ The fourth starter (stand-in PIKACHU, same as VELDRIS_FOURTH_STARTER). VAR_STARTER_MON 3
@ is valid because sStarterMon has a fourth entry.
Hollowbrook_ProfFennickLab_EventScript_Ball4::
	lock
	goto_if_ge VAR_HOLLOWBROOK_STATE, 3, Hollowbrook_ProfFennickLab_EventScript_BallGone
	setvar VAR_0x8008, 4
	bufferspeciesname STR_VAR_1, SPECIES_PIKACHU
	showmonpic SPECIES_PIKACHU, 10, 3
	msgbox Hollowbrook_Text_LabBallAsk, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Hollowbrook_ProfFennickLab_EventScript_BallDeclined
	setvar VAR_TEMP_TRANSFERRED_SPECIES, SPECIES_PIKACHU
	setvar VAR_STARTER_MON, 3
	givemon SPECIES_PIKACHU, 5
	goto Hollowbrook_ProfFennickLab_EventScript_BallGiven
	end

Hollowbrook_ProfFennickLab_EventScript_BallDeclined::
	hidemonpic
	release
	end

@ After the choice, the two leftover balls stay on the table but are not for taking.
Hollowbrook_ProfFennickLab_EventScript_BallGone::
	msgbox Hollowbrook_Text_LabBallGone, MSGBOX_DEFAULT
	release
	end

@ Only reachable if the scene is skipped somehow (debug warps).
Hollowbrook_ProfFennickLab_EventScript_BallNotYet::
	msgbox Hollowbrook_Text_LabBallNotYet, MSGBOX_DEFAULT
	release
	end

@ Shared tail. VAR_RESULT still holds givemon's answer here.
Hollowbrook_ProfFennickLab_EventScript_BallGiven::
	goto_if_eq VAR_RESULT, MON_GIVEN_TO_PARTY, Hollowbrook_ProfFennickLab_EventScript_ChosenToParty
	goto_if_eq VAR_RESULT, MON_GIVEN_TO_PC, Hollowbrook_ProfFennickLab_EventScript_ChosenToPC
	hidemonpic
	goto Common_EventScript_NoMoreRoomForPokemon
	end

Hollowbrook_ProfFennickLab_EventScript_ChosenToParty::
	call Hollowbrook_ProfFennickLab_EventScript_AnnounceChoice
	call Hollowbrook_ProfFennickLab_EventScript_TakeChosenBall
	msgbox gText_NicknameThisPokemon, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Hollowbrook_ProfFennickLab_EventScript_ChoiceDone
	call Common_EventScript_GetGiftMonPartySlot
	call Common_EventScript_NameReceivedPartyMon
	goto Hollowbrook_ProfFennickLab_EventScript_ChoiceDone
	end

Hollowbrook_ProfFennickLab_EventScript_ChosenToPC::
	call Hollowbrook_ProfFennickLab_EventScript_AnnounceChoice
	call Hollowbrook_ProfFennickLab_EventScript_TakeChosenBall
	msgbox gText_NicknameThisPokemon, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Hollowbrook_ProfFennickLab_EventScript_ChosenTransferred
	call Common_EventScript_NameReceivedBoxMon
	goto Hollowbrook_ProfFennickLab_EventScript_ChosenTransferred
	end

Hollowbrook_ProfFennickLab_EventScript_ChosenTransferred::
	call Common_EventScript_TransferredToPC
	goto Hollowbrook_ProfFennickLab_EventScript_ChoiceDone
	end

Hollowbrook_ProfFennickLab_EventScript_AnnounceChoice::
	playfanfare MUS_OBTAIN_ITEM
	message Hollowbrook_Text_LabBallChosen
	waitmessage
	waitfanfare
	return

Hollowbrook_ProfFennickLab_EventScript_TakeChosenBall::
	switch VAR_0x8008
	case 1, Hollowbrook_ProfFennickLab_EventScript_TakeBall1
	case 2, Hollowbrook_ProfFennickLab_EventScript_TakeBall2
	case 3, Hollowbrook_ProfFennickLab_EventScript_TakeBall3
	case 4, Hollowbrook_ProfFennickLab_EventScript_TakeBall4
	return

Hollowbrook_ProfFennickLab_EventScript_TakeBall1::
	removeobject LOCALID_HOLLOWBROOK_LAB_BALL_1
	setflag FLAG_HIDE_HOLLOWBROOK_LAB_BALL_1
	return

Hollowbrook_ProfFennickLab_EventScript_TakeBall2::
	removeobject LOCALID_HOLLOWBROOK_LAB_BALL_2
	setflag FLAG_HIDE_HOLLOWBROOK_LAB_BALL_2
	return

Hollowbrook_ProfFennickLab_EventScript_TakeBall3::
	removeobject LOCALID_HOLLOWBROOK_LAB_BALL_3
	setflag FLAG_HIDE_HOLLOWBROOK_LAB_BALL_3
	return

Hollowbrook_ProfFennickLab_EventScript_TakeBall4::
	removeobject LOCALID_HOLLOWBROOK_LAB_BALL_4
	setflag FLAG_HIDE_HOLLOWBROOK_LAB_BALL_4
	return

@ State 3 lets Troglodyte appear outside and unblocks the door. No Pokedex handout yet.
Hollowbrook_ProfFennickLab_EventScript_ChoiceDone::
	hidemonpic
	setvar VAR_HOLLOWBROOK_STATE, 3
	setflag FLAG_SYS_POKEMON_GET
	setflag FLAG_ADVENTURE_STARTED
	applymovement LOCALID_HOLLOWBROOK_LAB_FENNICK, Common_Movement_FacePlayer
	waitmovement 0
	msgbox Hollowbrook_Text_LabAfterChoice, MSGBOX_DEFAULT
	release
	end

@ ===========================================================================
@ LAB NPCS AND FURNITURE
@ ===========================================================================

Hollowbrook_ProfFennickLab_EventScript_AideNervous::
	lock
	faceplayer
	goto_if_ge VAR_HOLLOWBROOK_STATE, 3, Hollowbrook_ProfFennickLab_EventScript_AideNervousAfter
	msgbox Hollowbrook_Text_AideNervous, MSGBOX_DEFAULT
	release
	end

Hollowbrook_ProfFennickLab_EventScript_AideNervousAfter::
	call Hollowbrook_EventScript_BufferTrogSpecies
	msgbox Hollowbrook_Text_AideNervousAfter, MSGBOX_DEFAULT
	release
	end

Hollowbrook_ProfFennickLab_EventScript_AideDeadpan::
	lock
	faceplayer
	goto_if_ge VAR_HOLLOWBROOK_STATE, 3, Hollowbrook_ProfFennickLab_EventScript_AideDeadpanAfter
	msgbox Hollowbrook_Text_AideDeadpan, MSGBOX_DEFAULT
	release
	end

Hollowbrook_ProfFennickLab_EventScript_AideDeadpanAfter::
	call Hollowbrook_EventScript_BufferTrogSpecies
	msgbox Hollowbrook_Text_AideDeadpanAfter, MSGBOX_DEFAULT
	release
	end

Hollowbrook_ProfFennickLab_EventScript_Fennick::
	lock
	faceplayer
	goto_if_ge VAR_HOLLOWBROOK_STATE, 4, Hollowbrook_ProfFennickLab_EventScript_FennickRepeat
	goto_if_ge VAR_HOLLOWBROOK_STATE, 3, Hollowbrook_ProfFennickLab_EventScript_FennickAfter
	msgbox Hollowbrook_Text_LabApology3, MSGBOX_DEFAULT
	release
	end

Hollowbrook_ProfFennickLab_EventScript_FennickAfter::
	msgbox Hollowbrook_Text_FennickIdleAfter, MSGBOX_DEFAULT
	release
	end

Hollowbrook_ProfFennickLab_EventScript_FennickRepeat::
	msgbox Hollowbrook_Text_FennickIdleAfter2, MSGBOX_DEFAULT
	release
	end

Hollowbrook_ProfFennickLab_EventScript_Computer::
	msgbox Hollowbrook_Text_LabComputer, MSGBOX_SIGN
	end

Hollowbrook_ProfFennickLab_EventScript_Notes::
	msgbox Hollowbrook_Text_LabNotes, MSGBOX_SIGN
	end

Hollowbrook_ProfFennickLab_EventScript_Machine::
	msgbox Hollowbrook_Text_LabMachine, MSGBOX_SIGN
	end

@ ===========================================================================
@ TEXT (from design/dialogue/hollowbrook.inc, plus the lab-only lines below)
@ ===========================================================================

Hollowbrook_Text_LabExitBlocked::
	.string "Oh, please don't leave yet.\n"
	.string "Choose one of the POKéMON first.$"

Hollowbrook_Text_LabBallGone::
	.string "The other POKé BALLS are not\n"
	.string "for taking. Nice try.$"

Hollowbrook_Text_LabBallNotYet::
	.string "A POKé BALL. Better not touch it\n"
	.string "without asking the PROFESSOR.$"

Hollowbrook_Text_LabNotes::
	.string "Research notes on POKéMON habitats\n"
	.string "around the VELDRIS region.$"

Hollowbrook_Text_LabMachine::
	.string "It's a machine for studying\n"
	.string "POKéMON. It's humming softly.$"


Hollowbrook_Text_AideNervous::
	.string "Oh! Oh, thank goodness.\n"
	.string "Somebody sensible.\p"
	.string "There's a... a person in the\n"
	.string "back. He's very loud.$"

Hollowbrook_Text_AideDeadpan::
	.string "Between us, the staff call him\n"
	.string "TROGLODYTE.\p"
	.string "Not to his face. We like our\n"
	.string "jobs, and our shoes.$"

Hollowbrook_Text_AideNervousAfter::
	.string "He took the {STR_VAR_2}, didn't he.\n"
	.string "I'm sorry. I'd have given him\l"
	.string "the ZIGZAGOON.\p"
	.string "Nobody ever stands up to him.$"

Hollowbrook_Text_AideDeadpanAfter::
	.string "Bet you ten that the {STR_VAR_2}\n"
	.string "bites him by Route 2.$"

Hollowbrook_Text_LabTrogScene1::
	.string "...three HOURS! I waited three\n"
	.string "hours in this damn MILTANK pasture!\p"
	.string "Where is my grandfather? He\n"
	.string "wrote that he'd be here!$"

Hollowbrook_Text_LabTrogScene2::
	.string "Ah. {PLAYER}. Good timing.\n"
	.string "Or possibly awful timing.\p"
	.string "BEAUREGARD, this is the young\n"
	.string "person I was telling you about.$"

Hollowbrook_Text_LabTrogScene3::
	.string "Who? Him? Her? Whatever. Do I\n"
	.string "look like I care?\p"
	.string "Professor, the old man promised\n"
	.string "me a POKéMON. You have some.$"

Hollowbrook_Text_LabTrogScene4::
	.string "Those are for new trainers,\n"
	.string "BEAUREGARD. Not for...\p"
	.string "Did I ask? Do you know who my\n"
	.string "father is? Do you know who\l"
	.string "OWNS this building?$"

Hollowbrook_Text_LabTrogScene5::
	.string "Technically the professor\n"
	.string "owns the building.\p"
	.string "Nobody asked you. Hand one\n"
	.string "over. Hell, I'll even say\l"
	.string "please. Once.$"

Hollowbrook_Text_LabTrogScene6::
	.string "...Oh, very well.\n"
	.string "Choose, BEAUREGARD.$"

Hollowbrook_Text_LabTrogTakes::
	.string "Hah! This one. Obviously.\p"
	.string "I was going to pick the\n"
	.string "{STR_VAR_2} anyway. Good taste\l"
	.string "is hereditary.$"

Hollowbrook_Text_LabTrogSneer::
	.string "You're in my light.\n"
	.string "Move, whoever you are.\p"
	.string "I'll be Champion before you've\n"
	.string "tied those shoes.\p"
	.string "Tell my grandfather I was here.\n"
	.string "Actually, don't. He'd only ask\l"
	.string "if I behaved.$"

Hollowbrook_Text_LabTrogLeaves::
	.string "The door slams. Outside, a\n"
	.string "ZIGZAGOON yelps and scatters.$"

Hollowbrook_Text_LabApology1::
	.string "Oh dear. I am so sorry,\n"
	.string "{PLAYER}. You came for a\l"
	.string "POKéMON and got... that.$"

Hollowbrook_Text_LabApology2::
	.string "I always keep one back for\n"
	.string "emergencies. I think this\l"
	.string "counts as one.$"

Hollowbrook_Text_LabApology3::
	.string "Please, have a look. The fourth\n"
	.string "was in the back room.\p"
	.string "Choose whichever you like.\n"
	.string "Any of the three that are left.$"

Hollowbrook_Text_LabBallAsk::
	.string "Choose the {STR_VAR_1}?$"

Hollowbrook_Text_LabBallChosen::
	.string "{PLAYER} chose the {STR_VAR_1}!$"

Hollowbrook_Text_LabAfterChoice::
	.string "A fine choice. Look after it.\n"
	.string "And do try to be kind.\p"
	.string "It's very hard to be unkind to\n"
	.string "someone who is kind to you.\p"
	.string "...Not impossible. But hard.$"

Hollowbrook_Text_FennickIdleAfter::
	.string "Off you go, {PLAYER}.\n"
	.string "Write when you can.\p"
	.string "Or don't. Just win something.$"

Hollowbrook_Text_FennickIdleAfter2::
	.string "Oh, hello, {PLAYER}. I'm just\n"
	.string "mending a kettle. With a\l"
	.string "POKéMON.$"

Hollowbrook_Text_LabBookshelf::
	.string "Rows of notes. ‘On The Habits\n"
	.string "of ZIGZAGOON’ has been borrowed\l"
	.string "eleven times by the same person.$"

Hollowbrook_Text_LabComputer::
	.string "A screen full of ZIGZAGOON weights.\n"
	.string "One is labelled ‘Menace.’$"
