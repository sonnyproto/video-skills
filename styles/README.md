# styles

**What a film looks like, kept apart from how it is built.**

A film in [films/](../films/) is a recipe: what kind of film, how the story runs, how picture meets narration. A style
is a skin: palette, type, texture, light, materials, how characters stay the same, and the motion feel. Any recipe can
take any style that fits it, so "a launch film in low-poly" does not need a new film.

Shots are in [moves/](../moves/), the process in [workflows/](../workflows/).

## Styles

| Stills | Style | Fits | Worked example |
|---|---|---|---|
| <img src="paper-collage/stills/2.jpg" width="240"> | [**paper-collage**](paper-collage/) Torn paper, halftone b-roll, stamps and typed labels that land on their words | explainer | [films/explainer/paper-collage](../films/explainer/paper-collage/) |
| <img src="cut-paper-stop-motion/stills/1.jpg" width="240"> | [**cut-paper-stop-motion**](cut-paper-stop-motion/) Printed paper cut-outs posed 15 times a second under a smooth camera | explainer, social | moves: [parallax-sheets](../moves/parallax-sheets/), [stop-motion-clock](../moves/stop-motion-clock/) |
| <img src="paper-lightbox/stills/1.jpg" width="240"> | [**paper-lightbox**](paper-lightbox/) Backlit cut paper at night, warm on one side and neon on the other, a wet floor | explainer, social | moves: [medallion-burst-lock](../moves/medallion-burst-lock/), [wet-floor-reflection](../moves/wet-floor-reflection/) |

## Using a style

1. Pick the film from `films/` first, then a style whose `fits` includes its category and method.
2. For a one-off film, show the person three styles, one still each, and let them choose. For a series, choose once.
3. Read the style's `STYLE.md` and build the film's elements with it. Where the film's own `taste.json` `style`
   differs, the chosen style wins on look, the film wins on everything else.

## Making a style

From a reference video or account: [workflows/style/style-from-reference](../workflows/style/style-from-reference/WORKFLOW.md).
Format: [STYLE.md](STYLE.md).

## Licence

MIT. Stills: CC BY 4.0, except real photos and logos inside them, which belong to their owners.
