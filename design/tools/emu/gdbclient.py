"""A very small GDB remote-serial-protocol client, written for mGBA's GDB stub.

Only what the test harness needs: read memory, write memory, continue, interrupt, one connection.
Standard library only.

How mGBA's stub behaves (measured against mgba-sdl 0.10.2 started with `mgba -g`, 2026-10-09; see README.md):

* It listens on port 2345 and that cannot be changed (`-C gdb.port=...` is ignored). It serves ONE connection for
  the whole life of the emulator: once a client disconnects, a second client is never answered. So connect once and
  keep the socket open until the emulator is shut down.
* Until a client connects the game just runs. The moment the client connects the stub stops the game, and the first
  `?` is answered with the stop reply 'S02'. Nothing runs again until the client sends 'c'.
* Packets: '$payload#cc' with a two-digit hex checksum, and a '+' acknowledgement from the receiver for each one.
  'm' (read) and 'M' (write, hex) are used. A single read of more than 512 bytes fails (error E06), so reads and
  writes go in 256 byte pieces. Binary 'X' writes also work but are not needed.
* **Reads and writes work while the game is running**: the stub answers them between two CPU instructions in under a
  millisecond (4000 reads in 3 s cost no frames at all). One packet is therefore one consistent snapshot of that
  memory range. That is the normal way this harness looks at the game.
* **The trap: a memory packet sent within about 0.1 s after 'c' freezes the game, and it stays frozen for as long as
  packets keep arriving** (seen as 'script running forever' and 'zero frames'; silence frees it again). At normal
  speed a packet right after 'c' froze it every time, 0.05 s later in 3 of 12 tries, 0.07 s or later in none of 72.
  The 0x03 interrupt is not affected. This client therefore waits 0.15 s after every 'c' before it sends the next
  'm' or 'M' (`QUIET_AFTER_CONT`).
* Stopping the game (0x03, wait for 'S02') and starting it again ('c') costs the emulator some game time and 0.15 s
  of quiet. Stop the game only when several things must be read or written as one unit (`with gdb.halted():`),
  never in a polling loop.
"""

import socket
import time


class GdbError(Exception):
    pass


def checksum(payload):
    return sum(payload) & 0xFF


def frame(payload):
    return b"$" + payload + b"#" + b"%02x" % checksum(payload)


