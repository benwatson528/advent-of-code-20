import pytest

from main.day15.rambunctious_recitation import solve


def test_simple():
    assert solve(parse_input("0,3,6"), 10) == 0


def test_part_one_real():
    assert solve(parse_input("11,0,1,10,5,19"), 2020) == 870


@pytest.mark.skip(reason="Takes about 30s")
def test_part_2_real():
    assert solve(parse_input("11,0,1,10,5,19"), 30000000) == 9136


def parse_input(line):
    return [int(x) for x in line.split(",")]
