import os
import re
from pathlib import Path

from main.day12.instruction import Instruction
from main.day12.rain_risk import solve


def test_simple():
    assert solve(read_input("data/test_input.txt")) == 25


def test_real():
    assert solve(read_input("data/input.txt")) == 1441


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f:
            regex = re.search(r"^([A-Z])(\d*)$", line)
            lines.append(Instruction(regex.group(1), int(regex.group(2))))
        return lines
