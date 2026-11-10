import sys, html
out = sys.argv[1]
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"
SURF, INK, INK2, MUTED, GRID, AXIS = "#fcfcfb", "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#c3c2b7"
BLUE, ORANGE = "#2a78d6", "#eb6834"
e = html.escape

# ---------- banner ----------
W, H = 1280, 320
b = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="video-to-skill: Claude watches a tutorial, runs it, and only saves what worked">',
     f'<rect width="{W}" height="{H}" rx="16" fill="#1a1a19"/>',
     f'<text x="72" y="128" font-family="{MONO}" font-size="64" font-weight="700" fill="#f0efec">video-to-skill</text>',
     f'<text x="72" y="182" font-family="{SANS}" font-size="26" fill="#c3c2b7">Claude watches a tutorial, runs it on a sample,</text>',
     f'<text x="72" y="216" font-family="{SANS}" font-size="26" fill="#c3c2b7">and only saves what worked.</text>',
     f'<text x="72" y="268" font-family="{MONO}" font-size="17" fill="#898781">ingest  &#8594;  extract  &#8594;  gate  &#8594;  execute  &#8594;  propose</text>']
# motif: video card -> verified skill card
vx, vy = 820, 96
b += [f'<rect x="{vx}" y="{vy}" width="150" height="104" rx="12" fill="none" stroke="#f0efec" stroke-width="2.5"/>',
      f'<path d="M{vx+62} {vy+34} L{vx+62} {vy+70} L{vx+94} {vy+52} Z" fill="#3987e5"/>',
      f'<rect x="{vx+16}" y="{vy+86}" width="118" height="4" rx="2" fill="#383835"/>',
      f'<rect x="{vx+16}" y="{vy+86}" width="46" height="4" rx="2" fill="#3987e5"/>',
      f'<path d="M{vx+172} {vy+52} H{vx+226}" stroke="#898781" stroke-width="2.5" stroke-linecap="round"/>',
      f'<path d="M{vx+218} {vy+44} L{vx+228} {vy+52} L{vx+218} {vy+60}" fill="none" stroke="#898781" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>']
sx, sy = vx + 250, vy - 14
b += [f'<rect x="{sx}" y="{sy}" width="110" height="132" rx="12" fill="none" stroke="#f0efec" stroke-width="2.5"/>']
for i, w in enumerate([62, 74, 50, 68]):
    b.append(f'<rect x="{sx+18}" y="{sy+24+i*18}" width="{w}" height="5" rx="2.5" fill="#52514e"/>')
b += [f'<circle cx="{sx+82}" cy="{sy+106}" r="17" fill="#0ca30c"/>',
      f'<path d="M{sx+74} {sy+106} l6 6 l11 -12" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>',
      f'<text x="{vx+75}" y="{vy+150}" text-anchor="middle" font-family="{SANS}" font-size="15" fill="#898781">tutorial video</text>',
      f'<text x="{sx+55}" y="{vy+150}" text-anchor="middle" font-family="{SANS}" font-size="15" fill="#898781">verified skill</text>',
      '</svg>']
open(f"{out}/banner.svg", "w").write("\n".join(b))

# ---------- pipeline ----------
W, H = 1280, 330
steps = [("1", "Ingest", ["Transcript, plus frames", "only where the narrator", "points at the screen"]),
         ("2", "Extract", ["A step table with the", "exact command and an", "evidence tag per step"]),
         ("3", "Capability gate", ["Every step must map", "to a tool Claude can", "operate in the session"]),
         ("4", "Execute", ["Run each step on a", "disposable sample and", "measure the result"]),
         ("5", "Propose", ["Verified steps only,", "with corrections and", "pitfalls recorded"])]
bw, bh, gap, x0, y0 = 208, 150, 40, 40, 64
p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Pipeline: ingest, extract, capability gate, execute, propose. If a step has no tool, the run stops and reports.">',
     f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="16" fill="{SURF}" stroke="{GRID}"/>',
     f'<text x="{x0}" y="40" font-family="{SANS}" font-size="20" font-weight="600" fill="{INK}">How a video becomes a skill</text>']
for i, (n, t, lines) in enumerate(steps):
    x = x0 + i * (bw + gap)
    gate = (i == 2)
    p.append(f'<rect x="{x}" y="{y0}" width="{bw}" height="{bh}" rx="12" fill="#ffffff" stroke="{INK if gate else AXIS}" stroke-width="{2 if gate else 1.5}"/>')
    p.append(f'<circle cx="{x+28}" cy="{y0+30}" r="13" fill="{INK}"/>')
    p.append(f'<text x="{x+28}" y="{y0+35}" text-anchor="middle" font-family="{SANS}" font-size="14" font-weight="700" fill="#ffffff">{n}</text>')
    p.append(f'<text x="{x+50}" y="{y0+36}" font-family="{SANS}" font-size="18" font-weight="600" fill="{INK}">{e(t)}</text>')
    for j, ln in enumerate(lines):
        p.append(f'<text x="{x+18}" y="{y0+72+j*22}" font-family="{SANS}" font-size="15" fill="{INK2}">{e(ln)}</text>')
    if i < 4:
        ax = x + bw + 6
        p.append(f'<path d="M{ax} {y0+bh/2} H{ax+gap-14}" stroke="{MUTED}" stroke-width="2" stroke-linecap="round"/>')
        p.append(f'<path d="M{ax+gap-20} {y0+bh/2-6} L{ax+gap-12} {y0+bh/2} L{ax+gap-20} {y0+bh/2+6}" fill="none" stroke="{MUTED}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>')
