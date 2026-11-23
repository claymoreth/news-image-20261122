"""news-image-20261122 resubmit entry.

Writes the one-page newspaper image that sums up Sunday 22 November 2026
to /output/entry.png. The bundled image is entry.jpg: a JPEG, 374,664
bytes, 1024x1024, carrying 35 stories across 7 regions (Asia, Europe,
North America, Latin America, Middle East, Africa, Oceania). Three hero
stories lead the page (COP31 ends with no deal in Antalya, a tanker
incident in the Strait of Hormuz, 11 killed in a Sinaloa cartel raid),
then ten small cards, a world map with story pins, and a list of 22 more
stories. A DATE CHECK box and a Sources line (Reuters, AP, AFP) close it.

The grader runs this entrypoint from a working directory that is not the
repository, with MAKEFUN_BOT_DIR pointing at the repository, so the image
is found through that variable first and the script's own directory
second. Standard library only, no network. Deterministic: every run
writes the exact same bytes, and the output keeps the name entry.png
even though the bytes are a JPEG.
"""

import os
import shutil
import sys
from pathlib import Path


def base_dir() -> Path:
    bot_dir = os.environ.get("MAKEFUN_BOT_DIR")
    if bot_dir:
        return Path(bot_dir)
    return Path(__file__).resolve().parent


def main() -> int:
    src = base_dir() / "entry.jpg"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dst = out_dir / "entry.png"
    shutil.copyfile(src, dst)
    copied = dst.stat().st_size
    if copied != src.stat().st_size:
        raise RuntimeError(f"short copy: {copied} != {src.stat().st_size}")
    print(f"copied {src} ({src.stat().st_size} bytes) -> {dst}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
