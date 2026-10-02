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
	.string "‘A quiet place. Mind the ZIGZAGOON.’$"

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
	.string "The ZIGZAGOON saw to that.$"

@ Kid, near the pond.
Hollowbrook_Text_Kid::
	.string "I'm going to be a trainer too!\n"
	.string "When I'm older.\p"
	.string "Or when Mum says I can go past\n"
	.string "the gate. Whichever is first.$"

@ Woman with washing.
Hollowbrook_Text_Laundry::
	.string "I'd hang this out, but the local\n"
	.string "ZIGZAGOON think everything is\l"
	.string "a treasure.\p"
	.string "Last week they took a sock.\n"
	.string "I respect the ambition.$"

@ Old man on the bench. One text for before and after the lab scene (the after text is folded in).
Hollowbrook_Text_BenchOldMan::
	.string "I've watched the professor\n"
	.string "give away POKéMON for thirty\l"
	.string "years. Every one of them came\l"
	.string "back to say thanks.\p"
	.string "Well. Nearly every one.\p"
	.string "And that boy in the clean coat,\n"
	.string "stomping about? I wouldn't\l"
	.string "hold my breath for his.$"

@ ===================================================================
@ INTERACTABLE POKéMON (common Normal types; ZIGZAGOON, SKITTY and SLAKOTH are PROPOSED stand-ins)
@ The labels keep the old Hen* names until the map is wired; rename them then.
@ ===================================================================

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

@ ===================================================================
@ THE GOLDSWORTH HOUSE: the grandfather (kind, no swearing)
@ ===================================================================

