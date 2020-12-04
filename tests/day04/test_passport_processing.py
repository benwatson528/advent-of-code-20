import os
from pathlib import Path

from main.day04.passport_processing import solve


def test_simple():
    data = read_input("data/test_input.txt")
    assert solve(data) == 2


def test_real():
    data = read_input("data/input.txt")
    assert solve(data) == 170


def test_validation_simple():
    data = read_input("data/validated_test_input.txt")
    assert solve(data, True) == 4


def test_validation_real():
    data = read_input("data/input.txt")
    assert solve(data, True) == 103


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return f.read()
