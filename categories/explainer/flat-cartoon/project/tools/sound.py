"""Synthesise the film's sound (no samples, no keys): a pad, a riser into the Sun's collapse, a thump, a shimmer for
the travelling light, night wind, a pop on the character's take, breath puffs and frost tinkles.
Times follow the scene timing in tools/templates/. Usage, from project/:
  python3 tools/sound.py /tmp/raw.wav && ffmpeg -y -i /tmp/raw.wav -af loudnorm=I=-14:TP=-1.5:LRA=7 -ar 48000 -b:a 192k assets/audio/sound.mp3"""
import math, random, struct, sys, wave

SR, DUR = 48000, 10.0
N = int(SR * DUR)
L = [0.0] * N; R = [0.0] * N
rnd = random.Random(7)

def add(t0, t1, fn, pan=0.0, gain=1.0):
    a, b = int(t0 * SR), min(N, int(t1 * SR))
    gl, gr = gain * (1 - max(0, pan)), gain * (1 + min(0, pan))
    for i in range(a, b):
        v = fn(i / SR - t0, t1 - t0)
        L[i] += v * gl; R[i] += v * gr

def env(t, d, a=0.02, r=0.2):
    return min(1.0, t / a if a else 1.0) * min(1.0, (d - t) / r if r else 1.0)

class Noise:  # one-pole low-passed noise
    def __init__(self, k): self.k, self.y = k, 0.0
    def __call__(self):
        self.y += self.k * (rnd.uniform(-1, 1) - self.y); return self.y

# pad: space (A minor-ish), dims after the collapse, warmer and lower on the ground
for f, g in [(110, 0.06), (164.8, 0.045), (220, 0.035), (329.6, 0.02)]:
    add(0, 5.4, lambda t, d, f=f: math.sin(2 * math.pi * f * t) * (0.75 + 0.25 * math.sin(2 * math.pi * 0.3 * t)) * env(t, d, 0.6, 0.5) * (1 if t < 3.4 else 0.55), gain=g)
for f, g in [(98, 0.05), (146.8, 0.04), (196, 0.03)]:
    add(5.4, 10.0, lambda t, d, f=f: math.sin(2 * math.pi * f * t) * env(t, d, 0.3, 0.8) * (1 if t < 1.5 else max(0.45, 1 - (t - 1.5))), gain=g)
# riser into the swell (2.75-3.45)
nz = Noise(0.25)
add(2.6, 3.45, lambda t, d: (math.sin(2 * math.pi * (180 * t + 500 * t * t)) * 0.5 + nz() * 0.8) * (t / d) ** 2, gain=0.22)
# thump + crack at the collapse / flash (3.45)
add(3.45, 4.6, lambda t, d: math.sin(2 * math.pi * (70 - 30 * t) * t) * math.exp(-t * 4.5), gain=0.55)
nz2 = Noise(0.6)
add(3.45, 3.75, lambda t, d: nz2() * math.exp(-t * 18), gain=0.35)
# shimmer for the travelling light (3.5-5.4)
add(3.55, 5.4, lambda t, d: (math.sin(2 * math.pi * 1760 * t) + 0.5 * math.sin(2 * math.pi * 2637 * t)) * (0.5 + 0.5 * math.sin(2 * math.pi * 6 * t)) * env(t, d, 0.3, 0.5), pan=0.3, gain=0.025)
# night wind (ground scene, light dies at 6.9)
nw = Noise(0.02)
add(6.7, 10.0, lambda t, d: nw() * (0.6 + 0.4 * math.sin(2 * math.pi * 0.4 * t)) * env(t, d, 0.9, 0.6), gain=0.9)
# pop on the take (7.4)
add(7.42, 7.7, lambda t, d: math.sin(2 * math.pi * (380 + 900 * t) * t) * math.exp(-t * 16), gain=0.3)
# breath puffs (8.7, 8.78, 9.55)
for t0 in (8.7, 8.78, 9.55):
    nb = Noise(0.12)
    add(t0, t0 + 0.6, lambda t, d, nb=nb: nb() * math.sin(math.pi * t / d), pan=-0.2, gain=0.5)
# frost tinkles (8.6-9.4)
for k in range(9):
    t0, f = 8.6 + k * 0.09, rnd.choice([2093, 2349, 2637, 3136, 3520])
    add(t0, t0 + 0.4, lambda t, d, f=f: math.sin(2 * math.pi * f * t) * math.exp(-t * 12), pan=rnd.uniform(-0.6, 0.6), gain=0.05)

peak = max(max(abs(x) for x in L), max(abs(x) for x in R)) or 1.0
with wave.open(sys.argv[1], "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes(b"".join(struct.pack("<hh", int(l / peak * 0.8 * 32767), int(r / peak * 0.8 * 32767)) for l, r in zip(L, R)))
print("wrote", sys.argv[1])