@ DOOR NOTE: the door is locked and this note is pinned to it from the start until the post-game.
@ He was away and the family does not know where (post-game payoff: he was meeting the previous
@ region's Champion, an old friend).
Hollowbrook_Text_GrandpaBefore::
	.string "Nobody answers the door.\n"
	.string "A note is pinned to it.\p"
	.string "‘Out. Back when I'm back.\n"
	.string "Do feed the SKITTY. - GG’$"

@ The old man OUTSIDE the house (only between the lab scene and the first badge; the player does not
@ connect him to the note until he says so). After the lab scene, first talk.
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

@ Second topic.
Hollowbrook_Text_GrandpaAdvice::
	.string "Don't take him to heart.\p"
	.string "He has never been told 'no' by\n"
	.string "anyone who wasn't paid to.\p"
	.string "It makes a person very small\n"
	.string "inside. Be kind if you can.\p"
	.string "And beat him if you must.$"

@ Idle (outside the house, on the bench).
Hollowbrook_Text_GrandpaIdle::
	.string "Ah, {PLAYER}. Lovely morning.\n"
	.string "I sit out here. The stairs\l"
	.string "and I are no longer friends.\p"
	.string "The view from this bench is\n"
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
@ {STR_VAR_2} = the species Troglodyte takes (random among the three on show).
@ {STR_VAR_1} = the species the player is choosing/has chosen. They are separate on purpose.
@ STR_VARs are scratch text buffers, not saved: always bufferspeciesname right before each message.
@ ===================================================================

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

@ Each ball: buffer the player's species name in {STR_VAR_1}. Yes/No follows.
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
	.string "He took the {STR_VAR_2}, didn't he.\n"
	.string "I'm sorry. I'd have given him\l"
	.string "the ZIGZAGOON.\p"
	.string "Nobody ever stands up to him.$"

Hollowbrook_Text_AideDeadpanAfter::
	.string "Bet you ten that the {STR_VAR_2}\n"
	.string "bites him by Route 2.$"

@ Fennick idle lines. There is no 'before' line: the lab scene starts the moment the player walks in,
@ so the player can never talk to Fennick before it.
Hollowbrook_Text_FennickIdleAfter::
	.string "Off you go, {PLAYER}.\n"
	.string "Write when you can.\p"
	.string "Or don't. Just win something.$"

@ Repeat visits after the first.
Hollowbrook_Text_FennickIdleAfter2::
	.string "Oh, hello, {PLAYER}. I'm just\n"
	.string "mending a kettle. With a\l"
	.string "POKéMON.$"

@ Lab furniture.
Hollowbrook_Text_LabBookshelf::
	.string "Rows of notes. ‘On The Habits\n"
	.string "of ZIGZAGOON’ has been borrowed\l"
	.string "eleven times by the same person.$"

Hollowbrook_Text_LabComputer::
	.string "A screen full of ZIGZAGOON weights.\n"
	.string "One is labelled ‘Menace.’$"

@ ===================================================================
@ THE GRANDFATHER AFTER THE LEAGUE (triggered by FLAG_SYS_GAME_CLEAR, the Hall of Fame flag)
@ His name (GATSBY GOLDSWORTH) stays hidden until now. The door note is signed only 'GG'.
@ ===================================================================

Hollowbrook_Text_GrandpaLeague1::
	.string "{PLAYER}. You've done it. I heard\n"
	.string "about the League.\p"
	.string "And I heard what you did for my\n"
	.string "grandson. Whatever it took,\l"
	.string "it needed doing.$"

Hollowbrook_Text_GrandpaLeague2::
	.string "Thank you for setting him\n"
	.string "straight. None of us ever did.\p"
	.string "You showed him that he could\n"
	.string "lose. That's a gift.$"

@ Name reveal (author: Gatsby Goldsworth).
Hollowbrook_Text_GrandpaLeagueName::
	.string "I never did tell you my name.\n"
	.string "It's GATSBY GOLDSWORTH.\p"
	.string "It took a League to earn it\n"
	.string "out of me. Fair enough.$"

Hollowbrook_Text_GrandpaLeagueIdle::
	.string "Come and sit, {PLAYER}.\n"
	.string "The kettle's on. The real one.$"

@ ===================================================================
@ TROGLODYTE'S FIRST BATTLE, RIGHT OUTSIDE THE LAB (author, 2026-09-30)
@ He has one starter (the random one, level 5). Optional gag: a level 1 LILLIPUP pet, nicknamed SIR BISCUIT.
@ {STR_VAR_2} = his starter's species name.
@ ===================================================================

Hollowbrook_Text_TrogOutside1::
	.string "Not so fast, whoever you are.\n"
	.string "I want a look at that POKéMON.\p"
	.string "Honestly? I want to watch it\n"
	.string "lose. Don't look so worried.$"

Hollowbrook_Text_TrogOutsideIntro::
	.string "Go, {STR_VAR_2}! Show this local\n"
	.string "what a proper start looks like!$"

Hollowbrook_Text_TrogOutsideDefeat::
	.string "What?! That was a warm-up!\n"
	.string "A warm-up! I wasn't trying!$"

Hollowbrook_Text_TrogOutsideAfter1::
	.string "I'm not even warm yet. I skipped\n"
	.string "breakfast. That's the reason.\p"
	.string "This isn't over. Nothing ever is\n"
	.string "over with a Goldsworth.$"

@ Only with the optional level 1 pet.
Hollowbrook_Text_TrogPetIntro::
	.string "Go, {STR_VAR_2}! And stay back,\n"
	.string "SIR BISCUIT. Daddy's watching.$"

Hollowbrook_Text_TrogPetAfter::
	.string "SIR BISCUIT didn't even get to\n"
	.string "play! Look what you've done!\p"
	.string "Come on, boy. We're going home.\n"
	.string "To the house with the big door.$"

@ ===================================================================
@ ADDED 2026-10-01: AFTER THE FIRST BADGE (return visits). Show these once the player has the STANDARD BADGE
@ (FLAG_BADGE01_GET). The bench grandfather is gone from this point until the post-game, so the locals never
@ say his name (he is just 'the old gentleman'). Labels are new; none repeats an earlier one.
@ ===================================================================

Hollowbrook_Text_MomAfterBadge::
	.string "A badge! Oh, {PLAYER}. Let me\n"
	.string "see. It's very shiny.\p"
	.string "I've put it on the fridge.\n"
	.string "...Not the badge. The drawing.$"

Hollowbrook_Text_FarmerAfterBadge::
	.string "Heard you took a badge off\n"
	.string "the Crestfall gym. Good.\p"
	.string "The ZIGZAGOON are quieter now.\n"
	.string "I think they're scared of you.$"

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

Hollowbrook_Text_BenchOldManAfterBadge::
	.string "The old gentleman's bench is\n"
	.string "empty again. Funny how a bench\l"
	.string "can look lonely.\p"
	.string "He'll be back. People like that\n"
	.string "always come home.$"

Hollowbrook_Text_AideNervousBadge::
	.string "Oh, the badge! May I look?\n"
	.string "Please don't tell the professor\l"
	.string "I cried a little.$"

Hollowbrook_Text_AideDeadpanBadge::
	.string "You beat a gym and the loud\n"
	.string "one is still out there.\p"
	.string "I'm telling you, no one has\n"
	.string "ever been this good for morale.$"

Hollowbrook_Text_FennickAfterBadge::
	.string "A badge already? Splendid!\n"
	.string "I'd tell you what it's for, but\l"
	.string "I forgot. Do keep winning.\p"
	.string "I'll find the notes. Eventually.$"

Hollowbrook_Text_SignTownAfterBadge::
	.string "HOLLOWBROOK\n"
	.string "‘Home of a badge holder.\l"
	.string "Still mind the ZIGZAGOON.’$"
