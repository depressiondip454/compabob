#!/usr/bin/env bash
# UserPromptSubmit hook: inject the current date and time so the assistant is
# never guessing "today". stdout from a UserPromptSubmit hook is added to context.

echo "Current time: $(date '+%Y-%m-%d %H:%M %Z (%A)')"
exit 0
