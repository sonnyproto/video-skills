# The move format

Every move in `moves/<name>/` has the same files, so a move can be copied into any HyperFrames project on its own.

## move.json

```json
{
  "name": "crash-zoom-punch",
  "title": "Crash zoom punch",
  "summary": "The camera slams onto one card and stops dead, motion blur on the way in.",
  "tags": {
    "role": ["callout"],
    "fits": ["launch", "explainer"],
    "energy": "high"
  },
  "duration": 4.4,
  "variables": {
    "headline": "text shown on the card",
    "accent": "colour of the highlight"
  },
  "needs": ["one screenshot, 16:9"],
  "tool": "hyperframes@0.8.191",
  "source": "video-shotcraft demos/camera/crash-zoom-punch/CrashZoomReal.tsx",
  "licence": "Apache-2.0"
}
```

| Field | Rule |
|---|---|
| `name` | kebab-case, equals the folder and the composition id |
| `tags.role` | one or more of: hook, title, emphasis, list, metric, callout, demo, transition, background, outro |
| `tags.fits` | film categories it suits, matching video-skills folders (launch, explainer, ...) |
| `tags.energy` | low, mid or high |
| `variables` | every swappable value: copy, colours, images. Defaults reproduce the preview |
| `needs` | real material the move expects (a screenshot, a logo); empty if none |
| `source` | where it came from, exact file; "original" if made here |

## Rules

- The composition follows the HyperFrames contract (`npx hyperframes check` passes, or each remaining warning is
  explained in MOVE.md).
- No brand, product or person that the user did not supply: placeholders are neutral ("workspace", a plain mark).
- Self-contained: anything the move needs (helpers, textures) is inside its folder; no links to other moves.
- Taste lives in MOVE.md (when to use, when not), never in a shared file.
