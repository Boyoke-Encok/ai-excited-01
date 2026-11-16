"""ai-excited-01 entrypoint.

Copies the image entry.png that sits beside this file into the output
directory, so the grader finds it at $MAKEFUN_OUTPUT_DIR/entry.png.
Python 3.13, standard library only. Deterministic: the output is a
byte-for-byte copy of the source image on every run.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    # The source image lives next to this script; the destination is the
    # output directory the platform provides (or /output by default).
    here = Path(__file__).resolve().parent
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(here / "entry.png", out_dir / "entry.png")


if __name__ == "__main__":
    main()
