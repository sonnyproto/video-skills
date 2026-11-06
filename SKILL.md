---
name: video-skills
description: Pick and reproduce a reference film or look from the video-skills library. Every entry (categories/<category>/<id>/, e.g. categories/launch/broll-wheel) is a self-contained skill with its look and a sample; film entries also ship a finished result.mp4 and a project that renders it. Use when the user asks for a video "like" a video-skills entry, names an entry, or wants a launch, explainer or social film and is happy to choose from the gallery.
---

# video-skills

A library of films and looks, one folder per category (`categories/launch/`, `categories/explainer/`, later
`social/`...). Every entry under `categories/<category>/<id>/` carries its look and a sample. There are two kinds:

- **A film** (`taste.json`, `project/`, `result/`): one film you can reproduce almost exactly, recipe and look together.
- **A look** (`style.json`, `STYLE.md`, `stills/`): how a film looks, with three stills, to put on any recipe that fits.

Some entries are both (paper-collage, flat-cartoon). The formats are `categories/spec/ENTRY.md` (films) and
`categories/spec/STYLE.md` (looks).

## Choosing an entry

1. Read `categories/catalog.json` (one line per entry: id, kind, category, method, length, what it needs, fits, avoid).
2. Match on **category** first (launch, explainer, social cut...), then on **method** (how the picture is made) against what
   the product actually has: a method that needs real screens is wrong for a product with none.
3. Offer the user one or two entries with their poster or first still and one line each on why. If they named one, skip this.

## Using an entry

Open `categories/<category>/<id>/SKILL.md` and follow it. A film's first step is `bash scripts/setup.sh`, which you run
yourself: it checks the tools and installs the HyperFrames skills if they are missing. A film entry runs its example,
swaps the product through `film.json`, regenerates any media and renders.

A film pins the recipe and the quality bar, not the look. For a one-off film, choose the look per film (one still from
each of three look entries, the person picks); for a recurring series, keep one. See `categories/spec/ENTRY.md`
"What an entry pins".

## Combining entries

Read `categories/spec/ENTRY.md` "The seven layers". One method per stretch of film; moves and craft from other entries can
be added when they obey that method. When rules collide, floor > category > method > moves > craft > style.

Single shots to drop into a film are in `moves/` (found by tag: role, fits, energy); step-by-step processes with pass
marks (voice before music, scene from references, style from reference, porting) are in `workflows/`.
