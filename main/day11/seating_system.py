from typing import List, Optional, Callable

Grid = List[str]


def solve(grid: Grid) -> int:
    updated_grid = update_grid(grid, count_adjacent_tiles)
    if updated_grid == grid:
        tiles = count_all_tiles(updated_grid, '#')
        return tiles
    else:
        return solve(updated_grid)


def update_grid(grid: Grid, adjacency_function: Callable[[Grid, str, int, int], int]) -> List[str]:
    updated_grid = []
    for i in range(len(grid)):
        updated_grid.append("")
        for j in range(len(grid[0])):
            current_tile = grid[i][j]
            if current_tile == 'L' and adjacency_function(grid, '#', i, j) == 0:
                updated_grid[i] += '#'
            elif current_tile == '#' and adjacency_function(grid, '#', i, j) >= 4:
                updated_grid[i] += 'L'
            else:
                updated_grid[i] += current_tile
    return updated_grid


def count_all_tiles(grid: Grid, tile: str) -> int:
    num_seats = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == tile:
                num_seats += 1
    return num_seats


def count_adjacent_tiles(grid: Grid, tile: str, x: int, y: int) -> int:
    num_tiles = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            not_current = not (i == x and j == y)
            found_tile = get_tile(grid, i, j)
            is_desired_tile = found_tile == tile
            if not_current and is_desired_tile:
                num_tiles += 1
    return num_tiles


def get_tile(grid: Grid, x: int, y: int) -> Optional[str]:
    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
        return None
    else:
        return grid[x][y]
