# LeoB exterior builders (Route 1, Crestfall)

These scripts write map blocks, so per `CLAUDE.md` rule 2 run them only when the author asks for a map to be built; after that, edit in Porymap.

| Script | What it does |
|---|---|
| `leob_town.py` | Small town builder: roads (sand path 9-slice), forest fill on a 2x2 grid with LeoB tree autotiling, building stamps copied from vanilla Petalburg/Oldale, pond, crops, benches, fences, flowers, signs |
| `crestfall_build.py` | Crestfall layout B (approved 2026-10-01): writes `map.bin`, `border.bin`, the layout, map group, `event_scripts.s` include, `map.json` and the Route 1 connection |
| `crestfall_concepts.py` | The three Crestfall concept renders (A, B, C) the author chose from |
| `route1_leob.py` | Route 1 in LeoB tiles from the mirrored Route 29 source in `../gen4_tiles/route1_g4.py` (run `../gen4_tiles/sheet.py` first: it needs `uniq.npy`) |
| `path_blend.py` | Adds 24 grass-path-to-sand blend metatiles to the end of Petalburg (ids in the script header). Re-runnable |
| `hibits.json` | Default collision/elevation bits per metatile id, read from vanilla maps |

Paths point at `/home/claude/veldris`; change `V` if your checkout is elsewhere. Needs Python 3 with numpy and Pillow.
