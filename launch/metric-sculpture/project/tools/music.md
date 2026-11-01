# Music

`assets/audio/music.mp3` (21 s) was generated with ElevenLabs Music through fal (`fal-ai/elevenlabs/music`,
21 000 ms) from this prompt, and is used as generated at volume 0.3:

```
Playful bright product film score, 112 BPM. 0 to 7.5 seconds: a light hi-fi band, upright bass, tight brushed kit, electric piano, with a cute chiptune square-wave lead answering the piano. At 7.5 seconds it changes: marimba ostinato, vibraphone and harp in a warm studio, pulse bass. From 11.5 to 14.7 seconds it builds by subdivision, eighth notes to sixteenth notes, rising. At 14.7 seconds a short silence. At 15.0 seconds one big hit: timpani, bass drum and a bell. 15 to 21 seconds: warm confident resolved outro, marimba and soft pad, ending cleanly at 21 seconds. No vocals. Leaves room for a narrator.
```

```bash
python3 tools/fal.py fal-ai/elevenlabs/music '{"prompt":"…","music_length_ms":21000}' assets/audio/music-raw
cp assets/audio/music-raw.mp3 assets/audio/music.mp3   # then set music.duration in film.json
```

Make a new track for every film; keep the structure (change at 7.5, build 11.5–14.7, silence at 14.7, hit at 15.0, outro
to 21). Listen for the hit: if the model puts it late or early, regenerate rather than move the picture.
