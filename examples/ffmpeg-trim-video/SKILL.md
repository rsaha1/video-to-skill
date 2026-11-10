---
name: "ffmpeg-trim-video"
description: "Trim, cut, or extract a segment of a video file with ffmpeg: first N seconds, from a start point, between two timestamps, or the last N seconds."
---

# Trim video with ffmpeg

Learned from a tutorial video and verified by execution on a 10-second test clip with audio. Two behaviours differed from what the narration described; see Pitfalls. The `-ss`/`-to` commands were reconstructed from narration, so the on-screen originals may differ.

Always work on a copy and write to a new file name. Never overwrite the source.

## Pick the command

| Goal | Command | Notes |
|---|---|---|
| Keep from START to the end | `ffmpeg -ss START -i in.mp4 out.mp4` | Default choice. Fast; video and audio stay in sync. |
| Keep DURATION seconds from START | `ffmpeg -ss START -i in.mp4 -t DURATION out.mp4` | Preferred way to cut a segment. |
| Keep START to END (absolute times) | `ffmpeg -i in.mp4 -ss START -to END out.mp4` | `-ss` goes **after** `-i` here. Slower on long files. |
| Keep the last N seconds | `ffmpeg -sseof -N -i in.mp4 out.mp4` | Negative value. `-sseof -00:00:02` form also works. |
| Frame-exact cut inside a filter chain | `ffmpeg -i in.mp4 -vf "trim=start=S:end=E,setpts=PTS-STARTPTS" -af "atrim=start=S:end=E,asetpts=PTS-STARTPTS" out.mp4` | Only when other filters are already in use. |

Times accept seconds (`3`, `3.5`) or `HH:MM:SS`.

To cut without re-encoding (near-instant, no quality loss), add `-c copy` to the seeking commands. The cut then snaps to the nearest keyframe, so the start can be off by up to a few seconds. Use it when speed matters more than frame accuracy. `-c copy` cannot be combined with `-vf` or `-af`.

## Pitfalls found in verification

1. **The trim filter alone does not trim audio.** `-vf trim=...` cut the video to 3 seconds while the audio and the file stayed at the full 10 seconds. Add the matching `atrim` and `asetpts` on the audio, or use the seeking commands instead.
2. **`-to` after input seeking is not an end timestamp.** `ffmpeg -ss 3 -i in.mp4 -to 6 out.mp4` produced a 6-second clip (3s to 9s), not 3s to 6s, because `-ss` before `-i` resets the clock to zero. Use `-t DURATION` with input seeking, or put `-ss` after `-i` when using `-to`.
3. **`setpts=PTS-STARTPTS` is required** whenever `trim=start=` is used, or the output begins with a frozen or black lead-in.

## Acceptance check (run every time)

```bash
ffprobe -v error -show_entries stream=codec_type,duration -of csv=p=0 out.mp4
```

- Video duration and audio duration both match the intended length within about 0.05 seconds (re-encoded cuts) or about 0.5 seconds (`-c copy` cuts, which snap to keyframes).
- If they differ from each other, pitfall 1 or 2 applies; fix and rerun.
- For a `-c copy` cut, also report the actual start offset to the user, since it snapped to a keyframe.

## Provenance

- Source: "How to Trim Videos using FFmpeg", Bannerbear, https://www.youtube.com/watch?v=jCJxgMjJ0xw (learned 2026-11-10).
- Evidence: trim-filter commands read from an on-screen frame; `-ss`, `-t`, `-to`, and `-sseof` commands reconstructed from narration, then executed.
- Dropped: the video's closing segment promoting a paid merging API.
- Not covered by the video and not verified here: joining clips, batch trimming, subtitles.