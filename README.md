# Compabob

A customizable [Claude Code](https://docs.anthropic.com/en/docs/claude-code) setup for knowledge workers. Clone it, run `./setup.sh`, name your assistant, and you have a working AI work partner in about ten minutes: a constitution that defines how it behaves, a fleet of specialized agents, safety guards, slash-command workflows, and an Obsidian knowledge base.

This is **scaffolding, not a finished assistant.** The value compounds as you personalize it. What you get on day one is a well-structured starting point that already does more than a blank Claude Code session, and a clear path to make it yours.

## What this is (and is not)

- **Is**: an opinionated, single-user template. Architecture, conventions, and a set of agents/hooks/skills that took real iteration to get right, packaged so you do not start from zero.
- **Is not**: a product, a SaaS, or a no-config magic box. There is no signup, no telemetry, no upsell. It runs entirely on your machine under your own Claude Code subscription.

## Maintenance posture

**Actively maintained.** This kit is updated over time as its maintainers learn what works and as Claude Code evolves, so expect it to keep improving. You still own your copy outright: fork it, change anything, diverge as far as you like. Issues and PRs are welcome; reviews are best-effort, since the kit is maintained alongside other work.

## Quickstart

### Prerequisites

- macOS or Linux. On Windows, use [WSL](https://learn.microsoft.com/windows/wsl/install): the kit is bash- and `python3`-based and WSL runs it natively. Native Windows (PowerShell/cmd) is not supported.
- [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code): `npm install -g @anthropic-ai/claude-code`
- `git`, `bash`, `python3` (3.10+)
- Optional: [Obsidian](https://obsidian.md) to browse the knowledge base as a graph

### Setup

```bash
git clone <this-repo-url> compabob
cd compabob
./setup.sh
```

`setup.sh` asks a few questions (what to name your assistant, your name, role, language, and which persona fits your work), creates your personal `vault/`, `memory/`, and `config/` from the shipped seeds, and offers to set up integrations. Then:

```bash
claude
```

Your assistant introduces itself by the name you chose and is ready to work.

### Updating

```bash
./update.sh
```

Pulls the latest version of the kit. Your `vault/`, `memory/`, and `config/` are git-ignored and are never touched by an update, so you can personalize the kit freely and still stay current. See the [customization guide](docs/customization-guide.md) for how that works.

### First hour

Do not configure everything at once. Get one loop working end to end:

1. Ask your assistant to take notes from a real meeting or document into `vault/`.
2. Ask it to find and summarize what it stored.
3. Ask it to draft something using that context.

That second-brain loop is the core value. Once it feels useful, expand from there using the [customization guide](docs/customization-guide.md).

## What is inside

```
CONSTITUTION.md      The rules every session loads. How your assistant behaves.
.claude/agents/      Specialized agents (analyst, comms, CRM, strategy, ...).
.claude/skills/      Slash-command workflows (/morning-brief, /meeting-prep, ...).
.claude/output-styles/  The answer-first response style.
hooks/               Safety guards and lifecycle automation.
memory/              The assistant's memory (yours, created by setup, git-ignored).
vault/               Your Obsidian knowledge base (yours, created by setup, git-ignored).
config/              Your settings (yours, git-ignored).
modules/             Opt-in extensions (see below).
docs/                Architecture, onboarding, and customization guides.
*.example/           Seeds that setup copies into vault/ and memory/.
```

### Core agents

| Agent | What it does |
|-------|--------------|
| `daily-copilot` | Your everyday partner: prioritization, sparring, the daily brief |
| `second-brain` | Knowledge base operations: notes, meeting records, research synthesis |
| `analyst` | Metrics, KPIs, dashboards, data-backed reporting |
| `crm-relationships` | Contact, pipeline, and relationship tracking (works with or without a CRM) |
| `comms-meetings` | Email triage, meeting prep, briefings, follow-up tracking |
| `strategy-advisor` | Assumption testing, pre-mortems, second-order effects (advice only) |
| `principal-engineer` | Architecture and code review for technical work |
| `first-principles` | Rigorous reasoning under uncertainty |

Requests route automatically. You do not pick an agent.

### Skills

Skills are slash-command workflows. Type the command; the assistant runs the procedure.

| Skill | What it does |
|-------|--------------|
| `/morning-brief` | Start-of-day briefing: priorities, what is due, what is owed |
| `/meeting-prep` | Assemble attendees, history, and open items before a meeting |
| `/post-call` | Capture decisions and commitments right after a call |
| `/handover` | Write a handover note so the next session has full context |
| `/log-decision` | Record a decision, its reasoning, and a date to review it |
| `/tasks` | One aggregated view of open tasks from across the vault |
| `/reflect` | End-of-session reflection; proposes memory updates |
| `/index-memory` | Build the memory-search index for relevance-ranked retrieval |
| `/add-agent` | Scaffold a new specialized agent interactively |
| `/system-audit` | Health-check the assistant's own setup |
| `/visual-explainer` | Turn a system, plan, or dataset into a self-contained HTML page |

## Modules (opt-in)

The core runs with zero external services. Modules add capability when you want it:

| Module | Status | What it adds |
|--------|--------|--------------|
| `proactive` | Available | Scheduled automation: a morning brief and weekly review on a timer |
| `telegram` | Available | A Telegram bot: inbound messages drafted for your approval, never auto-sent |
| `integrations` | Available | MCP tools: browser automation, web search, Gmail, Calendar, utilities |
| `memory-search` | Roadmap | Semantic search over your memory and vault (needs a local embedding model) |
| `extra-agents` | Roadmap | An agent gallery: designer, evaluator, sales coach, project manager |
| `whatsapp` | Roadmap | WhatsApp channel — not built (account-ban risk); use Telegram instead |

See [modules/README.md](modules/README.md) to enable one.

## Lineage

This kit is distilled from a personal Claude Code setup the author refined over a year of daily use: the constitution, the agent fleet, the safety hooks, the memory system. The personal-life domains were stripped out and the patterns generalized into a clean starting point, and the result is what you are reading. Credit to the [Claude Code](https://docs.anthropic.com/en/docs/claude-code) team for the harness this builds on.

## Author

Built by [Philipp Wenger Lebron](https://www.linkedin.com/in/philippwenger/). Issues and pull requests are welcome.

## License

MIT. See [LICENSE](LICENSE). Use it, change it, ship it.
