# Map detailing index (PROPOSED, 2026-10-01)

Final map picture: [../art/region_map_final.png](../art/region_map_final.png). Conventions, route numbering and templates: [README.md](README.md). Everything here is PROPOSED; the names and the gym order are the only approved parts.

## What is here

- **Settlement cards** (17 new places, in `towns/`):

| Card | Size |
|---|---|
| [ALDERMERE (city, the 'Lost City', post-game, dead end; the sketch gives it no number)](towns/aldermere.md) | 174 lines |
| [BEACONMOUTH (city, lighthouse city, GYM 9 Water; the sketch gives it no number)](towns/beaconmouth.md) | 164 lines |
| [BRIARWICK (city, place 4)](towns/briarwick.md) | 161 lines |
| [BRINECOMBE (town, place 14, no gym)](towns/brinecombe.md) | 119 lines |
| [CRAGDALE (town, place 9, ridge town, no gym)](towns/cragdale.md) | 116 lines |
| [DRIFTSANDS (town, beach town; the sketch gives it no number)](towns/driftsands.md) | 96 lines |
| [EBBSWORTH (town, river port; the sketch gives it no number)](towns/ebbsworth.md) | 113 lines |
| [GILDHAVEN (city, place 8, gym 6 Flying, the skyscraper city)](towns/gildhaven.md) | 210 lines |
| [GLOOMSBY (town, place 5)](towns/gloomsby.md) | 131 lines |
| [HEMLOCK REACH (city, place 12, gym 7 Poison)](towns/hemlock-reach.md) | 171 lines |
| [HOARFELL (city, place 7)](towns/hoarfell.md) | 141 lines |
| [KINGSQUAY (city, big harbour city; the sketch gives it no number)](towns/kingsquay.md) | 115 lines |
| [LINGMOOR (town, place 10, heather highland, no gym)](towns/lingmoor.md) | 114 lines |
| [PRIMROSE VALE (city, place 13, gym 8 Fairy)](towns/primrose-vale.md) | 163 lines |
| [SMELTHAM (town, place 6)](towns/smeltham.md) | 121 lines |
| [VESPERHAVEN (city, post-game only, the hidden coast; the sketch gives it no number)](towns/vesperhaven.md) | 149 lines |
| [WAYMEET (town, place 11, crossroads and rail stop, no gym)](towns/waymeet.md) | 118 lines |

- **Road cards:** [routes-west.md](routes-west.md) (R3 to R9), [routes-centre.md](routes-centre.md) (R10 to R12, R18 to R21), [routes-east.md](routes-east.md) (R13 to R17), [routes-south.md](routes-south.md) (R22 to R31).
- **Landmarks:** [landmarks-west.md](landmarks-west.md) (Mothwood, Slagwell Mine, Hoarfell Ice cave), [landmarks-centre.md](landmarks-centre.md) (The Pinnacle), [landmarks-east.md](landmarks-east.md) (Mirror Isle), [landmarks-south.md](landmarks-south.md) (Silverstrand, Echo Hollow, Argent Peak).
- Hollowbrook, Crestfall, Wendlebury and R1, R2 keep their older docs (see README).

## Decisions (author, 2026-10-01)

- Route numbering R1 to R31 is confirmed, paired sketch numbers are one road each.
- Primrose Vale is a Surf-only pocket on purpose.
- Scheme Pokémon (MAGNEZONE, GLALIE, FLORGES, LAPRAS) are cutscene-only NPC Pokémon; Scheme 8 gets an NPC garden warden with the FLORGES.
- Mirror Isle has a static **DIALGA** (level 60 PROPOSED) and is the only place to catch DITTO. Aldermere (the ancient city) has a static **MEW** (level 70 PROPOSED). R18 reopens at the Feather Badge (confirmed).
- Goldsworth house split approved (Briarwick, Hoarfell, Hemlock Reach, Primrose Vale, Kingsquay, Beaconmouth).
- Troglodyte's later fights use the postgame core; **no Garchomp** (it is Cynthia's ace). Fixed in `troglodyte-arc.md`.
- All nine badges are needed for the League.
- R18 is under construction, not a toll road.
- Gildhaven traced from the Goldenrod render, **mirrored**.

## Still open (the rest of the original list)

Items 8 to 13 below remain open. Items 1 to 7 and the mirrored-render part of 10 are decided above.

## Original open questions (collected from the four writers and my review)

1. **Route numbering.** Are the paired sketch numbers (7/8, 14/17, 15/16, 18/19, 21/30, 22/29, 23/28, 24/27, 25/26) one road each? This gives 31 roads in the README table, not 33.
2. **Schemes against the built teams.** Scheme 4 needs a MAGNEZONE (HAGANE's team has none), Scheme 5 a GLALIE (WAKASAGI has none), Scheme 8 a FLORGES (SUZURAN has none), and Scheme 9 has MIZZLE's LAPRAS carry the box out to sea but MIZZLE is a man with no LAPRAS. The cards use a cutscene-only Pokémon in each case. Approve that, rewrite the schemes, or change the teams?
3. **Primrose Vale is a Surf-only pocket.** The sketch has no land road from Hemlock Reach to Primrose Vale, so R14 to R17 are all water. Intended?
4. **Goldsworth houses.** Briarwick (the Crestfall cousin set), Hoarfell (three cousins), Hemlock Reach, Primrose Vale, Kingsquay and Beaconmouth have one each; Gildhaven has the skyscraper instead; Aldermere and Vesperhaven get a kiosk or none. Confirm.
5. **Final Troglodyte team.** `troglodyte-arc.md` says the same six with Garchomp as ace; `postgame.md` says Stoutland, Gardevoir, Vaporeon, Tyranitar, Pyroar plus a starter. Which?
6. **How many badges the League needs.** The cards assume all nine before R20 (levels 56 to 62). With eight, lower R20 and Troglodyte fight 7 by about 4.
7. **R18** (the thin Hoarfell to Gildhaven line): read as a private Goldsworth toll road, shut from the Hoarfell side until the Feather Badge. Right?
8. **Waterfall and the south.** A weir at the end of R22 needs Waterfall (badge 8), which keeps the south chain behind gym 8. Is that what 'the Surf gate south' meant?
9. **Post-game.** R26 to R31 and Vesperhaven open at `FLAG_SYS_GAME_CLEAR` (coast guard blocks before). Cynthia's rematch at Vesperhaven or Hollowbrook? Does Troglodyte's cloakroom job at Vesperhaven suit Arc A?
10. **Gildhaven's skyscraper.** Emerald has no tall-tower tiles: new Radio-Tower-style tiles, the Battle Tower render, or a big office block? Trace the Goldenrod render mirrored so the sea is on the east?
11. **Mirror Isle:** optional? A legendary-style static encounter (MESPRIT proposed)? Where do the Old and Good Rods come from (Super Rod proposed at Brinecombe)?
12. **Road edges.** The writers picked which map edge each road uses from the Palladium renders; Wendlebury's west edge is used for R8. Confirm when you trace each map.
13. **Visuals.** Hoarfell has no snow tileset, Beaconmouth has no lighthouse tiles, Hemlock Reach has no Palladium render, Slagwell's Mt Mortar images look like one cavern.
