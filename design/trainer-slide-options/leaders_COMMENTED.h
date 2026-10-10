// PROPOSED, NOT APPROVED. Gym leader mid-battle lines (trainer slides) for Greta and gyms 2 to 9.
// Companion to slides_leaders_options.md (same folder). This file is NOT included by any build file and changes nothing.
// Every line below is commented out. To use a block once the author approves it: copy it into src/data/veldris_trainer_slides.h at
// '// rows go here', remove the leading '// ', keep ONE block per trainer id, then run
//     python3 design/tools/dialogue_check.py src/data/veldris_trainer_slides.h      and      make -j4
// All 97 distinct rows were checked with design/tools/slide_check.py (208 px, 2 lines, no scroll, wide and narrow player name).
// Rule reminders: single curly quotes only, no \n, {B_PLAYER_NAME} never {PLAYER}, one row per trigger per block.
//
// PART 1 is the RECOMMENDED option per leader (needs no data change). PART 2 holds every other option and the extras so that any pick
// is a copy and paste. ACE rows are only correct after 'Ace Pokemon' is added to that leader's AI: line in src/data/trainers.party.
// SCH rows call back to a Goldsworth scheme (a story beat) and need the author's separate yes.
//
// Row ids in the trailing comments match the tables in slides_leaders_options.md.

// ================================================================================================================
// PART 1: RECOMMENDED
// ================================================================================================================

// ---- GRETA (GRE), Gym 1, Crestfall (town), Normal, STANDARD BADGE: option B, Sassy ----
//     [TRAINER_CRESTFALL_GRETA] =
//     {
//         VELDRIS_SLIDE(SELF_LAST_SWITCHIN, "Meet MILTANK. Everyone remembers her. Nobody enjoys it."),   // GRE-B1
//         VELDRIS_SLIDE(OPPONENT_LAST_SWITCHIN, "Your last one? No pressure. ...Okay, a little pressure."),   // GRE-B2
//         VELDRIS_SLIDE(SELF_LAST_LOW_HP, "Oh, you're actually good. Don't let it go to your head, hotshot!"),   // GRE-B3
//     },

// ---- HACHIMEL (HAC), Gym 2, Briarwick (city), Bug, HUSK BADGE: option A, Gentle apology (in voice) ----
//     [TRAINER_HACHIMEL] =
//     {
//         VELDRIS_SLIDE(BEFORE_FIRST_TURN, "Please forgive the grass. It gets terribly keen around guests."),   // HAC-A1
//         VELDRIS_SLIDE(DEFENDER_TAKES_FIRST_DOWN, "Oh, KRICKETUNE, I'm so sorry. You played beautifully."),   // HAC-A2
//         VELDRIS_SLIDE(SELF_LAST_SWITCHIN, "VIVILLON, I'm so sorry. It's your turn. Do be elegant."),   // HAC-A3
//     },

// ---- SANZUFORD (SAN), Gym 3, Gloomsby (town), Ghost, WISP BADGE: option A, Dry apprentice (in voice) ----
//     [TRAINER_SANZUFORD] =
//     {
//         VELDRIS_SLIDE(BEFORE_FIRST_TURN, "Don't worry, the twisting wears off. Unlike my usual clients."),   // SAN-A1
//         VELDRIS_SLIDE(DEFENDER_TAKES_FIRST_DOWN, "SHUPPET is resting. We never say ‘fainted’. Bad for business."),   // SAN-A2
//         VELDRIS_SLIDE(SELF_LAST_LOW_HP, "Huh. The living put up more of a fight than I was told."),   // SAN-A3
//     },

// ---- HAGANE (HAG), Gym 4, Smeltham (town, foundry), Steel, RIVET BADGE: option A, Tired foreman (in voice) ----
//     [TRAINER_HAGANE] =
//     {
//         VELDRIS_SLIDE(BEFORE_FIRST_TURN, "Mind the sparks. The safety inspector's at lunch. So is everyone."),   // HAG-A1
//         VELDRIS_SLIDE(DEFENDER_TAKES_FIRST_DOWN, "BRONZOR's down. It's built like a manhole cover. It'll be fine."),   // HAG-A2
//         VELDRIS_SLIDE(SELF_LAST_LOW_HP, "Lads, a hand? ...Lunch. Of course. Right, I'll manage."),   // HAG-A3
//     },

