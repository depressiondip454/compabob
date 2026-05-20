#!/usr/bin/env python3
"""PreToolUse(Bash) hook: block obviously destructive shell commands.

Reads the tool call as JSON on stdin. Exit 0 allows the command; exit 2 blocks it
and shows the reason to the model. Fails open (exit 0) on any parse error so a
malformed input never breaks the session.
"""
import json
import re
import sys

# Patterns that are almost never intentional and are hard or impossible to undo.
DANGEROUS = [
    (r"\brm\s+(-[a-z]*r[a-z]*f|-[a-z]*f[a-z]*r)\s+(/|~|\$HOME|\*)(\s|$)", "recursive force-delete of a root, home, or wildcard path"),
    (r":\(\)\s*\{.*\}\s*;\s*:", "fork bomb"),
    (r"\bmkfs\.", "filesystem format"),
    (r"\bdd\s+.*\bof=/dev/", "raw write to a block device"),
    (r">\s*/dev/sd[a-z]", "raw write to a disk device"),
    (r"\bchmod\s+-R\s+0*777\s+/", "world-writable permissions on a root path"),
    (r"\bchown\s+-R\s+.*\s+/(\s|$)", "recursive ownership change on root"),
    (r"\bgit\s+push\s+.*--force\b.*\b(main|master)\b", "force-push to the main branch"),
    (r"\b(curl|wget)\b.*\|\s*(sudo\s+)?(bash|sh|zsh)\b", "piping a downloaded script straight into a shell"),
]


def main() -> int:
    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0  # fail open

    if data.get("tool_name") != "Bash":
        return 0
    command = (data.get("tool_input") or {}).get("command", "")
    if not isinstance(command, str):
        return 0

    for pattern, why in DANGEROUS:
        if re.search(pattern, command, re.IGNORECASE):
            sys.stderr.write(
                f"Blocked: this command looks like {why}. "
                "If it is genuinely intended, run it yourself in a terminal. "
                "The assistant does not execute destructive commands.\n"
            )
            return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
