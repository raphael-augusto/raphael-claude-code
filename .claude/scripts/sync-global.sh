#!/usr/bin/env bash
# Copia .claude/CLAUDE.md do projeto para o global ~/.claude/CLAUDE.md
# Dispara automaticamente via hook PostToolUse quando Write/Edit tocar CLAUDE.md

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_CLAUDE="$SCRIPT_DIR/../CLAUDE.md"
GLOBAL_CLAUDE="$HOME/.claude/CLAUDE.md"

[[ -f "$PROJECT_CLAUDE" ]] || exit 0

PYTHON=$(command -v python3 2>/dev/null || command -v python 2>/dev/null)
[[ -z "$PYTHON" ]] && exit 0

input=$(cat)

changed=$(echo "$input" | "$PYTHON" -c "
import sys, json
try:
    d = json.load(sys.stdin)
    name = d.get('tool_name', '')
    path = str(d.get('tool_input', {}).get('file_path', '')).replace('\\\\', '/')
    print('yes' if name in ('Write', 'Edit') and path.endswith('.claude/CLAUDE.md') else 'no')
except:
    print('no')
" 2>/dev/null)

if [ "$changed" = "yes" ]; then
    cp "$PROJECT_CLAUDE" "$GLOBAL_CLAUDE"
fi
