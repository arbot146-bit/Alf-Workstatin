# Machine Specifications

## Alf (Machine1)

| Spec | Detail |
|---|---|
| **OS** | WSL2 on Windows 10 (build 26200) |
| **Username** | arbot |
| **CPU** | 16 cores |
| **RAM** | 7.6 GB |
| **SSH** | Port 2222, key-only |
| **Hermes** | v0.15.1 (upgraded from v0.14.0 on May 29 2026) |
| **Model** | OpenRouter/owl-alpha |
| **Image gen** | OpenAI gpt-image-1 via direct API ($0.04/img) |
| **Bots** | Seven (primary), Claude1 (bridge) |

## Machine2 (DESKTOP-4PE1UFQ)

| Spec | Detail |
|---|---|
| **Hostname** | DESKTOP-4PE1UFQ |
| **Role** | Coding, rendering, browser tasks |
| **Bot** | Workstation2 (#6135 on Discord Seven) |
| **Display** | WSLg (for Firefox Studio auth) |

## Key Paths Reference

| Resource | Alf Path | Windows Equivalent |
|---|---|---|
| Hermes home | `/home/arbot/.hermes/` | `C:\Users\admin\.hermes\` |
| Obsidian vault | `/home/arbot/obsidian-vault/` | — |
| Obsidian binary | `/home/arbot/.local/bin/obsidian` | — |
| Fiverr portfolio | `/home/arbot/.hermes/cache/fiverr_portfolio/` | — |
| Claude1 bridge | `/home/arbot/.hermes-profiles/claude1/` | — |
| Stream assets | `C:\Users\Admin\Desktop\Good Vibe Room\` | `C:\Users\Admin\Desktop\Good Vibe Room\` |
