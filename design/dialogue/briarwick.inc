@ Briarwick dialogue DRAFT (city, place 4, gym 2 Bug, the first Goldsworth house). Status: PROPOSED, not wired.
@ Brief: design/maps/towns/briarwick.md. Check widths: python3 design/tools/dialogue_check.py design/dialogue/briarwick.inc
@ Rules: Pokemon only (no real animals: she keeps COMBEE and hives, never 'bees'), single curly quotes for speech,
@ only the Goldsworth house swears (mild, PG-13), TROGLODYTE written literally.
@ 'Before' = before Scheme 2 is beaten. 'After' = after. Badge lines use FLAG_BADGE02_GET. Names marked PROPOSED.
@ The cousin set moved here from crestfall_extra.inc (Crestfall is a town and has no Goldsworth house).
@ crestfall_extra.inc keeps the older Crestfall_ copy; this file replaces it for the build.

@ ===================================================================
@ SIGNS
@ ===================================================================

Briarwick_Text_TownSign::
	.string "BRIARWICK\n"
	.string "‘Where the forest keeps the\l"
	.string "town in line.’$"

Briarwick_Text_GymSign::
	.string "BRIARWICK POKéMON GYM\n"
	.string "Leader: HACHIMEL\p"
	.string "‘Please do not shake the hives.’$"

Briarwick_Text_GymSignSealed::
	.string "BRIARWICK POKéMON GYM\n"
	.string "Leader: HACHIMEL\p"
	.string "A paper notice is taped on top:\n"
	.string "‘CLOSED FOR HYGIENE. THANK YOU.’$"

Briarwick_Text_ApiarySign::
	.string "THE APIARY\n"
	.string "Hives, honey and a very long\l"
	.string "staircase. Knock softly.$"

Briarwick_Text_R3GateSign::
	.string "ROUTE 3, EAST: CRESTFALL\n"
	.string "‘Mind the road works.’$"

Briarwick_Text_R4Sign::
	.string "ROUTE 4, WEST: GLOOMSBY\n"
	.string "‘Fog possible. Courage advised.’$"

@ ===================================================================
@ SCHEME 2: the 'fumigation' tent (setup, reveal, collapse)
@ The tent stands in front of the gym door. Foreman = Mr Pargeter (PROPOSED).
@ ===================================================================

Briarwick_Text_ForemanBefore::
	.string "Good day. Please keep back from\n"
	.string "the tent. It is a routine\l"
	.string "hygiene treatment.\p"
	.string "The gym has been identified as\n"
	.string "a hazard. To hygiene.$"

Briarwick_Text_ForemanAsk::
	.string "You wish to enter? I'm afraid\n"
	.string "the building is under quarantine.\p"
	.string "Our client was most insistent.\n"
	.string "He pays for insistent.$"

Briarwick_Text_JuniorBefore::
	.string "I'm reading from the card.\n"
	.string "‘Do not engage the locals.’\p"
	.string "...It doesn't say what to do\n"
	.string "if the locals engage us.$"

Briarwick_Text_FanWorried::
	.string "The hives are inside! The\n"
	.string "COMBEE can't get out!\p"
	.string "HACHIMEL has been in there\n"
	.string "since the tent went up.$"

@ The reveal at the tent flap (coord_event trigger in front of the gym door).
Briarwick_Text_ForemanReveal::
	.string "Fumigation, you see. We seal\n"
	.string "the premises and treat it.\p"
	.string "Every crawling thing inside.\n"
	.string "Which is... all of it. Yes.\p"
	.string "It is a gym full of bugs. That\n"
	.string "is, technically, the point.$"

Briarwick_Text_TentCollapse1::
	.string "Something stirs inside the tent.\n"
	.string "A thread of silk crosses the flap.\p"
	.string "Then another. Then forty.$"

Briarwick_Text_TentCollapse2::
	.string "The tent is sealed from the\n"
	.string "inside. By a SPINARAK. Neatly.\p"
	.string "The crew finds itself wrapped\n"
	.string "up like a gift. With a bow.$"

Briarwick_Text_ForemanWrapped::
	.string "I would like it noted that this\n"
	.string "is not a hygiene issue.\p"
	.string "It is a... a ribbon issue.$"

Briarwick_Text_HachimelOut::
	.string "Oh dear. Oh, I'm so sorry,\n"
	.string "everyone. Please don't struggle.\p"
	.string "SPINARAK is very proud of its\n"
	.string "knots. It will tire eventually.$"

