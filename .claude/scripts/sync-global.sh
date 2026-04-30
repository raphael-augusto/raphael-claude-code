#!/usr/bin/env bash
# Sincroniza global-CLAUDE.md do repo para ~/.claude/CLAUDE.md
# Roda em todo PostToolUse — pure bash, diff apenas, overhead < 1ms
# Nova maquina: primeiro tool use ja sincroniza automaticamente

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE="$SCRIPT_DIR/../global-CLAUDE.md"
GLOBAL="$HOME/.claude/CLAUDE.md"

[[ -f "$SOURCE" ]] || exit 0

if ! diff -q "$SOURCE" "$GLOBAL" > /dev/null 2>&1; then
    cp "$SOURCE" "$GLOBAL"
fi
