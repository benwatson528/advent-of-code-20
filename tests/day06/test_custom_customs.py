import os
from pathlib import Path
from typing import List

from main.day06.custom_customs import find_anyone_response, find_everyone_response


def test_anyone_simple():
    assert find_anyone_response(read_input("data/test_input.txt")) == 11


def test_anyone_real():
    assert find_anyone_response(read_input("data/input.txt")) == 6742


def test_everyone_simple():
    assert find_everyone_response(read_input("data/test_input.txt")) == 6


def test_everyone_real():
    assert find_everyone_response(read_input("data/input.txt")) == 3447


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