// ---- WAKASAGI (WAK), Gym 5, Hoarfell (city, frozen lake), Ice, FROST BADGE: option A, Unhurried (in voice) ----
//     [TRAINER_WAKASAGI] =
//     {
//         VELDRIS_SLIDE(BEFORE_FIRST_TURN, "Ah, snow. Lovely. Take your time. Nobody hurries on a lake."),   // WAK-A1
//         VELDRIS_SLIDE(DEFENDER_TAKES_FIRST_DOWN, "SNEASEL's down. Fair enough. I'd sit, but the whole floor is ice."),   // WAK-A2
//         VELDRIS_SLIDE(SELF_LAST_LOW_HP, "Now that's a bite. Hold on while I pour a cup first."),   // WAK-A3
//     },

// ---- TOBIN (TOB), Gym 6, Gildhaven (skyscraper city), Flying, FEATHER BADGE (and HM Fly): option B, Wry safety demo ----
//     [TRAINER_TOBIN] =
//     {
//         VELDRIS_SLIDE(BEFORE_FIRST_TURN, "In the unlikely event of defeat, remain seated. Weeping is allowed."),   // TOB-B1
//         VELDRIS_SLIDE(OPPONENT_LAST_SWITCHIN, "Final approach, then. I'll hold the runway. Do land stylishly."),   // TOB-B2
//         VELDRIS_SLIDE(SELF_LAST_LOW_HP, "Mayday, mayday. Sorry, I've always wanted to say that."),   // TOB-B3
//     },

// ---- ASEBY (ASE), Gym 7, Hemlock Reach (town), Poison, VIAL BADGE: option A, Clipboard (in voice) ----
//     [TRAINER_ASEBY] =
//     {
//         VELDRIS_SLIDE(BEFORE_FIRST_TURN, "Pre-treated your side of the floor. Standard procedure. You're welcome."),   // ASE-A1
//         VELDRIS_SLIDE(DEFENDER_TAKES_FIRST_DOWN, "WEEZING: failed. Logging it. Next sample, please."),   // ASE-A2
//         VELDRIS_SLIDE(SELF_LAST_LOW_HP, "This batch is outside tolerance. Please hold while I rework it."),   // ASE-A3
//     },

// ---- SUZURAN (SUZ), Gym 8, Primrose Vale (city), Fairy, CHARM BADGE: option A, Sweet and sincere (in voice) ----
//     [TRAINER_SUZURAN] =
//     {
//         VELDRIS_SLIDE(BEFORE_FIRST_TURN, "Mist is lovely, isn't it? It hides the thorns."),   // SUZ-A1
//         VELDRIS_SLIDE(DEFENDER_TAKES_FIRST_DOWN, "You're being so gentle with us. How kind. You can stop now."),   // SUZ-A2
//         VELDRIS_SLIDE(SELF_LAST_LOW_HP, "I do wear flowers. I also have thorns. Sorry!"),   // SUZ-A3
//     },

// ---- MIZZLE (MIZ), Gym 9, Beaconmouth (town, flooded lighthouse), Water, TIDE BADGE: option A, Cheerful deadpan (in voice) ----
//     [TRAINER_MIZZLE] =
//     {
//         VELDRIS_SLIDE(BEFORE_FIRST_TURN, "Ha! Rain. Sorry. It does that when I'm excited."),   // MIZ-A1
//         VELDRIS_SLIDE(DEFENDER_TAKES_FIRST_DOWN, "GYARADOS is down. Fine. I once lost a pier. This is manageable."),   // MIZ-A2
//         VELDRIS_SLIDE(SELF_LAST_LOW_HP, "Ha ha! That's the sea for you. Giving, then taking. Mostly taking."),   // MIZ-A3
//     },

// ================================================================================================================
// PART 2: EVERY OTHER OPTION AND THE EXTRAS. Paste ONE option block per leader (never together with the recommended block above).
// ================================================================================================================

