#!/usr/bin/env node
// Compares colour per region between a reference and a render: mean brightness and saturation
// on a grid (default 3x3), reference against render. Catches "too grey" or "too dark" before a person has to say it.
//
// Usage: node color-stats.mjs ref.png render.png [--grid 3] [--max 0.08]
// Exit code 1 when any cell differs by more than --max (0..1) in brightness or saturation.
// Needs ffmpeg on PATH. No other dependencies.

import { spawnSync } from 'node:child_process';

const args = process.argv.slice(2);
let grid = 3, max = 0.08;
const files = [];
for (let i = 0; i < args.length; i++) {
  if (args[i] === '--grid') grid = Number(args[++i]);
  else if (args[i] === '--max') max = Number(args[++i]);
  else files.push(args[i]);
}
if (files.length !== 2) {
  console.error('usage: node color-stats.mjs ref.png render.png [--grid 3] [--max 0.08]');
  process.exit(2);
}

const W = grid * 16, H = grid * 16;
function pixels(file) {
  const r = spawnSync('ffmpeg', ['-hide_banner', '-loglevel', 'error', '-i', file, '-vf', `scale=${W}:${H}`,
    '-frames:v', '1', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], { maxBuffer: 1 << 24 });
  if (r.status !== 0) { console.error(`ffmpeg failed on ${file}: ${r.stderr}`); process.exit(2); }
  return r.stdout;
}
function cells(buf) {
  const out = [];
  for (let gy = 0; gy < grid; gy++) for (let gx = 0; gx < grid; gx++) {
    let v = 0, s = 0, n = 0;
    for (let y = gy * 16; y < gy * 16 + 16; y++) for (let x = gx * 16; x < gx * 16 + 16; x++) {
      const i = (y * W + x) * 3, R = buf[i] / 255, G = buf[i + 1] / 255, B = buf[i + 2] / 255;
      const mx = Math.max(R, G, B), mn = Math.min(R, G, B);
      v += mx; s += mx ? (mx - mn) / mx : 0; n++;
    }
    out.push({ v: v / n, s: s / n });
  }
  return out;
}

const a = cells(pixels(files[0])), b = cells(pixels(files[1]));
let worst = 0, fails = 0;
const f = (x) => x.toFixed(2);
console.log(`cell  bright ref/render   sat ref/render   (max delta ${max})`);
a.forEach((c, i) => {
  const dv = b[i].v - c.v, ds = b[i].s - c.s;
  const bad = Math.abs(dv) > max || Math.abs(ds) > max;
  worst = Math.max(worst, Math.abs(dv), Math.abs(ds));
  if (bad) fails++;
  const tag = bad ? (ds < -max ? '  too grey' : ds > max ? '  too saturated' : dv < 0 ? '  too dark' : '  too bright') : '';
  console.log(`r${Math.floor(i / grid) + 1}c${(i % grid) + 1}  ${f(c.v)} / ${f(b[i].v)}        ${f(c.s)} / ${f(b[i].s)}${tag}`);
});
console.log(fails ? `FAIL: ${fails} of ${a.length} cells off, worst delta ${f(worst)}` : `PASS: worst delta ${f(worst)}`);
process.exit(fails ? 1 : 0);
