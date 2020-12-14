import os
import re
from pathlib import Path
from typing import List

from main.day14.docking_data import solve_static, solve_floating
from main.day14.instruction import Instruction


def test_static_simple():
    assert solve_static(read_input("data/test_static_input.txt")) == 165


def test_static_real():
    assert solve_static(read_input("data/input.txt")) == 13556564111697


def test_floating_simple():
    assert solve_floating(read_input("data/test_floating_input.txt")) == 208


def test_floating_real():
    assert solve_floating(read_input("data/input.txt")) == 4173715962894


def read_input(file_name) -> List[Instruction]:
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        instructions = []
        current_mask = ""
        for line in f:
            line = line.strip("\n")
            if line.startswith("mask"):
                current_mask = line.split(" = ")[1]
            else:
                nums = [int(s) for s in re.findall(r'\d+', line)]
                instructions.append(Instruction(current_mask, nums[0], nums[1]))
        return instructions
