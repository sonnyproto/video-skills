# Swap in another product

The shortest path to the same film for a different product. Everything you change is in `project/film.json`,
`project/assets/` and the voice and music files. Nothing in `tools/build.py` or `tools/templates/` changes, unless the
product's app is laid out differently (§2).

## 1. Get the number

One metric with a before, an after and a period, from the person who owns it, with a source you can put on screen
("Source: <product>'s own monthly views"). Pick `unit` so that `after / unit` is 20–150 plates and `before / unit` is
1–5. A ratio over 150× does not fit as plates of one size: show a shorter period, or a different metric. Never round a
number up to make it fit.

## 2. Redraw the app

`screen.html` is a generic AI-team chat app: a sidebar (traffic lights, logo mark + name, three nav items, a team list,
the workspace), a header with a title and a status pill, a thread, and an input box. Fill it from the product's real app:
labels, agent names and roles, portraits, colours. If the real app looks different (top nav, no sidebar), rebuild the
markup and CSS in `tools/templates/screen.html` from screenshots, and keep these ids, which the choreography measures:
`#mark`, `#tile1`, `#tile3`, `#views`, `#x100`, `#zero`, `#report`, `#card`, `#input`, `#ph`, `#typed`, `#caret`,
`#send`, `#bubble`, `#rows`, `#t1`–`#t3`, `#p1`, `#p2`, `#on-<hero>`, `#st-<hero>`.

## 3. Fill the slots

| Slot (`film.json`) | What it must be | Used in |
|---|---|---|
| `brand.name`, `brand.logo`, `brand.mark`, `brand.workspace_initials` | product name; full logo (dark on light) for the lockup; the square mark for the sidebar | app, lockup |
| `metric.name`, `unit`, `before`, `after`, `days`, `per` | the metric's own name, the plate unit, the two values, the period in days, the unit line ("views / month") | result card, plates, readings |
| `metric.before_label`, `after_label`, `before_tile` | brass inlays on the base (caps); the tile and rewind label ("60 days ago") | studio, app |
| `metric.rule`, `verdict`, `verdict_line`, `zero_label`, `source` | "1 PLATE = …"; the hit ("100×"); one line under it; the "0" tile's label (what was not needed); the source line | studio, app |
| `app.*` | every label as the real app shows it; `agents` 2-5 with portrait; `hero_agent` the one who did the work; `request` typed into the input; `task_title` the thread title; `rows` 1-3 status lines for the time-lapse | app |
| `palette` | the app's own colours (`sidebar`, `main`, `line`, `ink`, `muted`, `brand`, `active`), the desktop `wall`, one `accent`, the studio `sweep` and three plate materials | everywhere |
| `mascot` | a **new** pixel character for every film: 14 × 12 grids for `stand`, `tuck`, `cheer`, in one colour no UI uses | app |
| `captions` | five lines: two `a` (pill, app), one `a`, two `b` (studio); the voice lines 1–4 word for word | captions |
| `lockup` | two lines: what it does, and the call to action | end |
| `voice.lines`, `voice.durations` | the five lines and the length of each rendered file (see slot maxima in RECIPE.md) | audio |
| `music` | a new track for this film, 21 s, same structure (`tools/music.md`) | audio |

## 4. Voice, music, build and look

```bash
# one file per line; voice.py writes assets/audio/vo.mp3 + words.json, then cut it into vo0..vo4 at the sentence starts
python3 tools/voice.py script.txt --voice Brian
python3 tools/fal.py fal-ai/elevenlabs/music '{"prompt":"<see tools/music.md>","music_length_ms":21000}' assets/audio/music-raw
python3 tools/build.py && python3 tools/sfx.py
npx --yes hyperframes@0.8.191 snapshot --at 0.3,1.7,3.8,5.5,6.2,7.0,7.7,8.6,9.8,12.5,14.6,15.4,17.0,19.5 -o snapshots .
```

Cut voice lines with `atrim`, not output-side seeking with a fade: the example's first cut faded four lines to silence.
After the render, check every line in the voice band of the final mix.

Check in the frames: the mascot lands on the tile on the key word and stands on edges, never floating; the typed request
fits the input; the bubble is not clipped; every plate renders (the instanced plates need `frustumCulled = false`); the
readings stay inside x ≥ 420, y ≤ 740 and clear of the captions; the counter only shows multiples of `unit`; the end
shot shows the whole tower with room above it; the verdict does not cover the tower.

## What never changes

Result first; one whip from the app to the studio and no way back; the mascot acting out the work; plates of one unit,
fed accelerating, counted by landing; every tenth plate in a second material with a rising mallet note; the hit at 15.0
with the verdict; the source line on screen; the lockup lower left on a paper plate.
