# Paper lightbox

Layered cut paper at night, lit from behind. Each sheet is one flat colour with hand-cut edges, fibre and a thin rim
of light on the edge that faces the light. Lights are separate additive sheets. The sky is indigo, warm behind one
side and neon behind the other, and a wet floor mirrors both.

## How each element is made

Canvas 2D, from the paper kit inlined in `moves/medallion-burst-lock` and `moves/wet-floor-reflection`.

| Element | Recipe |
|---|---|
| Sheets | flat colour toned toward the night, hand-cut edge, fibre, a rim in the colour of the light they face |
| Lights | windows, signs and halos drawn with `lighter` compositing and a shadow blur in the light's colour |
| Medallion | zig-zag rings, bands of cells with a half-cell offset; each piece baked unlit and backlit, crossfaded as it locks; a dark lead disc behind |
| Figures | faceless capsule skeletons drawn live into their own canvas, rimmed by the light they face |
| Wet floor | the scene above the feet copied flipped and blurred 2 px, laid back in 6 px swaying strips, alpha 0.62(1 − d)^1.5 |
| Text | Playfair Display italic in cream over a dark pool gradient at the bottom (16:9) or at the top (9:16) |

## The diptych

For a saying about two ways, split one scene down a vertical axis instead of cutting between two places. Pair every
contrast: warm and neon light, still and restless motion, gathered and scattered pieces. Put the favoured side on the
right. A brand colour takes the warm role.

## Use it when

A short contrast or a saying (manual vs automatic, before and after, calm and noise); a night mood; a hook where the
hero object assembles.

## Do not use it when

The film is bright and daytime, needs product UI, or has no real contrast to split the frame on.

## Stills

The three stills come from the demo moves, so two of them share a scene. Replace them with frames from the first
real film in this style, and set `worked_example` then.
