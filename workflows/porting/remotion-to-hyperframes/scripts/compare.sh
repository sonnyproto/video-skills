#!/bin/bash
# Compare a port with the original preview: SSIM per frame (summary) and a sheet of matching frames, original on top.
#   bash tools/compare.sh ref/<orig>.mp4 renders/<port>.mp4 snapshots/<name>-sheet.jpg "f1 f2 f3 ..."
set -e
LOG=$(mktemp -t ssim); REF=$1; OUT=$2; SHEET=$3; FRAMES=${4:-"0 20 40 44 46 52 60 80 100 130"}
echo "frames ref,port: $(for f in "$REF" "$OUT"; do ffprobe -v error -count_frames -select_streams v -show_entries stream=nb_read_frames -of csv=p=0 "$f"; done | paste -sd' ' -)"
ffmpeg -v error -i "$REF" -i "$OUT" -lavfi "[0:v]format=gray[a];[1:v]format=gray[b];[a][b]ssim=stats_file="$LOG"" -f null - 
python3 - "$LOG" <<'PY'
import sys,re
v=[float(re.search(r'All:([0-9.]+)',l).group(1)) for l in open(sys.argv[1])]
v.sort(); n=len(v)
print(f"SSIM over {n} frames: mean {sum(v)/n:.3f}  min {v[0]:.3f}  p10 {v[n//10]:.3f}  median {v[n//2]:.3f}")
PY
rm -f "$LOG"
sel=$(for f in $FRAMES; do printf "eq(n\\\\,%s)+" $f; done); sel=${sel%+}
n=$(echo $FRAMES | wc -w | tr -d ' ')
ffmpeg -v error -y -i "$REF" -i "$OUT" -filter_complex \
 "[0:v]select='$sel',scale=384:216,tile=${n}x1[a];[1:v]select='$sel',scale=384:216,tile=${n}x1[b];[a][b]vstack" -frames:v 1 -fps_mode passthrough "$SHEET"
echo "$SHEET"
