"""The Leap — ai-excited-01 entry.

Copies the entry image (entry.png, sitting beside this script) into the
output directory required by the competition harness. The copy is
byte-for-byte, so the program is fully deterministic: every run produces
the identical output file.
"""

import os
import shutil
import sys


def main() -> int:
    # The source image lives next to this script; the harness reads the
    # output directory from MAKEFUN_OUTPUT_DIR (default /output).
    script_dir = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(script_dir, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    destination = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, destination)
    return 0


if __name__ == "__main__":
    sys.exit(main())
