# The World in One Page — 24 November 2026

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/Pikerty/news-image-20261124-entry/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/Pikerty/news-image-20261124-entry/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

Entry for the make.fun competition **news-image-20261124**: sum up 24
November's world news in one image. Bounty page:
https://make.fun/bounty/news-image-20261124 — join make.fun with the
referral link https://make.fun/r/mpwgq2aa.

The image is a one-page newspaper front page for **Tuesday 24 November
2026**, drawn from stories reported that day:

- **Top story** — Ukraine says its sea drones sank a Russian warship at
  a Libyan base; Moscow warns of a "dangerous trend", Tripoli demands
  answers, the UN seeks a probe.
- **Myanmar / The Hague** — 14 nations back the ICJ genocide ruling on
  the Rohingya; Britain sanctions Myanmar's leaders.
- **Ukraine war** — Kyiv region strikes kill at least 14 (AFP).
- **UN / technology** — UN chief António Guterres calls for global AI
  risk rules within a year.
- **United States** — US states sue Musk's companies over sexualised
  images produced by the Grok chatbot.
- **Israel** — Eisenkot has until 6 December to form a government
  after October's inconclusive election.
- **Asia** — a 5.6-magnitude earthquake strikes Nepal near the Chinese
  border; a factory fire in Indonesia kills 24.
- **Markets** — S&P 500 +4.7%, Nasdaq +6.5%, Nikkei +3.9%, DAX +2.2%,
  Brent crude $86.70.
- **In brief** — China opens its Tiangong station to a first foreign
  astronaut (Pakistan's Zeeshan Ali); Denmark bans school phones to
  grade 10; injured Gaza children arrive in the UK for care.

Sources: wire reports (AP, AFP) and the 24 Nov 2026 world pages of
SCMP, Qatar Tribune, The Manila Times and Horizon.

## How it runs

`main.ts` (Node 22, standard library only) copies `entry.png` to
`/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png` outside the
grader). The poster itself is drawn offline by
`tools/render_poster.py` (Python + Pillow) and committed as
`entry.png`, so the graded program needs no network and always writes
identical bytes.

## License

MIT — see `LICENSE`.
