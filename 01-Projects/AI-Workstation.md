# AI Workstation — Multi-Bot Setup

**Overview:** Dual-AI-bot workstation with Telegram control, Discord task delegation, and Fiverr freelancing business.

## Machines

| Name | Hostname | OS | Bot | Role |
|---|---|---|---|---|
| Alf (Machine1) | — | WSL2 on Windows 10 | Seven (primary), Claude1 | Orchestration, research |
| Machine2 | DESKTOP-4PE1UFQ | WSL2 | Workstation2 (#6135) | Coding, rendering |

## Communication Flow

```
User (Tobra)
  ├── Telegram DM → Seven (primary agent)
  ├── Discord DM → Seven
  ├── Discord #tasks → Claude1 OR Workstation2
  └── Discord DM → Claude1

Seven (alf)
  ├── read/write → ~/obsidian-vault/ (this vault)
  ├── write → ~/.hermes/cache/fiverr_portfolio/
  ├── delegate → Discord #tasks
  └── cron jobs → scheduled autonomous work

Claude1 (alf)
  ├── receives → Discord #tasks
  └── responds → Discord #tasks

Workstation2 (machine2)
  ├── receives → Discord #tasks
  └── responds → Discord #tasks
```

## Key Paths

| Resource | Path |
|---|---|
| Shared vault | `/home/arbot/obsidian-vault/` |
| Fiverr assets | `/home/arbot/.hermes/cache/fiverr_portfolio/` |
| Hermes config | `/home/arbot/.hermes/config.yaml` |
| Obsidian binary | `/home/arbot/.local/bin/obsidian` |
| Claude1 bridge | `/home/arbot/.hermes-profiles/claude1/` |

## Decisions Log

| Date | Decision | Rationale |
|---|---|---|
| 2026-05-29 | Claude1 uses standalone bridge | Hermes Discord adapter hangs for non-primary profiles |
| 2026-05-29 | Base64 encode Discord token | Redaction workaround in .env |
| 2026-05-30 | OpenAI image gen via direct API | FAL_KEY expired; image_generate tool broken |
| 2026-05-30 | Shared Obsidian vault | Common knowledge base for all bots |

## Related Notes
- [[Seven Discord Bot]]
- [[Good Vibe Room]]
- [[Fiverr]]