gx = x0 + 2 * (bw + gap) + bw / 2
p += [f'<path d="M{gx} {y0+bh+4} V{y0+bh+34}" stroke="{MUTED}" stroke-width="2" stroke-dasharray="4 5" stroke-linecap="round"/>',
      f'<rect x="{gx-190}" y="{y0+bh+38}" width="380" height="44" rx="10" fill="#ffffff" stroke="{AXIS}" stroke-width="1.5" stroke-dasharray="5 5"/>',
      f'<text x="{gx}" y="{y0+bh+66}" text-anchor="middle" font-family="{SANS}" font-size="15" fill="{INK2}">A step with no tool: stop and report. Nothing is saved.</text>',
      '</svg>']
open(f"{out}/pipeline.svg", "w").write("\n".join(p))

# ---------- results chart ----------
rows = [("Trim filter", None),
        ("-vf trim=duration=3", 3, 10.01), ("-vf trim=duration=3 -c:a copy", 3, 10.00), ("-vf trim=end=3", 3, 10.01),
        ("-vf trim=start=3,setpts=…", 7, 10.01), ("-vf trim=start=3:end=6,setpts=…", 3, 10.01),
        ("Seeking", None),
        ("-ss 3 -i in.mp4", 7, 7.01), ("-ss 3 -i in.mp4 -t 3", 3, 3.00), ("-ss 3 -i in.mp4 -to 6", 3, 6.00), ("-i in.mp4 -ss 3 -to 6", 3, 3.00),
        ("From the end", None),
        ("-sseof -2 -i in.mp4", 2, 2.01), ("-sseof -00:00:02 -i in.mp4", 2, 2.01)]
W = 1280; lx = 400; px0 = 420; pw = 520; top = 150; rh = 32; gh = 34
def X(v): return px0 + pw * v / 10
n_rows = sum(1 for r in rows if r[1] is not None); n_grp = len(rows) - n_rows
ph = n_rows * rh + n_grp * gh
H = top + ph + 64
c = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Chart: 11 ffmpeg commands from one tutorial run on a 10-second test clip. 5 produced the output length the tutorial described; 6 did not.">',
     f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="16" fill="{SURF}" stroke="{GRID}"/>',
     f'<text x="40" y="44" font-family="{SANS}" font-size="20" font-weight="600" fill="{INK}">Taught vs. measured: 11 commands from one ffmpeg tutorial</text>',
     f'<text x="40" y="70" font-family="{SANS}" font-size="15" fill="{INK2}">Length of the output file, in seconds, when each command ran as taught on a 10-second clip with audio.</text>']
# legend
ly = 104
c += [f'<rect x="40" y="{ly-11}" width="14" height="14" rx="3" fill="{BLUE}"/>',
      f'<text x="62" y="{ly+1}" font-family="{SANS}" font-size="14" fill="{INK2}">Matched the tutorial (5)</text>',
      f'<rect x="250" y="{ly-11}" width="14" height="14" rx="3" fill="{ORANGE}"/>',
      f'<text x="272" y="{ly+1}" font-family="{SANS}" font-size="14" fill="{INK2}">Did not match (6)</text>',
      f'<path d="M420 {ly-13} V{ly+5}" stroke="{INK}" stroke-width="2.5" stroke-linecap="round"/>',
      f'<text x="432" y="{ly+1}" font-family="{SANS}" font-size="14" fill="{INK2}">Length the tutorial described</text>']
# grid
for v in range(0, 11, 2):
    c.append(f'<path d="M{X(v)} {top-6} V{top+ph}" stroke="{AXIS if v==0 else GRID}" stroke-width="1"/>')
    c.append(f'<text x="{X(v)}" y="{top+ph+22}" text-anchor="middle" font-family="{SANS}" font-size="13" fill="{MUTED}">{v}s</text>')
y = top
for r in rows:
    if r[1] is None:
        c.append(f'<text x="40" y="{y+23}" font-family="{SANS}" font-size="13" font-weight="600" fill="{MUTED}" letter-spacing="0.6">{e(r[0].upper())}</text>')
        y += gh; continue
    label, exp, act = r
    ok = abs(exp - act) < 0.1
    col = BLUE if ok else ORANGE
    cy = y + rh / 2; bh2 = 14; x1 = X(act); r4 = 4
    c.append(f'<text x="{lx}" y="{cy+5}" text-anchor="end" font-family="{MONO}" font-size="14" fill="{INK}">{e(label)}</text>')
    c.append(f'<path d="M{px0} {cy-bh2/2} H{x1-r4} a{r4} {r4} 0 0 1 {r4} {r4} V{cy+bh2/2-r4} a{r4} {r4} 0 0 1 -{r4} {r4} H{px0} Z" fill="{col}"><title>{e(label)}: described {exp}s, measured {act:.2f}s</title></path>')
    c.append(f'<path d="M{X(exp)} {cy-12} V{cy+12}" stroke="{SURF}" stroke-width="6.5" stroke-linecap="round"/>')
    c.append(f'<path d="M{X(exp)} {cy-11} V{cy+11}" stroke="{INK}" stroke-width="2.5" stroke-linecap="round"/>')
    if ok: note = f"{act:.1f}s"
    elif act > 9: note = f"{act:.1f}s  ·  audio left untrimmed"
    else: note = f"{act:.1f}s  ·  described as {exp}s"
    c.append(f'<text x="{max(x1, X(exp))+14}" y="{cy+5}" font-family="{SANS}" font-size="14" fill="{INK2}">{e(note)}</text>')
    y += rh
c.append(f'<text x="40" y="{H-18}" font-family="{SANS}" font-size="13" fill="{MUTED}">ffmpeg 6.1.1. Seeking commands were reconstructed from narration. Full log: examples/ffmpeg-trim-video/verification.md</text>')
c.append('</svg>')
open(f"{out}/results.svg", "w").write("\n".join(c))
