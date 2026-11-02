# Style from reference

Turn a video or an account you like into a style card in `styles/`, with three stills that prove it can be made.
The result is a look, not a film: it can go on any recipe in `films/` that it fits.

```
reference clips → frames and contact sheets → style card (look, consistency, motion, pace)
              → three stills → a person picks or rejects → styles/<name>/
```

## Steps

1. **Collect 2 to 5 clips** of the reference, downloaded by the person. More clips separate the style from one
   episode's content. Keep them local; never commit them or name them in public files.
2. **Extract.**
   ```bash
   ffmpeg -i clip.mp4 -vf "fps=2,scale=480:-1,tile=6x5" sheet_%02d.png          # contact sheets
   ffmpeg -i clip.mp4 -vf "select='gt(scene,0.3)',showinfo" -vsync vfr cut_%03d.png 2>&1 | grep pts_time   # cuts
   ```
   `films/tools/analyze.py` and `events.py` give average shot length and events per 10 s.
3. **Write the card** (`styles/STYLE.md` format), every field from what the frames show, as numbers where possible:
   - look: sample the palette from frames (5 to 7 colours with roles), name the type, texture, light, materials;
   - consistency: how does the main character or object stay the same? A code rig, one reference image fed to every
     generation, real photos, or it does not (then say so);
   - motion: list the moves frame by frame, each with its duration and easing;
   - pace: measured, not guessed;
   - banned: what would make it look like a different style.
4. **Decide how each element is made** (STYLE.md table): code (SVG, three.js, shader), a generated image or video with
   its prompt, or real material. Pick the cheapest one that holds up; a style that needs a 40-hour build per film
   is not reusable.
5. **Make three stills** on a neutral subject that is not the reference's: a wide, a close-up, a frame with type.
   Code-built stills go through `modeling/scene-from-references` (Light run). Generated stills keep their prompts.
6. **Compare** each still with the nearest reference frame side by side (the scripts in
   `modeling/scene-from-references/scripts/`) and with a zero-context critic: "Same style? Score 1 to 10, name what
   differs most."
7. **A person picks.** Yes: commit `styles/<name>/` and add its row to `styles/README.md`. No: note why in the card's
   `banned` or drop it.

## Pass marks

| Step | Pass |
|---|---|
| 3 | every field filled; palette as hex; pace from a command |
| 5 | three stills, different framings, at least one with type, subject not taken from the reference |
| 6 | critic scores "same style" ≥ 8 for every still; nothing from the reference copied 1:1 |
| 7 | a person says yes |

## Cost

One agent, about an hour: extraction is free, the card is reading, the stills are the only build. If step 4 says an
element needs a long build, make that element once as a reusable part (a rig, a shader) inside the style folder.

## What a style is not

- Not the script or the topic. "What if you could rewind 10 seconds" is content; the dusk light and the rig are style.
- Not the reference's characters, logos or catchphrases. Borrow how it looks, never what it owns.
