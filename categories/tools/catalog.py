"""Write categories/catalog.json (one record per entry, from taste.json + metrics.json, or style.json for a look) and the table between the CATALOG markers in every README*.md at the repo root."""
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # categories/
REPO = ROOT.parent
rows = []
for e in sorted(p.parent for p in ROOT.glob("*/*/SKILL.md")):  # <category>/<id>/
    path = f"categories/{e.parent.name}/{e.name}"
    if (e / "taste.json").exists():
        t = json.loads((e / "taste.json").read_text())
        m = json.loads((e / "result/metrics.json").read_text()) if (e / "result/metrics.json").exists() else {}
        rows.append({"id": t["id"], "kind": "film", "title": t["title"], "summary": t["summary"], "category": e.parent.name,
                     "method": t["layers"]["method"], "duration_s": t["spec"]["duration_s"], "ratio": t["spec"]["ratio"],
                     "events_per_10s": m.get("events_per_10s"), "still_share": m.get("still_share"), "shots": m.get("shots"),
                     "needs": t["needs"], "fits": t["fits"], "avoid": t["avoid"], "path": path, "poster": f"{path}/result/poster.jpg",
                     "preview": f"{path}/result/preview.gif", "video": f"{path}/result/result.mp4"})
    else:
        s = json.loads((e / "style.json").read_text())
        rows.append({"id": s["name"], "kind": "look", "title": s["title"], "summary": s["summary"], "category": e.parent.name,
                     "method": "look only", "duration_s": None, "ratio": None, "events_per_10s": s.get("pace", {}).get("events_per_10s"),
                     "fits": s.get("fits", {}), "path": path, "poster": f"{path}/stills/1.jpg", "preview": f"{path}/stills/1.jpg", "video": None})
(ROOT / "catalog.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n")

def length(r):
    if r["kind"] == "look":
        return "stills"
    return f"{r['duration_s']} s {' + '.join(r['ratio']) if isinstance(r['ratio'], list) else r['ratio']}"

table = "| Preview | Entry | Category · method | Sample | Events / 10 s |\n|---|---|---|---|---|\n" + "".join(
    f"| <img src=\"{r['preview']}\" width=\"240\"> | [**{r['id']}**]({r['path']}/) {r['title']} | {r['category']} · {r['method']} | {length(r)} | {r['events_per_10s'] if r['events_per_10s'] is not None else ''} |\n"
    for r in rows)
for p in sorted(REPO.glob("README*.md")):
    p.write_text(re.sub(r"(<!-- CATALOG -->\n).*?(<!-- /CATALOG -->)", lambda mm: mm.group(1) + table + mm.group(2), p.read_text(), flags=re.S))
print(len(rows), "entries")
