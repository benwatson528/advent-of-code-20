import os
from pathlib import Path
from typing import Set

import pytest

from main.day17.conway_cubes import solve_3d, solve_4d
from main.day17.coord import Coord


def test_3d_simple():
    assert solve_3d(read_input("data/test_input.txt")) == 112


def test_3d_real():
    assert solve_3d(read_input("data/input.txt")) == 265


@pytest.mark.skip(reason="Takes about 6s")
def test_4d_simple():
    assert solve_4d(read_input("data/test_input.txt")) == 848


@pytest.mark.skip(reason="Takes about 12s")
def test_4d_real():
    assert solve_4d(read_input("data/input.txt")) == 1936


def read_input(file_name) -> Set[Coord]:
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f:
            lines.append(line.strip('\n'))
        cubes = set()
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                current_cell = lines[i][j]
                if current_cell == "#":
                    cubes.add(Coord(i, j, 0))
        return cubes
