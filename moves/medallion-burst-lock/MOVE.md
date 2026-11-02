# Medallion burst and lock

A hook that assembles the hero object. 336 inlay pieces (bands of 16, 32, 56, 96, 136 cells between zig-zag rings,
a half-cell offset every other band) burst out to five spiral arms in 0.5 s, then ease home. Each piece locks with an
ease-out-back at a time staggered by radius, then angle (inner rings first, 1.3 to 3.55 s), and crossfades from its
unlit bake to its backlit bake as it locks: warm on the right, neon on the left. Big blurred pieces fly past the lens
in screen space during the first second; the camera pulls back from 1.22 to 1 as the pieces come home.

## Closed form

Every piece's position is a function of t alone: burst radius `(r·1.15 + 150 + jitter)·(1 − e^(−4t/0.5))`, pulled
80 % of the way to its arm angle plus a spin that grows with radius, mixed toward home by a smoothstep. Fast pieces
draw two fading copies at t − 0.025 and t − 0.05.

## Use it when

A logo, a seal or a badge needs an entrance; an outro that gathers "many into one"; a saying about two halves.

## Do not use it when

The mark must stay exact (the pieces are a pattern, not the client's logo), or the frame is busy.

## Pitfalls

- The leading is a dark disc behind the pieces that fades in as they lock; without it the medallion reads as a
  candy wheel.
- Keep one colour family dominant (here gold, three pieces in six on the warm side), or it turns into a rainbow.
- Pulling pieces fully onto the arm angle makes one clump per ring; spread them along the arm.
