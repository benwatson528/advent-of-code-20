from typing import Dict

from main.day23.crab_cups import solve


def test_part_one_simple():
    end_cups = solve("389125467", 100)
    assert pivot_answer(end_cups) == "67384529"


def test_part_one_real():
    end_cups = solve("219347865", 100)
    assert pivot_answer(end_cups) == "36472598"


def test_part_two_simple():
    end_cups = solve("389125467", 100)
    assert pivot_answer(end_cups) == "67384529"


def test_part_two_real():
    end_cups = solve("219347865", 100)
    assert pivot_answer(end_cups) == "36472598"


def pivot_answer(end_cups: Dict[int, int]) -> str:
    ans = ""
    next_cup = 1
    for _ in range(1, 9):
        next_cup = end_cups[next_cup]
        ans += str(next_cup)
    return ans
