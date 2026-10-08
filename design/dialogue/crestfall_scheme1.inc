@ Crestfall Scheme 1, 'the private booking' (author, 2026-10-08). DRAFT for the author's review, not wired.
@ Author fixed: Troglodyte's attendant pushes the player aside at the gym door ('the golden boy goes first');
@ Troglodyte thinks nothing of it, it is how he was raised. The attendant is a kind, posh old man who served
@ Troglodyte's father before him. The parents booked the gym for a private session with a photographer for
@ 'the future Champion's first badge'; Greta beats him in two turns; the photo of his loss goes on the town
@ noticeboard; he battles the player to 'prove it was a fluke'.
@ PROPOSED: the attendant's name HOLLIS, the photographer, the sign and noticeboard wording, every line below.
@ Replaces the consultant lines in crestfall.inc (ConsultantOutside to GretaAfterTrog).
@ Check widths: python3 design/tools/dialogue_check.py design/dialogue/crestfall_scheme1.inc
@ {STR_VAR_2} = Troglodyte's species (set by the lab scene).

@ ===================================================================
@ SETUP (Crestfall town, before the player reaches the gym)
@ ===================================================================

@ Sign hung on the gym door while the booking lasts.
Crestfall_Text_S1_GymClosedSign::
	.string "CLOSED TODAY.\n"
	.string "Private session booked by the\l"
	.string "GOLDSWORTH family.\p"
	.string "Underneath, in pencil:\n"
	.string "‘Says who?’ - G.$"

@ The hired photographer, setting up a tripod outside the gym.
Crestfall_Text_S1_Photographer::
	.string "Don't mind me. I've been hired\n"
	.string "for a very important photo.\p"
	.string "‘The future Champion's first\n"
	.string "badge.’ Their words, not mine.\p"
	.string "I was told to bring the good\n"
	.string "lens. And a lot of flattery.$"

@ A local by the square.
Crestfall_Text_S1_Local::
	.string "Some rich family booked the\n"
	.string "whole gym. For one boy.\p"
	.string "My grandson's been waiting for\n"
	.string "a challenge since breakfast.$"

@ ===================================================================
@ REVEAL (coord trigger in front of the gym door)
@ ===================================================================

@ Hollis, the attendant, steps in front of the player. Gentle, apologetic, firm.
Crestfall_Text_S1_HollisStop::
	.string "Ah. Terribly sorry, young one.\n"
	.string "Might I ask you to step aside?\p"
	.string "The young master goes first.\n"
	.string "He always has, I'm afraid.$"

@ Troglodyte walks up. The player is moved aside (scripted step), Troglodyte barely notices.
Crestfall_Text_S1_TrogArrive::
	.string "HOLLIS. The door.\p"
	.string "Oh, it's you. Wait behind me.\n"
	.string "That's where people stand.$"

Crestfall_Text_S1_HollisDoor::
	.string "Of course, young master.\n"
	.string "Mind the step.$"

@ Hollis, to the player once Troglodyte is inside. Quietly.
Crestfall_Text_S1_HollisAside::
	.string "Forgive the manners. I served\n"
	.string "his father the very same way.\p"
	.string "Golden boys go first. It's how\n"
	.string "they were raised. And I raised\l"
	.string "a fair few of them.\p"
	.string "I don't expect this will take\n"
	.string "long. One way or another.$"

@ ===================================================================
@ COLLAPSE (after a short fade: Troglodyte comes back out)
@ ===================================================================

@ The photographer comes out first.
Crestfall_Text_S1_PhotographerOut::
	.string "Well. I got the shot.\p"
	.string "It's just not the shot they\n"
	.string "paid for.$"

@ Greta at the door.
Crestfall_Text_S1_GretaDoor::
	.string "Two turns. I didn't even get\n"
	.string "to stretch.\p"
	.string "Booking's over, by the way.\n"
	.string "My gym is open. To everyone.$"

@ ===================================================================
@ TROGLODYTE BATTLES THE PLAYER (his fight 2)
@ ===================================================================

Crestfall_Text_S1_TrogToPlayer::
	.string "That was a fluke. The light was\n"
	.string "wrong. The floor was wrong.\p"
	.string "You. You're going to help me\n"
	.string "prove it. Battle me. Now.$"

@ Battle window texts.
Crestfall_Text_S1_TrogBattleIntro::
	.string "Watch closely. This is how a\n"
	.string "Goldsworth wins! Go, {STR_VAR_2}!$"

Crestfall_Text_S1_TrogBattleDefeat::
	.string "No! That's two flukes in a row!\n"
	.string "That's not even possible!$"

Crestfall_Text_S1_TrogAfter::
	.string "This town is broken. The gym is\n"
	.string "broken. You are broken.\p"
	.string "HOLLIS! Bring the car round.\n"
	.string "And delete that photo.$"

Crestfall_Text_S1_HollisLeave::
	.string "Right away, young master.\p"
	.string "...You battle very well.\n"
	.string "Please don't tell him I said so.$"

@ ===================================================================
@ HUMILIATION (the noticeboard by the square, from now on)
@ ===================================================================

@ The photographer pins the photo up as the car leaves.
Crestfall_Text_S1_PhotographerPin::
	.string "The family didn't want this\n"
	.string "photo. The town, however...\p"
	.string "There. Best work I've done\n"
	.string "all year.$"

@ The noticeboard (bg event), for the rest of the game.
Crestfall_Text_S1_Noticeboard::
	.string "CRESTFALL NOTICEBOARD\p"
	.string "A photo of a rich boy mid-yell,\n"
	.string "his POKéMON fainted at his feet.\p"
	.string "Someone has written underneath:\n"
	.string "‘The future Champion.’$"

@ A local after the scheme.
Crestfall_Text_S1_LocalAfter::
	.string "Did you see the photo? Framed\n"
	.string "it'd look lovely in the inn.\p"
	.string "My grandson finally got his\n"
	.string "challenge. Lost, mind. Happily.$"

@ ===================================================================
@ GRETA lines that mentioned the old scheme (replacements)
@ ===================================================================

@ Replaces GretaAfterTrog: she sends the player in.
Crestfall_Text_S1_GretaInvite::
	.string "That's him sorted. For about\n"
	.string "a week, I'd guess.\p"
	.string "Come on in, {PLAYER}. Mind the\n"
	.string "gates. They swing both ways.$"

@ Replaces GretaIdleAfter (it joked about MILTANK eating paperwork).
Crestfall_Text_S1_GretaIdleAfter::
	.string "Back already? Flattering.\p"
	.string "If a man with a camera asks,\n"
	.string "I'm booked. For everyone.$"
