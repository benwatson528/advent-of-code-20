import os
from pathlib import Path

from main.day05.seat import Seat
from main.day05.binary_boarding import solve


def test_simple():
    assert solve("FBFBBFFRLR") == Seat(44, 5, 357)
    assert solve("BFFFBBFRRR") == Seat(70, 7, 567)
    assert solve("FFFBBBFRRR") == Seat(14, 7, 119)
    assert solve("BBFFBBFRLL") == Seat(102, 4, 820)


def test_real():
    assert max(map(lambda x: solve(x).seat_id, read_input("data/input.txt"))) == 915


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f:
            lines.append(line.strip('\n'))
        return lines
