import os
from pathlib import Path
from typing import List, Tuple

from main.day22.crab_combat import solve


def test_simple():
    p1, p2 = read_input("data/part_one_test_input.txt")
    assert solve(p1, p2) == 306


def test_real():
    p1, p2 = read_input("data/input.txt")
    assert solve(p1, p2) == 34255


def read_input(file_name: str) -> Tuple[List[int], List[int]]:
    players = []
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        for line in f:
            stripped_line = line.strip('\n')
            if stripped_line.startswith("Player"):
                cards = []
            elif len(stripped_line) == 0:
                players.append(cards)
                cards = []
            else:
                cards.append(int(stripped_line))
        players.append(cards)
        return players[0], players[1]
