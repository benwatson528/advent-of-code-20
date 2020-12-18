import os
from pathlib import Path

from main.day18.operation_order import solve


def test_no_precedence_simple():
    assert solve("1 + 2 * 3 + 4 * 5 + 6") == 71
    assert solve("1 + (2 * 3) + (4 * (5 + 6))") == 51
    assert solve("2 * 3 + (4 * 5)") == 26
    assert solve("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 437
    assert solve("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 12240
    assert solve("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 13632


def test_no_precedence_real():
    assert sum(solve(x) for x in read_input("data/input.txt")) == 21022630974613


def test_addition_precedence_simple():
    assert solve("1 + 2 * 3 + 4 * 5 + 6", True) == 231
    assert solve("1 + (2 * 3) + (4 * (5 + 6))", True) == 51
    assert solve("2 * 3 + (4 * 5)", True) == 46
    assert solve("5 + (8 * 3 + 9 + 3 * 4 * 3)", True) == 1445
    assert solve("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", True) == 669060
    assert solve("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", True) == 23340


def test_addition_precedence_real():
    assert sum(solve(x, True) for x in read_input("data/input.txt")) == 169899524778212


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f:
            lines.append(line.strip('\n'))
        return lines
