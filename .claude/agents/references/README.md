# Agent references

This directory is for long-tail reference files that support an agent without
bloating the agent file itself.

The core agents in this template are written to be self-contained, so this
directory ships empty. Use it when one of your agents grows long: move the
detail (a large mental-models library, a domain glossary, query recipes, field
mappings) into a file here, and have the agent point at it with a line like:

> For the full model library, read `.claude/agents/references/strategy-models.md`.

Keeping the agent file short keeps routing sharp and makes the agent easy to
read. Keeping the detail in a reference keeps it available when actually needed.
