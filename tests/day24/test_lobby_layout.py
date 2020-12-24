import os
import re
from pathlib import Path
from typing import List

from main.day24.lobby_layout import solve


def test_simple():
    assert solve(read_input("data/test_input.txt")) == 10


def test_real():
    assert solve(read_input("data/input.txt")) == 244


def read_input(file_name) -> List[List[str]]:
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f:
            lines.append([m.group() for m in re.finditer(r"(se)|(sw)|(nw)|(ne)|(e)|(w)", line)])
        return lines
