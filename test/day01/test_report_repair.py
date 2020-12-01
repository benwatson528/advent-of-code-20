import os
import sys
from main.day01.report_repair import solve


def test_simple():
    f = open(os.path.join(sys.path[0], "data/test_input.txt"))
    lines = []
    for line in f:
        lines.append(int(line.strip('\n')))
    assert solve(lines, 2020) == 514579


def test_part_1():
    f = open(os.path.join(sys.path[0], "data/input.txt"))
    lines = []
    for line in f:
        lines.append(int(line.strip('\n')))
    assert solve(lines, 2020) == 197451
