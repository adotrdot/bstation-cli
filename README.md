## bstation-cli
==============================

bstation-cli is a command line interface to browse and watch anime.

This tool scrapes the site [bilibili.tv](https://www.bilibili.tv).

## Dependencies
==============================

- curl
- grep
- mpv
- python with selenium + firefox + geckodriver
- sed
- wc

## Download
==============================

```bash
git clone https://github.com/adotrdot/bstation-cli.git
```

## Usage
==============================

1. Install selenium (if hasn't) by running `python pip install selenium`
1. Install firefox (if hasn't)
1. Set up geckodriver, follow the guide [here](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/)
1. Give execute permission to the program by running `chmod +x` on it
1. Run `./bstation-cli`

## Misc
==============================

- The development of this program is for educational purpose.
- This program was written from scratch, but was heavily inspired by [ani-cli](https://github.com/pystardust/ani-cli)
- I don't support piracy, thus I won't add a download feature.
- Currently, video quality is maxed at 480p and some shows aren't accessible because one needs to have an account at Bilibili to access those.
- Getting episode list might take a while. This is because of a page functionality that hides some episodes, thus requires using selenium to click some buttons first. It's a bit overwhelming to use selenium just for getting the episode list, but I haven't found any other solutions.
- Converting subtitle might also take a while. This is because bilibili has a unique subtitle format that needs to be converted to `.srt`.
- Be warned that this code is still messy. I haven't written any comments, and such.
