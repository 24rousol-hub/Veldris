#!/bin/bash
# Veldris SessionStart hook (Claude Code on the web: the container is fresh every session).
# Synchronous, idempotent, no prompts. Only runs in the web environment.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "${CLAUDE_PROJECT_DIR:-.}"

# Turn on the tracked pre-commit hook (ROM/save guard, text-fit check, wild-table lint). git keeps this setting in
# .git/config, which a fresh clone does not have, so without this line the guard silently does nothing.
git config core.hooksPath .githooks

# The hook needs python3 for the text and wild-table checks; say so loudly instead of failing at commit time.
if ! command -v python3 >/dev/null 2>&1; then
  echo "WARNING: python3 not found: .githooks/pre-commit cannot run its dialogue and wild-table checks." >&2
fi

# NOT done on purpose (changes how long every session takes to start, and needs the author's OK):
# installing the GBA toolchain that CLAUDE.md lists under Build.
# if ! command -v arm-none-eabi-gcc >/dev/null 2>&1; then
#   apt-get update -qq
#   apt-get install -y -qq gcc-arm-none-eabi binutils-arm-none-eabi libnewlib-arm-none-eabi libpng-dev pkg-config
# fi
