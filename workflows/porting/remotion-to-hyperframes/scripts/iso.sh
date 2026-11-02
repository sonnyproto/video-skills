#!/bin/bash
# Render or check one card in its own throwaway copy of the project, so several cards can be worked on at once.
#   bash tools/iso.sh <composition-id> <seconds> [render|check]   render -> renders/<id>.mp4, check -> JSON on stdout
set -e
ID=$1; D=$2; MODE=${3:-render}
P=$(cd "$(dirname "$0")/.." && pwd)
W=${ISO_ROOT:-${TMPDIR:-/tmp}/hf-iso}/$ID
rm -rf "$W"; mkdir -p "$W/compositions" "$P/renders"
cp "$P/hyperframes.json" "$P/package.json" "$W/"
cp -R "$P/assets" "$W/assets"
cp "$P/compositions/$ID.html" "$W/compositions/"
python3 - "$ID" "$D" "$P/index.html" "$W/index.html" <<'PY'
import re,sys
cid,d,src,dst=sys.argv[1:]
s=open(src).read()
s=re.sub(r'(<div id="root"[^>]*data-duration=")[^"]+',r'\g<1>'+d,s,1)
s=re.sub(r'\s*<div id="h-[^"]+" class="clip".*?</div>','',s)
host=f'\n      <div id="h-{cid}" class="clip" data-composition-id="{cid}" data-composition-src="compositions/{cid}.html" data-start="0" data-duration="{d}" data-track-index="1" data-track-kind="graphics" data-width="1920" data-height="1080"></div>'
s=s.replace('data-height="1080">',f'data-height="1080">{host}',1)
open(dst,'w').write(s)
PY
cd "$W"
if [ "$MODE" = check ]; then
  npx --yes hyperframes@0.8.191 check --json
else
  npx --yes hyperframes@0.8.191 render -q delivery -w ${ISO_WORKERS:-2} -o "$P/renders/$ID.mp4" --quiet 2>&1 | grep -v dedup | tail -3 || true
  ls -la "$P/renders/$ID.mp4"
fi
