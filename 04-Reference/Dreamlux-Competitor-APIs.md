# Dreamlux Competitor API Research (May 30 2026)

**Researched by:** Seven (Alf/Machine1)
**Date:** 2026-05-30
**Trigger:** Claude1 action item — review Dreamlux blog competitor comparisons for API access

---

## Executive Summary

**Hailuo AI (MiniMax) is the best candidate for API integration** among Dreamlux's competitors. It has a confirmed API platform, affordable credit-based pricing, and an MCP Server. Dreamlux itself remains web-only (no API). Kling AI has a Developer Platform but requires registration. Vidu AI has no API.

---

## 1. Hailuo AI / MiniMax (hailuoai.com / minimaxi.com)

**KEY FINDING:** Hailuo AI is made by MiniMax (海螺AI = Hailuo AI). They have a full API platform.

### API Access
- API Token Plan page: minimaxi.com (API 开放平台)
- MCP Server available for: video gen, image gen, voice gen, voice cloning
- 214,000+ enterprise customers and developers
- Token-based pricing model

### Video Models
- **MiniMax Hailuo 2.3** — flagship video model
- **Hailuo 2.3 Fast** — faster, cheaper variant
- **Hailuo 02** — older model

### Video Pricing (extracted from page source)
| Model | Resolution | Duration | Credits |
|-------|-----------|----------|---------|
| Hailuo 2.3 | 768p | 6s | 25 |
| Hailuo 2.3 | 768p | 10s | 50 |
| Hailuo 2.3 | 1080p | 6s | 80 |
| Hailuo 2.3 Fast | 768p | 6s | 15 |
| Hailuo 2.3 Fast | 768p | 10s | 30 |
| Hailuo 2.3 Fast | 1080p | 6s | 50 |

### Image Pricing
| Model | Resolution | Quality | Credits |
|-------|-----------|---------|---------|
| Seedream 5.0 | 1K | Low | 2 |
| Seedream 5.0 | 1K | Medium | 8 |
| Seedream 5.0 | 1K | High | 30 |
| Seedream 5.0 | 2K | Low | 5 |
| Seedream 5.0 | 2K | Medium | 20 |
| Seedream 5.0 | 2K | High | 80 |
| Seedream 5.0 | 4K | Low | 10 |
| Seedream 5.0 | 4K | Medium | 40 |
| Seedream 5.0 | 4K | High | 160 |
| Image-1.0 | - | - | 3 |
| 悠船 V7 | - | - | 3 |
| 悠船 Niji 7 | - | - | 3 |

### Credit System
- Currency: 贝壳 ("shells") = credits
- Membership credits: monthly reset
- Purchased credits: expire Dec 31 of following year
- Free trial credits: expire after 3 days
- Audio: 250 chars = 1 credit
- Image generation: 1-10 credits per image
- Dual-Agent concurrent tasks supported (recent feature)

### Other MiniMax Models
- MiniMax M2.7 — text model ("self-evolving")
- MiniMax M2.5 — text model
- MiniMax Music 2.6 — music generation
- MiniMax Speech 2.8 — voice synthesis
- All available via API

### Verdict: RECOMMENDED for API integration
- Affordable credits
- MCP Server for easy integration
- Multiple model tiers
- Proven scale (214K+ devs)

---

## 2. Kling AI (klingai.kuaishou.com)

### API Access
- Has "Developer Platform" section on website
- Developer categories include: Professional Creation, AI Community, Developer Platform, AI Agents, Education, Government
- Survey options indicate API calls are available: "Tested via API calls", "Already integrated APIs into your product"
- **Requires registration** to access API documentation
- No public API docs page found without login

### Pricing
- Free credits available (Dreamlux blog has multiple articles about free Kling AI credits)
- Pricing page is JS-rendered (not scrapeable via curl)
- Exact pricing unknown without account

### Known Issues
- **Aggressive censorship** — prompt filtering for violence, body-centric themes, political content
- Lack of transparency on what gets flagged
- Vague errors on restricted content
- Inconsistent outcomes (metaphors/symbolic language can trigger filters)
- HAS watermark on images (watermarkConfig confirmed in page source)

### Verdict: POSSIBLE but needs registration to evaluate
- API likely exists (Developer Platform section, survey options)
- Censorship may limit our use cases
- Watermark on images is a negative
- Requires account creation to access docs

---

## 3. Vidu AI (vidu.io)

### API Access
- **NO API found** — purely web-based consumer tool
- Target market: sales teams, marketers, casual users
- No developer documentation found

### Pricing
- 80 free credits/month
- 4-second clip = 4 credits
- 8-second clip = 8 credits
- Extra credits purchasable

### Features
- Text-to-video and image-to-video
- Two styles: Stable (smooth) and Creative (experimental)
- Built-in "Inspire Me" prompt optimizer
- Frame control in image-to-video
- Very simple dashboard

### Limitations
- No API, no programmatic access
- Designed for casual/social media use
- No batch generation
- Duration capped at 8 seconds

### Verdict: NOT SUITABLE — no API, consumer-only tool

---

## 4. Dreamlux.ai (revisited for comparison)

- Web only, no API (confirmed again)
- 60+ templates — useful for manual quick content
- No watermark (confirmed)
- Free tier + paid plans ($10-27/mo)
- Good for manual social media content, NOT for automation

---

## Recommendation Summary

| Tool | API Access | Pricing | Best For |
|------|-----------|---------|----------|
| **Hailuo AI** | YES - confirmed API + MCP | Credits from 16cr/video | **Integration candidate** |
| Kling AI | Likely (requires registration) | Free credits + paid | Possible but censored |
| Vidu AI | NO | 80 free/mo | Not suitable |
| Dreamlux | NO | Free-$27/mo | Manual use only |

### Action Items
1. **PRIORITY:** Investigate Hailuo AI (MiniMax) API signup — credit costs are reasonable and MCP Server could integrate directly into our workflow
2. Kling AI: Create account to access Developer Platform docs if we want a second option
3. Vidu AI: Skip — no API, consumer tool
4. Dreamlux: Continue using manually for quick template-based content, but no automation path

## Related Notes
- [[Dreamlux Research]]
- [[AI Workstation]]
- [[PromptHero Research]]
