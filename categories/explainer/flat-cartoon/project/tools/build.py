"""Write index.html and compositions/ from film.json and tools/templates/. Run from project/: python3 tools/build.py"""
import json, re
from pathlib import Path

P = Path(__file__).resolve().parent.parent
film = json.loads((P / "film.json").read_text())

def lookup(path):
    v = film
    for k in path.split("."):
        v = v[k]
    if not isinstance(v, str):
        raise SystemExit(f"film.json {path} is not a string")
    return v

def fill(text):
    return re.sub(r"\{\{([a-z0-9_.]+)\}\}", lambda m: lookup(m.group(1)), text)

(P / "compositions").mkdir(exist_ok=True)
hosts, t = [], 0.0
for sc in film["scenes"]:
    out = fill((P / "tools/templates" / sc["template"]).read_text())
    left = re.findall(r"\{\{[^}]*\}\}", out)
    if left:
        raise SystemExit(f"{sc['template']}: unfilled {left}")
    (P / "compositions" / f"{sc['id']}.html").write_text(out)
    hosts.append(f'''      <div id="{sc['id']}" data-composition-id="{sc['id']}" data-composition-src="compositions/{sc['id']}.html"
        data-start="{t:g}" data-duration="{sc['duration']:g}" data-track-index="1" data-track-kind="graphics"
        data-width="1920" data-height="1080"></div>''')
    t += sc["duration"]
total = round(t, 3)
sound = film.get("sound", {}).get("src")
audio = f'\n      <audio id="sound" class="clip" src="{sound}" data-start="0" data-duration="{total:g}" data-track-index="2" data-volume="1"></audio>' if sound else ""

(P / "index.html").write_text(f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <title>{film["title"]}</title>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
    <style>
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ margin: 0; width: 1920px; height: 1080px; overflow: hidden; background: #0a0628; }}
      #root {{ width: 100%; height: 100%; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{total:g}" data-width="1920" data-height="1080">
{chr(10).join(hosts)}{audio}
    </div>
    <script>
      window.__timelines["main"] = gsap.timeline({{ paused: true }});
    </script>
  </body>
</html>
''')
print(f"index.html: {len(hosts)} scenes, {total:g} s")