Briarwick_Text_HachimelToCrew::
	.string "I do apologise for the web.\n"
	.string "The Pokémon Center will have\l"
	.string "scissors. And tea.\p"
	.string "...Please take the tent with\n"
	.string "you. It's a little loud.$"

Briarwick_Text_HachimelInvite::
	.string "And you must be {PLAYER}.\n"
	.string "Thank you for waiting.\p"
	.string "The gym is open. Mind the\n"
	.string "webs. They're not decorative.$"

@ After the scheme (town NPCs).
Briarwick_Text_ForemanAfter::
	.string "The Pokémon Center has been\n"
	.string "very kind. Biscuits, even.\p"
	.string "I have never been so thoroughly\n"
	.string "wrapped. I think it's the knots.$"

Briarwick_Text_JuniorAfter::
	.string "The card didn't cover this.\n"
	.string "I'm writing a new card.\p"
	.string "‘Step one: do not poke the\n"
	.string "SPINARAK.’$"

Briarwick_Text_FanAfter::
	.string "She walked out of that tent\n"
	.string "apologising to the tent.\p"
	.string "That's HACHIMEL. We love her.$"

@ ===================================================================
@ THE GYM: HACHIMEL (young Apiary keeper in a veil, gentle, formal, apologises to every Bug)
@ ===================================================================

Briarwick_Text_GymStatue::
	.string "BRIARWICK POKéMON GYM\n"
	.string "Leader: HACHIMEL\p"
	.string "‘Bug types dislike fire,\n"
	.string "flying and rock. Do be kind.’$"

Briarwick_Text_GymStatueWin::
	.string "BRIARWICK POKéMON GYM\n"
	.string "Leader: HACHIMEL\p"
	.string "‘Winners today: {PLAYER}.\n"
	.string "The hives send their regards.’$"

Briarwick_Text_Trainer1Intro::
	.string "I have trained every day this\n"
	.string "week. The GYM has made me brave.\p"
	.string "The webs have made me careful.$"

Briarwick_Text_Trainer1Defeat::
	.string "Oh, I lost. I'll bring a\n"
	.string "bigger net next time.$"

Briarwick_Text_Trainer1After::
	.string "Left at the hedge, then right at\n"
	.string "the web. The web moves, though.$"

Briarwick_Text_Trainer2Intro::
	.string "The leader is lovely, truly.\n"
	.string "I only work here for the scent.\p"
	.string "But I do enjoy a battle.$"

Briarwick_Text_Trainer2Defeat::
	.string "I'll go and smell something\n"
	.string "calming. For my nerves.$"

Briarwick_Text_Trainer2After::
	.string "HACHIMEL apologises to every\n"
	.string "Pokémon before a battle.\p"
	.string "It makes them try harder.\n"
	.string "Out of guilt, I think.$"

Briarwick_Text_HachimelChallenge::
	.string "Welcome to the BRIARWICK GYM.\n"
	.string "I'm HACHIMEL. Pleased to meet you.\p"
	.string "I keep the hives up at the\n"
	.string "APIARY. And this gym, when I can.$"

Briarwick_Text_HachimelChallenge2::
	.string "I must apologise in advance.\n"
	.string "To you, and to my Pokémon.\p"
	.string "They are small, and they will\n"
	.string "try very hard. Please be gentle.$"

Briarwick_Text_HachimelBattleIntro::
	.string "KRICKETUNE, I'm sorry. Do go on.\n"
	.string "Play something brave.$"

Briarwick_Text_HachimelAce::
	.string "VIVILLON, I'm so sorry. It's\n"
	.string "your turn. Do be elegant.$"

Briarwick_Text_HachimelDefeat::
	.string "Oh! Oh, well done. I'm sorry,\n"
	.string "you're very strong.\p"
	.string "Please don't feel bad on my\n"
	.string "account. I feel bad enough.$"

Briarwick_Text_HachimelBadge::
	.string "Please take the HUSK BADGE.\n"
	.string "It's light, but it's yours.\p"
	.string "{PLAYER} received the HUSK BADGE!$"

Briarwick_Text_HachimelRockSmash::
	.string "And these. HM ROCK SMASH, so\n"
	.string "you can break the stones.\p"
	.string "And TM THIEF. I'm sorry. It's\n"
	.string "an unkind move. It's useful.$"

