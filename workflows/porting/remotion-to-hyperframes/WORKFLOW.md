# Remotion to HyperFrames

Port a Remotion component to a HyperFrames composition so that it renders the same video, frame for frame, and prove it.
Used to port 12 video-shotcraft shot recipes (Apache-2.0), all at SSIM 0.93–0.98 against the author's previews.

## Why it works

A Remotion component is a pure function of the frame number. Keep that function as `render(f)`, build the DOM once,
and drive it from one linear GSAP tween whose `onUpdate` passes the frame. Eases, springs and seeded randomness port
line for line, so timing matches exactly.

```js
const drive = (tl, durFrames, render) => {
  const p = { f: 0 };
  render(0);
  tl.to(p, { f: durFrames, duration: durFrames / 30, ease: 'none', onUpdate: () => render(p.f) }, 0);
};
```

## Steps

1. **Port shared helpers once** (bezier eases, `interpolate`, Remotion's `spring` at 30 fps, seeded random) into one
   runtime file; each component then ports only its own file.
2. **Port the component** as `render(f)`: same constants, same frame math. React elements become DOM built once;
   per-frame props become style writes.
3. **Swap what you may not ship:** the author's brand → neutral placeholder; system fonts → bundled fonts; note every
   change in the file header.
4. **Render in isolation** (`scripts/iso.sh <id> <seconds>`): a throwaway copy of the project with only this
   composition, so several ports can render at once.
5. **Compare** (`scripts/compare.sh ref.mp4 port.mp4 sheet.jpg "frames"`): frame counts, SSIM per frame, and a sheet
   with the original on top. Look at the sheet, not only the number.
6. **Check** with `npx hyperframes check`; fix what the port introduced, explain what the original carries.

## Pass marks

| Step | Pass |
|---|---|
| 5 | same frame count, SSIM mean ≥ 0.93 (grey, every frame), no visible difference in the sheet except the listed swaps |
| 6 | no errors introduced by the port |

## Cost

15–30 minutes of one agent per component; a render takes under 10 s. A batch of 120 is a multi-agent job: port one
or two first, and port the rest only when a film needs them.
