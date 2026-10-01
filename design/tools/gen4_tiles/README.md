# Gen 4 outdoor tiles: how Hollowbrook and Route 1 were built

Built 2026-10-01 at the author's request (every town and route in a Gen 4 style). These scripts cut Project Palladium's map pictures into GBA tiles and paint the two maps. They write map blocks, so per `CLAUDE.md` rule 2 run them only when the author asks for a map to be built; otherwise edit in Porymap.

Paths inside the scripts point at `/home/claude/veldris` and `/home/claude/24rousol-hub/team-aquas-asset-repo`. Change `V` and `P` if your checkout lives elsewhere. Needs Python 3 with numpy and Pillow.

| Script | What it does |
|---|---|
| `tiles.py` | Loads a Palladium picture and splits it into 16x16 tiles (strips the 1 px grid on the 17-px pictures) |
| `sheet.py` | Finds the unique tiles of New Bark Town and Route 29, quantised to GBA 15-bit colour. Writes `uniq.npy` and `grids.json` (run first) |
| `g4lib.py` | Compositing, palette packing and the tileset writer (tiles.png, palettes, metatiles.bin, attributes) |
| `hollowbrook_g4.py` | Hollowbrook: forest cells, paths, building stamps (mirrored where a door must stay put), pond, signs, flowers |
| `route1_g4.py` | Route 1: Route 29 mirrored, gatehouse replaced by forest, colours matched to New Bark Town, sign posts |
| `fitpal.py` | Merges the closest near-identical colours until the primary fits six palettes; writes `remap.json` |
| `build_all.py` | Compiles both tilesets and writes `map.bin` and `border.bin` for both maps |
| `install_route1.py` | One-off: layouts, map groups, Route 1 map.json and scripts, trainers, flags, wild table, the connection |
| `preview.py` | `python3 preview.py hollowbrook_g4 out.png 2 [coll]` renders a map (with collision tint) |

Order: `sheet.py`, then `fitpal.py` (only if palettes overflow), then `build_all.py`, then `make`.

**Adding the next town:** add its Palladium picture to `sheet.py`, write a `<town>_g4.py` like Hollowbrook's (or use the picture tile-for-tile), give it its own secondary, and keep `gTileset_Gen4Outdoor` as the primary so connections draw correctly. Credit the Palladium team in `CREDITS.md` for each picture used.
