---
name: flat-cartoon
description: Make a short science explainer (10 s sample, 16:9, 1080p) in a flat-vector cartoon look - deep violet grounds, one glowing key light, layered cel shading with rim light, grain - where image-model background plates give the illustration detail and code draws and animates everything that moves (light, sky, stars, labels, an original character rig). Use when the user asks for this entry by name, wants a flat-vector science-channel-style explainer of a fact or mechanism, or wants a film that looks like its result/result.mp4. Ships a complete HyperFrames project that renders the example film as is.
---

# flat-cartoon

This folder reproduces one film. `result/result.mp4` is what you will get; `project/` renders it unchanged with no keys.
To explain something else you change `project/film.json` and `project/assets/`, and nothing in `project/tools/templates/`.

Read before you start, in this order:
- `taste.json`: what it needs, what it fits, what it requires
- `references/floor.md`: the rules every film keeps
- `references/sourcing.md`: every number on screen needs a source
- `STYLE.md`: the look, element by element (palette, light, the four shading layers, texture, pace)
- `references/RECIPE.md`: the film beat by beat
- `references/SWAP.md`: the slots in `film.json`, how to make new layers, what never changes

## 0. Requirements and fit

- Run `bash scripts/setup.sh` first, yourself. It checks Node 20+, ffmpeg and Python 3 and installs the HyperFrames skills.
- The renderer is pinned and fetched by npx: `hyperframes@0.9.23`.
- No keys are needed to render the example. New background plates need an image model that can output transparent PNGs
  (`OPENAI_API_KEY` for GPT Image; the example used GPT Image 2.6 through the Higgsfield MCP). The sound is synthesised
  by `tools/sound.py` and needs nothing.
- Fits a fact, a mechanism or a what-if that can be shown with one light source, a few objects, labels and one reacting
  character. Does not fit a true story about real people (use `paper-collage`), a product launch, or long talking scripts.

## 1. Run the example first

```bash
cd project
python3 tools/build.py
npx --yes hyperframes@0.9.23 check
npx --yes hyperframes@0.9.23 render -o renders/film.mp4
```

## 2. Write, show, then spend

Write the beats (RECIPE.md shape: question → setup with labels → the event → the consequence, felt by the character)
and the facts with their sources, and show them before generating any plate. Then follow `references/SWAP.md`.

## 3. Look, render, measure

`npx hyperframes snapshot --at <every beat>` and read each frame against `STYLE.md` "Banned". Typical failures: a baked
warm rim light that survives the light going out, a plate whose horizon does not meet the character's feet, a label
under 28 px. Then render and measure:

```bash
uv run --with librosa --with numpy --with pillow python -I scripts/analyze.py project/renders/film.mp4 /tmp/m
uv run --with numpy python -I scripts/events.py project/renders/film.mp4 /tmp/m
```

## 4. Deliver

Report the file, the beats, the facts and their sources, which plates were generated and with what prompt, the metrics,
and what you could not judge from stills (the sound, motion feel). Show generated plates for sign-off before shipping.
Do not post it anywhere unless the user asks.

## This film's style rules

These are this entry's taste, not universal rules (full recipe in `STYLE.md`).
- Never pure black, grey or black outlines; the darkest colour is an inky violet.
- One key light per scene, usually inside the frame; it decides every shadow side and rim.
- Every object has base, shadow shape, highlight and rim; glows are blurred, never hard rings.
- Generated plates hold the scenery only (no characters, no text, transparent above the ridge); the character, light,
  sky, stars and labels are code, so they can act, change light and stay consistent.
- Something new every 2-3 s; the camera never stops moving.
- Original characters only; never a character, logo or look lifted from an existing channel.
