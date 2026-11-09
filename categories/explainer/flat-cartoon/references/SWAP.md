# Explain something else

Everything you change is `project/film.json` and `project/assets/`. Nothing in `project/tools/templates/` or
`project/tools/build.py` changes.

## 1. Facts and beats first (show them before generating anything)

One question, one event, one consequence the character feels. Every number on screen goes into `film.json` `sources`
with a URL (`references/sourcing.md`). Show the beats and sources and wait for a yes.

## 2. The slots in film.json

| Slot | What |
|---|---|
| `copy.title_before / title_accent / title_after` | the question; the accent word takes the key-light colour |
| `copy.label_*` | the four pills (≤ 3 words each) |
| `copy.caption_1 / caption_2` | the ground-scene captions |
| `palette.*` | label fills (white text must reach 3:1), title accent, the character's main and shadow colour |
| `images.far / mid / near` | the three scenery plates |
| `scenes[].duration` | shot lengths (keep the sum, or re-time the templates' beats) |
| `sound.src` | the mastered sound file |

## 3. New scenery plates (tools/layers.md)

Three transparent 16:9 plates (far, mid, near), the style block from `tools/layers.md` in every prompt, the light from
the same side as the code key light, no characters, no text. Generate two candidates each, pick, and show them for
sign-off. Put them in `assets/bg/` (2304 px wide is enough) and line their ridges up with `top` in the ground template
only if the horizon moves.

## 4. Sound

Edit the cue times at the top of each block in `tools/sound.py` if beats moved, then:

```bash
python3 tools/sound.py /tmp/raw.wav
ffmpeg -y -i /tmp/raw.wav -af loudnorm=I=-14:TP=-1.5:LRA=7 -ar 48000 -b:a 192k assets/audio/sound.mp3
```

## 5. Build and render

```bash
python3 tools/build.py
npx --yes hyperframes@0.9.23 check
npx --yes hyperframes@0.9.23 render -o renders/film.mp4
```

## What never changes

One key light per scene and the four shading layers; a new element every 1-3 s; the camera always moving; frame 0 shows
the question; the consequence is acted, not written; plates hold scenery only; -14 LUFS.
