import math
import os
import re
from collections import defaultdict
from pathlib import Path
from typing import List, Dict

from main.day20.jurassic_jigsaw import solve


def test_simple():
    corner_tiles = solve(read_input("data/test_input.txt"))
    assert math.prod(corner_tiles) == 20899048083289


def test_real():
    corner_tiles = solve(read_input("data/input.txt"))
    assert math.prod(corner_tiles) == 15003787688423


def read_input(file_name: str) -> Dict[int, List[str]]:
    tiles = defaultdict(List[str])
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        for line in f:
            stripped_line = line.strip('\n')
            if stripped_line.startswith("Tile"):
                tile_id = int(re.search(r'\d+', stripped_line).group())
                tile = []
            elif len(stripped_line) == 0:
                tiles[tile_id] = tile
                tile = []
            else:
                tile.append(stripped_line)
        tiles[tile_id] = tile
        return tiles
