# Cut-paper stop-motion

Printed paper cut-outs shot frame by frame: flat colour made rich by texture, wobbly hand-cut edges, soft contact
shadows on the sheet behind, and a stepped pose rate under a perfectly smooth camera.

## How each element is made

All in Canvas 2D from the paper kit inlined at the top of each move's script (`moves/parallax-sheets`,
`moves/stop-motion-clock`).

| Element | Recipe |
|---|---|
| Hand-cut edge | `cut(points)`: subdivide every ~12 px, push each point ±1 px along the edge normal |
| Paper fibre | a tileable 512² tile of blotches and short fibres, laid on each sprite with soft-light at 0.45-0.55 |
| Sprite | `sprite(w, h, draw, {rim, lines, shadow})`: baked once with fibre, print lines, a rim of light and a blurred silhouette |
| Contact shadow | the sprite's silhouette blurred 10 px at 0.3, offset (14, 10) in world space before rotation |
| Backdrop | `backdrop()`: gradient, mottling at two scales, print lines, dust, warm key light, dark corners |
| Depth | `sheet(g, cam, p, ...)`: 3-7 sheets, zoom^p around a centre moved p times the camera |
| Clock | `clock(15)`: `q(t)` for poses, `boil(id, t)` and `flicker(t)` re-rolled per pose; the camera uses t |
| Characters | flat parts on pivots: one cut coat or body, capsule limbs, a head on a neck pivot; faces dot eyes or none |
| Text | letters as paper sprites that drop, squash one pose and rest at a slight tilt |

## Palette

Four values do the work: ground about 60 %, the accent and its warm neighbours 25 %, cream and ink 15 %. To change
the mood change ground and accent as a pair (red on teal, ochre on navy, coral on sage). A brand colour takes the
accent role.

## Use it when

Warm, small stories: a shop, a craft, a chain of cause and effect, a character living the message. Explainers
for a non-technical audience.

## Do not use it when

The film must show real product UI, real people or real places (paper replaces them), or it should feel futuristic.

## Stills

The three stills come from the demo moves, so two of them share a scene. Replace them with frames from the first
real film in this style, and set `worked_example` then.
