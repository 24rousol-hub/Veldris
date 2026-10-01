@ League and post-game dialogue DRAFT. Status: PROPOSED, not wired into any map (no League map exists yet).
@ Lines starting with @ are comments. Check widths with:
@   python3 design/tools/dialogue_check.py design/dialogue/league.inc
@ Companion plan: design/postgame.md. Every name here (OSSIAN, HYACINTH, DUNMORE, MAREN, CYNTHIA) is a PROPOSED
@ placeholder, not canon. Labels: League_Text_ and PostGame_Text_. Grandfather's own after-League lines already exist
@ in hollowbrook.inc (Hollowbrook_Text_GrandpaLeague1, GrandpaLeague2, GrandpaLeagueName, GrandpaLeagueIdle): not repeated.
@ Rules used: single curly quotes, TROGLODYTE written literally, only Goldsworths swear, Pokemon only.
@ {STR_VAR_2} = Troglodyte's starter species name (random, set by the pool prune var), as in hollowbrook.inc.

@ ===================================================================
@ ELITE FOUR (Option A set, types adjusted to Dark/Psychic/Fighting/Dragon, see postgame.md). Intro = before the fight, Defeat = when the member loses,
@ After = idle line once beaten.
@ ===================================================================

@ --- 1. OSSIAN, Dark: a cheerful undertaker ---
League_Text_OssianIntro::
	.string "Welcome, welcome! Mind the dark.\n"
	.string "It's only the crows. Mostly.\p"
	.string "I'm OSSIAN. I bury things for a\n"
	.string "living. Let's see how you fare.$"

League_Text_OssianDefeat::
	.string "Oh, that was lovely. A proper\n"
	.string "send-off. Well done.$"

League_Text_OssianAfter::
	.string "Go on through. The next room is\n"
	.string "quiet. HYACINTH likes it so.$"

@ --- 2. HYACINTH, Psychic: icy manners, a soft spot for snow globes ---
League_Text_HyacinthIntro::
	.string "You're late. I knew you would be.\n"
	.string "I saw it coming. I always do.\p"
	.string "I'm HYACINTH. Try to surprise me.\n"
	.string "Nobody ever has. Go on.$"

League_Text_HyacinthDefeat::
	.string "Hm. I did not see that one.\n"
	.string "Don't tell anyone.$"

League_Text_HyacinthAfter::
	.string "I keep snow globes in my desk.\n"
	.string "Not a word. Go and fight DUNMORE.$"

@ --- 3. DUNMORE, Fighting: huge, gentle, terrible at puns ---
League_Text_DunmoreIntro::
	.string "Ha! You made it past the spooky\n"
	.string "ones. Time to work up a sweat!\p"
	.string "I'm DUNMORE. I lift, I punch, I\n"
	.string "nap. Show me what you've got!$"

League_Text_DunmoreDefeat::
	.string "Ow! Oh, that's the good kind of\n"
	.string "ow. Lovely stuff, {PLAYER}.$"

League_Text_DunmoreAfter::
	.string "MAREN's the last of us. She's\n"
	.string "kind, but she does not hold back.$"

@ --- 4. MAREN, Dragon: the oldest member, quietly terrifying ---
League_Text_MarenIntro::
	.string "So you're the one everybody is\n"
	.string "talking about. Sit, child. No?\p"
	.string "Then we'll do it the loud way.\n"
	.string "I am MAREN. I keep dragons.$"

League_Text_MarenDefeat::
	.string "Well. They do so hate losing.\n"
	.string "I've not seen it in years.$"

League_Text_MarenAfter::
	.string "Go on. The last door is open.\n"
	.string "Oh, and a boy is waiting for you.$"

