# Scene from references

Build a scene in code (three.js, HTML, SVG) to match reference images, prove the match with side-by-side stills,
and only then animate it. Distilled from [Athenaion](https://github.com/Leonxlnx/athenaion) (MIT), a three.js world
built by Claude Code to match 9 reference images, and from [cook](https://github.com/Leonxlnx/cook) (MIT), the loop
its author packaged afterwards: references as the bar, numeric scores, zero-context critics, stills before video.

```
script and shot list → [ reference images → code model → still vs reference ]  → animation, voice, music, render
                         └──────── loop until each still passes ────────┘
```

## Steps

1. **Lock the script and shot list.** What each shot shows, its framing and length, and what every visual element
   means. One element, one meaning for the whole film: if water is AI, water is never money. A person approves this in
   words before any code; changing words is cheap, changing a scene is not.
2. **References.** One image per shot, 3 to 12 for the film.
   - Atmosphere, places, objects: generate the target image with an image model first, then build to it.
   - Real products, logos and people: from their real source, never generated.
   - Motion references: extract frames (`ffmpeg -i ref.mp4 -vf fps=10 f_%04d.png`) and list every effect with its
     timecode, easing and duration. Take from many references; never copy one element 1:1.
3. **Write the standards before the code** (templates/):
   - `ART_BIBLE.md`: palette, materials, light, what each element means, the ban list, what "too much" looks like;
   - `COMPOSITION.md`: per shot, camera position, what sits where, the focal point;
   - `CONTRACT.md`: if several agents build parts, how the parts plug together (units, origin, naming).
4. **Base first.** Renderer, a fixed camera preset per shot, light, the still-export script. Stills render at the
   reference's aspect ratio. Everyone shares it.
5. **Model by part, each in its own loop.** Build → render the shot still → `scripts/side-by-side.mjs` → fix.
6. **Score with a fresh critic.** A subagent with no context gets only the side-by-side image and the rubric below,
   optionally a different model. Your own score is logged, never decisive. Also run `scripts/color-stats.mjs` per shot.
7. **Director pass.** Look at whole shots: composition, colour, detail density. Fix the weakest dimension in the
   weakest shot first, in depth, before widening.
8. **Stills to a person.** Nothing moves until a person approves the stills. Their words beat the critic.
9. **Then** animation, voice and music (see audio/voiceover-then-music), render.

## Scripts

Need Node 18+ and ffmpeg, nothing else.

```bash
node scripts/side-by-side.mjs --out compare/r01.jpg refs/1.png stills/1.png refs/2.png stills/2.png
node scripts/color-stats.mjs refs/1.png stills/1.png        # per-cell brightness and saturation, exit 1 if off
```

## Rubric

Score each shot from 1 to 10 on each dimension. One number per dimension, never one overall number, so the weakest
cannot hide.

| Dimension | Checks | Typical failure |
|---|---|---|
| Composition | framing, scale, focal point, horizon | subject too small, empty foreground |
| Light | direction, softness, shadows, haze | flat light, hard shadows |
| Colour | hue, saturation, brightness per region | grey and washed out, or oversaturated |
| Materials | how surfaces take light | plastic look |
| Detail density | near and far, variety | bare distance, visible repeats |
| Reading | can a stranger say what the shot means in one line | the metaphor needs explaining |

Critic prompt:

```text
Left is a reference, right is a render made in code. Score the right image 1 to 10 on composition, light, colour,
materials, detail density, and reading (can you say in one line what it shows). Then name the single change that
would raise the lowest score most. Be strict: 7 is decent, 9 holds up next to the reference.
```

Models score their own work too high, and critics share some of it. When a person's estimate differs, log the gap and
subtract it from later critic scores.

## Pass marks

| Step | Pass |
|---|---|
| 1 | a person approved the shot list in words; every visual element has one meaning |
| 5 | the part reads the same as the reference in a side-by-side still |
| 6 | critic median ≥ 9 on every dimension of every shot; `color-stats.mjs` passes (delta ≤ 0.08 per cell) |
| 8 | a person says yes |

## Cost

Athenaion took ~45 h, 55 agents (up to 12 in parallel) and ~11M output tokens, about $2k at API prices. Size the run:

- **Light (default for social and explainer films):** one agent, steps 4 to 8, at most 3 rounds or 1 hour, then the
  stills go to the person whatever their score, with the scores attached.
- **Full:** parallel agents per part (step 5) and a director round; only when the scene is the film. Set a time
  budget up front and read the clock every round.

Most of the cost is rework, not detail: re-reading a growing project every round, and rebuilding a scene whose
meaning changed. Step 1 is the cheapest place to save.

## What went wrong before

- An explainer ("AI is rising water") was built four times: 2D, 3D, then two more 3D versions. No reference images,
  the look was decided while coding, and the water meant AI in the first half and money in the second, so viewers
  lost the argument. Stick figures were rejected only after the full build. The fixes were step 1 (one element, one
  meaning, shot list approved in words) and step 2 (target images before code).
- The builder checked its own frames and passed copy and shots that a person found unclear, several rounds in a row.
  The fix was step 6: a critic with no context, and a "reading" dimension.
- Code-made music sounded cheap. Sound comes from a licensed library or a music model (see
  audio/voiceover-then-music), not from code, unless it truly holds up.
