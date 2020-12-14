import os
import re
from pathlib import Path
from typing import List

from main.day14.docking_data import solve
from main.day14.instruction import Instruction


def test_simple():
    assert solve(read_input("data/test_input.txt")) == 165


def test_real():
    assert solve(read_input("data/input.txt")) == 13556564111697


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
