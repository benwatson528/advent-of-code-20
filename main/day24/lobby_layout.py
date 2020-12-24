from dataclasses import dataclass
from typing import List, Set


@dataclass(frozen=True)
class Coord:
    x: int
    y: int


def solve_place_tiles(tiles: List[List[str]]) -> Set[Coord]:
    flipped_tiles = set()
    for tile in tiles:
        coord = Coord(0, 0)
        for movement in tile:
            coord = move(coord, movement)
        update_tiles(coord, flipped_tiles)
    return flipped_tiles


def solve_update_tiles(tiles: List[List[str]], num_days: int) -> Set[Coord]:
    updated_flipped_tiles = solve_place_tiles(tiles)
    for _ in range(num_days):
        updated_flipped_tiles = progress_day(updated_flipped_tiles)
    return updated_flipped_tiles


def progress_day(flipped_tiles: Set[Coord]):
    updated_flipped_tiles = flipped_tiles.copy()
    min_x, min_y = (min(c.x for c in flipped_tiles), min(c.y for c in flipped_tiles))
    max_x, max_y = (max(c.x for c in flipped_tiles), max(c.y for c in flipped_tiles))
    for i in range(min_x - 1, max_x + 2):
        for j in range(min_y - 1, max_y + 2):
            coord = Coord(i, j)
            num_black_adjacent_tiles = find_black_adjacent_tiles(coord, flipped_tiles)
            is_black_tile = coord in flipped_tiles
            if is_black_tile and (num_black_adjacent_tiles == 0 or num_black_adjacent_tiles > 2):
                updated_flipped_tiles.remove(coord)
            elif not is_black_tile and num_black_adjacent_tiles == 2:
                updated_flipped_tiles.add(coord)
    return updated_flipped_tiles


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


def find_black_adjacent_tiles(coord: Coord, flipped_tiles: Set[Coord]) -> int:
    adjacent_tiles = {Coord(coord.x, coord.y + 1),
                      Coord(coord.x - 1, coord.y + 1),
                      Coord(coord.x, coord.y - 1),
                      Coord(coord.x + 1, coord.y - 1),
                      Coord(coord.x + 1, coord.y),
                      Coord(coord.x - 1, coord.y)}
    return len(set.intersection(adjacent_tiles, flipped_tiles))
