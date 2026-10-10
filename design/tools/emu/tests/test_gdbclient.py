#!/usr/bin/env python3
"""The GDB client on its own, against a pretend stub: no emulator is started, so this takes a second.

It checks the parts of the protocol that mGBA's real stub never gets wrong, so they could otherwise go untested:
a reply with a bad checksum, a reply that never comes, run-length and escaped data, an error reply, the interrupt
byte, and the quiet time the client keeps after 'c' (see gdbclient.py for why).
"""
import os
import socket
import sys
import threading
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import testkit
from gdbclient import Gdb, GdbError, checksum, frame
from testkit import check, check_eq


class FakeStub(threading.Thread):
    """A one-connection RSP server. `script` maps the request number of an 'm' packet to what to do with it."""

    def __init__(self, script=None):
        super().__init__(daemon=True)
        self.listener = socket.socket()
        self.listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listener.bind(("127.0.0.1", 0))
        self.listener.listen(1)
        self.port = self.listener.getsockname()[1]
        self.script = script or {}
        self.seen = []  # (time, payload) of every packet received
        self.nacks = 0
        self.last = b""  # the last reply payload, sent again when the client says '-'
        self.stop = False
        self.start()

    def reply(self, conn, payload, bad_checksum=False):
        self.last = payload
        pkt = frame(payload)
        if bad_checksum:
            pkt = pkt[:-2] + (b"00" if pkt[-2:] != b"00" else b"11")
        conn.sendall(pkt)

    def run(self):
        conn, _ = self.listener.accept()
        conn.settimeout(0.1)
        buf, n_m = b"", 0
        while not self.stop:
            try:
                data = conn.recv(4096)
            except socket.timeout:
                continue
            except OSError:
                return
            if not data:
                return
            buf += data
            while buf:
                if buf[:1] == b"-":
                    self.nacks += 1
                    buf = buf[1:]
                    self.reply(conn, self.last)  # what a real stub does: send it again, this time correctly
                    continue
                if buf[:1] in (b"+",):
                    buf = buf[1:]
                    continue
                if buf[:1] == b"\x03":
                    buf = buf[1:]
                    self.seen.append((time.time(), b"\x03"))
                    self.reply(conn, b"S02")
                    continue
                end = buf.find(b"#")
                if buf[:1] != b"$" or end < 0 or len(buf) < end + 3:
                    break
                payload, buf = buf[1:end], buf[end + 3:]
                self.seen.append((time.time(), payload))
                conn.sendall(b"+")
                if payload[:1] == b"m":
                    n_m += 1
                    action = self.script.get(n_m, "ok")
                    addr, _, length = payload[1:].partition(b",")
                    length = int(length, 16)
                    if action == "silence":
                        continue
                    if action == "badsum":
                        self.reply(conn, b"ab" * length, bad_checksum=True)
                        continue
                    if action == "rle":  # 'a' then '* ' = repeat three more times: four bytes of 0xaa
                        conn.sendall(b"$a* #" + b"%02x" % checksum(b"a* "))
                        continue
                    if action == "escape":  # 0x7d (shown as '}' then 0x5d) and 0x23 ('#' as '}' then 0x03)
                        body = b"}]" + b"}\x03"
                        conn.sendall(b"$" + body + b"#" + b"%02x" % checksum(body))
                        continue
                    if action == "error":
                        self.reply(conn, b"E06")
                        continue
                    self.reply(conn, b"%02x" % (int(addr, 16) & 0xFF) * length)
                elif payload[:1] == b"M":
                    self.reply(conn, b"OK")
                elif payload == b"?":
                    self.reply(conn, b"S02")
                elif payload == b"c":
                    pass  # no reply until the next stop

    def close(self):
        self.stop = True
        self.listener.close()


@testkit.test("gdb client: checksums, resends, odd data, errors, interrupt, quiet time", emulator=False)
def gdb_client(ctx):
    # 1. a normal read comes back as bytes; the address picks the byte pattern in the pretend stub
    stub = FakeStub()
    g = Gdb(port=stub.port, timeout=0.4, connect_wait=3)
    check_eq(g.initial_stop(), "S02", "stop reply at connect")
    check_eq(g.read(0x02000007, 3), b"\x07\x07\x07", "plain read")
    g.write(0x02000000, b"\x01\x02\x03")
    check_eq(stub.seen[-1][1], b"M2000000,3:010203", "write packet")
    # a long read is cut into pieces of at most 256 bytes
    check_eq(len(g.read(0x02000000, 600)), 600, "600 byte read")
    sizes = [int(p[1:].split(b",")[1], 16) for _, p in stub.seen if p[:1] == b"m"]
    check(max(sizes) <= 256, "a read asked for more than 256 bytes at once: %s" % sizes)
    g.close()
    stub.close()

    # 2. bad checksum -> '-' -> the stub sends it again; silence -> the client sends the request again; error reply
    stub = FakeStub({1: "badsum", 2: "silence", 4: "error"})  # request 3 is the resend of request 2
    g = Gdb(port=stub.port, timeout=0.4, connect_wait=3)
    g.initial_stop()
    check_eq(g.read(0x02000000, 1), b"\xab", "read after a bad checksum")  # 1: bad sum, the client sends '-'
    check_eq(stub.nacks, 1, "the client should have sent exactly one '-'")
    check(g.read(0x02000000, 1) == b"\x00", "read after silence")
    check(g.resends >= 1, "the client should have resent the silent request")
    try:
        g.read(0x02000000, 1)
    except GdbError as e:
        check("failed" in str(e), "error text should say the read failed: %s" % e)
    else:
        check(False, "an E06 reply must raise GdbError")
    g.close()
    stub.close()

    # 3. run-length encoding and '}' escapes in a reply are undone (as GDB's own stubs may send them)
    check_eq(Gdb._unescape(b"a* "), b"aaaa", "run-length data")
    check_eq(Gdb._unescape(b"}]}\x03"), b"}#", "escaped data")

    # 4. interrupt: 0x03 gets an S02; and after 'c' the client keeps quiet before the next memory packet
    stub = FakeStub()
    g = Gdb(port=stub.port, timeout=0.5, connect_wait=3)
    g.QUIET_AFTER_CONT = 0.2
    g.initial_stop()
    g.cont()
    check(g.running, "running after cont")
    t_cont = time.time()
    g.read(0x02000000, 1)  # sent while 'running': must wait out the quiet time first
    first_m = [t for t, p in stub.seen if p[:1] == b"m"][0]
    check(first_m - t_cont >= 0.19, "a memory packet went out %.3f s after 'c' (needs >= 0.2 s)" % (first_m - t_cont))
    g.interrupt()
    check(not g.running, "stopped after interrupt")
    check(any(p == b"\x03" for _, p in stub.seen), "the stub never saw the 0x03 byte")
    with g.halted():  # already stopped: neither interrupts nor resumes
        check(not g.running, "halted() must not resume a game that was stopped")
    g.cont()
    with g.halted():
        check(not g.running, "halted() stops a running game")
    check(g.running, "halted() resumes a game that was running")
    g.close()
    stub.close()


if __name__ == "__main__":
    testkit.main()
