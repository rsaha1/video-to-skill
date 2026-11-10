# Verification log: ffmpeg-trim-video

Source video: "How to Trim Videos using FFmpeg", Bannerbear, https://www.youtube.com/watch?v=jCJxgMjJ0xw
Run date: 2026-11-10. ffmpeg 6.1.1. Sample: generated 10-second 640x360 clip with a sine-wave audio track.

Evidence column: `frame` = command read from an on-screen frame; `narration` = reconstructed from the spoken transcript, so the creator's exact on-screen command may differ.

| Command (output name omitted) | Evidence | Expected | Video | Audio | Verdict |
|---|---|---|---|---|---|
| `-i in.mp4 -vf trim=duration=3` | frame | 3s | 3.00s | 10.01s | Corrected: audio not trimmed |
| `-i in.mp4 -vf trim=duration=3 -c:a copy` | frame | 3s | 3.00s | 10.00s | Corrected: audio not trimmed |
| `-i in.mp4 -vf trim=end=3` | frame | 3s | 3.00s | 10.01s | Corrected: audio not trimmed |
| `-i in.mp4 -vf "trim=start=3,setpts=PTS-STARTPTS"` | frame | 7s | 7.00s | 10.01s | Corrected: audio not trimmed |
| `-i in.mp4 -vf "trim=start=3:end=6,setpts=PTS-STARTPTS"` | frame | 3s | 3.00s | 10.01s | Corrected: audio not trimmed |
| `-ss 3 -i in.mp4` | narration | 7s | 7.00s | 7.01s | Works |
| `-ss 3 -i in.mp4 -t 3` | narration | 3s | 3.00s | 3.00s | Works |
| `-ss 3 -i in.mp4 -to 6` | narration | 3s | 6.00s | 6.00s | Corrected: use `-t`, or put `-ss` after `-i` |
| `-i in.mp4 -ss 3 -to 6` | narration | 3s | 3.00s | 3.00s | Works |
| `-sseof -2 -i in.mp4` | narration | 2s | 2.00s | 2.01s | Works |
| `-sseof -00:00:02 -i in.mp4` | narration | 2s | 2.00s | 2.01s | Works |
| `-i in.mp4 -vf "trim=start=3:end=6,setpts=PTS-STARTPTS" -af "atrim=start=3:end=6,asetpts=PTS-STARTPTS"` | added | 3s | 3.00s | 3.00s | Works (the correction) |
| `-ss 3.5 -i in.mp4 -t 3 -c copy` | added | 3s | 3.17s | 3.00s | Works, keyframe-snapped |

Notes

- The audio finding only shows up on clips that have an audio track. The demo clip in the video may not have had one.
- First frame of the 3-second cuts matched the source frame at t=3s (PSNR 40 dB).
