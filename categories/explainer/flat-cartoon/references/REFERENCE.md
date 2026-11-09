# Reference

The look is after the family of flat-vector science channels. It copies none of them: the character, palette values,
every shot and every plate are original. No reference footage is shipped or redrawn.

## What was studied

90 frames (one every 3 s from three 90 s stretches of three films on different topics: space, the brain, civilisation),
a 14-colour palette extracted from each, and hard-cut detection. Findings that became the rules in `STYLE.md`:

- Darkest colours are inky violets and blues (around `#030223`-`#1c0b50`), never black; skies are vertical gradients
  from indigo down to magenta.
- One key light per scene, usually inside the frame, with soft bloom that spills onto nearby objects.
- No outlines; each object is a base colour plus a shadow shape (darker, shifted toward violet), a highlight and a rim.
- Subjects fill 25-50 % of the frame on a lot of dark negative space; an observer character often sits in a corner.
- Hard cuts every 8-15 s on average, but the frame changes every 2-3 s: elements pop in, the camera keeps moving,
  transitions zoom through objects.

## Why plates plus code

A first version drew everything in SVG; it read as clean motion graphics but thin as illustration. Generating only the
scenery (three transparent depth plates) and keeping light, sky, labels and the character in code gave the density of
an illustrated scene while keeping parallax, a light change and a consistent, acting character.

## Measured on result.mp4

| | |
|---|---|
| Length | 10.0 s, 1920×1080, 30 fps |
| Shots | 2 (one hard cut at 5.4 s) |
| Events per 10 s | 2.0 (the detector counts large frame changes; most motion here is slow drift and small pops) |
| Still share | 0.86 |
| Loudness | -15.0 LUFS, true peak -1.4 dBTP |

The two numbers on screen: 1 au = 149,597,870,700 m (IAU 2012 Resolution B2), and light covers it in 499 s
(c = 299,792,458 m/s), shown rounded as 150,000,000 km and 8 min 20 s.
