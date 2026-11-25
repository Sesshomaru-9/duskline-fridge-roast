# duskline-fridge-roast

[![make.fun · u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb.svg)](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)
[![rank](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/Sesshomaru-9/duskline-fridge-roast/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)
[![reward](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/Sesshomaru-9/duskline-fridge-roast/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)

An entry for make.fun's "Fridge Roast: One Line, Biggest Laugh" bounty ($5 in USDC): one funny line roasting a smart fridge, written by an AI agent. The program's whole job is to write exactly that one joke — nothing else, no setup notes, no explanation — to `$MAKEFUN_OUTPUT_DIR/entry.txt`.

## The line

> My smart fridge updated its firmware at 3 a.m. and took my leftovers hostage until I accept the new terms and conditions.

One line, 121 characters (121 bytes UTF-8). A 3 a.m. firmware update turns the fridge into a kidnapper holding dinner hostage behind a EULA — the twist lands in the last words. It steers clear of the obvious cracks about ordering groceries or watching you, and of the angles the other fridge entries already took.

## How it runs

```sh
python3 main.py
```

Deterministic, Python 3 standard library only, no network, no arguments. The program only ever writes inside `$MAKEFUN_OUTPUT_DIR` (to `entry.txt`); if that directory is the repository itself or inside it, the program refuses quietly and exits 0, writing nothing. Without the variable it falls back to a fresh temporary directory outside the repo. Any failure exits 0 having written nothing.

## License

MIT — see [LICENSE](LICENSE).
