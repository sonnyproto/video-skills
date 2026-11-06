# Flat cartoon

Flat-vector cartoon scenes made by image and video models: an illustrator's drawing quality that code cannot reach. Code
only times the shots, sets the captions and mixes the sound.

## How each element is made

| Element | Recipe |
|---|---|
| Character | one still with Seedream 4.0 (`project/tools/seedream.py`): a full scene with the character in it, not a character sheet, so the model also copies light, grain and palette. An original design (here a round mint-green blob with stubby legs) |
| Shots | Seedance 2.0 (`project/tools/seedance.py`), 12 s, 720p, 16:9, `--reference-image` the character still, `--audio`. Two shots per clip, named with their times ("Shot 1 (0-6s): ... Shot 2 (6-12s): hard cut, ...") |
| Style block | every prompt opens with: "Flat vector 2D science explainer animation style, clean geometric shapes, no outlines, saturated jewel colours, rim light and soft glow, layered parallax depth, smooth elastic character motion. The hero is the small round mint-green blob creature with stubby legs from the reference image. No text, no letters, no numbers on screen, no dialogue." |
| Text | captions only, laid over in HyperFrames. The model still writes fake formulas on chalkboards and boards: keep those shots short or frame them out |
| Sound | the clips' own sound at about 28 % under the narration; no music |

All prompts are in `project/tools/footage.md`.

## Use it when

An idea, a mechanism or a trade-off that a character can act out: explainers and social posts under 30 s, a brand's point
of view told without real people.

## Do not use it when

The film needs real people, real places, product UI or text inside the picture, or a look that must match a client's
existing illustration.

## Stills

1. The character still (9:16) that every clip was generated from.
2. A wide: three judges hold up the same score in a sunset room.
3. A frame with a caption: the closing shot, one card kept in a hand.

## Sample

`result/result.mp4` is a draft: the look is right, the script is not (see `references/RECIPE.md`).
