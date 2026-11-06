"""Narrate each line of a script with ElevenLabs (via fal), one file per line.

    python3 tools/voice.py script.txt [--voice Brian] [--speed 1.05]

One line of script.txt per narration line. Writes assets/audio/line-N.mp3 and prints each file's length and the pauses
inside it (where to split the caption). Needs FAL_KEY.
"""
import argparse
import re
import subprocess
from pathlib import Path

from fal import fetch

ROOT = Path(__file__).resolve().parent.parent
p = argparse.ArgumentParser()
p.add_argument("script")
p.add_argument("--voice", default="Brian")
p.add_argument("--speed", type=float, default=1.05)
a = p.parse_args()

for i, text in enumerate([t.strip() for t in Path(a.script).read_text().splitlines() if t.strip()], 1):
    _, paths = fetch("fal-ai/elevenlabs/tts/multilingual-v2",
                     {"text": text, "voice": a.voice, "stability": 0.5, "speed": a.speed}, ROOT / f"assets/audio/line-{i}")
    out = subprocess.run(["ffmpeg", "-i", str(paths[0]), "-af", "silencedetect=n=-35dB:d=0.18", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    length = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(paths[0])],
                            capture_output=True, text=True).stdout.strip()
    pauses = re.findall(r"silence_end: ([0-9.]+)", out)
    print(f"line {i}: {float(length):.2f} s, speech resumes after pauses at {', '.join(pauses) or 'none'}  | {text}")
