# Adding an entry

1. Make the film first. A film entry starts from a finished film someone would want to copy, not from a template. A look
   with no finished film yet goes in as a look entry: `SKILL.md`, `style.json`, `STYLE.md` and three stills
   ([spec/STYLE.md](categories/spec/STYLE.md)), in the category folder it fits first.
2. Copy the shape of an existing entry: `categories/<category>/<new-id>/` (category folders: `categories/launch/`, `categories/explainer/`, `categories/artistic/`, `tutorial/`, `data/`, `social/`, `sting/`; make one if yours is new) with the files listed in [spec/ENTRY.md](categories/spec/ENTRY.md).
   Name it by its method and look (`broll-wheel`), never by another company's brand.
   Copy `categories/tools/floor.md` to `references/floor.md` and `categories/tools/{analyze,events}.py` and `categories/tools/setup.sh` to `scripts/`; do not edit the copies.
   Declare external tools in `taste.json` `requires`. Put the film's own taste in its `SKILL.md` and `RECIPE.md`, not in floor.md.
3. Move everything that is the product into `project/film.json`. Someone swapping products should never open the generator.
4. Ship generated media (b-roll, music) in `project/assets/` and the prompts that made them in `project/tools/`.
5. Measure the result from the repo root:
   ```bash
   uv run --with librosa --with numpy --with pillow python -I <category>/<id>/scripts/analyze.py <category>/<id>/result/result.mp4 /tmp/m
   uv run --with numpy python -I <category>/<id>/scripts/events.py <category>/<id>/result/result.mp4 /tmp/m
   cp /tmp/m/metrics.json <category>/<id>/result/
   ```
6. `python3 tools/validate.py <id>` must pass, then `python3 tools/catalog.py`.

## The bar

- `project/` renders `result/result.mp4` with no edits.
- Loudness about -14 LUFS, true peak under -1 dBTP.
- Every product claim in the example comes from the product's own material; anything invented is labelled on screen.
- No reference footage, logos or characters are redistributed. `REFERENCE.md` describes and measures; it does not copy.
- You have the right to publish the example product's assets, or you replace them with your own.
