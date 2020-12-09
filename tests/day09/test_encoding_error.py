import os
from pathlib import Path

from main.day09.encoding_error import solve


def test_simple():
    assert solve(read_input("data/test_input.txt"), 5) == 127


def test_real():
    assert solve(read_input("data/input.txt"), 25) == 731031916


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f:
            lines.append(int(line.strip('\n')))
        return lines
