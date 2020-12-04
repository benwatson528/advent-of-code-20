import os
from pathlib import Path

from main.day01.report_repair import solve_two, solve_three


def test_part_1_simple():
    lines = read_input("data/test_input.txt")
    assert solve_two(lines, 2020) == 514579


def test_part_1():
    lines = read_input("data/input.txt")
    assert solve_two(lines, 2020) == 197451


def test_part_2_simple():
    lines = read_input("data/test_input.txt")
    assert solve_three(lines, 2020) == 241861950


def test_part_2():
    lines = read_input("data/input.txt")
    assert solve_three(lines, 2020) == 138233720


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f:
            lines.append(int(line.strip('\n')))
        return lines
