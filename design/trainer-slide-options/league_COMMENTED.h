// PROPOSED, NOT APPROVED, NOT WIRED. Draft rows for src/data/veldris_trainer_slides.h (stream slides-league, 2026-10-09).
// Elite Four (OSSIAN, HYACINTH, DUNMORE, DRAYDEN), Champion CYNTHIA and the planned bosses of the Commons and the Drowned Crown.
// Every line is a PROPOSAL for the author to pick from; the full A/B/C options, tone notes and measurements are in
// slides_league_options.md. This file holds ONLY the recommended option per battle, with every code line commented out.
//
// To use a block once the author has approved wording (key battles, CLAUDE.md rules 9 and 10):
//   1. Paste the block into the empty 'rows go here' area of src/data/veldris_trainer_slides.h (inside the VELDRIS_SLIDE
//   define/undef pair). Swap in the rows of another option if the author picked one.
//   2. Remove the leading '//' from the block lines (the ones indented four or more spaces); e.g.
//   sed -E 's#^//( {4,})#\1#' veldris_trainer_slides_league_COMMENTED.h
//   3. python3 design/tools/dialogue_check.py src/data/veldris_trainer_slides.h   (same tool as slide_check.py), then make -j4.
// Rules that still apply: list each trainer id ONCE per file (aliases share an id); a slide name may appear only once per block;
// single curly quotes only (none are needed here); {B_PLAYER_NAME}, never {PLAYER}.
//
// The last three blocks key on names that DO NOT EXIST yet (TRAINER_TEDDY, TRAINER_CROWN_LEADER, TRAINER_CROWN_OFFICER_MOTHWOOD).
// Define them as aliases of reused vanilla ids when the trainer blocks are built, for example
//   #define TRAINER_TEDDY         TRAINER_MAXIE_MAGMA_HIDEOUT   (601, class Magma Leader)
//   #define TRAINER_CROWN_LEADER  TRAINER_ARCHIE                (34, class Aqua Leader)
//   #define TRAINER_CROWN_OFFICER_MOTHWOOD  TRAINER_MATT        (30, class Aqua Admin)
// These ids are suggestions only; check that no other block already uses them before reusing.

// ---- OSSIAN, Elite Four 1 (Dark) ---- PROPOSED Option A "Sunny undertaker" (alternatives B/C in slides_league_options.md)
//    [TRAINER_OSSIAN] =
//    {
//        VELDRIS_SLIDE(DEFENDER_TAKES_FIRST_DOWN, "Well struck! That's one for the guest book. Do carry on."),
//        VELDRIS_SLIDE(SELF_LAST_SWITCHIN, "My last one. Now the service proper begins. Do mind the flowers."),
//        VELDRIS_SLIDE(SELF_LAST_LOW_HP, "Lovely! That's my funeral, I think. Wonderful turnout."),
//    },

// ---- HYACINTH, Elite Four 2 (Psychic) ---- PROPOSED Option A "I saw it coming" (alternatives B/C in slides_league_options.md)
//    [TRAINER_HYACINTH] =
//    {
//        VELDRIS_SLIDE(DEFENDER_TAKES_FIRST_DOWN, "Mm. That was in my notes. Page nine, I believe."),
//        VELDRIS_SLIDE(OPPONENT_LAST_SWITCHIN, "Your last one. Naturally. I put it in my diary this morning."),
//        VELDRIS_SLIDE(SELF_LAST_LOW_HP, "I saw this coming. I did rather hope I was wrong."),
//    },

// ---- DUNMORE, Elite Four 3 (Fighting) ---- PROPOSED Option A "Terrible puns" (alternatives B/C in slides_league_options.md)
//    [TRAINER_DUNMORE] =
//    {
//        VELDRIS_SLIDE(DEFENDER_TAKES_FIRST_DOWN, "Well, that was a punch line! ...No? I'll keep working on it."),
//        VELDRIS_SLIDE(SELF_LAST_SWITCHIN, "Last round! My best, hands down! ...Hands. Fists. Never mind."),
//        VELDRIS_SLIDE(SELF_LAST_LOW_HP, "Whew! Running low. Don't let me sit down. I'll nap!"),
//    },

// ---- DRAYDEN, Elite Four 4 (Dragon) ---- PROPOSED Option B "Quiet terror" (alternatives B/C in slides_league_options.md)
//    [TRAINER_DRAYDEN] =
//    {
//        VELDRIS_SLIDE(BEFORE_FIRST_TURN, "Be at ease, child. The first few minutes are the gentle ones."),
//        VELDRIS_SLIDE(OPPONENT_LAST_SWITCHIN, "Your last, I see. Do keep breathing. They notice when you stop."),
//        VELDRIS_SLIDE(SELF_LAST_SWITCHIN, "Ah. This is the one I keep by the fire. Mind your manners."),
//    },

// ---- CYNTHIA, Champion (aged, author-chosen) ---- PROPOSED Option A "Warm and sincere" (alternatives B/C in slides_league_options.md)
//    [TRAINER_CYNTHIA] =
//    {
//        VELDRIS_SLIDE(DEFENDER_TAKES_FIRST_DOWN, "Oh, well done, dear! Lovely timing. I was getting drowsy."),
//        VELDRIS_SLIDE(SELF_LAST_SWITCHIN, "Come along, old friend. Show the youngster what we can do."),
//        VELDRIS_SLIDE(SELF_LAST_LOW_HP, "Splendid. It has been years since my heart raced like this."),
//    },

// ---- TEDDY, leader of the Commons (double battle with Troglodyte) ---- PROPOSED Option A "Tired and fair" (alternatives B/C in slides_league_options.md)
// (trainer block and constant do not exist yet; see the note at the top of this file)
//    [TRAINER_TEDDY] =
//    {
//        VELDRIS_SLIDE(BEFORE_FIRST_TURN, "No hard feelings, mate. Plenty for the Goldsworth, mind."),
//        VELDRIS_SLIDE(DEFENDER_TAKES_FIRST_DOWN, "Fair play, that's one. I'll not hold it against you. Him, though."),
//        VELDRIS_SLIDE(SELF_LAST_LOW_HP, "Go easy, mate. There's a whole crew's lunch riding on this."),
//    },

// ---- The Drowned Crown's leader (the R19 climax; name not decided) ---- PROPOSED Option A "Imperious" (alternatives B/C in slides_league_options.md)
// (trainer block and constant do not exist yet; see the note at the top of this file)
//    [TRAINER_CROWN_LEADER] =
//    {
//        VELDRIS_SLIDE(BEFORE_FIRST_TURN, "We shall be brief. Kneel, or sink. Most do both."),
//        VELDRIS_SLIDE(DEFENDER_TAKES_FIRST_DOWN, "Our first loss. Someone shall be dismissed. Possibly everyone."),
//        VELDRIS_SLIDE(SELF_LAST_SWITCHIN, "Behold the last of the line. Do try not to blink. We never do."),
//    },

// ---- OPTIONAL: a Crown officer at Mothwood (my suggestion, not in factions.md) ---- PROPOSED Option A "Brisk borrower" (alternatives B/C in slides_league_options.md)
// (trainer block and constant do not exist yet; see the note at the top of this file)
//    [TRAINER_CROWN_OFFICER_MOTHWOOD] =
//    {
//        VELDRIS_SLIDE(BEFORE_FIRST_TURN, "Please don't touch the shrine. We're only borrowing it. For ever."),
//        VELDRIS_SLIDE(SELF_LAST_LOW_HP, "Careful, it's delicate! ...Oh dear. I suppose it's already stopped."),
//    },
