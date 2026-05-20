---
title: Home
tags: [moc]
---

# Home

The front door to {{USER_NAME}}'s knowledge base. This vault is where {{ASSISTANT_NAME}} stores and retrieves what it knows: meeting notes, people, projects, decisions.

> [!note] The notes in this vault right now are fictional examples
> Every note tagged `#example` is sample content showing the structure. Delete them
> once you have seen how things fit together, and replace them with your own.

## Structure

| Folder | What goes here |
|--------|----------------|
| `People/` | One note per person you work with. Title Case filename. Relationship history. |
| `Meetings/` | Meeting notes, filename `YYYY-MM-DD-<slug>.md`. |
| `Projects/` | One note per project or initiative. |
| `Daily/` | Daily notes, filename `YYYY-MM-DD.md`. Priorities, what happened. |
| `Decisions/` | Decision records, written by the `/log-decision` skill. |
| `Sources/` | Imported and reference material. |

## How it is used

- `second-brain` owns this vault: it creates notes, retrieves context, and keeps links healthy.
- `comms-meetings` reads `People/` and `Meetings/` to prepare you for what is coming.
- `/meeting-prep` and `/post-call` open and close the loop around every meeting.
- Wikilinks (`[[Note Name]]`) connect everything. The graph view shows the shape of it.

## Conventions

- Every note gets frontmatter: at least `title`, `date`, `tags`.
- People are Title Case in `People/`. Topics are linked with `[[wikilinks]]`.
- Notes are written in {{PRIMARY_LANGUAGE}}, whatever the source language of the input.
