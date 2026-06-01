# The Good Vibe Room — YouTube Live Stream

**Channel:** UCpK7nG6nnlphTpN2YJFcv9g
**URL:** https://www.youtube.com/@TheGoodVibeRoom
**Status:** Active 24/7 stream
**Operated from:** Machine2 (DESKTOP-4PE1UFQ)
**Last checked:** 2026-05-30

## Current Stream Details

- **Active Video ID:** 00xW1vRjZ70
- **Studio URL:** https://studio.youtube.com/video/00xW1vRjZ70/livestreaming
- **Visibility:** Public (was Private on last creation — fixed)

## Stream Architecture

```
garden_loop.mp4 (video) + playlist_combined.aac (audio)
        ↓ ffmpeg loop
    RTMP → YouTube Live
```

## Asset Locations

| Asset | Path |
|---|---|
| Video loop | `C:\Users\Admin\Desktop\Good Vibe Room\garden_loop.mp4` |
| Audio playlist | `C:\Users\Admin\Desktop\Good Vibe Room\playlist_combined.aac` |
| Stream folder | `C:\Users\Admin\Desktop\Good Vibe Room\` |

## Known Issues & Fixes

### Issue 1: Stream shows "Processing Soon"
**Cause:** Firefox session signs out of YouTube Studio
**Fix:** Re-login to YouTube Studio in WSLg Firefox

### Issue 2: New stream defaults to Private
**Cause:** YouTube defaults new streams to Private visibility
**Fix:** Go to Studio → Visibility → set to Public before going live

## Maintenance Log

| Date | Action | Notes |
|---|---|---|
| 2026-05-29 | Stream created | Active ID: 00xW1vRjZ70 |
| 2026-05-30 | Verified | Stream running |
