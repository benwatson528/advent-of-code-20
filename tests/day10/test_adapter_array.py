import os
from functools import reduce
from pathlib import Path

from main.day10.adapter_array import solve_diffs, solve_combinations


def test_diffs_simple():
    assert prepare_results("data/small_test_input.txt") == 35


def test_diffs_large():
    assert prepare_results("data/large_test_input.txt") == 220


def test_diffs_real():
    assert prepare_results("data/input.txt") == 1836


def test_combinations_simple():
    assert solve_combinations(read_input("data/small_test_input.txt")) == 8


def test_combinations_large():
    assert solve_combinations(read_input("data/large_test_input.txt")) == 19208


def test_combinations_real():
    assert solve_combinations(read_input("data/input.txt")) == 43406276662336


def prepare_results(file_name: str):
    return reduce(lambda x, y: x * y, solve_diffs(read_input(file_name)))


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f:
            lines.append(int(line.strip('\n')))
        return lines
