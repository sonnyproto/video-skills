# Recipe: metric-sculpture

21.6 s · 1920×1080 · 30 fps · 112 BPM · one hit at 15.0. Source of truth: `project/tools/templates/` (`screen.html` for
0–8 s, `index.html` for the studio, `lockup.html`, `captions.html`). This file is their readable form.

## Energy

```
0          4.4       6.4     7.5  8.0         11.4        14.7 15.0           21.6
result     rewind +  time-   whip one plate   the feed    hit  verdict, lockup
(app)      request   lapse        (before)    (after)
4.4        2.0       1.1     0.5  3.4         3.3         0.3  6.6
```

Result first, then how it happened, then the number made physical. The film says the outcome in the first second and
spends the rest proving it twice: once as work in the app, once as an object you can count.

## Beats

| # | Start | Len | Where | What happens | Moves |
|---|---|---|---|---|---|
| 1 | 0.0 | 4.4 | app | Window rises (0.6 s expo.out) on the dark desktop; the result card; the metric tile counts up to `after` in steps of `unit` (0.4–1.65); the `×ratio` tag pops; camera pushes 1.45× onto the tile. The mascot is born from the logo mark (0.55) and jumps onto the tile, landing at about 1.6 on the voice's key word. Camera moves to the zero tile (2.45); it fades in, its 0 pops (3.25); the mascot jumps onto it and cheers (3.75) | living-screencast, count-up, mascot-born, mascot-jump |
| 2 | 4.4 | 2.0 | app | "◀◀ 60 days ago" tag; the card blurs out; the cursor clicks the input (4.92), the request is typed at 39 ms a key, "⏎ Return" HUD (5.95); the bubble flies from the input into the thread with the mascot riding it (6.02); the hero agent row goes active (6.3) | rewind-tag, typed-request, bubble-ride |
| 3 | 6.4 | 1.1 | app | "▶▶ Day 1 → Day N"; ten status rows tick in 0.11 s apart and scroll up; the mascot hops along them | time-lapse |
| 4 | 7.48 | 0.5 | app → studio | Whip left (0.42 s power3.in) with an 18 px blur; the studio is already there, camera travelling right | whip |
| 5 | 8.0 | 3.4 | studio | Empty walnut base with inlaid brass labels; the rule "1 PLATE = …" at the front edge (8.35); the `before` plate(s) fall with gravity and one damped bounce at 9.45; the reading pins to them (9.6) | plate-drop, pinned-reading |
| 6 | 11.4 | 3.3 | studio | The `after` plates are fed onto TODAY at T_i = 11.4 + 3.3 (i/(N−1))^0.62, accelerating; each drops 0.6 with quintic ease-out and a yaw that unwinds; every tenth is the second material. The camera cranes with the top; the reading rides the top and counts plates × unit | plate-feed, crane |
| 7 | 14.7 | 0.3 | studio | Suck-out: a short silence in the music | — |
| 8 | 15.0 | 6.6 | studio | Hit. The verdict (`metric.verdict`, 170 px, accent) upper left with its rule drawing in; pull back to the whole installation (to 16.0), then a slow creep. Lockup plate lower left from 15.8: logo, line 1 at 17.35, line 2 at 20.23 | verdict, pull-back, lockup |

The end camera is framed for 100 plates and scales with the tower (`KE` in `index.html`), so 20–150 plates still fit.

## Voice

ElevenLabs Brian through fal, five separate files, placed at fixed slots. Captions mirror lines 1–4 (two pill captions
bottom centre in the app, two lower-left captions in the studio); line 5 is carried by the lockup.

| Slot | Start | Max length | Example |
|---|---|---|---|
| vo0 | 0.40 | 4.4 s | "Our views just went up a hundred times. And we never hired a marketer." |
| vo1 | 4.90 | 2.9 s | "We used Votrix SEO." |
| vo2 | 7.90 | 3.2 s | "Sixty days ago: two thousand views a month." |
| vo3 | 11.12 | 2.9 s | "Today: two hundred thousand." |
| vo4 | 15.60 | 6.0 s | "Votrix SEO. Gets you found on Google and in ChatGPT. Free to start." |

Caption times (`captions.html`): 0.42–2.6, 2.68–4.45, 4.95–6.85, 8.1–10.95, 11.28–13.3.

## Sound

- Music at 0.3: 112 BPM; a light band with a chiptune lead for the app, a change to marimba/vibraphone at 7.5, a build by
  subdivision 11.5–14.7, silence at 14.7, one big hit at 15.0, a warm outro to 21. Prompt in `project/tools/music.md`.
- Foley (`tools/sfx.py`, synthesized, standard library only): 8-bit blips for the mascot (born, take-off, landing, cheer),
  click and keys for the request, a rewind sweep, ticks for the rows, a whoosh on the whip; in the studio a metal plate
  for `before`, one acrylic tok per plate (louder as the gaps shrink), a mallet note on every tenth plate climbing a
  pentatonic scale, and the impact at 15.0.
- Master to -14 LUFS, true peak under -1 dBTP (`tools/master.sh`).