class Gdb:
    # One 'm' packet may ask for at most 512 bytes (measured); 256 leaves a margin.
    CHUNK = 256
    # Seconds of silence after 'c' (see the module notes: a packet inside that window freezes the game).
    QUIET_AFTER_CONT = 0.15

    def __init__(self, host="127.0.0.1", port=2345, timeout=3.0, connect_wait=15.0):
        self.host, self.port = host, port
        self.timeout = timeout
        self.sock = None
        self.buf = b""
        self.running = False       # the game is running (we sent 'c' and have not seen a stop reply)
        self.stop_replies = 0      # unexpected stops seen while we thought the game was running
        self.resends = 0           # how often a packet had to be sent again (a health indicator)
        self._quiet_until = 0.0
        self._connect(connect_wait)

    # ---- connection -------------------------------------------------------

    def _connect(self, wait):
        """Connect, retrying while the emulator is still starting up."""
        deadline = time.time() + wait
        last = None
        while time.time() < deadline:
            try:
                self.sock = socket.create_connection((self.host, self.port), timeout=self.timeout)
                self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                return
            except OSError as e:
                last = e
                time.sleep(0.2)
        raise GdbError("could not connect to the GDB stub on port %d: %s" % (self.port, last))

    def close(self):
        if self.sock:
            try:
                self.sock.close()
            except OSError:
                pass
            self.sock = None

    # ---- raw packets ------------------------------------------------------

    def _read_some(self, timeout):
        self.sock.settimeout(timeout)
        try:
            data = self.sock.recv(65536)
        except socket.timeout:
            return False
        except OSError as e:
            raise GdbError("socket error: %s" % e)
        if not data:
            raise GdbError("the emulator closed the GDB connection (did it crash?)")
        self.buf += data
        return True

    @staticmethod
    def _unescape(body):
        """Undo run-length encoding ('x*n') and binary escaping ('}' xor 0x20)."""
        out = bytearray()
        i = 0
        while i < len(body):
            c = body[i]
            if c == 0x2A and out:  # '*': repeat previous byte (n - 29) more times
                out.extend(bytes([out[-1]]) * (body[i + 1] - 29))
                i += 2
            elif c == 0x7D and i + 1 < len(body):  # '}'
                out.append(body[i + 1] ^ 0x20)
                i += 2
            else:
                out.append(c)
                i += 1
        return bytes(out)

    def _get_packet(self, timeout):
        """Return the payload of the next packet, or None on timeout.

        Acks ('+') and nacks ('-') that come before it are returned as the
        strings b'+' and b'-'. Bad checksums are nacked and skipped.
        """
        deadline = time.time() + timeout
        while True:
            # look for something complete in the buffer
            while self.buf[:1] in (b"+", b"-"):
                c, self.buf = self.buf[:1], self.buf[1:]
                return c
            start = self.buf.find(b"$")
            if start >= 0:
                end = self.buf.find(b"#", start)
                if end >= 0 and len(self.buf) >= end + 3:
                    body = self.buf[start + 1:end]
                    want = int(self.buf[end + 1:end + 3], 16)
                    self.buf = self.buf[end + 3:]
                    if checksum(body) != want:
                        self.sock.sendall(b"-")
                        continue
                    self.sock.sendall(b"+")
                    return self._unescape(body)
            elif self.buf:
                # junk without a '$' (stray bytes): drop it
                self.buf = b""
            left = deadline - time.time()
            if left <= 0:
                return None
            self._read_some(left)

    def _drain(self):
        """Throw away anything that arrived late, so an old reply is never taken for a new one."""
        self.buf = b""
        self.sock.settimeout(0)
        try:
            while self.sock.recv(65536):
                pass
        except (BlockingIOError, socket.timeout):
            pass
        except OSError:
            pass

    @staticmethod
    def _is_stop(pkt):
        return pkt[:1] in (b"S", b"T", b"W", b"X") and len(pkt) >= 3

    def _transact(self, payload, timeout=None, retries=3):
        """Send one packet and return the reply payload. Works with the game running or stopped.

        A '-' (nack) or a silence of `timeout` seconds sends the packet again, up to `retries` times; a late reply to
        an earlier try is thrown away first so it cannot be mistaken for the answer to this one. If the game turns out
        to have stopped by itself (a stop reply instead of data), that is recorded and the request is asked again.
        """
        timeout = timeout or self.timeout
        self.wait_quiet()  # never send a memory packet right after 'c': it would freeze the game
        for attempt in range(retries):
            if attempt:
                self.resends += 1
                self._drain()
            self.sock.sendall(frame(payload))
            deadline = time.time() + timeout
            while True:
                pkt = self._get_packet(max(0.01, deadline - time.time()))
                if pkt is None:
                    break  # timed out: resend
                if pkt == b"+":
                    continue
                if pkt == b"-":
                    break  # nacked: resend
                if payload[:1] in b"mM" and self._is_stop(pkt):
                    self.running = False  # the game stopped on its own (it should not); carry on halted
                    self.stop_replies += 1
                    continue
                return pkt
        raise GdbError("no reply to %r after %d tries" % (payload[:24], retries))

    # ---- run control ------------------------------------------------------

    def wait_stop(self, timeout=5.0):
        """Wait for a stop reply (S02, T05..., W00...). Returns it as text."""
        deadline = time.time() + timeout
        while True:
            pkt = self._get_packet(max(0.01, deadline - time.time()))
            if pkt is None:
                raise GdbError("the emulator did not stop within %.1f s" % timeout)
            if pkt in (b"+", b"-"):
                continue
            if pkt[:1] in (b"S", b"T"):
                self.running = False
                return pkt.decode("ascii", "replace")
            if pkt[:1] in (b"W", b"X"):
                self.running = False
                raise GdbError("the emulator process ended: %s" % pkt.decode("ascii", "replace"))
            # 'O' console output or anything else: ignore

    def initial_stop(self, timeout=10.0):
        """The stub halts the game when we connect. Fetch the reason ('S02')."""
        self.running = False
        return self._transact(b"?", timeout=timeout).decode("ascii", "replace")

    def cont(self):
        """Resume the game. There is no reply until the next stop."""
        if self.running:
            return
        self.sock.sendall(frame(b"c"))
        self.running = True
        self._quiet_until = time.time() + self.QUIET_AFTER_CONT

    def interrupt(self, timeout=5.0):
        """Stop a running game (sends the 0x03 byte) and wait for the stop reply."""
        if not self.running:
            return
        self.sock.sendall(b"\x03")
        self.wait_stop(timeout)

    def wait_quiet(self):
        """Sleep until the quiet time after the last 'c' is over (only matters right after a halted() block)."""
        if self.running:
            left = self._quiet_until - time.time()
            if left > 0:
                time.sleep(left)

    class _Halted:
        def __init__(self, gdb):
            self.gdb = gdb
            self.was_running = False

        def __enter__(self):
            self.was_running = self.gdb.running
            if self.was_running:
                self.gdb.interrupt()
            return self.gdb

        def __exit__(self, *exc):
            if self.was_running:
                self.gdb.cont()
            return False

    def halted(self):
        """`with gdb.halted(): ...` stops the game for the block, then resumes.

        Use it only when several reads or writes must see (or make) one consistent state, for example when pointing
        the script engine at new code. It costs the emulator about 30 ms of game time every time. It nests.
        """
        return Gdb._Halted(self)

    # ---- memory -----------------------------------------------------------

    def read(self, addr, length):
        """Read `length` bytes. Does not stop the game. Each 256 byte piece is one consistent snapshot."""
        out = bytearray()
        while length > 0:
            n = min(length, self.CHUNK)
            reply = self._transact(b"m%x,%x" % (addr, n))
            if reply[:1] == b"E" or len(reply) != 2 * n:
                raise GdbError("read of %d bytes at 0x%08x failed: %r" % (n, addr, reply[:20]))
            out += bytes.fromhex(reply.decode("ascii"))
            addr += n
            length -= n
        return bytes(out)

    def write(self, addr, data):
        """Write bytes. Does not stop the game. Each 256 byte piece lands between two CPU instructions."""
        data = bytes(data)
        pos = 0
        while pos < len(data):
            piece = data[pos:pos + self.CHUNK]
            reply = self._transact(b"M%x,%x:" % (addr + pos, len(piece)) + piece.hex().encode("ascii"))
            if reply != b"OK":
                raise GdbError("write of %d bytes at 0x%08x failed: %r" % (len(piece), addr + pos, reply[:20]))
            pos += len(piece)

    # Typed helpers (little endian, like the GBA).
    def u8(self, addr):
        return self.read(addr, 1)[0]

    def u16(self, addr):
        return int.from_bytes(self.read(addr, 2), "little")

    def u32(self, addr):
        return int.from_bytes(self.read(addr, 4), "little")

    def put_u8(self, addr, v):
        self.write(addr, bytes([v & 0xFF]))

    def put_u16(self, addr, v):
        self.write(addr, (v & 0xFFFF).to_bytes(2, "little"))

    def put_u32(self, addr, v):
        self.write(addr, (v & 0xFFFFFFFF).to_bytes(4, "little"))