Briarwick_Text_HachimelAfter::
	.string "Thank you for the battle.\n"
	.string "And for the tent.\p"
	.string "I won't ask who sent the crew.\n"
	.string "I think we both know.$"

Briarwick_Text_HachimelToTrog::
	.string "That boy in the clean coat\n"
	.string "stood across from me once.\p"
	.string "He said he'd beat me with one\n"
	.string "hand. I gave him mine, for balance.$"

Briarwick_Text_HachimelRematch::
	.string "Ready for another? I'll\n"
	.string "apologise to the Pokémon again.\p"
	.string "It makes the battles feel\n"
	.string "properly tidy.$"

@ ===================================================================
@ THE REST OF THE TOWN (topics from the brief)
@ ===================================================================

@ R3 east gatehouse. Before badge 1 the road works are on the Crestfall end, so the guard is idle.
Briarwick_Text_R3GuardBefore::
	.string "Coming from CRESTFALL? Then you\n"
	.string "came the long way round.\p"
	.string "The road works are shut on that\n"
	.string "side. By GOLDSWORTH ROADWAYS.$"

Briarwick_Text_R3GuardAfter::
	.string "The road works lifted. Cones\n"
	.string "gone. Nobody told us why.\p"
	.string "I assume someone asked nicely.$"

Briarwick_Text_R3HikerBefore::
	.string "Is the road open yet? I've\n"
	.string "been sat here since Tuesday.\p"
	.string "The bench is very comfortable.\n"
	.string "That's the real problem.$"

Briarwick_Text_R3HikerAfter::
	.string "The road's open! I stood up.\n"
	.string "My legs have forgotten how.$"

@ R9 north-east gatehouse (Mothwood). DROPPED (author, 2026-10-08): no R9; reuse the line on R8's Mothwood gate.
Briarwick_Text_R9Guard::
	.string "MOTHWOOD has no map.\n"
	.string "Bring snacks and a friend.\p"
	.string "If you get lost, stand still.\n"
	.string "Eventually the trees move on.$"

Briarwick_Text_KidNet::
	.string "MOTHWOOD is bigger inside than\n"
	.string "outside. I measured it.\p"
	.string "With my net. It didn't reach.$"

@ Pokemon Center visitor: gossip and the optional Troglodyte sighting.
Briarwick_Text_CenterVisitor::
	.string "A rich boy came through here.\n"
	.string "Good coat. Bad attitude.\p"
	.string "He had a LILLIPUP in a little\n"
	.string "jumper. He complained about\l"
	.string "the grass. Then he left.$"

Briarwick_Text_CenterVisitorAfter::
	.string "The tent crew is in the lobby,\n"
	.string "eating biscuits. Quietly.\p"
	.string "The nurse says they've stopped\n"
	.string "struggling. It's progress.$"

Briarwick_Text_Clerk::
	.string "Welcome. We sell no bug sprays.\n"
	.string "House rule. HACHIMEL asked.$"

