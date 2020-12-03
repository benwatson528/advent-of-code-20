import os
import sys
from functools import reduce
from main.day03.toboggan_trajectory import solve


def test_simple():
    grid = read_input("data/test_input.txt")
    assert solve(grid, 3, 1) == 7


def test_real():
    grid = read_input("data/input.txt")
    assert solve(grid, 3, 1) == 286


def test_multiple_simple():
    assert iterate_multiple(read_input("data/test_input.txt")) == 336


def test_multiple_real():
    assert iterate_multiple(read_input("data/input.txt")) == 3638606400


def iterate_multiple(grid):
    movements = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    solutions = map(lambda x: solve(grid, x[0], x[1]), movements)
    return reduce(lambda x, y: x * y, solutions)


def read_input(file_name):
    f = open(os.path.join(sys.path[0], file_name))
    lines = []
    for line in f:
        lines.append(line.strip('\n'))
    return lines
