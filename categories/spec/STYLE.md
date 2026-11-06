# The look format

A look lives inside an entry, `categories/<category>/<name>/`, next to its sample. A look-only entry has these files plus a
short `SKILL.md`; a film entry may carry them too (paper-collage, flat-cartoon). A film can take any look without reading
another film.

```
<name>/
├── style.json     the card: look, how things stay the same, motion, pace, banned, what it fits
├── STYLE.md       how to make it: per element, the recipe (code, shader, prompt); when to use it, when not
└── stills/        1.jpg 2.jpg 3.jpg: three frames in this style, at least one with text on screen
```

No whole film is needed. A style is proven by its three stills and by the recipe in STYLE.md that made them.

## style.json

```json
{
  "name": "paper-collage",
  "title": "Paper collage",
  "summary": "One line a person can picture.",
  "look": {
    "ground": "what the frame sits on: paper, a sky, a void",
    "palette": [{ "role": "ground", "hex": "#efe9dc", "where": "paper scenes" }],
    "type": "families and where each one goes",
    "texture": "grain, halftone, outline, none",
    "light": "direction, softness, time of day; 'flat' is a valid answer",
    "materials": "how surfaces take light: paper, clay, low-poly flat shading"
  },
  "consistency": "how a character, object or place stays the same across shots (a rig in code, one reference image passed to every generation, real photos)",
  "motion": { "feel": "land, glide, bounce, snap", "moves": ["slap: 1.3-1.7x to 1x in 0.32 s, back.out(2.2)"] },
  "pace": { "avg_shot_s": 4.9, "events_per_10s": 9.8, "text": "when words appear and how long they hold" },
  "banned": ["what breaks this style"],
  "fits": { "categories": ["explainer"], "methods": ["narrated-paper-collage"] },
  "made_with": { "renderer": "hyperframes@0.8.191", "generators": ["what made any generated media"] },
  "worked_example": "categories/explainer/paper-collage",
  "source": "original, or the kind of reference it was derived from (never a named third-party clip)",
  "licence": "MIT; stills CC BY 4.0"
}
```

| Field | Rule |
|---|---|
| `name` | kebab-case, equals the folder |
| `look.palette` | hex values with a role; the brand's colours replace roles, never add to them |
| `consistency` | required when the style has a character or a recurring object; "none" otherwise |
| `pace` | measured on the source (`categories/tools/analyze.py`, `events.py`), not guessed. It is the style's feel; a film's recipe wins on pacing |
| `banned` | what would make it look like a different style or like slop |
| `worked_example` | a film entry in `categories/` that uses it, if one exists; empty is fine |

## Rules

- Real people, logos and product UI in the stills are the real thing, or neutral placeholders; never generated.
- Three stills show range (a wide, a close-up, a frame with type), not three crops of one frame.
- A style never names a client, product or brand as part of the look.
- New styles come from `workflows/style/style-from-reference`.
