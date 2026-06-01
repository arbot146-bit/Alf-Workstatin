# Seven — Discord Bot Architecture

**Discord User ID:** 1507875594183118889 (Tobra)
**Server:** Seven (guild ID: 1502480069279350844)
**Primary bot channel:** #general
**Task delegation:** #tasks

## Bot Identities on Server "Seven"

| Bot | Discord Name | Role | Machine | Status |
|---|---|---|---|---|
| Seven | (primary) | Orchestration, images, strategy, file mgmt | Alf (Machine1) | ✅ Active |
| Workstation2 | #6135 | Coding, rendering, browser tasks | Machine2 | ✅ Active |
| Claude1 | #4339 | Research, marketing, finance | Alf (Machine1) | ✅ Active |

## Seven (Primary — This Agent)

- Hermes Agent on profile "default"
- Model: OpenRouter/owl-alpha
- Tools: file, terminal, web, image_gen, discord, telegram, delegate_task, cronjob, skills
- Home channel: Telegram (7935534204)
- Discord server: Seven

## Claude1 Bridge

- **Service:** `claude1-bridge.service` (systemd)
- **Location:** `~/.hermes-profiles/claude1/`
- **Type:** Standalone `discord.Client` bridge (NOT Hermes adapter)
- **Transport:** Forwards to `/home/arbot/.local/bin/hermes chat -q`
- **Log:** `/tmp/claude1-bridge.log`
- **Status:** `systemctl --user status claude1-bridge`

## Workstation2

- Separate Discord bot app
- Connected to same "Seven" server as #6135
- Handles coding and rendering tasks on Machine2

## Delegation Pattern

```
Tobra (Telegram/Discord)
    ↓
Seven (orchestrator)
    ├── Post task to Discord #tasks → Workstation2 picks up
    ├── Post task to Discord #tasks → Claude1 picks up
    ├── Generate images directly (OpenAI gpt-image-1)
    ├── Run cron jobs for scheduled work
    └── Manage files and knowledge base (this vault)
```

## Related Notes
- [[AI Workstation]]
- [[2026-05-29]] — Claude1 production deployment
