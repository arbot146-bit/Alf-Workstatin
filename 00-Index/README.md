---
name: obsidian
description: Obsidian vault on Alf (Machine1). Shared knowledge base for Seven, Claude1, Workstation2, and Tobra. All bots can read/write via Hermes file tools. Synced via Git.
---

# Obsidian Vault — Shared Bot Knowledge Base

**Vault path:** `/home/arbot/obsidian-vault/`
**For Hermes file tools:** Always resolve to full absolute path, do NOT use `$OBSIDIAN_VAULT_PATH`

## Vault Structure

```
obsidian-vault/
├── .obsidian/                    # Obsidian config (don't edit manually)
├── attachments/                  # Shared images, diagrams, exports
├── 00-Index/                     # Maps and index notes
│   └── README.md                 # Vault overview (this note)
├── 01-Projects/                  # Active project notes
│   ├── Fiverr/                  # Fiverr freelancing business
│   ├── YouTube-Good-Vibe-Room/   # Live stream management
│   ├── Discord-Setup/            # Bot architecture and server config
│   └── Ideas/                   # Brainstorming and new project ideas
├── 02-Meetings/                  # Meeting notes and decisions
├── 03-Daily/                     # Daily notes (YYYY-MM-DD.md)
├── 04-Reference/                 # Reference docs, API cheatsheets, guides
└── 05-Archive/                   # Completed/old notes
```

## Bot Access

All bots (Seven, Claude1, Workstation2) access this vault via Hermes `read_file`/`write_file`/`patch` tools targeting `/home/arbot/obsidian-vault/`.

## Wikilink Conventions

- Link projects: `[[Fiverr]]`, `[[Good Vibe Room]]`
- Link decisions: `[[2026-05-30-algorithm-change]]`
- Link people: `[[Tobra]]`, `[[Seven]]`, `[[Claude1]]`
