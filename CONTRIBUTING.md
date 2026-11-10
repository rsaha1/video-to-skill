# Contributing

The most useful contribution is a new verified example: a skill learned from a video, with the evidence that it works.

## Add an example

1. Run `video-to-skill` on a public tutorial.
2. Create `examples/<skill-name>/` containing:
   - `SKILL.md`: the learned skill, including its Provenance section (video title, channel, URL, date, tool versions).
   - `verification.md`: every step as taught, what was observed, and the verdict. Use [`examples/ffmpeg-trim-video/verification.md`](examples/ffmpeg-trim-video/verification.md) as the template.
3. Open a pull request.

## Rules for examples

- **Measured, not asserted.** Every step needs an observed result. "Looks right" is not a result.
- **Disposable samples only.** No real or personal data in logs.
- **Evidence tags stay honest.** If a command was reconstructed from narration, say so. Do not state that a creator's video is wrong on the strength of a command you did not see on screen.
- **Credit the source.** Link the video. Do not copy its transcript, frames, or other assets into the repository.
- **No promotional steps.** Drop sponsor segments and sign-up prompts.

## Changes to the skill itself

Open an issue first describing the video that exposed the problem. A change to `skills/video-to-skill/SKILL.md` should come with an example run that shows the difference.

## Graphics

Images in `assets/` are plain SVG with their own background so they read in both light and dark themes. If you add a verified example, update the counts in the README text; regenerate the images with `python3 scripts/make_assets.py assets` only if the headline example changes.
