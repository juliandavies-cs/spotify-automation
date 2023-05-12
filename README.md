# Spotify Automation

Spotify Automation is a testing implementation of the website spotify.

Tests are run with Selenium using Python

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pipenv.

```bash
pip install pipenv
cd /spotify-automation
pipenv install
pipenv shell
```

## Run Test Cases

All Tests:
```bash
pytest tests/spotify_tests.py
```

Create playlist Test:
```bash
pytest -m slow tests/spotify_tests.py
```

## Test Cases

- Login
- Create Playlist w/ 3 songs

## Possible Improvements

Automation setup and cleanup with pytest fixtures to prevent errors coming from previous tests failing
