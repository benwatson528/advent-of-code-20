import os
from pathlib import Path

from main.day11.seating_system import solve


def test_simple():
    assert solve(read_input("data/test_input.txt")) == 37


def test_real():
    assert solve(read_input("data/input.txt")) == 2468


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f:
            lines.append(line.strip('\n'))
        return lines
