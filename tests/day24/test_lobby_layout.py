import os
import re
from pathlib import Path
from typing import List

import pytest

from main.day24.lobby_layout import solve_place_tiles, solve_update_tiles


def test_place_tiles_simple():
    assert len(solve_place_tiles(read_input("data/test_input.txt"))) == 10


def test_place_tiles_real():
    assert len(solve_place_tiles(read_input("data/input.txt"))) == 244


def test_update_tiles_simple():
    assert len(solve_update_tiles(read_input("data/test_input.txt"), 100)) == 2208


@pytest.mark.skip(reason="Takes about 5s")
def test_update_tiles_real():
    assert len(solve_update_tiles(read_input("data/input.txt"), 100)) == 3665


def read_input(file_name) -> List[List[str]]:
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f:
            lines.append([m.group() for m in re.finditer(r"(se)|(sw)|(nw)|(ne)|(e)|(w)", line)])
        return lines
