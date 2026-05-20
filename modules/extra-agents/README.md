# Module: Extra Agents (roadmap)

**Status: planned, not yet built.**

## What it will add

A gallery of additional agents to copy into `.claude/agents/` when your work calls for them:

- **designer** — visual assets, decks, diagrams, simple graphics.
- **evaluator** — adversarial review: checks a draft, a report, or a plan before you act on it.
- **sales-coach** — deal strategy, objection handling, competitive framing.
- **project-manager** — planning, status tracking, dependency and risk surfacing.

## How it will work

Each agent will be a single `.md` file you copy into `.claude/agents/`, then register in `CONSTITUTION.md` and `_orchestrator-reference.md`. The `/add-agent` skill already does that registration for you.

## Why it is not in this release

The eight core agents cover the common shape of knowledge work. More agents are valuable but role-specific, and adding all of them by default would clutter routing for people who do not need them. A gallery you pull from on purpose is the right model.

## Build your own meanwhile

You do not need this module to add an agent. Run `/add-agent`, or copy `.claude/agents/_agent-template.md`. That is the intended way to make the kit yours. This gallery just saves you writing the common ones from scratch.
