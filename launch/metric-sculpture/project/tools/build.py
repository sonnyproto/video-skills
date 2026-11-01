"""Writes index.html and compositions/*.html for the metric-sculpture film (21.6 s, 112 BPM, 16:9).

Product content (app labels, agents, the metric, palette, mascot, captions, voice, music) comes from film.json;
change that, not this file. The film itself (scene order and times, camera keys, the plate schedule, eases) lives in
tools/templates/: index.html is the studio (Three.js), screen.html the living screencast, lockup.html and captions.html.
Templates take {{dotted.path}} values (HTML-escaped), {{@block}} snippets built here, and __FILM__ (the whole film as JSON).
Run: python3 tools/build.py
"""
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TPL = ROOT / "tools/templates"
FILM = json.loads((ROOT / "film.json").read_text())
M, A = FILM["metric"], FILM["app"]

# ---- checks: the schedule and camera are tuned for 20-150 plates on the right and 1-5 on the left ----
problems = []
n, n0 = M["after"] / M["unit"], M["before"] / M["unit"]
if n != int(n) or n0 != int(n0):
    problems.append(f"metric.before and metric.after must be whole multiples of metric.unit ({M['unit']})")
if not 20 <= n <= 150:
    problems.append(f"metric.after / metric.unit = {n:g} plates; keep it 20-150 (pick another unit)")
if not 1 <= n0 <= 5:
    problems.append(f"metric.before / metric.unit = {n0:g} plates; keep it 1-5")
heroes = [a for a in A["agents"] if a["id"] == A["hero_agent"]]
if not heroes:
    problems.append(f"app.hero_agent '{A['hero_agent']}' is not one of app.agents")
if not 2 <= len(A["agents"]) <= 5:
    problems.append("app.agents: 2-5 agents fit the sidebar")
if len(A["nav"]) != 3:
    problems.append("app.nav: exactly 3 items (each has an icon in the template)")
if len(FILM["captions"]) != 5 or len(FILM["voice"]["durations"]) != 5:
    problems.append("captions and voice.durations: exactly 5 lines, one per slot (references/RECIPE.md)")
for d, cap in zip(FILM["voice"]["durations"], [4.4, 2.9, 3.2, 2.9, 6.0]):
    if d > cap:
        problems.append(f"a voice line of {d} s overruns its {cap} s slot; rewrite it shorter")
for f in [FILM["brand"]["logo"], FILM["brand"]["mark"], FILM["music"]["src"]] + [a["img"] for a in A["agents"]]:
    if not (ROOT / f).exists():
        problems.append(f"missing file {f}")
if problems:
    sys.exit("film.json:\n  " + "\n  ".join(problems))

hero = heroes[0]
ratio = M["after"] / M["before"]
VALUES = {**FILM, "hero": hero, "ratio": f"{ratio:,.0f}" if ratio == int(ratio) else f"{ratio:,.1f}",
          "before_fmt": f"{M['before']:,}"}
JSON = {**FILM, "hero": hero}

CAP_CLASS = {"a": "a", "b": "b"}
BLOCKS = {
    "agents": "\n        ".join(
        f'<div class="agent" id="ag-{a["id"]}" style="top:{326 + 68 * i}px"><div class="on" id="on-{a["id"]}"></div>'
        f'<img src="{html.escape(a["img"])}" alt=""><div><b>{html.escape(a["name"])}</b><span>{html.escape(a["role"])}</span></div>'
        f'<i class="st" id="st-{a["id"]}"></i></div>'
        for i, a in enumerate(A["agents"])),
    "captions": "\n    ".join(
        f'<div class="cap {CAP_CLASS[k]}" id="c{i}">{html.escape(t)}</div>' for i, (t, k) in enumerate(FILM["captions"])),
}


def look(path):
    v = VALUES
    for part in path.split("."):
        v = v[int(part)] if isinstance(v, list) else v[part]
    return html.escape(str(v))


def fill(text):
    text = text.replace("__FILM__", json.dumps(JSON, ensure_ascii=False))
    text = re.sub(r"\{\{@(\w+)\}\}", lambda m: BLOCKS[m.group(1)], text)
    return re.sub(r"\{\{([\w.]+)\}\}", lambda m: look(m.group(1)), text)


COMP = ROOT / "compositions"
COMP.mkdir(exist_ok=True)
for f in COMP.glob("*.html"):
    f.unlink()
(ROOT / "index.html").write_text(fill((TPL / "index.html").read_text()))
for name in ["screen", "lockup", "captions"]:
    (COMP / f"{name}.html").write_text(fill((TPL / f"{name}.html").read_text()))
left = re.findall(r"\{\{[^}]*\}\}|__FILM__", "".join(p.read_text() for p in [ROOT / "index.html", *COMP.glob("*.html")]))
if left:
    sys.exit(f"unfilled placeholders: {sorted(set(left))}")
print(f"index.html + compositions/ written: {int(n)} plates of {M['unit']:,}, verdict {M['verdict']}")
