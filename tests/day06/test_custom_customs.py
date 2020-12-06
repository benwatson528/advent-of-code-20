import os
from pathlib import Path
from typing import List

from main.day06.custom_customs import solve


def test_simple():
    assert solve(read_input("data/test_input.txt")) == 11


def test_real():
    assert solve(read_input("data/input.txt")) == 6742


def read_input(file_name) -> List[List[str]]:
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        groups = []
        group = []
        for line in f:
            line = line.strip('\n')
            if not line:
                groups.append(group)
                group = []
            else:
                group.append(line.strip('\n'))
        groups.append(group)
        return groups
