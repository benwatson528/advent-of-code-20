from dataclasses import dataclass
from typing import List, Set


def solve(tiles: List[List[str]]) -> int:
    flipped_tiles = set()
    for tile in tiles:
        coord = Coord(0, 0)
        for movement in tile:
            coord = move(coord, movement)
        update_tiles(coord, flipped_tiles)

    return len(flipped_tiles)


@dataclass(frozen=True)
class Coord:
    x: int
    y: int


# Axial coords - https://www.redblobgames.com/grids/hexagons/#coordinates-axial
def move(coord: Coord, movement: str) -> Coord:
    if movement == "se":
        coord = Coord(coord.x, coord.y + 1)
    elif movement == "sw":
        coord = Coord(coord.x - 1, coord.y + 1)
    elif movement == "nw":
        coord = Coord(coord.x, coord.y - 1)
    elif movement == "ne":
        coord = Coord(coord.x + 1, coord.y - 1)
    elif movement == "e":
        coord = Coord(coord.x + 1, coord.y)
    elif movement == "w":
        coord = Coord(coord.x - 1, coord.y)
    return coord


def update_tiles(coord: Coord, flipped_tiles: Set[Coord]):
    if coord in flipped_tiles:
        flipped_tiles.remove(coord)
    else:
        flipped_tiles.add(coord)
