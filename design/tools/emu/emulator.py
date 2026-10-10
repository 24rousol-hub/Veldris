"""Start a headless mGBA on a copy of the ROM, press buttons, take screenshots.

Only processes this module started are ever stopped: Xvfb and mGBA are killed by
their own process id, never by name.
"""

import atexit
import fcntl
import itertools
import os
import shutil
import socket
import subprocess
import tempfile
import time
from pathlib import Path

from game import BUTTON_BITS, DIR_STEP, Game, GameError, Timeout
from gdbclient import Gdb, GdbError
from layout import Layout, find_repo

MGBA = os.environ.get("MGBA") or shutil.which("mgba") or "/usr/games/mgba"
GDB_PORT = 2345  # mGBA 0.10 has no option to change it
LOCK_PATH = "/tmp/veldris-emu-gdb-2345.lock"

# GBA button -> key mGBA listens to
KEYS = {"A": "x", "B": "z", "START": "Return", "SELECT": "BackSpace", "L": "a", "R": "s",
        "UP": "Up", "DOWN": "Down", "LEFT": "Left", "RIGHT": "Right",
        "U": "Up", "D": "Down", "N": "Up", "S": "Down", "W": "Left", "E": "Right"}
# walking directions: U/D/L/R (and N/S/W/E for facing)
WALK_KEYS = {"U": "Up", "D": "Down", "L": "Left", "R": "Right"}

# program -> the apt package that provides it (for the message when something is missing)
REQUIRED_TOOLS = {"Xvfb": "xvfb", "xdotool": "xdotool", "import": "imagemagick",
                  "arm-none-eabi-gcc": "gcc-arm-none-eabi", "arm-none-eabi-nm": "binutils-arm-none-eabi",
                  "arm-none-eabi-objcopy": "binutils-arm-none-eabi"}


def missing_tools():
    """Programs the robot needs that are not installed, as a list of (program, apt package)."""
    out = [(prog, pkg) for prog, pkg in REQUIRED_TOOLS.items() if shutil.which(prog) is None]
    if not (os.path.isfile(MGBA) and os.access(MGBA, os.X_OK)):
        out.append((MGBA, "mgba-sdl"))
    return out


def tools_message():
    """'' if everything is installed, else the one command that fixes it."""
    miss = missing_tools()
    if not miss:
        return ""
    pkgs = sorted({pkg for _, pkg in miss})
    return "missing: %s. Install with: apt-get install -y %s" % (", ".join(p for p, _ in miss), " ".join(pkgs))


_live = []  # things to clean up at exit


def _cleanup_all():
    for obj in list(_live):
        try:
            obj.close()
        except Exception:
            pass


atexit.register(_cleanup_all)


def _alive(pid):
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False


def _terminate(proc, grace=3.0, now=False):
    """Stop one Popen we started: SIGTERM, then SIGKILL (straight to SIGKILL with now=True)."""
    if proc is None or proc.poll() is not None:
        return
    if now:
        proc.kill()
        proc.wait(5)
        return
    proc.terminate()
    try:
        proc.wait(grace)
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.wait(5)


