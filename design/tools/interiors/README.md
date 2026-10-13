# Interior builders

These write map blocks, so per `CLAUDE.md` rule 2 run them only when the author asks for a map to be built; afterwards edit in Porymap.

| Script | What it does |
|---|---|
| `mrender.py` | Renders any layout to PNG (`python3 mrender.py LAYOUT_ID out.png 3 [ids] [coll]`). Works for the Building/Gen 4 Interior sets |
| `houses.py` | The shared house layouts H1 (cottage) and H5 (bedroom house), from pieces of the Hollowbrook interiors |
| `layoutkit.py` | Kit for layout builders: `Spec`, piece helpers (`blank`, `put`, `grab`, `stamp`), `lint` (shape, tileset ranges, door, reachability), pictures. `python3 layoutkit.py fam_x OUT_DIR` checks and renders one family |
| `atlas.py` | Metatile atlas of any tileset pair with ids and behaviours (`python3 atlas.py PRIMARY SECONDARY OUT_DIR`) |
| `fam_*.py` | One module per family of shared layouts (each defines `SPECS`) |
| `install_layouts.py` | Lints every `fam_*.py`, writes `map.bin` and `border.bin` under `data/layouts/` and appends `layouts.json` (`--check` lints only, `--doc` prints the docs table) |
| `install_crestfall_interiors.py` | One-off: Crestfall Center 1F/2F, Mart, House A/B, door warps, fly flag, heal location, fly row, region grid cell |

Run from this folder; paths are relative to the repo root (`mrender.py` finds it from its own location). `install_crestfall_interiors.py` is the first-version one-off and still names `/home/claude/veldris`.

Note (2026-10-08): the author later dropped the Center 2F. `Crestfall_PokemonCenter_2F` was removed and the 1F now uses `LAYOUT_VELDRIS_POKEMON_CENTER_1F` (no escalator); the installer above still shows the first version.
