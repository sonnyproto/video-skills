---
name: metric-sculpture
description: Make a 21.6 s narrated launch film (16:9, 112 BPM) that proves one real growth number - the product's own app redrawn as a living screencast where a pixel mascot acts out the work (result card, rewind, the request typed, a 60-day time-lapse), then one whip into a 3D studio where the number is built as physical plates on a walnut base, a hit on the verdict ("100×") and the logo lockup. Use when the user asks for this entry by name, picks it from the video-skills gallery, has a real before/after metric to show, or wants a film that looks like its result/result.mp4. Ships a complete HyperFrames project that renders the example film as is.
---

# metric-sculpture

This folder reproduces one film. `result/result.mp4` is what you will get; `project/` renders it unchanged. To make it for
another product you change `project/film.json`, the images and the five voice lines, and nothing else.

Read before you start, in this order:
- `taste.json`: what it needs, what it fits, what it requires
- `references/floor.md`: the rules every film keeps
- `references/sourcing.md`: how to collect the real screens, logo and copy
- `references/RECIPE.md`: this film beat by beat
- `references/SWAP.md`: the slots to fill, and what never changes

## 0. Requirements and fit

- Run `bash scripts/setup.sh` first, yourself; do not hand it to the user. It checks Node 20+, ffmpeg and Python 3 (and
  says how to install any that are missing) and installs the HyperFrames agent skills if they are not there.
- Freshly installed skills load in the next session. Do not stop for that: read `~/.claude/skills/hyperframes/SKILL.md`
  (or `~/.agents/skills/hyperframes/`) directly for the render contract. This entry's templates already follow it.
- The renderer is pinned and fetched by npx: `hyperframes@0.8.191`. Three.js 0.170 and GSAP 3.14.2 load from jsdelivr.
- No keys needed to render. New voice lines and new music need `FAL_KEY` (ElevenLabs through fal).
- The film stands on **one true number with a before and an after** (views, signups, revenue, leads) and the product's
  real app. Read `taste.json` `fits` / `avoid`. No real metric, or no app to redraw: say so and suggest another entry.
  Never make a number up or round it up for the film.

## 1. Run the example first

```bash
cd project
python3 tools/build.py                       # film.json + tools/templates -> index.html and compositions/
python3 tools/sfx.py                         # the foley track, from the same times and the plate count
npx --yes hyperframes@0.8.191 check
npx --yes hyperframes@0.8.191 render -q delivery -o renders/film.mp4 --quiet
bash tools/master.sh renders/film.mp4 film.mp4   # -14 LUFS, peaks under -1 dBTP
```

It should match `result/result.mp4`. The example product is Votrix AI; its logo and agent portraits ship in
`project/assets/img/` (see `project/assets/THIRD_PARTY.md`).

## 2. Collect the real material, then swap the product

First follow `references/sourcing.md` yourself: the product's app (screenshots or a demo account), logo, agent or feature
names and the copy, with where each came from. Then get the metric from the person who owns it and write down its source;
it goes on screen as `metric.source`.

- Must be real: the app's labels and layout, the logo, names, the number and every claim.
  Only the mascot, the studio, the music and the foley are made for the film.
- Look in order: its site → press kit, docs, launch post → official social accounts → press coverage → store pages it
  controls → only then the user. Blocked (Cloudflare, 403)? Do not get around it; take the next source.
- The time-lapse rows are the product's own demo or status lines. If they are illustrative, say so in the hand-over.

Then follow `references/SWAP.md`: fill every slot in `film.json`, draw a new mascot, write and voice the five lines,
make new music, build, run `sfx.py`. `build.py` refuses a film.json that breaks the recipe's limits and says why.

Ask the user only for what you cannot get yourself: the metric and its source, a demo account, the logo file.

## 3. Look, render, measure

Follow the Process in `references/floor.md`: snapshot the moments in `SWAP.md` §4, read every frame, fix, render, master.
Then listen: every voice line, the plate toks, the hit at 15.0. Measure and compare with `result/metrics.json`:

```bash
uv run --with librosa --with numpy --with pillow python -I scripts/analyze.py project/film.mp4 /tmp/m
uv run --with numpy python -I scripts/events.py project/film.mp4 /tmp/m
```

## 4. Deliver

Report the file, what came from the product and what was generated, the metric's source, the metrics, and what you could
not judge from stills. Do not post it anywhere unless the user asks.

## This film's style rules

These are this entry's taste, not universal rules; they hold for this film.
- Two worlds, one cut: the flat app on a dark desktop, then a warm physical studio. They meet in a single whip at 7.5 s;
  never cut back.
- The app is redrawn 1:1 from the real one, at about 1.4×. Nothing in it is invented; the cursor is the user, never a hand.
- The mascot is the only thing that moves on its own in the app, in one colour no UI uses. It stands only on measured top
  edges (tiles, bubbles, rows) and lands with a squash and dust.
- Numbers count by plates, never by time: the counter is plates landed × unit. One plate is one unit, always.
- The plates fall with gravity and accelerate (the feed gets faster); every tenth plate is a different material and gets a
  mallet note a step higher.
- One accent colour, only on the verdict and the last line. No glow, bloom or dark void in the studio.
- The hook is the result, said in the first second: "Our views just went up a hundred times."