// ---- GRETA (GRE) ----
// Option A, Warm coach:
//     [TRAINER_CRESTFALL_GRETA] =
//     {
//         VELDRIS_SLIDE(DEFENDER_TAKES_FIRST_DOWN, "SKITTY, you were lovely. Go and nap in the hay."),   // GRE-A1
//         VELDRIS_SLIDE(SELF_LAST_SWITCHIN, "Free tip, since it's gym one: MILTANK rolls harder every turn."),   // GRE-A2
//         VELDRIS_SLIDE(SELF_LAST_LOW_HP, "Between us, I'm proud of you. Don't tell MILTANK. She'd want a raise."),   // GRE-A3
//     },
// Option C, Showgirl:
//     [TRAINER_CRESTFALL_GRETA] =
//     {
//         VELDRIS_SLIDE(BEFORE_FIRST_TURN, "Ladies, gentlemen and hay bales: welcome to the main event!"),   // GRE-C1
//         VELDRIS_SLIDE(SELF_LAST_SWITCHIN, "Lights! Music! Roll out the big, pink stove: MILTANK!"),   // GRE-C2
//         VELDRIS_SLIDE(SELF_LAST_LOW_HP, "This is where I stage my comeback. Watch closely. I'm very good."),   // GRE-C3
//     },
// SCH row (STORY: Scheme 1 (consultants, hay maze, MILTANK eat the paperwork)). Needs the author's yes; one row per trigger, so it replaces any row already on SELF_LAST_SWITCHIN:
//         VELDRIS_SLIDE(SELF_LAST_SWITCHIN, "Meet MILTANK. She ate a consultant's whole report this week."),   // GRE-SCH

// ---- HACHIMEL (HAC) ----
// Option B, Polite menace:
//     [TRAINER_HACHIMEL] =
//     {
//         VELDRIS_SLIDE(DEFENDER_TAKES_FIRST_DOWN, "KRICKETUNE did its best. I'm sorry in advance: VIVILLON is better."),   // HAC-B1
//         VELDRIS_SLIDE(OPPONENT_LAST_SWITCHIN, "Is that your last one? I'm terribly sorry. I'll be quick."),   // HAC-B2
//         VELDRIS_SLIDE(SELF_LAST_LOW_HP, "Sorry, VIVILLON. Sorry, grass. Sorry, hives. Sorry, floor."),   // HAC-B3
//     },
// Option C, Ceremonial:
//     [TRAINER_HACHIMEL] =
//     {
//         VELDRIS_SLIDE(BEFORE_FIRST_TURN, "By the honour of the APIARY, I regret everything that follows."),   // HAC-C1
//         VELDRIS_SLIDE(SELF_LAST_SWITCHIN, "Hush, hives. VIVILLON takes the floor, and I take full responsibility."),   // HAC-C2
//         VELDRIS_SLIDE(SELF_LAST_LOW_HP, "It is said the gentle inherit the meadow. Not today, apparently."),   // HAC-C3
//     },
// SCH row (STORY: Scheme 2 (the fumigation tent)). Needs the author's yes; one row per trigger, so it replaces any row already on BEFORE_FIRST_TURN:
//         VELDRIS_SLIDE(BEFORE_FIRST_TURN, "I did apologise to the tent, afterwards. It looked so crumpled."),   // HAC-SCH

// ---- SANZUFORD (SAN) ----
// Option B, Service-industry deadpan:
//     [TRAINER_SANZUFORD] =
//     {
//         VELDRIS_SLIDE(SELF_LAST_SWITCHIN, "My last one. Try to be a good audience. The dead usually are."),   // SAN-B2
//         VELDRIS_SLIDE(OPPONENT_LAST_SWITCHIN, "That's your last one? Don't worry. I'll keep it tasteful."),   // SAN-B1
//         VELDRIS_SLIDE(SELF_LAST_LOW_HP, "Ugh, this is running late. I've got a funeral at four."),   // SAN-B3
//     },
// Option C, Gothic ham:
//     [TRAINER_SANZUFORD] =
//     {
//         VELDRIS_SLIDE(BEFORE_FIRST_TURN, "Dearly beloved, we are gathered to watch you lose. Refreshments after."),   // SAN-C1
//         VELDRIS_SLIDE(DEFENDER_TAKES_FIRST_DOWN, "A moment of silence for SHUPPET. ...That's enough. Moving on."),   // SAN-C2
//         VELDRIS_SLIDE(SELF_LAST_LOW_HP, "Wait! I haven't finished the eulogy! Give me a minute here!"),   // SAN-C3
//     },
// ACE row (needs 'Ace Pokemon' on this leader's AI: line). Add it to a block that has no SELF_LAST_SWITCHIN row, or swap it for one:
//         VELDRIS_SLIDE(SELF_LAST_SWITCHIN, "MIMIKYU's shy. Be kind to the costume. It's all it has."),   // SAN-ACE
// SCH row (STORY: Scheme 3 (frat guys in sheets, a real HAUNTER joins in)). Needs the author's yes; one row per trigger, so it replaces any row already on BEFORE_FIRST_TURN:
//         VELDRIS_SLIDE(BEFORE_FIRST_TURN, "A real ghost took the boys' sheets. I call that peer review."),   // SAN-SCH

