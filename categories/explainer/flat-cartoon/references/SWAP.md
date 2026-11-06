# Tell another idea

Everything you change is `project/film.json` and `project/assets/`. Nothing in `tools/build.py` changes.

## 1. Write four lines (show them before generating anything)

One idea, four beats (references/RECIPE.md): easy case, hard case, what goes wrong, what it means for the viewer.
15-17 words a line, everyday words, one point a line. Show the four lines and the four shot descriptions to the person
and wait for a yes: the next steps cost money and cannot be undone.

## 2. Character and footage (tools/footage.md)

1. One character still with `tools/seedream.py` (or the person's own art). Original characters only: never a
   character, logo or look lifted from an existing channel.
2. Two Seedance clips, two shots each, the still as `--reference-image`, the same style block in both prompts.
3. Put the files in `assets/footage/` and list them in `film.json` `footage` with their start times.

## 3. Narrate

```bash
python3 tools/voice.py script.txt     # one line per narration line; writes assets/audio/line-N.mp3
```

Put each file in `film.json` `lines`, `at` 0.3 s into its shot. Split each line into two captions at the pause it prints.
If a line runs past its shot, shorten the words rather than speeding the voice.

## 4. Build and render

```bash
python3 tools/build.py
npx --yes hyperframes@0.8.229 check
npx --yes hyperframes@0.8.229 render -o renders/film.mp4
```

## What never changes

The four-beat order, one line per shot, captions always on, the clip sound under the voice, and the loudness target.
