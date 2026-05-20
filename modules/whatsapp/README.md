# Module: WhatsApp (roadmap — documented, intentionally not built)

**Status: roadmap.** There is no code in this module on purpose. This file
explains why, and what would change that.

## Why it is not built

WhatsApp has no general-purpose official API for an individual's personal
account. The two real options both have problems for a kit like this:

- **WhatsApp Business Platform (Cloud API)** — official, but built for
  businesses. It needs a Meta Business account, a registered business phone
  number, and template-message approval for anything proactive. That is heavy
  overhead for a personal assistant.
- **Unofficial bridges** — libraries that reverse-engineer the WhatsApp Web
  session. They work, but they violate WhatsApp's terms of service and **put
  your account at risk of being banned.** This kit will not ship code that can
  get your primary messaging account suspended.

## What would make it viable

If you already have a **WhatsApp Business Cloud API** number, a connector is
straightforward: a bot token in `.env`, polling or a webhook, and the same
draft-first safety contract the rest of the kit uses. It would slot in almost
exactly like the Telegram module. If that describes you, use
[`modules/telegram/`](../telegram/) as the reference implementation and adapt it.

## Recommended path today

Use the **Telegram module** ([`modules/telegram/`](../telegram/)). Telegram has a
clean, official Bot API, no account-ban risk, and the kit ships it as a working,
draft-first integration. For most people that covers the "chat with my assistant"
use case completely.
