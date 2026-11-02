# moves

**Single shots for HyperFrames films: one folder per move, each with its preview, its code and its tags.**

A move is one beat of a film: a crash zoom onto a card, a price that slams in, a word filled on the downbeat, a logo
lockup. Whole films are in [films/](../films/), how to make them in [workflows/](../workflows/). This folder holds the parts.

## Layout

```
<name>/
├── <name>.html     the HyperFrames composition (copy, colours and duration are variables)
├── move.json       name, tags, duration, what to swap, source and licence (MOVE.md)
├── MOVE.md         intent, parameters, pitfalls, when not to use it
├── poster.jpg      one frame
└── preview.gif     ~3 s, for the catalogue (the full mp4 is a release asset, not in git)
catalog.json        one line per move, rebuilt from every move.json
```

The list is flat. Moves are found by their tags, not by folders: `role` (hook, emphasis, metric, callout, demo,
transition, outro...), `fits` (launch, explainer, social...) and `energy` (low, mid, high). See [MOVE.md](MOVE.md).

## Using a move

Copy `moves/<name>/<name>.html` into your project's `compositions/`, mount it from `index.html`, set its variables.
A film that uses a move keeps its own copy, so the film still renders if the move changes here.

## Status

Empty for now. The first moves come from ports of
[video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) (Remotion) to HyperFrames, each measured frame by frame
against the original preview (SSIM ≥ 0.93) before it is made swappable and added here.

## Licence

This folder is Apache-2.0 ([LICENSE](LICENSE)), unlike the MIT rest of the repo, because most moves are derived from video-shotcraft (Apache-2.0); see [NOTICE](NOTICE).
Preview media: CC BY 4.0.
