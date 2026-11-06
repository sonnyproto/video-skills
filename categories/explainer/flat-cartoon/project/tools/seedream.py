#!/usr/bin/env python3
"""Generate a still with BytePlus ModelArk Seedream and download it.

usage: seedream.py out.png "prompt" [--size 1440x2560] [--image ref.png] [--model seedream-4-0-250828]

Reads BYTEPLUS_API_KEY from the environment or from project/.env.
"""
import argparse, base64, json, mimetypes, sys, urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from seedance import call  # noqa: E402

URL = "https://ark.ap-southeast.bytepluses.com/api/v3/images/generations"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("out")
    p.add_argument("prompt")
    p.add_argument("--model", default="seedream-4-0-250828")
    p.add_argument("--size", default="1440x2560")
    p.add_argument("--image", action="append", default=[], help="reference image, repeatable")
    p.add_argument("--seed", type=int)
    a = p.parse_args()

    body = {"model": a.model, "prompt": a.prompt, "size": a.size,
            "response_format": "url", "watermark": False}
    if a.seed is not None:
        body["seed"] = a.seed
    if a.image:
        imgs = [f"data:{mimetypes.guess_type(i)[0] or 'image/png'};base64,"
                f"{base64.b64encode(Path(i).read_bytes()).decode()}" for i in a.image]
        body["image"] = imgs[0] if len(imgs) == 1 else imgs
    r = call("POST", URL, body)
    urllib.request.urlretrieve(r["data"][0]["url"], a.out)
    print(f"saved {a.out} usage={json.dumps(r.get('usage'))}")


if __name__ == "__main__":
    main()
