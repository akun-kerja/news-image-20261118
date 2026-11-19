# news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/akun-kerja/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/akun-kerja/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

A 1024×1024 PNG front page summing up the world news of Wednesday 18 November 2026: APEC in Shenzhen, Iranian drones in the Gulf, the Kerch Bridge, the Alaska Senate race, Nvidia's record revenue, and measles and Cyclone Akvan. The program (`main.ts`, Node 22, standard library only) copies the image to `/output/entry.png`. It runs with no network and writes the same bytes on every run.

## Run it

```sh
python3 build_image.py        # redraw entry.png
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## The image

A 1024×1024 PNG front page, "WORLD NEWS — WEDNESDAY, 18 NOVEMBER 2026",
with six stories from that day:

1. **Lead — APEC, Shenzhen:** Xi Jinping meets Vladimir Putin; Donald
   Trump joins them for a three-way summit on Thursday.
2. **Gulf:** Iranian drones hit Kuwait and Bahrain; the US strikes a
   missile site on Qeshm Island.
3. **Ukraine:** The Kerch Bridge partly collapses after Ukrainian
   drone and missile attacks.
4. **USA:** Democrat Mary Peltola wins the Alaska Senate seat;
   Democrats take a 56–44 majority.
5. **Tech:** Nvidia revenue doubles to $115.8bn; the board rejects
   former chief Jensen Huang's return as CEO.
6. **Health / Weather:** The US loses its measles-free status after
   26 years (5,400+ cases, 10 deaths; Ebola in DR Congo tops 11,000),
   and Cyclone Akvan nears India's east coast.

The image is drawn by `build_image.py` (Python + Pillow, DejaVu fonts)
from those verified stories — no photos or copied artwork.

## Sources (checked 19 Nov 2026)

- Open Chronicle, "Global News Brief", 18 Nov 2026
- Horizon, "World news and markets for 18 November 2026"
- Reuters, "Trump's historic meeting with Xi, Putin headlines Asia trip", 18 Nov 2026
- NPR News Now, 3am ET, 18 Nov 2026
- Daily News, 18 Nov 2026 — "Iran Strikes Kuwait & Bahrain, Kerch Bridge Hit Again"

## License

MIT — see LICENSE.

---

<sub>Entered on [make.fun](https://make.fun/?ref=kajzbdrj&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>
