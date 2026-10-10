"""A very small test runner (no pytest needed) for the emulator tests.

A test file looks like this (see tests/test_new_game.py):

    import os, sys
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
    import testkit
    from testkit import check, check_eq

    @testkit.test("new game defaults")
    def new_game_defaults(emu):
        check(emu.game.flag_get("FLAG_SYS_EXP_SHARE_ON"), "Exp. Share should start on")

    if __name__ == "__main__":
        testkit.main()

`python3 tests/test_new_game.py` runs that file's tests; `python3 run_tests.py` runs them all.
"""

import argparse
import importlib.util
import os
import signal
import sys
import tempfile
import time
import traceback
from pathlib import Path

HERE = Path(__file__).resolve().parent
REGISTRY = []


class CheckFailed(AssertionError):
    pass


def check(condition, message):
    """Fail the test with `message` unless `condition` is true."""
    if not condition:
        raise CheckFailed(message)


def check_eq(actual, expected, what):
    if actual != expected:
        raise CheckFailed("%s: expected %r, got %r" % (what, expected, actual))


class Test:
    def __init__(self, fn, name, boot, slow, emulator, timeout, turbo):
        self.fn, self.name, self.boot, self.slow = fn, name, boot, slow
        self.emulator, self.timeout, self.turbo = emulator, timeout, turbo
        self.file = Path(fn.__code__.co_filename).name


def test(name, boot="new_game", slow=False, emulator=True, timeout=None, turbo=True):
    """Register a test.

    boot:     "new_game" (default) starts the emulator and begins a new game (title SELECT quickstart, bedroom);
              "title" stops at the title screen; None starts the emulator and leaves everything to the test.
    slow:     only runs with --slow.
    emulator: False for tests that only need the built ELF (no emulator is started; the test gets a Context).
    timeout:  seconds before the test is stopped (default 180, slow tests 900).
    """
    def deco(fn):
        REGISTRY.append(Test(fn, name, boot, slow, emulator, timeout or (900 if slow else 180), turbo))
        return fn
    return deco


class Context:
    """What an emulator-free test receives."""

    def __init__(self, repo, layout):
        self.repo = Path(repo)
        self.layout = layout


class _Timeout(Exception):
    pass


def _alarm(signum, frame):
    raise _Timeout()


def load_test_files(directory=None):
    d = Path(directory) if directory else HERE / "tests"
    for f in sorted(d.glob("test_*.py")):
        spec = importlib.util.spec_from_file_location("emu_test_" + f.stem, f)
        mod = importlib.util.module_from_spec(spec)
        sys.path.insert(0, str(HERE))
        spec.loader.exec_module(mod)


def run(tests, args):
    from emulator import Display, Emulator
    from game import GameError
    from gdbclient import GdbError
    from layout import Layout, LayoutError, find_repo

    repo = Path(args.repo) if args.repo else find_repo()
    rom = Path(args.rom) if args.rom else repo / "pokeemerald.gba"
    elf = rom.with_suffix(".elf")
    fail_dir = Path(args.fail_dir) if args.fail_dir else Path(tempfile.gettempdir()) / "veldris_emu_fail"
    fail_dir.mkdir(parents=True, exist_ok=True)

    for p in (rom, elf):
        if not p.exists():
            print("ERROR: %s is missing. Build the game first: make -j4" % p)
            return 2
    from emulator import missing_tools, tools_message
    if any(t.emulator for t in tests) and missing_tools():
        print("ERROR: " + tools_message())
        return 2
    t0 = time.time()
    try:
        layout = Layout(repo, elf)
    except LayoutError as e:
        print("ERROR: %s" % e)
        return 2
    print("layout ready (%s, %.1fs)" % ("rebuilt" if layout.regenerated else "cached", time.time() - t0))

    display = Display(int(os.environ.get("EMU_DISPLAY", "97")))
    results = []
    signal.signal(signal.SIGTERM, lambda s, f: (_ for _ in ()).throw(KeyboardInterrupt()))
    try:
        display.start()
        for t in tests:
            if t.slow and not args.slow:
                print("SKIP  %s  (slow; use --slow)" % t.name)
                results.append("skip")
                continue
            start = time.time()
            emu = None
            status, detail, shot = "PASS", "", None
            signal.signal(signal.SIGALRM, _alarm)
            signal.setitimer(signal.ITIMER_REAL, t.timeout)
            try:
                if t.emulator:
                    emu = Emulator(rom=rom, repo=repo, display=display, layout=layout, turbo=t.turbo)
                    emu.start()
                    if t.boot == "title":
                        emu.boot_to_title()
                    elif t.boot == "new_game":
                        emu.new_game()
                    t.fn(emu)
                else:
                    t.fn(Context(repo, layout))
            except CheckFailed as e:
                status, detail = "FAIL", str(e)
            except _Timeout:
                status, detail = "FAIL", "test took longer than %d s" % t.timeout
            except (GameError, GdbError, LayoutError) as e:
                status, detail = "FAIL", "%s: %s" % (type(e).__name__, e)
            except KeyboardInterrupt:
                raise
            except Exception:
                status, detail = "FAIL", traceback.format_exc(limit=6)
            finally:
                signal.setitimer(signal.ITIMER_REAL, 0)
            if status == "FAIL" and emu is not None and emu.alive():
                try:
                    safe = "".join(c if c.isalnum() else "_" for c in t.name)
                    shot = emu.screenshot(fail_dir / (safe + ".png"))
                    detail += "\n      game: " + emu.game.summary()
                except Exception:
                    pass
            if emu is not None:
                emu.close()
            elapsed = time.time() - start
            line = "%s  %s  (%.1f s)" % (status, t.name, elapsed)
            if detail:
                line += "\n      " + detail.replace("\n", "\n      ")
            if shot:
                line += "\n      screenshot: " + shot
            print(line, flush=True)
            results.append(status.lower())
    except KeyboardInterrupt:
        print("interrupted")
        return 130
    finally:
        display.close()
    failed = results.count("fail")
    print("%d passed, %d failed, %d skipped  (%.0f s)" % (results.count("pass"), failed, results.count("skip"),
                                                          time.time() - t0))
    return 1 if failed else 0


def parse_args(argv=None):
    ap = argparse.ArgumentParser(description="Veldris emulator tests")
    ap.add_argument("--only", help="run only tests whose name contains this text (case-insensitive)")
    ap.add_argument("--list", action="store_true", help="list the tests and exit")
    ap.add_argument("--slow", action="store_true", help="also run the slow tests")
    ap.add_argument("--rom", help="ROM to test (default: pokeemerald.gba in the repo)")
    ap.add_argument("--repo", help="repo root (default: found from this file, or $VELDRIS_REPO)")
    ap.add_argument("--fail-dir", help="where screenshots of failures go (default: /tmp/veldris_emu_fail)")
    return ap.parse_args(argv)


def main(argv=None):
    """Run the tests registered so far. Test files call this at the bottom."""
    args = parse_args(argv)
    tests = [t for t in REGISTRY if not args.only or args.only.lower() in t.name.lower()]
    if args.list:
        for t in tests:
            print("%-52s %s%s" % (t.name, t.file, "  [slow]" if t.slow else ""))
        return 0
    if not tests:
        print("no tests match")
        return 2
    sys.exit(run(tests, args))
