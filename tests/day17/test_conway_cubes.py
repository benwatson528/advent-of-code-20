import os
from pathlib import Path
from typing import Set

from main.day17.conway_cubes import solve
from main.day17.coord import Coord


def test_simple():
    assert solve(read_input("data/test_input.txt")) == 112


def test_real():
    assert solve(read_input("data/input.txt")) == 265


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
