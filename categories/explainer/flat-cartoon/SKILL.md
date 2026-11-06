---
name: flat-cartoon
description: Make a 24 s narrated idea explainer (16:9, 720p) in a flat-vector cartoon look - one original character acts out four beats (easy case, hard case, what goes wrong, what it means for you), two generated Seedance clips of two shots each, one narration line per shot, captions always on. Use when the user asks for this entry by name, wants a short cartoon explainer of an idea rather than a true story with real people, or wants a film that looks like its result/result.mp4. Ships a complete HyperFrames project that renders the example film as is.
---

# flat-cartoon

This folder reproduces one film. `result/result.mp4` is what you will get; `project/` renders it unchanged. To explain
another idea you change `project/film.json` and `project/assets/`, and nothing else.

Read before you start, in this order:
- `taste.json`: what it needs, what it fits, what it requires
- `references/floor.md`: the rules every film keeps
- `references/sourcing.md`: if the idea has facts in it, where they must come from
- `references/RECIPE.md`: the four beats, and what the example's script got wrong
- `references/SWAP.md`: the slots in `film.json`, and what never changes

## 0. Requirements and fit

- Run `bash scripts/setup.sh` first, yourself. It checks Node 20+, ffmpeg and Python 3 and installs the HyperFrames skills.
- The renderer is pinned and fetched by npx: `hyperframes@0.8.229`.
- No keys are needed to render the example. A new film needs `BYTEPLUS_API_KEY` (Seedream still, Seedance clips) and
  `FAL_KEY` (ElevenLabs narration). Read them from the environment or `project/.env`; never print them.
- Fits an idea that can be acted out by a character in four shots. Does not fit a true story about real people (use
  `paper-collage`), a product launch, or anything that needs real screens.

## 1. Run the example first

```bash
cd project
python3 tools/build.py
npx --yes hyperframes@0.8.229 check
npx --yes hyperframes@0.8.229 render -o renders/film.mp4
```

## 2. Write, show, then spend

Write the four lines and the four shot descriptions, and show them to the person before any generation. Seedance jobs
cannot be cancelled once they start. Then follow `references/SWAP.md` and `project/tools/footage.md`.

## 3. Look, render, measure

Pull a frame from each shot and read it: look for fake text the model wrote, a character that drifted, a caption over
the action. Then render and measure:

```bash
uv run --with librosa --with numpy --with pillow python -I scripts/analyze.py project/renders/film.mp4 /tmp/m
uv run --with numpy python -I scripts/events.py project/renders/film.mp4 /tmp/m
```

## 4. Deliver

Report the file, the script, which media was generated and with what, the metrics, and what you could not judge from
stills (the voice and the mix). Do not post it anywhere unless the user asks.

## This film's style rules

These are this entry's taste, not universal rules.
- One original character in every shot, fixed by one reference still. Never a character or look from an existing channel.
- Saturated colour on dark or dusk grounds, rim light and glow, flat shapes, no outlines.
- No text inside the picture; all words are captions.
- A plain sentence per caption in Inter 700 on a dark rounded box at the bottom.