// ---- HAGANE (HAG) ----
// Option B, Paperwork deadpan:
//     [TRAINER_HAGANE] =
//     {
//         VELDRIS_SLIDE(SELF_LAST_SWITCHIN, "That's my last one. It's been on shift since six. Please be gentle."),   // HAG-B2
//         VELDRIS_SLIDE(OPPONENT_LAST_SWITCHIN, "Last one, is it? Take five. I would, if anyone covered my shift."),   // HAG-B1
//         VELDRIS_SLIDE(SELF_LAST_HALF_HP, "That's half. I'll need an incident report. I'll fill it in myself."),   // HAG-B3
//     },
// Option C, Foundry boom:
//     [TRAINER_HAGANE] =
//     {
//         VELDRIS_SLIDE(BEFORE_FIRST_TURN, "Behold! Forty years of iron, sweat and unpaid overtime!"),   // HAG-C1
//         VELDRIS_SLIDE(DEFENDER_TAKES_FIRST_DOWN, "Strike while the iron's hot, I always say. Nobody ever listens."),   // HAG-C2
//         VELDRIS_SLIDE(SELF_LAST_LOW_HP, "Everything I've got! Hammer and tongs! Don't tell the union."),   // HAG-C3
//     },
// ACE row (needs 'Ace Pokemon' on this leader's AI: line). Add it to a block that has no SELF_LAST_SWITCHIN row, or swap it for one:
//         VELDRIS_SLIDE(SELF_LAST_SWITCHIN, "TINKATUFF, you're on. Bring your own hammer. The lads took ours to lunch."),   // HAG-ACE
// SCH row (STORY: Scheme 4 (hard hats, the crane, the neat cube with a receipt)). Needs the author's yes; one row per trigger, so it replaces any row already on BEFORE_FIRST_TURN:
//         VELDRIS_SLIDE(BEFORE_FIRST_TURN, "Did you see the cube out front? It came with a receipt. I'm keeping it."),   // HAG-SCH

// ---- WAKASAGI (WAK) ----
// Option B, Wry angler:
//     [TRAINER_WAKASAGI] =
//     {
//         VELDRIS_SLIDE(SELF_LAST_SWITCHIN, "This is my last, and it's in no hurry. Neither am I."),   // WAK-B2
//         VELDRIS_SLIDE(OPPONENT_LAST_SWITCHIN, "Last one, eh? Good. I've waited all winter for a proper bite."),   // WAK-B1
//         VELDRIS_SLIDE(SELF_LAST_HALF_HP, "Half already? Here, hold my thermos. Careful, it's hot."),   // WAK-B3
//     },
// Option C, Storyteller:
//     [TRAINER_WAKASAGI] =
//     {
//         VELDRIS_SLIDE(BEFORE_FIRST_TURN, "Did I ever tell you about the winter the lake froze twice? No? Later."),   // WAK-C1
//         VELDRIS_SLIDE(DEFENDER_TAKES_FIRST_DOWN, "That reminds me of a story. It's long. We'll do it afterwards."),   // WAK-C2
//         VELDRIS_SLIDE(SELF_LAST_LOW_HP, "This reminds me of the Great Frost. I lost that one too."),   // WAK-C3
//     },
// ACE row (needs 'Ace Pokemon' on this leader's AI: line). Add it to a block that has no SELF_LAST_SWITCHIN row, or swap it for one:
//         VELDRIS_SLIDE(SELF_LAST_SWITCHIN, "AVALUGG's slow to get going. Lucky I've got all day."),   // WAK-ACE
// SCH row (STORY: Scheme 5 (flags in the lake, ‘angling rights’, the crew sold soup)). Needs the author's yes; one row per trigger, so it replaces any row already on BEFORE_FIRST_TURN:
//         VELDRIS_SLIDE(BEFORE_FIRST_TURN, "A fellow bought the ‘angling rights’ to this lake. Then I sold him soup."),   // WAK-SCH

