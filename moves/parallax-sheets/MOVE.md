# Parallax sheets

Depth without 3D. Each sheet has a depth p (sky 0.12, hills 0.35, far houses 0.6, near houses 0.85, the subject 1,
foreground 1.35). The camera's zoom applies as `zoom^p` around a centre that moves p times as far as the camera, so one
slow push-in (1 to 1.14 over 6 s) slides the sheets past each other.

## How it is made

- Every piece is a baked sprite from the paper kit at the top of the script: a hand-cut edge (subdivided every
  ~12 px, pushed ±1 px along the normal), paper fibre laid on with soft-light, a rim of light on the edge that faces
  the light, and a blurred silhouette for the contact shadow, offset in world space.
- The walker steps on the stop-motion clock (15 poses a second) while the camera moves every frame. Boil (±1 px,
  ±0.003 rad) and exposure flicker (±2.5 %) are re-rolled per pose.
- Four values carry the palette: a mid-value ground, one accent kept for the subject, a cream for small lights, an
  ink for the smallest details. Shades mix toward the ink or the cream, never toward black or white.

## Use it when

An establishing shot for a small story: a street, a shop, a town the product lives in. The push gives life to an
otherwise still frame under a voiceover.

## Do not use it when

The film shows product UI (paper fights screens), or the scene needs more than one thing moving the eye.

## Pitfalls

- Run each wall down past the ground line, or its base shows when the sheets slide.
- Keep the accent for one thing. With red roofs and a red coat, nothing reads first.
- Bake sprites at the largest zoom they are seen at.
