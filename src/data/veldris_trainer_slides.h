// Hack-owned (not upstream). Mid-battle trainer lines (trainer slides) for Veldris trainers. See design/trainer-slides.md.
// Included ONCE, inside the DIFFICULTY_NORMAL block of sTrainerSlides in src/trainer_slide.c. Only that block is read
// (B_VAR_DIFFICULTY is 0, include/config/battle.h).
//
// One block per trainer, keyed by trainer id. Alias names are fine (TRAINER_HACHIMEL, TRAINER_TROGLODYTE_HOLLOWBROOK) but
// list each id ONCE: TRAINER_ROXANNE_1 is the same id as TRAINER_HACHIMEL, and a second block is a build error.
// A partner is [TRAINER_PARTNER(PARTNER_STEVEN)]. Ids must be below 866.
//
// Row: VELDRIS_SLIDE(<name after TRAINER_SLIDE_>, "text"). Plain sentences, no \n (the game wraps at 208 px, 2 lines),
// single curly quotes only, {B_PLAYER_NAME} never {PLAYER}, write TROGLODYTE literally.
// Check: python3 design/tools/dialogue_check.py src/data/veldris_trainer_slides.h
//
// NO ROWS YET: the wording of Troglodyte's and the gym leaders' lines is the author's call (CLAUDE.md rules 9 and 10).
// PROPOSED options are in design/trainer-slides.md. Shape of a block, once a line is approved:
//     [TRAINER_TROGLODYTE_HOLLOWBROOK] =
//     {
//         VELDRIS_SLIDE(DEFENDER_TAKES_FIRST_DOWN, "..."),
//     },
#define VELDRIS_SLIDE(slide, text) [TRAINER_SLIDE_ ## slide] = COMPOUND_STRING(text "{PAUSE_UNTIL_PRESS}")

// rows go here

#undef VELDRIS_SLIDE
