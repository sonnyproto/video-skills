# Reference

**What it reproduces:** our own film "100×" for Votrix AI (2026-10-30, 21.6 s), turned into a generator. It is the
example film in `result/result.mp4`, so the reference and the result are the same film.

**Where the grammar comes from:** two styles from lemomo-ai/lemo-opuscar (MIT), used as written descriptions only, no
code: *Living Screencast* (`styles/living-screencast/STYLE.md`, a real app redrawn with a character that acts out the
work) for 0–7.9 s, and *Data Physicalization* (`styles/data-physical/STYLE.md`, data as physical objects in a lit
studio) for 7.4–21.6 s. Joining them with one whip is this film's own idea.

**The example product** is Votrix AI. The metric (monthly views 2,000 → 200,000 in 60 days, no marketer hired) came from
the Votrix team on 2026-10-31; the app labels, agent names and roles, and "Free to start" from votrixai.com the same day.
The three time-lapse rows are the site's own demo lines for its SEO agent, shown as a time-lapse.

## Measured (result/result.mp4)

See `result/metrics.json`. 21.6 s, 30 fps, -14 LUFS integrated, true peak under -1 dBTP.

## Why it works

- The outcome is the first sentence and the first picture; everything after is proof.
- The proof is shown twice, in two languages: as work (the request, the agent going active, sixty days of rows) and as
  quantity (a hundred plates you can count, one unit each).
- The number is earned on screen: the counter only moves when a plate lands, so the viewer watches it being built.
- Acceleration carries the second half: the feed gets faster, the toks get louder and closer, the mallet climbs, then a
  beat of silence and the hit.
- The mascot gives a flat UI a body, so a 7 s screencast reads as a scene rather than a demo.

## Known and kept

- `hyperframes check` warns that the time-lapse rows are on screen under 1 s and that some app labels are under 28 px:
  they are the app's own UI scale and a deliberate 60-day time-lapse.
- It also warns that "Free to start." holds 1.3 s before the end; the voice says it at the same moment.
- Loudest stretch is the feed (11–15 s, about -12.5 LUFS short-term), the outro about -20.
