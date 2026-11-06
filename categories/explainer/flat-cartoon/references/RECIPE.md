# Recipe

A 24 s idea explainer: one claim, four beats, a cartoon character acting each beat out. Everything you see is generated;
the craft is in the order of the beats, one narration line per shot, and captions that change where the voice pauses.

## Beat by beat

| Time | Shot | Line (example) | What the shot shows |
|---|---|---|---|
| 0-6 | 1 | A math problem has a right answer. An AI can try a million times and learn from every miss. | the character at a chalkboard; every attempt gets a check or a cross |
| 6-12 | 2 | But a painting? There's no answer key. Score it an 8, and it still doesn't know what to fix. | the character paints; judges hold up identical scores; it looks lost |
| 12-18 | 3 | So it piles on every pretty trick it knows. Nothing wrong with it. Nothing you'd watch twice. | the canvas buried in glitter and ribbons; the audience yawns |
| 18-24 | 4 | AI makes making things cheap. What's scarce now is knowing what to keep, and what to throw away. | a machine prints hundreds of cards; one hand keeps one; the rest dissolve |

The shape: **easy case → hard case → what goes wrong → what that means for you.** Shot 1 sets up a rule the viewer
can see (a check mark), shot 2 breaks it, shot 3 shows the result as a joke, shot 4 lands on a person.

## Rules this film keeps

- One line of narration per shot, 15-17 words, read in 5-6 s. The line starts 0.3 s into its shot.
- Two shots per generated clip, cut in the middle of the clip, so a 24 s film needs two generations.
- Captions always on, one sentence at a time, switching where the narration pauses (`tools/voice.py` prints the pauses).
- The clips' own sound sits at 28 % under the voice. No music: the clip sound carries the gaps.
- -14 LUFS target, true peak under -1.5 dBTP (`tools/build.py` normalises the mix).

## What the example got wrong (fix it in your film)

The example's script was rejected by the person it was made for. Keep the structure; write the words better:

- **Every "so" must be a real cause.** Line 3 says "so it piles on" right after "it doesn't know what to fix". That
  is not why it piles on. Say the actual mechanism in plain words.
- **No clipped triples or slogans.** "Nothing wrong with it. Nothing you'd watch twice." and "AI makes making things
  cheap" are filler that sounds clever. A ten-year-old should understand every line on first hearing.
- **Open with a question or a contrast the viewer cares about**, not a flat statement ("AI keeps getting better at
  math and code. But not at writing. Why?").
- **End on something the viewer can do**, not on a general truth.
- **Show the script before spending.** Generation cannot be cancelled once it runs; get the words approved first.
