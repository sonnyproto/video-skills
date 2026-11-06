# Footage

The whole picture is generated: two 12 s Seedance 2.0 clips (BytePlus ModelArk), 720p, 16:9, each holding two 6 s shots
with a hard cut in the middle. One reference still fixes the character, so it looks the same in every shot. The shipped
files in `assets/footage/` are the clips as generated; the film renders without any key.

## 1. The character still (Seedream 4.0)

`assets/img/character-ref.png` was made first with `tools/seedream.py` and is passed to every clip as a reference image.
Make it a full scene, not a character sheet: the model copies the rendering (light, grain, palette) as well as the figure.

```bash
python3 tools/seedream.py assets/img/character-ref.png "Flat vector illustration for a science explainer animation, clean geometric shapes, no outlines, smooth gradients, saturated jewel colours, strong rim light on every object, soft glow and bloom, subtle grain, layered depth with foreground midground background, cinematic composition, vertical 9:16, no text, no logo. Ground-level scene on a grassy hill under a coral and violet dusk sky, a giant wall of wind and dust sweeping from the left, trees bending, houses and small rocks flying, several tiny cute original round mint-green blob creatures with stubby legs tumbling through the air, bright rim light from a low sun, glowing particles, sense of motion and drama" --seed 11
```

## 2. The clips (Seedance 2.0)

Every prompt starts with the same style block, then names two shots with their times. Ask for no text: the model
writes fake letters and fake maths when it is allowed to.

Style block:

```
Flat vector 2D science explainer animation style, clean geometric shapes, no outlines, saturated jewel colours, rim light and soft glow, layered parallax depth, smooth elastic character motion. The hero is the small round mint-green blob creature with stubby legs from the reference image. No text, no letters, no numbers on screen, no dialogue.
```

| File | Shots | Prompt after the style block |
|---|---|---|
| pair-1.mp4 | 1 maths, 2 judges | Shot 1 (0-6s): in a cozy violet study the blob scribbles math on a chalkboard, each time a giant glowing green check mark or red cross stamps instantly beside it, faster and faster, the blob bounces happily. Shot 2 (6-12s): hard cut, the blob proudly paints on an easel in a coral-sunset gallery; three judge blobs hold up identical scorecards with just a plain dot, the blob looks back and forth confused, shrugging. |
| pair-2.mp4 | 3 overload, 4 the pick | Shot 1 (0-6s): the blob piles shiny decorative things onto its painting: gold sparkles, lens flares, glitter, ribbons, neon, until the canvas becomes a gaudy overloaded tower that wobbles; an audience of blobs yawns and walks away. Shot 2 (6-12s): calm teal night, a robotic arm prints hundreds of glowing cards that fly past; a single human hand reaches in, picks one simple quiet card, and the rest dissolve into light; slow push in on the chosen card. |

```bash
python3 tools/seedance.py assets/footage/pair-1.mp4 "<style block> <prompt>" --duration 12 --ratio 16:9 --resolution 720p --reference-image assets/img/character-ref.png --audio
```

Each clip took about 5 minutes. `--audio` gives the clip its own sound effects, which the mix uses as the bed. The
chalkboard in pair-1 still came out with fake formulas despite "no text"; keep such shots short or cover them with a
caption.
