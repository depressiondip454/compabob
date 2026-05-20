# Module: Team Mode (deferred)

**Status: deferred to a future release.**

## What it would add

Multi-user mode: turn the single-user assistant into a setup a whole team or company can share, with three tiers of configuration:

- **Shared** — agents, skills, and knowledge common to everyone.
- **Department** — scoped to a group, owned by that group's lead.
- **Personal** — each member's own agents and memory, private to them.

Plus the governance that a shared setup needs: who can change what, how personal knowledge gets promoted to shared, and how each member's data stays isolated from the others.

## Why it is deferred

Team mode is a substantial addition. It needs a permission model, per-user isolation, and a governance process, and each of those deserves real hardening rather than a quick port. The priority for this release is to get the single-user experience genuinely right. A multi-user layer built on a weak single-user core would inherit every rough edge and multiply it.

Shipping the solo kit well first, then adding team mode as its own considered release, is the deliberate sequence.

## In the meantime

The single-user kit is complete and useful on its own. If a team wants to adopt it now, the simplest path is for each person to run their own copy. A shared knowledge base can be a separate, jointly-owned vault that individual setups point at.
