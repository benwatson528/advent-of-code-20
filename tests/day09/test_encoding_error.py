import os
from pathlib import Path

from main.day09.encoding_error import solve_any_two, solve_contiguous


def test_any_two_simple():
    assert solve_any_two(read_input("data/test_input.txt"), 5) == 127


def test_any_two_real():
    assert solve_any_two(read_input("data/input.txt"), 25) == 731031916


def test_contiguous_simple():
    assert sum(solve_contiguous(read_input("data/test_input.txt"), 127)) == 62


def test_contiguous_real():
    assert sum(solve_contiguous(read_input("data/input.txt"), 731031916)) == 93396727


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f:
            lines.append(int(line.strip('\n')))
        return lines
