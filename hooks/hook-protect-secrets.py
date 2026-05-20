#!/usr/bin/env python3
"""PreToolUse(Read) hook: block reading credential and secret files.

Keeps secrets out of the model's context. Reading a key file means it can end up
in a transcript, a summary, or a tool call. Exit 0 allows; exit 2 blocks. Fails open.
"""
import json
import re
import sys

# File paths that should never be read into context.
SECRET_PATTERNS = [
    r"(^|/)\.env$",
    r"(^|/)\.env\.(?!example$|template$|sample$)[\w.-]+$",
    r"(^|/)\.secrets/",
    r"(^|/)secrets\.env$",
    r"(^|/)id_(rsa|ed25519|ecdsa|dsa)$",
    r"\.pem$",
    r"(^|/)\.ssh/(?!known_hosts$|config$)",
    r"(^|/)\.aws/credentials$",
    r"(^|/)\.npmrc$",
    r"(^|/)\.pypirc$",
    r"(^|/)credentials\.json$",
    r"(^|/)service-account.*\.json$",
]
COMPILED = [re.compile(p, re.IGNORECASE) for p in SECRET_PATTERNS]


def main() -> int:
    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0

    if data.get("tool_name") != "Read":
        return 0
    path = (data.get("tool_input") or {}).get("file_path", "")
    if not isinstance(path, str) or not path:
        return 0

    for pattern in COMPILED:
        if pattern.search(path):
            sys.stderr.write(
                f"Blocked: {path} looks like a secret or credential file. "
                "Do not read it into context. If a value is needed, ask the user "
                "to provide just that value, or reference it from the environment.\n"
            )
            return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
