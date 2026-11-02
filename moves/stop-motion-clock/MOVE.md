# Stop-motion clock

Two clocks in one picture. Puppets pose 15 times a second (`floor(15t)/15`, each pose held two frames at 30 fps);
the camera pushes every frame. The contrast between the stepped puppet and the smooth camera is the look.

## Beats (6 s)

| Time | What |
|---|---|
| 0–0.8 | the bird sits on the table, turns its head at 0.4 |
| 0.8–1.0 | crouch (squash 0.82) |
| 1.0–1.6 | a ballistic hop onto the cup rim; three replacement wing drawings cycle per pose |
| 1.6–1.74 | landing squash, then head turns every 0.6 s |
| 3.0– | letters drop one per 0.1 s: a 0.27 s fall, a one-pose squash, rest at −4 to +3 deg |

## Variables

The headline is the text of `#fontwarm` (Archivo Black, also used to load the font). Colours are the CSS variables on
`#root`.

## Use it when

A handmade, warm title: a small business, a craft, "made by hand", a cause and effect told by one object.

## Do not use it when

The brand is cold or technical, or the shot needs continuous fluid motion (the stepped poses read as stutter there).

## Pitfalls

- Divide the output rate evenly: 15 or 10 poses a second at 30 fps. 12 a second alternates two- and three-frame
  holds and stutters.
- Start every pose change on the pose grid, or boil and pose drift apart.
- Flying things use replacement drawings (wing up, level, down), never a rotated wing.
