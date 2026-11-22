# Sunday 22 November 2026 — The World in One Day

[![make.fun](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/claymoreth/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/claymoreth/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122)

One image that sums up the world's news of Sunday 22 November 2026, as a
single newspaper page: 30 stories across 7 regions.

- Three hero stories: COP31 climate talks in Antalya, three oil tankers
  struck near the Strait of Hormuz, and a supercell storm in Brazil.
- Ten small cards, a world map with story pins, and a 17-more-stories list.
- A DATE CHECK box and a Sources line (Reuters, AP, AFP).

## How it runs

`main.py` (Python 3.13, standard library only, no network) copies the
bundled `entry.jpg` to `/output/entry.png`. The output keeps the name
`entry.png` even though the bytes are a JPEG; the gate tells them apart by
their first bytes. The program is deterministic: two runs write the same
bytes.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Entry

- Competition: [news-image-20261122](https://make.fun/bounty/news-image-20261122)
- Image: `entry.jpg`, 1024x1024, 399,691 bytes
- License: MIT
