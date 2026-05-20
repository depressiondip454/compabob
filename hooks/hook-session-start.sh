#!/usr/bin/env bash
# SessionStart hook: orient the assistant at the start of a session (and after a
# compaction). Injects the memory index and any handover note from a prior session.
# stdout from a SessionStart hook is added to the session context.

set -u
PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "$0")/.." && pwd)}"

MEM="$PROJECT_DIR/memory/MEMORY.md"
if [ -f "$MEM" ]; then
  echo "## Memory index (memory/MEMORY.md)"
  echo
  cat "$MEM"
  echo
  echo "Follow the links above into memory/topics/ only as needed."
fi

HANDOVER="$PROJECT_DIR/.tmp/handover.md"
if [ -f "$HANDOVER" ]; then
  echo
  echo "## Handover from the previous session (.tmp/handover.md)"
  echo
  cat "$HANDOVER"
fi

exit 0
