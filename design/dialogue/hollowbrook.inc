@ Hollowbrook dialogue DRAFT. Status: PROPOSED, not wired into any map (no map exists yet).
@ Lines starting with @ are comments. Check widths with:
@   python3 design/tools/dialogue_check.py design/dialogue/hollowbrook.inc
@ When the maps exist, each label moves into the map's scripts.inc (see design/dialogue-style.md).
@ Rules used: single curly quotes for speech, TROGLODYTE/BEAUREGARD written literally, only Goldsworths swear,
@ species are not decided so the scene buffers names with {STR_VAR_1}/{STR_VAR_2} (bufferspeciesname).
@ Fennick calls him BEAUREGARD (formal). The staff call him TROGLODYTE, which seeds the nickname.

@ ===================================================================
@ MOM (the player's house)
@ ===================================================================

@ After the intro, first time in the house.
Hollowbrook_Text_MomWakeUp::
	.string "Oh, you're up! FENNICK phoned.\n"
	.string "He wants you at the lab.\p"
	.string "Be polite if you meet the\n"
	.string "Goldsworth boy. He's been\l"
	.string "stomping around town all morning.\p"
	.string "And take a clean handkerchief.\n"
	.string "You never know.$"

@ Idle, before the lab scene.
Hollowbrook_Text_MomIdleBefore::
	.string "Off to the lab, {PLAYER}.\n"
	.string "FENNICK doesn't like to wait.\p"
	.string "Well. He doesn't notice waiting.\n"
	.string "But he'd feel bad afterwards.$"

@ Right after the player gets a starter.
Hollowbrook_Text_MomGotPokemon::
	.string "You have a POKéMON! Let me see.\p"
	.string "Oh, what a face. You two are\n"
	.string "going to get into trouble.\p"
	.string "I heard about the Goldsworth\n"
	.string "boy. FENNICK told me everything.\p"
	.string "Don't let him get to you.\n"
	.string "...Or do. A little.$"

@ Idle, after the lab scene.
Hollowbrook_Text_MomIdleAfter::
	.string "Come home when you're hungry.\n"
	.string "Or when you're losing.\p"
	.string "I've made soup either way.$"

@ ===================================================================
@ SIGNS
@ ===================================================================

Hollowbrook_Text_TownSign::
	.string "HOLLOWBROOK\n"
	.string "‘A quiet place. Mind the hens.’$"

Hollowbrook_Text_LabSign::
	.string "FENNICK'S POKéMON LAB\n"
	.string "Knock. Then knock again.$"

Hollowbrook_Text_GoldsworthSign::
	.string "GOLDSWORTH HOUSE\n"
	.string "Please wipe your feet.$"

Hollowbrook_Text_PlayerHouseSign::
	.string "{PLAYER}'s house$"

@ ===================================================================
@ TOWN NPCs
@ ===================================================================

@ Farmer, by the fence. Before the lab scene.
Hollowbrook_Text_FarmerBefore::
	.string "Morning. A boy in a very clean\n"
	.string "coat went by asking for the\l"
	.string "old gentleman's house.\p"
	.string "I pointed at the big one.\n"
	.string "He didn't say thank you.$"

@ Farmer, after the lab scene.
Hollowbrook_Text_FarmerAfter::
	.string "That clean coat stormed past\n"
	.string "again. Muttering.\p"
	.string "Didn't look where he stepped.\n"
	.string "The hens saw to that.$"

@ Kid, near the pond.
Hollowbrook_Text_Kid::
	.string "I'm going to be a trainer too!\n"
	.string "When I'm older.\p"
	.string "Or when Mum says I can go past\n"
	.string "the gate. Whichever is first.$"

@ Woman with washing.
Hollowbrook_Text_Laundry::
	.string "I'd hang this out, but the hens\n"
	.string "think everything is a nest.\p"
	.string "Last week they took a sock.\n"
	.string "I respect the ambition.$"

@ Old man on the bench.
Hollowbrook_Text_BenchOldMan::
	.string "I've watched the professor\n"
	.string "give away POKéMON for thirty\l"
	.string "years. Every one of them came\l"
	.string "back to say thanks.\p"
	.string "Well. Nearly every one.$"

@ Old man on the bench, after the lab scene.
Hollowbrook_Text_BenchOldManAfter::
	.string "Nearly every one. Until today,\n"
	.string "anyway.\p"
	.string "That boy will never be back to\n"
	.string "say thanks.$"

@ ===================================================================
@ INTERACTABLE POKéMON (the hens)
@ ===================================================================

Hollowbrook_Text_HenA::
	.string "The hen eyes you with deep\n"
	.string "suspicion.\p"
	.string "It seems to be deciding whether\n"
	.string "you are a threat or a snack.$"

Hollowbrook_Text_HenB::
	.string "The hen is sitting on an\n"
	.string "egg-shaped rock.\p"
	.string "It dares you to say something.$"

Hollowbrook_Text_HenC::
	.string "The hen pecks at your shoe.\n"
	.string "It is not sorry.$"

Hollowbrook_Text_HenAfterTrog::
	.string "The hen struts past, chest out.\p"
	.string "A fine white feather is stuck to\n"
	.string "its beak. It looks very pleased.$"

@ ===================================================================
@ THE GOLDSWORTH HOUSE: the grandfather (kind, no swearing)
@ ===================================================================

@ First visit, before the lab scene.
Hollowbrook_Text_GrandpaBefore::
	.string "Hello, dear. Come in, come in.\n"
	.string "Mind the rug. It bites.\p"
	.string "I'm told my grandson is due in\n"
	.string "town today. I hope I've not\l"
	.string "missed him.\p"
	.string "If you see a very stern young\n"
	.string "man, tell him I'm sorry.$"

@ After the lab scene, first visit.
Hollowbrook_Text_GrandpaAfter::
	.string "So you've met my grandson.\n"
	.string "Oh dear. I can see it on you.\p"
	.string "He gets his manners from the\n"
	.string "people who brought him up.\l"
	.string "Not from me, I hope.\p"
	.string "I was meant to be there when he\n"
	.string "came. I'm very sorry I wasn't.$"

@ Second topic.
Hollowbrook_Text_GrandpaAdvice::
	.string "Don't take him to heart.\p"
	.string "He has never been told 'no' by\n"
	.string "anyone who wasn't paid to.\p"
	.string "It makes a person very small\n"
	.string "inside. Be kind if you can.\p"
	.string "And beat him if you must.$"

@ Idle.
Hollowbrook_Text_GrandpaIdle::
	.string "Ah, {PLAYER}. Come and sit.\n"
	.string "I can't climb the stairs so\l"
	.string "well these days.\p"
	.string "The view from this chair is\n"
	.string "quite good enough.$"

@ ===================================================================
@ THE LAB: before the Troglodyte scene
@ ===================================================================

@ Aide 1 (nervous), when the player first enters.
Hollowbrook_Text_AideNervous::
	.string "Oh! Oh, thank goodness.\n"
	.string "Somebody sensible.\p"
	.string "There's a... a person in the\n"
	.string "back. He's very loud.$"

@ Aide 2 (deadpan).
Hollowbrook_Text_AideDeadpan::
	.string "Between us, the staff call him\n"
	.string "TROGLODYTE.\p"
	.string "Not to his face. We like our\n"
	.string "jobs, and our shoes.$"

@ ===================================================================
@ THE TROGLODYTE ENCOUNTER (lab, coord_event trigger at the door)
@ Order: Fennick spots the player -> Troglodyte rants -> he takes a POKéMON
@        -> he dismisses the player -> Fennick apologises -> fourth POKéMON
@        -> the player chooses.
@ {STR_VAR_1} = the species Troglodyte takes (random among the three on show).
@ ===================================================================

Hollowbrook_Text_LabTrogScene1::
	.string "...three HOURS! I waited three\n"
	.string "hours in this damn cow pasture!\p"
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
	.string "{STR_VAR_1} anyway. Good taste\l"
	.string "is hereditary.$"

Hollowbrook_Text_LabTrogSneer::
	.string "You're in my light.\n"
	.string "Move, whoever you are.\p"
	.string "I'll be Champion before you've\n"
	.string "tied those shoes.\p"
	.string "Tell my grandfather I was here.\n"
	.string "Actually, don't. Damn hens.$"

Hollowbrook_Text_LabTrogLeaves::
	.string "The door slams. A hen squawks\n"
	.string "somewhere outside.$"

@ Fennick apologises and reveals the fourth.
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

@ Each ball: buffer the species name in {STR_VAR_1}. Yes/No follows.
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

@ Aides after the scene.
Hollowbrook_Text_AideNervousAfter::
	.string "He took the {STR_VAR_1}, didn't he.\n"
	.string "I'm sorry. I'd have given him\l"
	.string "the hens.\p"
	.string "Nobody ever stands up to him.$"

Hollowbrook_Text_AideDeadpanAfter::
	.string "Bet you ten that the {STR_VAR_1}\n"
	.string "bites him by Route 2.$"

@ Fennick idle lines.
Hollowbrook_Text_FennickIdleBefore::
	.string "Oh, hello, {PLAYER}. I'm just\n"
	.string "mending a kettle. With a\l"
	.string "POKéMON.$"

Hollowbrook_Text_FennickIdleAfter::
	.string "Off you go, {PLAYER}.\n"
	.string "Write when you can.\p"
	.string "Or don't. Just win something.$"

@ Lab furniture.
Hollowbrook_Text_LabBookshelf::
	.string "Rows of notes. ‘On The Habits\n"
	.string "of Hens’ has been borrowed\l"
	.string "eleven times by the same person.$"

Hollowbrook_Text_LabComputer::
	.string "A screen full of hen weights.\n"
	.string "One is labelled ‘Menace.’$"
