#!/usr/bin/env python3
from brain_games.scripts.games import (
    greeting,
    start_game,
    finish_game,
)


def main():
    name = greeting()
    result = start_game('brain-prime')
    finish_game(result, name)


if __name__ == '__main__':
    main()
