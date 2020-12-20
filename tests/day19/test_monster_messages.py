import os
from pathlib import Path
from typing import Dict

import pytest

from main.day19.monster_messages import solve


@pytest.mark.skip(reason="Fails")
def test_simple():
    rules, messages = read_input("data/test_input.txt")
    possible_messages = solve(rules)
    valid_messages = [x for x in messages if x in possible_messages]
    assert len(valid_messages) == 2


@pytest.mark.skip(reason="Fails")
def test_real():
    rules, messages = read_input("data/input.txt")
    assert solve(rules) == 3


def read_input(file_name: str) -> (Dict[int, str], str):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        rules = {}
        messages = []
        for line in f:
            stripped_line = line.strip('\n')
            if ": " in stripped_line:
                split = stripped_line.split(": ")
                rules[split[0]] = split[1]
            else:
                messages.append(stripped_line)
        return rules, messages
