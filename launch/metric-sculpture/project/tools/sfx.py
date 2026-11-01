"""Synthesize the film's foley into one track, from the same times the scenes use.

    python3 tools/sfx.py        -> assets/audio/sfx.wav

Screencast: 8-bit mascot blips, keys, clicks, pops, whooshes. Studio: a metal plate, one acrylic tok per plate, a mallet note on
every 10th (brass) plate climbing a pentatonic scale, and the impact at 15.0. Standard library only.
"""
import json
import math
import random
import wave
from array import array
from pathlib import Path

FILM = json.loads((Path(__file__).resolve().parent.parent / "film.json").read_text())
SR, LEN = 44100, 21.6
buf = [0.0] * int(SR * LEN)
rng = random.Random(20261031)


def add(t, dur, fn, amp=1.0):
    i0 = int(t * SR)
    for k in range(int(dur * SR)):
        if 0 <= i0 + k < len(buf):
            buf[i0 + k] += amp * fn(k / SR)


def square(f):
    return 1.0 if math.sin(2 * math.pi * f) >= 0 else -1.0


def blip(t, f0, f1, dur, amp=0.18):
    ph = [0.0]
    def fn(x):
        f = f0 + (f1 - f0) * x / dur
        ph[0] += f / SR
        return square(ph[0]) * (1 - x / dur)
    add(t, dur, fn, amp)


def noise_sweep(t, dur, rise=True, amp=0.3):
    lp = [0.0]
    def fn(x):
        u = x / dur
        a = (u if rise else 1 - u)
        c = 0.02 + 0.5 * a
        lp[0] += c * (rng.uniform(-1, 1) - lp[0])
        return lp[0] * math.sin(math.pi * u) * 2
    add(t, dur, fn, amp)


def click(t, amp=0.35):
    add(t, 0.006, lambda x: rng.uniform(-1, 1) * (1 - x / 0.006), amp)
    add(t, 0.03, lambda x: math.sin(2 * math.pi * 180 * x) * math.exp(-x * 120), amp * 0.6)


def key(t, amp=0.22):
    add(t, 0.004, lambda x: rng.uniform(-1, 1), amp * 0.8)
    add(t, 0.05, lambda x: math.sin(2 * math.pi * (140 + rng.uniform(-8, 8)) * x) * math.exp(-x * 70), amp)


def pop(t, f=900, amp=0.25):
    add(t, 0.09, lambda x: math.sin(2 * math.pi * f * x * (1 + 2 * x)) * math.exp(-x * 45), amp)


def tick(t, f=2200, amp=0.08):
    add(t, 0.03, lambda x: math.sin(2 * math.pi * f * x) * math.exp(-x * 160), amp)


def metal(t, amp=0.5):
    parts = [(3150, 1.0), (4420, 0.7), (5870, 0.5), (7300, 0.35)]
    add(t, 0.7, lambda x: sum(a * math.sin(2 * math.pi * f * x) for f, a in parts) / 2.5 * math.exp(-x * 7), amp)
    add(t, 0.2, lambda x: math.sin(2 * math.pi * 90 * x) * math.exp(-x * 22), amp * 1.2)


def tok(t, amp):
    f = 1400 + rng.uniform(-250, 450)
    add(t, 0.06, lambda x: (math.sin(2 * math.pi * f * x) + 0.4 * math.sin(2 * math.pi * f * 2.3 * x)) * math.exp(-x * 75), amp)


def mallet(t, f, amp=0.22):
    add(t, 0.9, lambda x: (math.sin(2 * math.pi * f * x) + 0.25 * math.sin(2 * math.pi * f * 4 * x) * math.exp(-x * 30)) * math.exp(-x * 5), amp)


def impact(t):
    ph = [0.0]
    def punch(x):
        f = 120 - 60 * min(1, x / 0.25)
        ph[0] += f / SR
        return math.sin(2 * math.pi * ph[0]) * math.exp(-x * 5)
    add(t, 0.9, punch, 0.8)
    add(t, 0.08, lambda x: rng.uniform(-1, 1) * (1 - x / 0.08), 0.25)
    add(t, 2.4, lambda x: (math.sin(2 * math.pi * 1318.5 * x) + 0.5 * math.sin(2 * math.pi * 2637 * x)) * math.exp(-x * 1.8), 0.16)


# ---- screencast (times match tools/templates/screen.html) ----
blip(0.55, 400, 900, 0.08)                         # born from the logo
for at, d in [(1.0, 0.5), (2.95, 0.44), (6.5, 0.3)]:
    blip(at + 0.08, 300, 700, 0.12)                # take-off
    blip(at + 0.1 + d, 180, 90, 0.07, 0.2)          # landing
pop(1.65, 950); pop(3.25, 820)
for k, f in enumerate([1046.5, 1318.5, 1568.0]):    # cheer
    blip(3.75 + k * 0.07, f, f, 0.06, 0.12)
noise_sweep(4.38, 0.35, rise=False, amp=0.25)       # rewind
click(4.92)
for i in range(1, len(FILM["app"]["request"]) + 1):
    key(5.02 + i * 0.039 + rng.uniform(-0.008, 0.008))
key(5.97, 0.32)                                     # Return
noise_sweep(6.0, 0.3, amp=0.18)                     # send
for i in range(10):
    tick(6.45 + i * 0.11)
noise_sweep(7.45, 0.45, amp=0.45)                   # whip

# ---- studio (times match tools/templates/index.html) ----
metal(9.45)
N = round(FILM["metric"]["after"] / FILM["metric"]["unit"])
FEED0, FEED, POW = 11.4, 3.3, 0.62
T = [FEED0 + FEED * (i / (N - 1)) ** POW for i in range(N)]
SCALE = [523.25, 587.33, 659.25, 783.99, 880.0, 1046.5, 1174.66, 1318.5, 1567.98, 1760.0]
for i, t in enumerate(T):
    gap = (T[i + 1] - t) if i + 1 < N else 0.05
    tok(t, 0.1 + 0.3 * min(1, gap / 0.1) ** 0.5)
    if (i + 1) % 10 == 0:
        mallet(t, SCALE[((i + 1) // 10 - 1) % len(SCALE)])
impact(15.0)

peak = max(abs(v) for v in buf) or 1
out = array("h", (int(max(-1, min(1, v / peak * 0.9)) * 32767) for v in buf))
p = Path(__file__).resolve().parent.parent / "assets/audio/sfx.wav"
with wave.open(str(p), "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(out.tobytes())
print(p, f"peak {peak:.2f}")
