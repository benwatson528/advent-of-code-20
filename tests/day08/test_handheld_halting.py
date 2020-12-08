import os
from pathlib import Path

from main.day08.handheld_halting import solve, fix
from main.day08.instruction import Instruction
from main.day08.operation import Operation


def test_infinite_simple():
    assert solve(read_input("data/test_input.txt")) == (5, False)


def test_infinite_real():
    assert solve(read_input("data/input.txt")) == (2014, False)


def test_terminate_simple():
    assert fix(read_input("data/test_input.txt")) == (8, True)


def test_terminate_real():
    assert fix(read_input("data/input.txt")) == (2251, True)


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f:
            trimmed_line = line.strip('\n')
            operation, argument = trimmed_line.split(' ')
            lines.append(Instruction(Operation[operation], int(argument)))
        return lines
