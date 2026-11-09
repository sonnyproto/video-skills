# Flat cartoon

A flat-vector science-explainer look: saturated colour on deep violet grounds, one glowing key light, layered cel shading
with rim light, a little grain. Image-model plates supply the illustration detail of the scenery; code supplies
everything that has to move, change light or stay identical across shots.

Derived from studying the general look of flat-vector science channels (90 frames from three films, palette extraction,
cut detection); no frame, character or scene of any reference is used or redrawn.

## How each element is made

| Element | Recipe |
|---|---|
| Ground | vertical gradient, never black: `#0a0628` top → `#1d1160` → `#5a2177` bottom (space); dusk `#1d1160 → #5a2177 → #c2477a → #ff7a45 → #ffd27a` |
| Key light | one per scene, usually in frame. White-hot core (`#fff6d6`) → saturated colour → 2-3 blurred halo circles (`feGaussianBlur` 40-80, opacity 0.15-0.55), soft ray wedges (radial-gradient fill, blur 14), drifting dust particles |
| Shading (code objects) | four layers: base; shadow = the same shape shifted away from the light and clipped by the original (a crescent), hue +15° toward violet, value -25 %; highlight = blurred lighter blob on the lit side; rim = 4-8 px warm stroke on the lit edge. Cast shadows: flat darker ground colour, slightly blurred |
| Scenery | generated plates, one per depth (far / mid / near), transparent above the ridge, lit from the same side as the code key light. Prompts in `project/tools/layers.md`. Far is hazy and low-contrast, near is saturated |
| Night / light change | per-layer CSS `filter: brightness() saturate()` on the plates (far darkest), code sky crossfades to a night gradient, warm rims fade and a cool `#9ab8ff` rim appears on the character |
| Character | an original SVG rig (head, brows, eyes, pupils, mouth states, arms, hoodie) with the same four shading layers. Acting: anticipation squash → stretch → elastic settle; head leads, arms follow, never both arms at once |
| Stars | seeded dots 0.5-3 px, tinted white / lavender / ice / cream, a few 4-point sparkles, some twinkle on finite repeats |
| Texture | animated grain (`feTurbulence` seed tweened, opacity 0.06, overlay) and a violet vignette on every frame |
| Labels | pill tags, saturated fill, white Nunito 800, ≥ 30 px, pop in `scale 0 → 1` with `back.out(1.8)` |
| Titles | Montserrat 800, `#f7f3ff`, one accent word in the key-light colour |
| Sound | synthesised (`tools/sound.py`): pad, riser into the event, thump, shimmer, wind, pop, breath, tinkles; -14 LUFS |

## Use it when

A fact, a scale, a mechanism or a what-if that one light, a few objects and one reacting character can carry: science
explainers, social posts, intros.

## Do not use it when

The film needs real people, real places, product UI, or a look that must match a client's existing illustration.

## Banned

Pure black, neutral grey, black outlines; hard-edged concentric halos; rectangular darkening overlays (darken by shape or
filter); flat objects with no shadow layer; a frame that holds still for more than 1 s; paragraphs of on-screen text;
a generated plate with characters or text in it; baked warm light left on after the light goes out (see RECIPE "Known
weak point"); anything taken from an existing channel.

## Stills

1. A wide at dusk: three generated layers, the code sky and key light, the character, a caption.
2. A close-up at night: the character's take, cool rim, frost on the ground.
3. A frame with type: the code space scene with labels and the distance line.
