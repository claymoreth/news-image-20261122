"""news-image-20261122 entry.

Writes the one-page newspaper image that sums up Sunday 22 November 2026
to /output/entry.png. The bundled image is a JPEG (399,691 bytes, 1024x1024);
the output file keeps the name entry.png either way, and the gate tells PNG
from JPEG by the first bytes. The page carries 30 stories across 7 regions,
with three hero stories (COP31 in Antalya, tankers near Hormuz, the Brazil
supercell storm), ten small cards, a world map and a 17-more-stories list.
Standard library only, no network. Deterministic: every run writes the
exact same bytes.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.jpg")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUT = os.path.join(OUT_DIR, "entry.png")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, OUT)


if __name__ == "__main__":
    main()
