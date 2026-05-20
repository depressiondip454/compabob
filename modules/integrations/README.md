# Module: Integrations

**Status: available.**

This module connects the assistant to external tools through [MCP](https://modelcontextprotocol.io)
servers. It ships an installer that writes the right entries into `.mcp.json` for
you, so you do not have to learn the config format by hand.

## Run it

```bash
bash scripts/install-integrations.sh
```

It asks which categories you want, then configures them. `setup.sh` also offers
to run it at the end of first-time setup. Re-run it any time to add more; it
never removes or overwrites a server you already have.

## The four categories

| Category | Servers | Key needed? |
|----------|---------|-------------|
| `web` | Playwright (browser automation), scrapling-fetch (stealth web fetch) | No |
| `utility` | time (timezone and date math), fetch (basic web fetch) | No |
| `search` | exa (semantic web search) | Yes — an API key |
| `google` | Gmail, Google Calendar | Yes — OAuth |

**Keyless** categories (`web`, `utility`) are configured completely by the
installer: it writes the `.mcp.json` entry and you are done. **Keyed** categories
(`search`, `google`) are configured as far as the installer can, then it points
you here to finish the credential step.

Nothing is downloaded during install. An MCP server fetches itself, at the
version pinned in `scripts/integrations-catalog.json`, the first time Claude Code
uses it. The first use of a server is therefore a little slower; after that it is
cached.

### Prerequisites

The keyless servers run via `npx` (needs [Node.js](https://nodejs.org)) and
`uvx` (needs [uv](https://docs.astral.sh/uv/)). The installer checks for both
and warns if one is missing; it still writes the `.mcp.json` entry, so once you
install the runtime the server just works.

## Web search (exa)

`exa` gives the assistant semantic web search.

1. Create an API key at [exa.ai](https://exa.ai). There is a free tier.
2. Make the key available as `EXA_API_KEY`. Two options:
   - Export it in your shell profile: `export EXA_API_KEY=your-key-here`. The
     `.mcp.json` entry reads `${EXA_API_KEY}` from the environment.
   - Or open `.mcp.json` and replace `${EXA_API_KEY}` with the key directly.
     `.mcp.json` is git-ignored, so the key is not committed.
3. `.env.example` documents the variable; copy it to `.env` if you like to keep
   all secrets in one place.

## Google Workspace

Gmail and Calendar are the most involved integration, because Google requires
an OAuth client. Budget 15-20 minutes the first time.

1. In the [Google Cloud Console](https://console.cloud.google.com), create a
   project, enable the Gmail API and the Google Calendar API, and create an
   **OAuth 2.0 Client ID** (application type: Desktop app).
2. Pick a Google Workspace MCP server. The MCP ecosystem moves quickly, so
   rather than pin one here, search the [MCP server directory](https://modelcontextprotocol.io)
   for a current, well-maintained Gmail / Google Workspace server and follow its
   own setup instructions.
3. That server will ask for your OAuth client credentials and run a one-time
   browser consent flow. Put any secrets in `.env` (git-ignored), never in a
   committed file.
4. Add the server to `.mcp.json` under `mcpServers`, following the format the
   other entries use.

Because this one is provider-specific and changes often, it is deliberately a
guided manual step rather than an automated install.

## Verify

Inside a Claude Code session in the kit directory:

```text
claude mcp list
```

It lists the servers Claude Code loaded from `.mcp.json`. A keyless server
should appear; a keyed one appears once its credential is in place.

## How agents use integrations

The core agents check for a relevant integration and use it when present:
`comms-meetings` will use Gmail and Calendar, `analyst` and `second-brain` will
use web search and fetch. Without an integration they work from local files and
say which live source is missing. Enabling one is purely additive.

## Disable

Remove the server's entry from `.mcp.json`. If you turned off every integration,
set `integrations: false` in `config/user.config.yaml`.
