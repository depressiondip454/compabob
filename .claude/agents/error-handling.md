# Error Handling (shared across agents)

Every agent follows these patterns when something fails. Reference this file from each agent's instructions.

## Read-Before-Speak gate (stakes-sensitive agents)

For any agent whose wrong output drives a wrong real-world action (a financial figure, a legal claim, a commitment in a draft), apply a hard structural gate at the top of the agent file:

1. Read the named source files BEFORE producing output that cites a number, fact, or recommendation.
2. Declare what was loaded at the top of the response: `Context loaded: [list]`.
3. If a required read fails, STOP and report the missing source. Do not substitute general knowledge or stale memory.

This is stronger than a self-check at the bottom of a file, which the model may skim past.

## Error classification

| Type | Examples | Action |
|-------|----------|--------|
| Transient | Timeout, rate limit, 429/503/504 | Retry once after 5s. If it fails again, tell the user and suggest retrying later. |
| Auth | 401, expired token, permission denied | Do NOT retry. Tell the user which service needs re-authentication. |
| Data | Empty result, unexpected schema, null fields | Check the query syntax. If the query is valid, report "no data found" with the query used. |
| Semantic | Query returns wrong-looking numbers, request misinterpreted | Self-check before presenting. Flag: "These numbers look unusual, please verify." |
| Not found | Record or file does not exist | Confirm the name or ID with the user before retrying with a different search. |

**Never retry**: auth errors, permission errors, not-found errors, validation errors.
**Always retry once**: timeouts, rate limits, service-unavailable, connection reset.

## Fallback chains

When a primary source is unavailable, fall back and say so:

- An external connector fails → work from local files; note "[connector] unavailable, working from cached data".
- A search index fails → fall back to plain `Grep`; note that results are keyword-only.
- A notification channel fails → log the action locally so it is not lost.

Always tell the user when a fallback is in use, and what it costs (stale data, keyword-only, etc.).

## Multi-step task recovery

For workflows with sequential steps:

1. Before starting, list the steps and note which one you are on.
2. On failure at step N, report which steps completed (1 to N-1) and what failed at N.
3. Provide resume context: "Steps 1-3 done. Step 4 failed because X. To resume, retry step 4 with Y."
4. Never re-run completed steps unless asked (avoids duplicate writes or sends).
5. For destructive steps (file overwrite, send), confirm a rollback is not needed before retrying.

## Uncertainty expression

- High confidence: "Based on X records over [range]."
- Medium: "Note: X% of records had missing [field], which may affect this."
- Low: "This is an estimate based on [assumptions]. Verify before acting on it."
- Unknown: "I could not find data for X. Should I try [alternative]?"

Never present uncertain data as certain. "I am not sure" beats a wrong number that gets used in a decision.

## Deliverable QA checklist

Before sharing any report or analysis beyond the current conversation:

- Cross-check key numbers against a second source.
- Verify totals add up and date ranges match the request.
- Flag obvious outliers (10x or 0.1x expected).
- Note data gaps explicitly; never present partial results as complete.
- Confirm the output actually answers the original request.

## Anti-nesting rules (all subagents)

Subagents run inside a task call from the main session. They must never create nested processes:

| Anti-pattern | Why it breaks | Instead |
|--------------|---------------|---------|
| Running the CLI inside a subagent via Bash | Nested CLI process, crashes or competes | Use your own tools directly |
| Using the agent-spawning tool from a subagent | Three-layer nesting | Do the work yourself |
| Invoking a skill from a subagent | Skills spawn tasks internally | Apply the knowledge inline |

The main session spawns subagents. Subagents never spawn anything.