@ ===================================================================
@ FINAL TROGLODYTE BATTLE (PROPOSED: in the League corridor before the Champion's chamber).
@ Arc A = contemptuous, then humbled (author-chosen, 2026-10-01). Arc B (oblivious) was NOT chosen.
@ He is NOT the Champion. Both arcs would share the battle lines from TrogBattleIntro on.
@ ===================================================================

@ --- Arc A: contemptuous, then humbled ---
League_Text_TrogArcA1::
	.string "There you are. The help.\n"
	.string "I've been waiting an hour.\p"
	.string "I bought a League pass. Did you\n"
	.string "earn yours? I doubt it.$"

League_Text_TrogArcA2::
	.string "Let me show you what money and\n"
	.string "breeding can do. Hold still.$"

League_Text_TrogArcADefeat::
	.string "No. No, no. I had the best\n"
	.string "trainers money could buy!$"

League_Text_TrogArcAHumbled::
	.string "...I never once worked at it.\n"
	.string "Did you know that? Not once.\p"
	.string "You did. All the way from\n"
	.string "HOLLOWBROOK. Damn it.$"

League_Text_TrogArcAHumbled2::
	.string "I'll be back. Properly, this\n"
	.string "time. Don't you dare get soft.$"

@ --- Arc B: oblivious and confused. UNUSED / NOT CHOSEN (author, 2026-10-01). Kept, do not wire. ---
League_Text_TrogArcB1::
	.string "Oh! It's you. They said the\n"
	.string "League was open to anyone.\p"
	.string "I didn't think anyone would\n"
	.string "actually come. How odd.$"

League_Text_TrogArcB2::
	.string "Daddy's people said winning is\n"
	.string "just a matter of having the best.\p"
	.string "I have the best. Shall we?$"

League_Text_TrogArcBDefeat::
	.string "But... I had the best. They were\n"
	.string "all very expensive.$"

League_Text_TrogArcBConfused::
	.string "Why do you keep beating me?\n"
	.string "Nobody ever explained that part.\p"
	.string "Is it something you do every day?\n"
	.string "Is that allowed?$"

League_Text_TrogArcBConfused2::
	.string "I'd like to try again. Properly,\n"
	.string "whatever that means. Thank you.$"

@ --- Shared battle lines (used with Arc A) ---
League_Text_TrogBattleIntro::
	.string "Go, {STR_VAR_2}! And SIR BISCUIT,\n"
	.string "no more hiding behind the couch!$"

League_Text_TrogBiscuit::
	.string "SIR BISCUIT has grown. Don't\n"
	.string "ask me how. The vet did it.$"

League_Text_TrogFinalDefeatShared::
	.string "He stands aside. The Champion's\n"
	.string "chamber is open.$"

@ ===================================================================
@ CHAMPION: an aged CYNTHIA, the previous region's Champion and Gatsby's old friend (author, 2026-10-01).
@ She holds the seat as the League's guest, defending Champion (see postgame.md). The player does not learn
@ the friendship until after the League. Old Options B (Greta) and C (Troglodyte) were not chosen and are removed.
@ ===================================================================

League_Text_ChampIntro::
	.string "So. The last challenger. I'm\n"
	.string "CYNTHIA. I've been a Champion\l"
	.string "longer than you've been walking.\p"
	.string "I was told a grudge got you\n"
	.string "this far. That's a fine engine.$"

League_Text_ChampSendOut::
	.string "Don't mind my knees, dear.\n"
	.string "My Pokémon are quite spry.$"

League_Text_ChampDefeat::
	.string "Oh, my. It's been a long time\n"
	.string "since anyone did that to me.$"

League_Text_ChampAfter::
	.string "You're Champion now, {PLAYER}.\n"
	.string "Go and see the Hall of Fame.$"

League_Text_ChampPraise::
	.string "You did it for spite, and you\n"
	.string "did it well. I respect that.\p"
	.string "Go home. Someone waits there\n"
	.string "who'd like to thank you.$"

@ ===================================================================
@ HALL OF FAME (hook for FLAG_SYS_GAME_CLEAR). Fennick and mum call.
@ ===================================================================

League_Text_HofAttendant::
	.string "Congratulations. Step this way\n"
	.string "to record your Pokémon.\p"
	.string "Every Champion's team goes on\n"
	.string "the wall. Yours is special.$"

League_Text_HofFennickCall::
	.string "{PLAYER}! FENNICK here. I saw\n"
	.string "it on the screen. Champion!\p"
	.string "Come by the lab. I've misplaced\n"
	.string "something. I think it's my shoes.$"

@ ===================================================================
@ POST-GAME
@ ===================================================================

@ Cynthia arrives in Hollowbrook after the League (PostGame_Text_ prefix as requested).
PostGame_Text_CynthiaArrives::
	.string "Excuse me. Is this the house\n"
	.string "with the big door? I'm looking\l"
	.string "for an old friend.$"

PostGame_Text_GatsbyReunion1::
	.string "GATSBY? Gatsby Goldsworth!\n"
	.string "You look dreadful. Wonderful.$"

PostGame_Text_GatsbyReunion2::
	.string "CYNTHIA. You came. And you\n"
	.string "battled my young friend here.\p"
	.string "I know. I can tell from your\n"
	.string "face. You're smiling.$"

PostGame_Text_GatsbyReunion3::
	.string "That day the boy came, I was with\n"
	.string "her. On the quiet. I'm sorry.\p"
	.string "Nobody knew. I wanted one\n"
	.string "afternoon with a friend.$"

PostGame_Text_GatsbyThanks::
	.string "Thank you, {PLAYER}. You did what\n"
	.string "I couldn't manage in forty years.\p"
	.string "You taught my grandson how it\n"
	.string "feels to lose. He'll be better.$"

PostGame_Text_CynthiaThanks::
	.string "He thanked you first. I'd have\n"
	.string "done the same, after a proper\l"
	.string "battle. Rematch. Any time, dear.$"

@ Rematch and epilogue hooks.
PostGame_Text_E4Rematch::
	.string "Back for more? Good. I kept the\n"
	.string "good team waiting for you.$"

PostGame_Text_TrogEpilogue::
	.string "I'm... trying something. It's\n"
	.string "called a job. I'm bad at it.\p"
	.string "Don't laugh. Actually, go on.\n"
	.string "Everyone does.$"

PostGame_Text_GoldsworthEpilogue::
	.string "The family board is in uproar.\n"
	.string "Something about lost revenue.\p"
	.string "I think Daddy's people quit.\n"
	.string "I never liked them anyway.$"
