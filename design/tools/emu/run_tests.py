#!/usr/bin/env python3
"""Run every emulator test: python3 design/tools/emu/run_tests.py

    --list          show the tests
    --only TEXT     run the tests whose name contains TEXT
    --slow          also run the slow ones (the Route 1 night encounters)

Prints one PASS / FAIL line per test and exits with a non-zero code if anything failed.
Screenshots of failures go to /tmp/veldris_emu_fail/. See README.md.
"""

import testkit

if __name__ == "__main__":
    testkit.load_test_files()
    testkit.main()
