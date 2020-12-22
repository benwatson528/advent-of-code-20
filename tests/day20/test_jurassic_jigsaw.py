import os
import re
from collections import defaultdict
from pathlib import Path
from typing import List, Dict

import pytest

from main.day20.jurassic_jigsaw import solve
from main.day20.tile import Tile


@pytest.mark.skip(reason="Not implemented")
def test_simple():
    assert solve(read_input("data/test_input.txt")) == 3


@pytest.mark.skip(reason="Not implemented")
def test_real():
    assert solve(read_input("data/input.txt")) == 3


def read_input(file_name: str) -> Dict[int, Tile]:
    tiles = defaultdict(Tile)
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        for line in f:
            stripped_line = line.strip('\n')
            if stripped_line.startswith("Tile"):
                tile_id = int(re.search(r'\d+', stripped_line).group())
                tile = []
            elif len(stripped_line) == 0:
                tiles[tile_id] = parse_tile(tile_id, tile)
                tile = []
            else:
                tile.append(stripped_line)
        tiles[tile_id] = parse_tile(tile_id, tile)
        return tiles


def parse_tile(tile_id: int, raw_tile: List[str]):
    return Tile(tile_id, raw_tile[0], raw_tile[-1], raw_tile[0], raw_tile[0], 0, False, raw_tile)
