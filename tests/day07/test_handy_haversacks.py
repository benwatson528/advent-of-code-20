import os
from pathlib import Path

from main.day07.handy_haversacks import solve_holders, solve_contents


def test_different_bags_simple():
    assert solve_holders(read_input("data/test_input.txt")) == 4


def test_different_bags_real():
    assert solve_holders(read_input("data/input.txt")) == 300


def test_count_bags_simple():
    assert solve_contents(read_input("data/test_input.txt")) == 32


def test_count_bags_complex():
    assert solve_contents(read_input("data/complex_test_input.txt")) == 126


def test_count_bags_real():
    assert solve_contents(read_input("data/input.txt")) == 8030


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return f.read().splitlines()
