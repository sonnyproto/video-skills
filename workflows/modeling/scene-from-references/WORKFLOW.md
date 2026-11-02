# Scene from references

Build a scene in code (three.js, HTML, SVG) to match reference images, prove the match with side-by-side stills,
and only then animate it. Distilled from [Athenaion](https://github.com/Leonxlnx/athenaion) (MIT), a three.js world
built by Claude Code to match 9 reference images.

```
script and shot list → [ reference images → code model → still vs reference ]  → animation, voice, music, render
                         └──────── loop until each still passes ────────┘
```

## Steps

1. **Script and shot list.** What each shot shows, its framing and length.
2. **References.** One image per shot. Generated images are fine for atmosphere and places; real products, logos and
   people must come from their real source.
3. **Write the standards before the code** (templates/):
   - `ART_BIBLE.md`: palette, materials, light, what "too much" looks like;
   - `COMPOSITION.md`: per shot, camera position, what sits where, the focal point;
   - `CONTRACT.md`: if several agents build parts, how the parts plug together (units, origin, naming).
4. **Base first.** Renderer, camera per shot, light, the still-export script. Everyone shares it.
5. **Model by part, each in its own loop.** Build → render the shot still → compare with the reference → fix.
6. **Director pass.** Look at whole shots: composition, colour, detail density, using side-by-side images and colour
   statistics against each reference.
7. **Stills to a person.** Nothing moves until a person approves the stills.
8. **Then** animation, voice and music (see audio/voiceover-then-music), render.

## Pass marks

| Step | Pass |
|---|---|
| 5 | the part reads the same as the reference in a side-by-side still |
| 6 | mean colour and saturation per shot within a set distance of the reference; composition matches the grid in COMPOSITION.md |
| 7 | a person says yes |

## Cost

Athenaion took ~45 h, 55 agents (up to 12 in parallel) and ~11M output tokens, about $2k at API prices. Size the run:

- **Light:** one agent, one or two shots, steps 4–7 only.
- **Full:** parallel agents per part (step 5) and a director round; only when the scene is the film.
