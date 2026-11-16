"""The Leap, round 4: copy the entry image to the output directory.

Reads entry.png from this repository and writes it, byte for byte, to
$MAKEFUN_OUTPUT_DIR/entry.png (or /output/entry.png when the variable
is unset). Deterministic: both runs write identical bytes.
"""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    with open(src, "rb") as f:
        magic = f.read(3)
    if magic != b"\xff\xd8\xff":
        raise SystemExit("entry.png is not a JPEG")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
