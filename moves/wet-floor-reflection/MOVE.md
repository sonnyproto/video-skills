# Wet floor reflection

A paper lightbox at night told in one scene. One vertical axis splits it: neon signs on the left, warm arched
windows on the right, two faceless figures back to back, each rimmed by the light it faces, and a backlit disc above
them. The floor mirrors everything.

## The wet floor

After the scene is drawn, everything above the feet line is copied into an offscreen canvas flipped
(`setTransform(1, 0, 0, −1, 0, line)`) with `blur(2px)`, then laid back in 6 px strips, each nudged sideways by
`sin(y·0.05 + 2.2t)` and faded as `0.62·(1 − d)^1.5`. A dark pool gradient from the bottom holds the text.

## Variables

The caption is the text of the `#line` spans (Playfair Display italic, words rise and unblur one by one from 3.6 s).
Colours are the CSS variables on `#root`.

## Use it when

A contrast: two ways, before and after, calm and craving. 16:9 puts the words at the bottom over the floor; 9:16
keeps them at the top, clear of the platform UI.

## Do not use it when

The two sides are not a real contrast in the story, or there is a product screen to show.

## Pitfalls

- Draw anything that lies on the floor after the reflection, or it gets reflected twice.
- A radial gradient filled into a rectangle smaller than its radius leaves a hard edge; fill the whole circle's box.
