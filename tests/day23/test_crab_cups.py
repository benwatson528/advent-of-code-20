from typing import Dict

import pytest

from main.day23.crab_cups import solve


def test_part_one_simple():
    end_cups = solve([int(c) for c in "389125467"], 100)
    assert pivot_answer(end_cups) == "67384529"


def test_part_one_real():
    end_cups = solve([int(c) for c in "219347865"], 100)
    assert pivot_answer(end_cups) == "36472598"


@pytest.mark.skip(reason="Takes about 11s")
def test_part_two_simple():
    cups = [int(c) for c in "389125467"] + list(range(10, 1000001))
    end_cups = solve(cups, 10000000)
    assert end_cups[1] * end_cups[end_cups[1]] == 149245887792


@pytest.mark.skip(reason="Takes about 11s")
def test_part_two_real():
    cups = [int(c) for c in "219347865"] + list(range(10, 1000001))
    end_cups = solve(cups, 10000000)
    assert end_cups[1] * end_cups[end_cups[1]] == 90481418730


def pivot_answer(end_cups: Dict[int, int]) -> str:
    ans = ""
    next_cup = 1
    for _ in range(1, 9):
        next_cup = end_cups[next_cup]
        ans += str(next_cup)
    return ans
