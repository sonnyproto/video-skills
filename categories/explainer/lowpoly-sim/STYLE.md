# Low-poly simulation

A flat-shaded low-poly world that a simulation pushes further and further. A person on a dusk city street, then the
rooftops, the planet, the solar system, the galaxy. A large counter of a real quantity climbs the whole time. It is
built live in three.js inside a HyperFrames composition: no model files, no generated media, about 40 s to render
60 s of 1080×1920 on a laptop.

## How it is wired

- `index.html` holds only the canvas, the text layers (question, counter, captions), the GSAP timeline and `<audio>`.
  Everything 3D lives in one `assets/scene.js`.
- `scene.js` is a pure function of film time. `renderAt(t)` runs on every `hf-seek`:
  `window.addEventListener("hf-seek", e => renderAt(e.detail.time))`.
  - It keeps no state between frames.
  - It sets every object's `visible` each frame, so nothing leaks from one scene into the next.
  - All randomness comes from one seeded generator (a Park-Miller `seed * 16807 % 2147483647`), never `Math.random()`.
- Renderer: `antialias: true`, `preserveDrawingBuffer: true`, `ACESFilmicToneMapping` at exposure 1.0,
  `PCFSoftShadowMap`.

## The simulation clock

The premise runs in simulated time and the film compresses it. A table of `[film_s, sim_s]` pairs maps one to the
other piecewise linearly; `simS(t)` goes one way and `tOf(s)` the other. The counter label shows sim time
(`QUANTITY · T+12.34 S`), so the speed-up is honest. Place every caption, sound and hit at `tOf(milestone)`. The
counter's value is computed from `simS(t)` every frame, never typed in.

Big numbers: write `m × 10<sup>e</sup>` in HTML. Unicode superscripts mix two glyph sets, and ¹²³ come out larger
than the rest. Carry a mantissa that rounds to 10.0 into the exponent.

## How each element is made

| Element | Recipe |
|---|---|
| Material | `new MeshStandardMaterial({ color, roughness: 0.95, flatShading: true })` for everything solid |
| Sky | a 4×512 canvas gradient `#5d4a68 → #9c7f93 → #d6aaa6 → #e9c4b2` on a back-faced sphere (`fog: false`), a soft sun sprite near the horizon |
| Fog | `THREE.Fog(#c9a3a8, 45, 300)`; open `near` and `far` as the camera rises (to 600 / 2600) |
| Light | `HemisphereLight(#f2d2d0, #4a3a48, 1.1)`, key `DirectionalLight(#ffd9c4, 1.5)` low behind the scene with soft shadows, fill `#f0c8cc` at 0.9 from the camera side |
| Buildings | boxes with a canvas window grid (16×20 px cells, 12 % lit `#f6dcb0`, `NearestFilter`) on the sides and a flat top; the far city is one `InstancedMesh` of boxes |
| Street | dark road, dashed centre line, low-poly trees (an icosphere canopy on a cylinder), lamp posts, boxy cars in five muted colours |
| Person | cylinders and boxes (shoes, legs, hoodie, arms), an icosphere head and hair, seen from behind; built by one function so the same rig appears in every scene |
| Smoke and gas | an `InstancedMesh` of `IcosahedronGeometry(1, 1)` puffs with `setColorAt`. Each puff has a direction, speed and size: it bursts out with ease-out, rolls, drifts and fades. Keep the cloud radius well under the camera distance or it fills the frame |
| Mushroom cloud | the same puffs placed as a rolling torus (cap), a cap top, a stem and a ground skirt. Colour lerps hot `#ffb070` → cool by height over about 1 s, with an additive glowing core inside the cap |
| Planet | an icosphere at detail 18. Faces are grouped by nearest of about 60 random seeds into chunks that can fly apart. Colours come from a 3-octave noise (seas from shallow to deep, grass, desert, ice at the poles), and vertices are pushed out by `1 + max(0, n - 0.53) * 0.12` for relief. A thin transparent atmosphere shell sits on top |
| Star | the same chunked sphere with `emissive` warm orange, a large additive halo sprite |
| Galaxy | about 40k points in two spiral arms (angle = arm·π + 0.055·r, wider jitter near the core), `vertexColors`, additive blending, a glow sprite at the core |
| Flash | a full-frame `#fff8ef` div whose opacity rises over 0.06-0.3 s and falls over 0.45-1.0 s, placed on every scene cut |
| Text | as in `look.type`: the question top third, the counter on the left at 57 % height, captions at 81 % in a `rgba(20,12,22,.55)` box with 14 px radius |

## Feedback on every event

Every repeated event in the premise (a step, a pulse, a doubling) gets its own visible hit. Scale each hit with the
quantity:

- `env = exp(-9 * dt)`, where `dt` is the time since the event.
- The object pops by `1 + (0.35 + 0.9g) · env`, where `g` runs from 0 to 1.
- The figure is shoved `sin(min(16·dt, π)) · (0.05 + 0.28g)` and settles back.
- A ground ring (additive, `fog: false`) spreads in 0.45 s.
- The camera nudges and the counter scales by 1.08-1.22.

Once events come faster than about two a second, keep them in the sound and move the big visual hits to the
milestones.

## Use it when

The premise is a quantity that grows past human scale: energy, speed, population, distance, time. Also a what-if
told through a real number at each step, or anything that should travel from a street to space in one film.

## Do not use it when

The film needs real people, product UI or real places that viewers must recognise. Also when it needs photoreal
material or warmth from footage, or has no number to count.

## Stills

1. A type frame: the question, a counter label and value, a caption over a planet.
2. A wide: the city from above with long dusk shadows.
3. Space: the galaxy with its glowing core.

They are rendered from the scene code, not taken from a finished film in this repo, so `worked_example` is empty.
