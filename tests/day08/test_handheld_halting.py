import os
from pathlib import Path

from main.day08.handheld_halting import solve
from main.day08.instruction import Instruction
from main.day08.operation import Operation


def test_simple():
    assert solve(read_input("data/test_input.txt")) == 5


def test_real():
    assert solve(read_input("data/input.txt")) == 2014


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f:
            trimmed_line = line.strip('\n')
            operation, argument = trimmed_line.split(' ')
            lines.append(Instruction(Operation[operation], int(argument)))
        return lines
