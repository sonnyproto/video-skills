# Recipe

The film, beat by beat. The shape is what you keep; the story is what you swap (`SWAP.md`).

| Time | Scene | What happens | Move | Sound |
|---|---|---|---|---|
| 0.0 | space | The question is already on screen (frame 0 is the thumbnail). Key light left, planet right, moon, nebula | title settles 1.04 → 1; camera push 1 → 1.06 over the shot | pad |
| 1.0 | space | Labels pop: star, planet | label pop, 0.1 s stagger | |
| 1.6 | space | A dashed line draws from light to planet; the distance label pops | scaleX 0 → 1, 0.6 s | |
| 2.75 | space | The event: the light swells (anticipation) | scale 1 → 1.12, 0.4 s | riser |
| 3.15 | space | ...and collapses; halos, rays and dust fade; flash bloom at 3.45 | back.in(2.2), 0.3 s | thump, crack |
| 3.5 | space | The twist: the planet stays lit. A glowing front keeps travelling along the line with the travel-time label | linear, 1.9 s | shimmer |
| 5.4 | ground | Hard cut to a dusk hilltop: three generated plates, code sky, low key light, character watching it | parallax plates, camera push 1 → 1.08 | pad, warmer |
| 5.6 | ground | Caption line 1 | fade-up 0.6 s | |
| 6.9 | ground | The light goes out: glow shrinks, sky crossfades to night, plates darken far-first, warm rims die, cool rim appears, stars and nebula come in | 0.8-1.6 s eases, staggered | wind |
| 7.15 | ground | Caption line 2 | fade-up 0.45 s | |
| 7.4 | ground | The character's take: squash, stretch, head up, brows up, mouth O, arms out (left first) | elastic settle | pop |
| 8.6 | ground | The consequence, without words: frost sparkles on the ground, two breath puffs, a shiver, arms in | back.out pops, 0.05 s shiver | tinkles, breath |
| 9.5-10 | ground | Hold the reaction; one blink | | |

## Known weak point

The generated plates are lit by a warm sunset from the left. After the light goes out the plates are darkened by filter,
but their baked warm rim (the big tree's orange edge) is still faintly visible. Fix for the next film: generate a night
version of each plate from the day plate as reference ("same scene, same composition, no warm light, cool moonlight from
the right") and crossfade it in at 6.9 s. The character rig is also plainer than the plates; give it more shadow shapes
(cloth folds, hair highlight) before a long film.
