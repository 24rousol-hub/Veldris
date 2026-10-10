#!/usr/bin/env python3
"""local_id names must be unique across ALL maps (hack tool; the pre-commit hook runs it for staged map.json files).

Every object event's local_id becomes a #define in the one header include/constants/map_event_ids.h. A clash builds
without error and the later value wins, so a script moves the wrong person (CLAUDE.md, seen with Greta, 2026-10-08).

Usage (repo root):
    python3 design/tools/localid_lint.py data/maps/Hollowbrook/map.json ...   fail if a local_id of these maps is also
                                                                                used by another map, or twice in one
    python3 design/tools/localid_lint.py --staged MAP.json ...                (the hook) judge only the local_ids a map
                                                                                has now and its copy at HEAD does not,
                                                                                so a vanilla map that already shares
                                                                                names never blocks a commit or a merge
    python3 design/tools/localid_lint.py                                      list every shared local_id (informational:
                                                                                vanilla Littleroot, UnionRoom and the
                                                                                FRLG copies share some; exit 0)
Reads the working tree. Exit code 1 if a named map clashes."""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def local_ids(text):
    """The local_id of every object event in a map.json text, in order (a repeat means the map clashes with itself)."""
    return [o["local_id"] for o in json.loads(text).get("object_events", []) if "local_id" in o]


def ids_at_head(folder):
    """local_ids the map had at HEAD: none for a new map, an unreadable one or a repository with no commits yet."""
    try:
        blob = subprocess.run(["git", "show", f"HEAD:data/maps/{folder}/map.json"], cwd=ROOT, capture_output=True,
                              check=True).stdout
        return set(local_ids(blob))
    except (OSError, ValueError, subprocess.CalledProcessError):
        return set()


def main():
    staged = "--staged" in sys.argv[1:]
    named = {Path(a).resolve().parent.name for a in sys.argv[1:] if not a.startswith("--")}
    where = {}                              # local_id -> map folder of every object event that uses it
    own = {}                                # named map folder -> its local_ids
    for mj in sorted((ROOT / "data/maps").glob("*/map.json")):
        try:
            ids = local_ids(mj.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            print(f"warning: cannot read {mj.relative_to(ROOT)}")
            continue
        for lid in ids:
            where.setdefault(lid, []).append(mj.parent.name)
        if mj.parent.name in named:
            own[mj.parent.name] = set(ids)
    bad = 0
    if named:
        judged = set()
        for folder in named:
            judged |= own.get(folder, set()) - (ids_at_head(folder) if staged else set())
        for lid in sorted(judged):
            if len(where[lid]) > 1:
                print(f"ERROR {lid} is used {len(where[lid])} times, in: {', '.join(sorted(set(where[lid])))}")
                bad += 1
        print(f"{len(named)} map(s) checked against {len(where)} local_ids, {bad} error(s)")
    else:
        for lid, maps in sorted(where.items()):
            if len(maps) > 1:
                print(f"note  {lid}: {', '.join(sorted(set(maps)))}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
