# Voiceover, then music

For any narrated film. The voice sets the timing of everything; the music is made for the finished voice, never
looped or faded to fit.

## Steps

1. **Script at the target pace.** Count words: a launch voice runs about 3.2 words a second (measured on
   @shipper_now films). Film length × 3.2 ≈ word budget, leaving ~2.5 s for the end card. Cut words, not speed.
2. **One continuous read.** Generate the whole script in one call (speed 1.0–1.06), with word timestamps. Shape pauses
   with punctuation (comma, full stop, "...") instead of cutting audio afterwards.
3. **Pick the voice by ear.** Generate the same script with 2–3 voices; compare pace (words/s), length and pauses.
   A person chooses.
4. **Only light edits.** If a pause is too long (> 0.5 s), shorten it to 0.25–0.35 s at the quietest point with a 20 ms
   crossfade, keeping the room tone. Never splice sentences into digital silence.
5. **Lock it.** Write sentence start times into the spec; every scene and on-screen word is timed to them.
6. **Music for this length.** Generate music after the lock, with sections sized to the film (intro, build, drop, end)
   and an ending that lands on the last frame. If the generator cannot take a duration plan, generate long and
   cut on a bar line so the natural ending falls on the last frame.
7. **Mix.** Music around 0.2–0.3 under the voice, ducked while the voice speaks; sound effects on visible actions.
   Master to about -14 LUFS, true peak ≤ -1 dBFS.

## Pass marks

| Step | Pass |
|---|---|
| 1 | words ÷ (film length − 2.5 s) ≈ 3.0–3.3 |
| 2 | one file, no audible joins; pauses come from the read |
| 4 | no gap quieter than the room tone (RMS of every gap > digital silence) |
| 6 | music audible to the last frame; its ending is the film's ending, not a fade |
| 7 | every audio element present in the final render (check each one) |

## What went wrong before

- Sentences generated separately and joined with 0.06 s of pure silence: hard joins, the intonation resets each line,
  breaths gone. The fix was step 2.
- Speed 1.12 to fit the length: sounded tense. Cut words instead (step 1).
- A music bed that stopped at 31 s of a 34.6 s film, patched by repeating 8 bars and fading: audible. The fix was step 6.