// ---- TOBIN (TOB) ----
// Option A, Calm captain (in voice):
//     [TRAINER_TOBIN] =
//     {
//         VELDRIS_SLIDE(BEFORE_FIRST_TURN, "Good tailwind today. Expected flight time: short."),   // TOB-A1
//         VELDRIS_SLIDE(DEFENDER_TAKES_FIRST_DOWN, "SWELLOW is grounded. A minor delay. Please remain seated."),   // TOB-A2
//         VELDRIS_SLIDE(SELF_LAST_LOW_HP, "A little turbulence. Do keep your seat belts fastened."),   // TOB-A3
//     },
// Option C, Vain showman:
//     [TRAINER_TOBIN] =
//     {
//         VELDRIS_SLIDE(BEFORE_FIRST_TURN, "Pardon the breeze. My hair took forty minutes and I'm not redoing it."),   // TOB-C1
//         VELDRIS_SLIDE(SELF_LAST_SWITCHIN, "Last flight of the day. Mind the paint, it's freshly waxed."),   // TOB-C2
//         VELDRIS_SLIDE(SELF_LAST_LOW_HP, "Fine. You win this approach. I'd like it noted my hair held up."),   // TOB-C3
//     },
// ACE row (needs 'Ace Pokemon' on this leader's AI: line). Add it to a block that has no SELF_LAST_SWITCHIN row, or swap it for one:
//         VELDRIS_SLIDE(SELF_LAST_SWITCHIN, "CORVIKNIGHT, you're cleared for takeoff. And for landing. On them."),   // TOB-ACE
// SCH row (STORY: Scheme 6 (the parents' gift basket, the sincere tip)). Needs the author's yes; one row per trigger, so it replaces any row already on BEFORE_FIRST_TURN:
//         VELDRIS_SLIDE(BEFORE_FIRST_TURN, "I've been tipped to lose today. I declined. Kindly. Twice."),   // TOB-SCH

// ---- ASEBY (ASE) ----
// Option B, Data-point dry:
//     [TRAINER_ASEBY] =
//     {
//         VELDRIS_SLIDE(SELF_LAST_SWITCHIN, "Final sample, and strictly speaking, the one that works."),   // ASE-B2
//         VELDRIS_SLIDE(OPPONENT_LAST_SWITCHIN, "That's your last one. Good. I only need one more data point."),   // ASE-B1
//         VELDRIS_SLIDE(SELF_LAST_HALF_HP, "Half. That's within tolerance. Barely. I'll note it."),   // ASE-B3
//     },
// Option C, Mad chemist:
//     [TRAINER_ASEBY] =
//     {
//         VELDRIS_SLIDE(BEFORE_FIRST_TURN, "Behold: science! Please don't touch the floor, the walls, or me."),   // ASE-C1
//         VELDRIS_SLIDE(DEFENDER_TAKES_FIRST_DOWN, "A failed trial! Wonderful! Failure is just data wearing a hat."),   // ASE-C2
//         VELDRIS_SLIDE(SELF_LAST_LOW_HP, "Fascinating. I appear to be losing. I must write this down."),   // ASE-C3
//     },
// ACE row (needs 'Ace Pokemon' on this leader's AI: line). Add it to a block that has no SELF_LAST_SWITCHIN row, or swap it for one:
//         VELDRIS_SLIDE(SELF_LAST_SWITCHIN, "TOXAPEX is the control sample. The rest were to make it look good."),   // ASE-ACE
// SCH row (STORY: Scheme 7 (hazmat inspectors, 47 violations written in advance)). Needs the author's yes; one row per trigger, so it replaces any row already on BEFORE_FIRST_TURN:
//         VELDRIS_SLIDE(BEFORE_FIRST_TURN, "Forty-seven violations, written in advance. I respect the efficiency."),   // ASE-SCH

