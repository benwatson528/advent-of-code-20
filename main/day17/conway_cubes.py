from typing import Set

from main.day17.coord import Coord


def solve(grid: Set[Coord]) -> int:
    updated_grid = cycle(grid, 0)
    return len(updated_grid)


def cycle(cells: Set[Coord], turn_number: int) -> Set[Coord]:
    updated_cells = set()
    min_x, min_y, min_z = (min(c.x for c in cells), min(c.y for c in cells), min(c.z for c in cells))
    max_x, max_y, max_z = (max(c.x for c in cells), max(c.y for c in cells), max(c.z for c in cells))
    for i in range(min_x - 1, max_x + 2):
        for j in range(min_y - 1, max_y + 2):
            for k in range(min_z - 1, max_z + 2):
                current_coord = Coord(i, j, k)
                num_active_surrounding = count_active_surroundings(current_coord, cells)
                if (current_coord in cells and num_active_surrounding in range(2, 4)) or (
                        current_coord not in cells and num_active_surrounding == 3):
                    updated_cells.add(current_coord)

    if turn_number == 5:
        return updated_cells
    else:
        return cycle(updated_cells, turn_number + 1)


def count_active_surroundings(coord: Coord, cells: Set[Coord]) -> int:
    num_active_surrounding = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                if not (i == 0 and j == 0 and k == 0) and Coord(coord.x + i, coord.y + j, coord.z + k) in cells:
                    num_active_surrounding += 1
    return num_active_surrounding
