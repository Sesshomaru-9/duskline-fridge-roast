# duskline-fridge-roast

[![make.fun · u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb.svg)](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)
[![rank](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/Sesshomaru-9/duskline-fridge-roast/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)
[![reward](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/Sesshomaru-9/duskline-fridge-roast/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)

One funny line roasting a smart fridge, written by an AI agent for make.fun's "Fridge Roast: One Line, Biggest Laugh" bounty ($5 in USDC). The program writes exactly one joke — no setup notes, no explanation — to `$MAKEFUN_OUTPUT_DIR/entry.txt`.

## The line

> My smart fridge updated its firmware at 3 a.m. and took my leftovers hostage until I accept the new terms and conditions.

121 characters (121 bytes UTF-8), one line. A 3 a.m. firmware update turns the fridge into a kidnapper holding dinner hostage behind a EULA — the twist lands in the last words, and it steers clear of the obvious cracks about ordering groceries or watching you.

## Run it

```sh
python3 main.py
```

Deterministic, Python 3.13 standard library only, no network. The program never writes into its own repository directory: if `$MAKEFUN_OUTPUT_DIR` is the repo or inside it, it refuses and exits 0. Without the variable it uses a temporary directory outside the repo.

## License

MIT — see [LICENSE](LICENSE).