@ The Apiary (Wilf, PROPOSED name, the keeper's assistant).
Briarwick_Text_WilfBefore::
	.string "Oh, hello. I'm WILF. I help\n"
	.string "HACHIMEL with the hives.\p"
	.string "She's still stuck in the gym.\n"
	.string "COMBEE are very worried.$"

Briarwick_Text_WilfAfter::
	.string "She's back! And the hives are\n"
	.string "calm again. Come in, come in.\p"
	.string "Please take some HONEY. She\n"
	.string "insists. Don't argue with her.$"

Briarwick_Text_WilfHoney::
	.string "{PLAYER} received HONEY!$"

Briarwick_Text_WilfIdle::
	.string "Honey is best left on a spoon.\n"
	.string "Or in a Pokémon's tray. Not a\l"
	.string "sandwich. Trust me.$"

Briarwick_Text_ApiaryKeeper::
	.string "The first bug-catching contest\n"
	.string "in the region was held right\l"
	.string "here, before the ponds filled.\p"
	.string "Nobody won. They all got lost\n"
	.string "in MOTHWOOD. It was lovely.$"

@ House A (west end): tired parent and child (Scheme 2 setup).
Briarwick_Text_HouseAParent::
	.string "The gym's been sealed for two\n"
	.string "days. Our whole street smells\l"
	.string "of lemon and regret.\p"
	.string "It's a hygiene thing, they said.\n"
	.string "Nobody in this town is unhygienic.$"

Briarwick_Text_HouseAParentAfter::
	.string "The smell is gone. I miss it\n"
	.string "slightly. Don't tell anyone.$"

Briarwick_Text_HouseAChild::
	.string "I saw the crew arrive. They had\n"
	.string "forty tent poles and a lorry.\p"
	.string "I counted. Nobody asked me to.$"

@ House B: Tansy (PROPOSED), retired champion of the bug-catching contest.
Briarwick_Text_TansyBefore::
	.string "I won the contest forty years\n"
	.string "ago. They gave me a trophy.\p"
	.string "It was a plain net. Quite\n"
	.string "right. I earned it.$"

Briarwick_Text_TansyHint::
	.string "If you head for MOTHWOOD, go\n"
	.string "round by the north tree line.\p"
	.string "The shrine inside needs a Cut\n"
	.string "tree opened first. Remember that.$"

Briarwick_Text_TansyAfter::
	.string "So that crew got wrapped. I'd\n"
	.string "have paid to see it.\p"
	.string "Take this SILVER POWDER. Off\n"
	.string "the shelf. It's gone to waste.$"

Briarwick_Text_TansyPowder::
	.string "{PLAYER} received SILVER POWDER!$"

@ House C (south-centre): a kid who saw the lorry.
Briarwick_Text_HouseCKid::
	.string "The men in white came in a\n"
	.string "lorry full of tent poles.\p"
	.string "One of them is scared of the\n"
	.string "ponds. I saw him jump.$"

@ ===================================================================
@ THE GOLDSWORTH HOUSE (NPC only, no trainers). Cold, tidy, rich. Residents swear mildly (PG-13),
@ are rude to the player and never cruel to townsfolk. Before/after hangs on the Scheme 2 flag, not the badge.
@ Replaces the Crestfall_ set in crestfall_extra.inc (same cousins, rewritten for the tent).
@ ===================================================================

Briarwick_Text_GoldsworthHouseSign::
	.string "GOLDSWORTH RESIDENCE\n"
	.string "‘Deliveries to the side gate.\l"
	.string "Visitors: don't.’$"

Briarwick_Text_ButlerDoor::
	.string "Welcome to the GOLDSWORTH\n"
	.string "residence. Please do not touch\l"
	.string "anything. Or breathe loudly.\p"
	.string "I have worked here for twenty\n"
	.string "years. It has been educational.$"

Briarwick_Text_ButlerAfter::
	.string "I must apologise on the\n"
	.string "family's behalf. A little.\p"
	.string "Not too much. They notice.$"

Briarwick_Text_BarnabyBefore::
	.string "Oh, great. A local. Wipe your\n"
	.string "feet. Not on the rug.\p"
	.string "I'm BARNABY GOLDSWORTH. Yes,\n"
	.string "THAT family. Try to keep up.$"

Briarwick_Text_BarnabyBoast::
	.string "My family owns this street.\n"
	.string "And the street after that.\p"
	.string "Dad bought a whole island once.\n"
	.string "He lost it. Bought another.\p"
	.string "That's how rich we are. Damn\n"
	.string "right we lose things.$"

Briarwick_Text_BarnabyBoast2::
	.string "Cousin TROGLODYTE is making a\n"
	.string "real name for himself.\p"
	.string "Bad name, sure. Names cost\n"
	.string "money. He has plenty.$"

Briarwick_Text_BarnabyAfter::
	.string "Fine. So the tent got wrapped.\n"
	.string "It was a bad line item.\p"
	.string "Hell, I told them. Nobody\n"
	.string "listens to the boaster.$"

Briarwick_Text_LoungerBefore::
	.string "Shh. I'm resting. It's a full\n"
	.string "time job in this family.\p"
	.string "Go away. Take your muddy\n"
	.string "boots with you.$"

Briarwick_Text_LoungerAfter::
	.string "Beau couldn't plan a nap.\n"
	.string "I heard about the tent.\p"
	.string "That's the funniest crap I've\n"
	.string "heard all year. Don't tell him.$"

Briarwick_Text_PetOwnerBefore::
	.string "My PERSIAN, DUCHESS, has a\n"
	.string "better pedigree than your town.\p"
	.string "Do not pet her. She bites. With\n"
	.string "contempt.$"

Briarwick_Text_PetOwnerAfter::
	.string "DUCHESS looks embarrassed.\n"
	.string "She won't say about what.\p"
	.string "KIP says it's the tent. I say\n"
	.string "it's the ribbon.$"