// ---- SUZURAN (SUZ) ----
// Option B, Gardener's dry:
//     [TRAINER_SUZURAN] =
//     {
//         VELDRIS_SLIDE(DEFENDER_TAKES_FIRST_DOWN, "Pruned already! Don't worry, things grow back stronger."),   // SUZ-B1
//         VELDRIS_SLIDE(OPPONENT_LAST_SWITCHIN, "Your last one? How brave. I do press the brave ones in books."),   // SUZ-B2
//         VELDRIS_SLIDE(SELF_LAST_LOW_HP, "Cut me down and I come back every spring. That's perennials, dear."),   // SUZ-B3
//     },
// Option C, Sweetness drops:
//     [TRAINER_SUZURAN] =
//     {
//         VELDRIS_SLIDE(BEFORE_FIRST_TURN, "Behold the wrath of the garden! Please stay off the lawn."),   // SUZ-C1
//         VELDRIS_SLIDE(SELF_LAST_SWITCHIN, "Now you've made me cross. Do you know how long a rose takes?"),   // SUZ-C2
//         VELDRIS_SLIDE(SELF_LAST_LOW_HP, "Wilt me? I bloom out of spite. Ask any daisy."),   // SUZ-C3
//     },
// ACE row (needs 'Ace Pokemon' on this leader's AI: line). Add it to a block that has no SELF_LAST_SWITCHIN row, or swap it for one:
//         VELDRIS_SLIDE(SELF_LAST_SWITCHIN, "They call me the small one. GARDEVOIR, dear, shall we discuss it?"),   // SUZ-ACE
// SCH row (STORY: Scheme 8 (surveyors, ‘Glade Heights’ condominiums)). Needs the author's yes; one row per trigger, so it replaces any row already on BEFORE_FIRST_TURN:
//         VELDRIS_SLIDE(BEFORE_FIRST_TURN, "They wanted condominiums here. I pressed their brochure in a book."),   // SUZ-SCH

// ---- MIZZLE (MIZ) ----
// Option B, Keeper's logbook:
//     [TRAINER_MIZZLE] =
//     {
//         VELDRIS_SLIDE(BEFORE_FIRST_TURN, "Thirty years on this lamp. Never lost a ship. Hats, yes. Hundreds."),   // MIZ-B1
//         VELDRIS_SLIDE(SELF_LAST_SWITCHIN, "My last one. Think of it as the lamp coming on. Do try not to stare."),   // MIZ-B3
//         VELDRIS_SLIDE(OPPONENT_LAST_SWITCHIN, "Down to your last? Don't fret. The tide goes out, then it comes back."),   // MIZ-B2
//     },
// Option C, Big and jolly:
//     [TRAINER_MIZZLE] =
//     {
//         VELDRIS_SLIDE(BEFORE_FIRST_TURN, "Welcome to the end of the road! Past me is only sea! No pressure!"),   // MIZ-C1
//         VELDRIS_SLIDE(DEFENDER_TAKES_FIRST_DOWN, "Overboard goes the first one! Don't worry. Most of them float."),   // MIZ-C2
//         VELDRIS_SLIDE(SELF_LAST_LOW_HP, "Now that's a wave! Somebody log it! ...Right. I'm somebody."),   // MIZ-C3
//     },
// ACE row (needs 'Ace Pokemon' on this leader's AI: line). Add it to a block that has no SELF_LAST_SWITCHIN row, or swap it for one:
//         VELDRIS_SLIDE(SELF_LAST_SWITCHIN, "MILOTIC, the lamp's all yours. Do try not to dazzle them."),   // MIZ-ACE
// SCH row (STORY: Scheme 9 (the box of 400 permits and invoices, carried out to sea)). Needs the author's yes; one row per trigger, so it replaces any row already on BEFORE_FIRST_TURN:
//         VELDRIS_SLIDE(BEFORE_FIRST_TURN, "Four hundred invoices, and the sea took them all. Poor sea."),   // MIZ-SCH
