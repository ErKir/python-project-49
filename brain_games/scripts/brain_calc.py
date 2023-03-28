#!/usr/bin/env python3
from brain_games.engine import game_engine
from brain_games.games import calc_game


def main():
    game_engine(calc_game)


if __name__ == '__main__':
    main()
