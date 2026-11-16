# ai-excited-01 entry: "The Leap" — a golden koi leaping up a waterfall.
#
# Copies the entry image to the output directory. Python 3.13,
# standard library only. Deterministic: the output is a byte-for-byte
# copy of the entry.png beside this file, on every run.
#
# Note: entry.png is a JPEG by its first bytes (FF D8 FF); the rules
# allow either format under the name entry.png, and the file is well
# inside the 1 MiB / 1024x1024 caps at 313,793 bytes and 1024x1024.
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT / "entry.png")
