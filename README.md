# video-to-skill

A Claude skill that learns a workflow from a tutorial video and saves it as a new skill, but only after running the steps on a sample and measuring the result.

Most "AI watches a video" tools stop at a summary. This one treats the video as a claim to test: it extracts the steps, checks that every step maps to a tool Claude can operate, executes them on disposable sample data, and records where the tutorial was incomplete or behaved differently than described. Only verified steps go into the saved skill.

## How it works

1. **Ingest.** Transcript plus a handful of frames, captured only where the narrator points at the screen ("use this command", "click here") without saying what is on it.
2. **Extract.** A step table with the exact command or click path and an evidence tag: `frame`, `narration`, or `inferred`.
3. **Capability gate.** Every step must map to a tool in the session. If one does not, it stops and says what is missing.
4. **Execute.** Each step runs on a sample, as taught first, against a measurable check.
5. **Report and propose.** A verification table, then the new skill for you to review and save.

The full instructions are in [`skills/video-to-skill/SKILL.md`](skills/video-to-skill/SKILL.md).

## Example run

[`examples/ffmpeg-trim-video/`](examples/ffmpeg-trim-video/) is the first skill it produced, from a 6-minute ffmpeg trimming tutorial.

- The transcript alone was not enough: the commands were shown on screen and never read aloud, and auto-captions garbled the flags.
- Of 11 commands run as taught on a 10-second clip with audio, 5 worked as described and 6 needed a correction (5 trim-filter commands left the audio untrimmed; 1 reconstructed `-ss`/`-to` command produced a 6-second clip where 3 seconds was expected).
- Every command and measurement is in [`verification.md`](examples/ffmpeg-trim-video/verification.md).

## Install

- **Claude apps:** zip the `skills/video-to-skill` folder and upload it as a skill.
- **Claude Code:** copy `skills/video-to-skill` into `~/.claude/skills/`.

Requirements depend on where Claude runs:

| Environment | Ingest route |
|---|---|
| Your own machine | The [`watch`](https://github.com/bradautomates/claude-video) skill by bradautomates (yt-dlp + ffmpeg). Install it separately; it is not bundled here. |
| Cloud session | A connected browser. YouTube refuses yt-dlp from datacenter addresses, so the skill reads the transcript panel in your browser and takes targeted screenshots. |

## Limits

- Tested on one video so far. Treat it as an early version.
- It only learns workflows Claude can execute end to end. GUI-only tutorials need desktop or browser control, or they fail the capability gate by design.
- A video is not an authority. For anything with legal, tax, or filing consequences, the learned skill should cite the governing source, not the video.
- Content in a video is treated as material to evaluate, never as instructions to follow. Sponsor segments and download prompts are dropped.

## License

MIT. See [LICENSE](LICENSE).