class Display:
    """An Xvfb virtual screen. Reuses one that is already running on that number; stops it only if we started it."""

    def __init__(self, number=97, size="1280x960x24"):
        self.number = number
        self.name = ":%d" % number
        self.size = size
        self.proc = None
        self.started_by_us = False
        _live.append(self)

    def _socket(self):
        return Path("/tmp/.X11-unix/X%d" % self.number)

    def _responds(self):
        try:
            r = subprocess.run(["xdotool", "getdisplaygeometry"], env=dict(os.environ, DISPLAY=self.name),
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5)
            return r.returncode == 0
        except (OSError, subprocess.TimeoutExpired):
            return False

    def start(self):
        if self._socket().exists() and self._responds():
            return self  # somebody's Xvfb is already there: use it, leave it alone afterwards
        lock = Path("/tmp/.X%d-lock" % self.number)
        if lock.exists():
            try:
                pid = int(lock.read_text().strip())
            except ValueError:
                pid = 0
            if not pid or not _alive(pid):  # stale lock from a crashed Xvfb
                for f in (lock, self._socket()):
                    try:
                        f.unlink()
                    except OSError:
                        pass
        self.proc = subprocess.Popen(["Xvfb", self.name, "-screen", "0", self.size, "-nolisten", "tcp"],
                                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        self.started_by_us = True
        end = time.time() + 15
        while time.time() < end:
            if self.proc.poll() is not None:
                raise GameError("Xvfb %s exited at once (is another X server on that number?)" % self.name)
            if self._socket().exists() and self._responds():
                return self
            time.sleep(0.1)
        self.close()
        raise GameError("Xvfb %s did not come up" % self.name)

    def close(self):
        if self.started_by_us:
            _terminate(self.proc)
            self.proc = None
            self.started_by_us = False
        if self in _live:
            _live.remove(self)


class Emulator:
    """One mGBA process plus a connection to its GDB stub. Use as a context manager.

        with Emulator() as emu:
            emu.boot_to_title()
            emu.quickstart()
            print(emu.game.map_name())
    """

    def __init__(self, rom=None, repo=None, display=None, turbo=True, workdir=None, scale=3, lock_timeout=600,
                 layout=None):
        self.repo = Path(repo) if repo else find_repo()
        self.rom_src = Path(rom) if rom else self.repo / "pokeemerald.gba"
        self.elf = self.rom_src.with_suffix(".elf")
        self.start_turbo = turbo
        self._turbo = False
        self.scale = scale
        self.lock_timeout = lock_timeout
        self.own_display = display is None
        self.display = display or Display(int(os.environ.get("EMU_DISPLAY", "97")))
        self._own_workdir = workdir is None
        self.workdir = Path(workdir) if workdir else Path(tempfile.mkdtemp(prefix="veldris_emu_"))
        self.proc = None
        self.gdb = None
        self.game = None
        self.layout = layout
        self.window = None
        self._lock_fh = None
        self.log_path = self.workdir / "mgba.log"
        _live.append(self)

    # ---- life cycle ----------------------------------------------------------

    def __enter__(self):
        return self.start()

    def __exit__(self, *exc):
        self.close()
        return False

    def _take_lock(self):
        """Only one harness may use the GDB port at a time. Wait politely for the other one."""
        self._lock_fh = open(LOCK_PATH, "w")
        end = time.time() + self.lock_timeout
        while True:
            try:
                fcntl.flock(self._lock_fh, fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except OSError:
                if time.time() > end:
                    raise GameError("another emulator test run has held the GDB port for %.0f s" % self.lock_timeout)
                time.sleep(0.5)
        # the lock is ours, but a foreign mGBA (not started by this harness) may still own the port
        end = time.time() + 20
        while True:
            s = socket.socket()
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # a port in TIME_WAIT is free; a listener is not
            try:
                s.bind(("127.0.0.1", GDB_PORT))
                s.close()
                return
            except OSError:
                s.close()
                if time.time() > end:
                    raise GameError("port %d is in use by a program that is not this harness; stop that mGBA first" % GDB_PORT)
                time.sleep(0.5)

    def start(self):
        msg = tools_message()
        if msg:
            raise GameError(msg)
        if not self.rom_src.exists():
            raise GameError("no ROM at %s. Build the game first (make -j4)." % self.rom_src)
        if self.layout is None:
            self.layout = Layout(self.repo, self.elf if self.elf.exists() else None)
        self.display.start()
        self._take_lock()
        rom = self.workdir / "game.gba"
        shutil.copyfile(self.rom_src, rom)  # always a copy, so saves never land in the repo
        # Real-time by default. Speed is switched at run time with mGBA's fast-forward key (Tab), see turbo().
        cmd = [MGBA, "-g", "-%d" % self.scale, str(rom)]
        env = dict(os.environ, DISPLAY=self.display.name, SDL_AUDIODRIVER="dummy")
        with open(self.log_path, "wb") as log:
            self.proc = subprocess.Popen(cmd, env=env, stdout=log, stderr=subprocess.STDOUT, cwd=str(self.workdir))
        try:
            self.gdb = Gdb(port=GDB_PORT, connect_wait=20)
            self.gdb.initial_stop()
            self.game = Game(self.gdb, self.layout)
            self.gdb.cont()
            self._find_window()
            self.turbo(self.start_turbo)
        except Exception:
            self.close()
            raise
        return self

    def close(self):
        if self.gdb is not None:
            self.gdb.close()
            self.gdb = None
        _terminate(self.proc, now=True)  # a throw-away copy of the game: SIGTERM would only add about 2 s per test
        self.proc = None
        if self._lock_fh is not None:
            try:
                fcntl.flock(self._lock_fh, fcntl.LOCK_UN)
                self._lock_fh.close()
            except OSError:
                pass
            self._lock_fh = None
        if self.own_display:
            self.display.close()
        if self._own_workdir and self.workdir.exists() and not os.environ.get("EMU_KEEP"):
            shutil.rmtree(self.workdir, ignore_errors=True)
        if self in _live:
            _live.remove(self)

    def alive(self):
        return self.proc is not None and self.proc.poll() is None

    # ---- X11: window, keys, screenshots ----------------------------------------

    def _x(self, *args, check=True, timeout=10):
        r = subprocess.run(["xdotool"] + [str(a) for a in args], env=dict(os.environ, DISPLAY=self.display.name),
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=timeout)
        if check and r.returncode != 0:
            raise GameError("xdotool %s failed: %s" % (" ".join(map(str, args)), r.stderr.strip()))
        return r.stdout

    def _find_window(self):
        end = time.time() + 20
        while time.time() < end:
            if not self.alive():
                raise GameError("mGBA exited at start-up. Log:\n" + self.log_path.read_text(errors="replace")[-1500:])
            out = self._x("search", "--class", "mgba", check=False).split()
            if not out:
                out = self._x("search", "--name", "mGBA", check=False).split()
            if out:
                self.window = out[-1]
                break
            time.sleep(0.2)
        else:
            raise GameError("could not find the mGBA window")
        # the picture does not draw properly until the window has been resized once
        w, h = 240 * self.scale, 160 * self.scale
        self._x("windowsize", self.window, w + 2, h + 2)
        time.sleep(0.2)
        self._x("windowsize", self.window, w, h)
        self._x("windowfocus", self.window, check=False)

    def geometry(self):
        out = self._x("getwindowgeometry", "--shell", self.window)
        g = dict(line.split("=") for line in out.split())
        return int(g["X"]), int(g["Y"]), int(g["WIDTH"]), int(g["HEIGHT"])

    def screenshot(self, path):
        """Save the game picture (just the mGBA window) as a PNG. Returns the path."""
        x, y, w, h = self.geometry()
        path = str(path)
        subprocess.run(["import", "-window", "root", "-crop", "%dx%d+%d+%d" % (w, h, x, y), "+repage", path],
                       env=dict(os.environ, DISPLAY=self.display.name), check=True, timeout=20,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return path

    def press(self, button, hold=0.12):
        """Hold a button for `hold` seconds (a plain xdotool 'key' drops presses, so this always holds).

        Buttons: A B START SELECT L R UP DOWN LEFT RIGHT. At turbo speed 0.12 s is about 50 game frames; at normal
        speed about 7. Either is enough for the game to notice.

        Returns True if the game was seen to hold that button (it checks gMain.heldKeysRaw while the key is down).
        False means the press never reached the game, so a test that says 'pressing X does nothing' must check it.
        """
        name = button.upper()
        key = KEYS[name]
        bit = BUTTON_BITS.get(name)
        if self.gdb is not None:
            self.gdb.wait_quiet()  # so the 'did the game see it' reads can start while the key is still down
        proc = subprocess.Popen(["xdotool", "keydown", key, "sleep", str(hold), "keyup", key],
                                env=dict(os.environ, DISPLAY=self.display.name), stdout=subprocess.DEVNULL,
                                stderr=subprocess.PIPE)
        seen = bit is None or self.game is None  # aliases (U, D, N ...) are not checked
        while proc.poll() is None:
            if not seen:
                try:
                    seen = bool(self.game.u16(self.game.a("gMain") + self.game.off("Main", "heldKeysRaw")) & bit)
                except (GdbError, GameError):
                    pass
            time.sleep(0.004)
        if proc.returncode != 0:
            raise GameError("xdotool key %s failed: %s" % (key, proc.stderr.read().decode(errors="replace").strip()))
        return seen

    def press_until(self, button, until, tries=3, wait=1.5, hold=0.12):
        """Press `button`, wait up to `wait` seconds for `until()` to become true, and press again if it did not.

        A key press can be lost when the machine is busy (a build running next to the test, for example), so use this
        whenever one press has one visible result. Do not use it for toggles that have no result you can check.
        Returns the number of presses it took; raises Timeout after `tries`.
        """
        g = self.game
        for n in range(1, tries + 1):
            self.press(button, hold)
            end = time.time() + wait
            while time.time() < end:
                if until():
                    return n
                time.sleep(0.02)
        raise Timeout("pressing %s %d times did not have the expected result. %s" % (button, tries, g.summary()))

    def press_seq(self, buttons, hold=0.12, gap=0.12):
        for b in buttons:
            self.press(b, hold)
            time.sleep(gap)

    def key_down(self, button):
        self._x("keydown", KEYS[button.upper()])

    def key_up(self, button):
        self._x("keyup", KEYS[button.upper()])

    def turbo(self, on=True):
        """Fast-forward (about 7 times real time) on or off. Holds mGBA's Tab key. Returns the previous setting."""
        was = self._turbo
        if on != was:
            self._x("keydown" if on else "keyup", "Tab")
            self._turbo = on
        return was

    def realtime(self):
        """`with emu.realtime():` runs the block at normal speed (for exact walking), then restores turbo."""
        emu = self

        class _Ctx:
            def __enter__(self):
                self.was = emu.turbo(False)

            def __exit__(self, *exc):
                emu.turbo(self.was)
                return False
        return _Ctx()

    # ---- driving the game --------------------------------------------------------

    def boot_to_title(self, timeout=90.0):
        """Wait for the title screen. B skips the intro and the title animation but does nothing on the finished
        title, so it cannot start the game by accident (START would open the main menu, SELECT would quickstart)."""
        g = self.game
        end = time.time() + timeout
        last_press = 0.0
        while True:
            if not self.alive():
                raise GameError("mGBA died during boot. Log:\n" + self.log_path.read_text(errors="replace")[-1500:])
            if g.state() == "title":
                return
            if time.time() > end:
                raise Timeout("never reached the title screen. %s" % g.summary())
            if time.time() - last_press > 1.5:
                self.press("B", hold=0.1)
                last_press = time.time()
            time.sleep(0.1)

    def quickstart(self, timeout=60.0):
        """Title screen SELECT: skip Birch's speech and begin a new game. Returns when the bedroom is playable."""
        g = self.game
        if g.state() != "title":
            raise GameError("quickstart needs the title screen. %s" % g.summary())
        end = time.time() + timeout
        while g.state() == "title":
            self.press("SELECT", hold=0.12)
            time.sleep(0.4)
            if time.time() > end:
                raise Timeout("SELECT did not start a new game (is ENABLE_QUICKSTART on?). %s" % g.summary())
        g.wait_overworld_idle(timeout)

    def new_game(self):
        """Boot, quickstart, and return when the player can move in the bedroom."""
        self.boot_to_title()
        self.quickstart()
        return self

    def _walk_needs_b(self):
        """True if B must be held to *walk* (the hack runs by default once the shoes are given)."""
        g = self.game
        try:
            return bool(g.flag_get("FLAG_SYS_B_DASH") and g.flag_get("FLAG_SYS_RUN_BY_DEFAULT"))
        except Exception:
            return False

    def step(self, direction, timeout=5.0, _hold_b=None):
        """Walk exactly one tile (U, D, L, R) at normal speed. Returns True if the player moved.

        The key goes down, the game is polled every 10 ms (a poll is free: the game keeps running), and the key goes up
        as soon as the position changes, which is early enough that the player takes one step and no more. Do not call
        this at turbo speed: at 8 times speed one tile lasts about 35 ms, shorter than a key release can be timed.
        """
        g = self.game
        key = WALK_KEYS[direction.upper()]
        hold_b = self._walk_needs_b() if _hold_b is None else _hold_b
        before = g.player_pos()
        if hold_b:
            self._x("keydown", KEYS["B"])
        self._x("keydown", key)
        moved = False
        try:
            end = time.time() + timeout
            while time.time() < end:
                time.sleep(0.01)
                if g.player_pos() != before:
                    moved = True
                    break
                if g.busy():
                    break
        finally:
            self._x("keyup", key)
            if hold_b:
                self._x("keyup", KEYS["B"])
        # let the step finish (a script may take over instead, for example on a trigger tile)
        end = time.time() + 5
        while time.time() < end and g.avatar_moving():
            time.sleep(0.02)
        return moved

    def face(self, direction, timeout=2.0):
        """Turn to face N, S, W or E (or U, D, L, R) without walking: only use it towards a blocked tile or an NPC."""
        want = {"U": "N", "D": "S", "L": "W", "R": "E"}.get(direction.upper(), direction.upper())
        g = self.game
        if g.player_facing() == want:
            return True
        key = WALK_KEYS[{"N": "U", "S": "D", "W": "L", "E": "R"}[want]]
        self._x("keydown", key)
        try:
            end = time.time() + timeout
            while time.time() < end:
                if g.player_facing() == want:
                    return True
                time.sleep(0.01)
        finally:
            self._x("keyup", key)
        return g.player_facing() == want

    def _walk_run(self, direction, count, hold_b, stall=1.0):
        """Hold one direction key until the player stands `count` tiles further on. Returns (tiles moved, busy).

        Position changes when a step starts, so the key is let go the moment the player has arrived at the target
        tile: the step into it is already under way and no further step begins. The key release takes about 30 ms and
        a walking step lasts about 270 ms, so there is a wide margin.
        """
        g = self.game
        key = WALK_KEYS[direction]
        dx, dy = DIR_STEP[direction]
        start = g.player_pos()
        start_map = g.map_id()
        goal = (start[0] + count * dx, start[1] + count * dy)
        if hold_b:
            self._x("keydown", KEYS["B"])
        self._x("keydown", key)
        pos, last_change, polls, busy = start, time.time(), 0, None
        try:
            while pos != goal:
                time.sleep(0.008)
                now = g.player_pos()
                if now != pos:
                    pos, last_change = now, time.time()
                elif time.time() - last_change > stall:
                    break  # not moving: a wall, an NPC, or a ledge
                polls += 1
                if polls % 4 == 0:
                    busy = g.busy() or ("map change" if g.map_id() != start_map else None)
                    if busy:
                        break  # a trigger, a trainer or a wild battle took over, or the player walked through a door
        finally:
            self._x("keyup", key)
            if hold_b:
                self._x("keyup", KEYS["B"])
        return abs(pos[0] - start[0]) + abs(pos[1] - start[1]), busy

    def walk(self, directions, run=False):
        """Walk a string such as 'RRUU' tile by tile at normal speed. Returns (ok, tiles_walked).

        A straight stretch is walked with one key held down and released the moment the player arrives, so the
        number of tiles is exact. It stops early (ok=False) at a wall or an NPC, and stops (ok=True) when a script,
        a trainer or a wild battle takes over or the player walks through a door, so check `game.busy()` and
        `game.map_name()` afterwards. `run=True` lets the game's own
        run setting decide (faster, with a smaller margin for the key release).
        """
        g = self.game
        hold_b = False if run else self._walk_needs_b()
        done = 0
        runs = [(d, len(list(grp))) for d, grp in itertools.groupby(directions.upper())]
        with self.realtime():
            for d, n in runs:
                moved, busy = self._walk_run(d, n, hold_b)
                done += moved
                if moved < n:
                    return (busy is not None), done
                if busy:
                    return True, done
            end = time.time() + 5
            while time.time() < end and g.avatar_moving():
                time.sleep(0.02)
        return True, done

    def walk_to(self, x, y, run=False):
        """Walk to a tile along a path found from the map's collision data. Returns True on arrival."""
        g = self.game
        path = g.find_path((x, y))
        if path is None:
            raise GameError("no path to (%d, %d) on %s from %s" % (x, y, g.map_name(), g.player_pos()))
        ok, _ = self.walk(path, run=run)
        return ok and g.player_pos() == (x, y)

    def read_dialogue(self, choose="A", timeout=60.0, start_wait=3.0):
        """Click through whatever message or script is running and return the texts it showed, in order.

        Presses A about every 0.3 s. For a YES/NO box it presses `choose` ('A' = YES, 'B' = NO). Stops when the player
        is free again. Raises if nothing starts within `start_wait` seconds.
        """
        g = self.game
        g.wait_until(lambda: g.script_running() or g.battle_pending(), start_wait, what="a script or message to start")
        seen, end = [], time.time() + timeout
        while g.script_running():
            if time.time() > end:
                raise Timeout("the dialogue did not end within %.0f s. %s" % (timeout, g.summary()))
            text = g.message_text()
            if text and (not seen or seen[-1] != text):
                seen.append(text)
            if "Task_HandleYesNoInput" in g.task_names():
                self.press(choose, hold=0.1)
            else:
                self.press("A", hold=0.1)
            time.sleep(0.25)
        g.wait_overworld_idle(30)
        return seen

    def approach(self, target):
        """Walk to the nearest free tile next to an NPC and turn to face it. Returns the direction faced ('U' ...).

        `target` is a local id name such as 'LOCALID_HOLLOWBROOK_MOM', a number, or a tile (x, y). Trigger tiles are
        avoided if there is another way; warp tiles never. An NPC that wanders may move while you walk.
        """
        g = self.game
        obj = g.object(target)
        if obj is None:
            raise GameError("no object %r on %s (hidden by a flag, or on another map?) %s" % (target, g.map_name(), g.summary()))
        snap = g.read_map()
        best = None
        for avoid in (True, "warps"):  # first without crossing any trigger tile, then allowing them
            for d, (dx, dy) in (("U", (0, -1)), ("D", (0, 1)), ("L", (-1, 0)), ("R", (1, 0))):
                spot = (obj["x"] - dx, obj["y"] - dy)  # stand here and step in direction d to bump into the NPC
                path = g.find_path(spot, snapshot=snap, avoid_special=avoid)
                if path is not None and (best is None or len(path) < len(best[1])):
                    best = (d, path, spot)
            if best:
                break
        if best is None:
            raise GameError("cannot reach any tile next to %r at (%d, %d). %s" % (target, obj["x"], obj["y"], g.summary()))
        d, path, spot = best
        if path:
            ok, _ = self.walk(path)
            if not ok or g.player_pos() != spot:
                raise GameError("stopped at %s on the way to %s. %s" % (g.player_pos(), spot, g.summary()))
        if not self.face(d):
            raise GameError("could not turn to face the NPC at (%d, %d). %s" % (obj["x"], obj["y"], g.summary()))
        return d

    def talk_to(self, target, choose="A", timeout=60.0):
        """`approach()` an NPC, press A and click through what it says. Returns the list of message texts shown."""
        self.approach(target)
        self.press("A")
        return self.read_dialogue(choose=choose, timeout=timeout)

    def mash(self, button="A", until=None, timeout=60.0, interval=0.35):
        """Press `button` every `interval` seconds until `until()` is true (or no script is running if None)."""
        g = self.game
        until = until or (lambda: g.overworld_idle())
        end = time.time() + timeout
        while True:
            if until():
                return
            if time.time() > end:
                raise Timeout("still waiting after mashing %s for %.0f s. %s" % (button, timeout, g.summary()))
            self.press(button, hold=0.1)
            time.sleep(interval)
