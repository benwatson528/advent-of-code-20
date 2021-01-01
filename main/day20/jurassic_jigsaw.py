import math
from typing import Dict, List, Set

import regex as re

RIGHT = "right"
LEFT = "left"
BOTTOM = "bottom"
TOP = "top"

Tiles = Dict[int, List[str]]

ANY_VALUE = "any"
UNIQUE_VALUE = "unique"

puzzle_size_length = 0


def solve_corners(raw_tiles: Tiles) -> Set[int]:
    all_sides = get_all_sides(raw_tiles)
    return find_outer_edge_tiles(all_sides, 2)


def solve_loch_ness(raw_tiles: Tiles) -> int:
    global puzzle_size_length
    puzzle_size_length = int(math.sqrt(len(raw_tiles)))
    all_sides = get_all_sides(raw_tiles)
    final_grid = build_grid(raw_tiles, all_sides)
    borderless = remove_borders(final_grid)
    num_loch_ness = find_loch_ness(borderless)
    loch_ness_pixels = 15
    num_hashes = sum(row.count('#') for row in borderless)
    roughness = num_hashes - (num_loch_ness * loch_ness_pixels)
    return roughness


def remove_borders(final_grid: List[str]) -> List[str]:
    borderless_grid = []
    current_row = 0
    for j in range(puzzle_size_length * 10):
        j_s = str(j)
        if j_s.endswith("0") or j_s.endswith("9"):
            continue
        else:
            borderless_grid.append("")
        for i in range(puzzle_size_length * 10):
            i_s = str(i)
            if not i_s.endswith("0") and not i_s.endswith("9"):
                borderless_grid[current_row] += final_grid[j][i]
        current_row += 1
    return borderless_grid


def find_loch_ness(grid: List[str]) -> int:
    loch_ness = r""".{18}#.{1}
#.{4}##.{4}##.{4}###
.{1}#.{2}#.{2}#.{2}#.{2}#.{2}#.{3}
""".split("\n")
    num_loch_ness = 0
    for transposition in transpose_tile(grid):
        for j in range(len(transposition) - 2):
            loch_ness_top_starts = set(m.start() for m in re.finditer(loch_ness[0], transposition[j], overlapped=True))
            loch_ness_middle_starts = set(
                m.start() for m in re.finditer(loch_ness[1], transposition[j + 1], overlapped=True))
            loch_ness_bottom_starts = set(
                m.start() for m in re.finditer(loch_ness[2], transposition[j + 2], overlapped=True))
            for top_start in loch_ness_top_starts:
                if top_start in loch_ness_middle_starts and top_start in loch_ness_bottom_starts:
                    num_loch_ness += 1
    return num_loch_ness


def find_outer_edge_tiles(tiles: Tiles, threshold: int) -> Set[int]:
    corner_tiles = set()
    for tile_id, sides in tiles.items():
        # Only compare against the original 4 sides - the flipped sides are accounted for in the main tiles list
        num_unique_sides = sum(1 for i in range(4) if is_unique_side(sides[i], tile_id, tiles))
        if num_unique_sides == threshold:
            corner_tiles.add(tile_id)
    return corner_tiles


def get_column(tile: List[str], idx: int) -> List[str]:
    return [row[idx] for row in tile]


def is_unique_side(side: str, tile_id: int, tiles: Tiles) -> bool:
    for iter_tile_id, iter_sides in tiles.items():
        if iter_tile_id == tile_id:
            continue
        for iter_side in iter_sides:
            if side == iter_side:
                return False
    return True


def get_all_sides(tiles: Tiles) -> Tiles:
    all_sides = {}
    for tile_id, tile in tiles.items():
        left_side = ''.join(get_column(tile, 0))
        left_side_reversed = ''.join(left_side[::-1])
        right_side = ''.join(get_column(tile, len(tile) - 1))
        right_side_reversed = ''.join(right_side[::-1])
        top = tile[0]
        top_reversed = top[::-1]
        bottom = tile[-1]
        bottom_reversed = bottom[::-1]
        all_sides[tile_id] = [left_side, right_side, top, bottom, left_side_reversed, right_side_reversed, top_reversed,
                              bottom_reversed]
    return all_sides


def build_grid(tiles: Tiles, all_sides: Tiles) -> List[str]:
    final_grid = [" " * 10 * puzzle_size_length] * puzzle_size_length * 10
    for j in range(0, puzzle_size_length):
        for i in range(0, puzzle_size_length):
            sides_to_fit = {TOP: find_top_bound(final_grid, i, j), BOTTOM: find_bottom_bound(final_grid, i, j),
                            LEFT: find_left_bound(final_grid, i, j), RIGHT: find_right_bound(final_grid, i, j)}
            matching_tiles = find_matching_tiles(sides_to_fit, tiles, all_sides)
            if len(matching_tiles) == 0:
                return []
            else:
                # We can safely take the first one because there is only one possible tile for each position
                tile_id, tile = next(iter(matching_tiles.items()))
                final_grid = add_tile_to_grid(tile, i, j, final_grid)
                tiles.pop(tile_id)
    return final_grid


def find_right_bound(final_grid: List[str], i: int, j: int) -> str:
    if i == puzzle_size_length - 1:
        return UNIQUE_VALUE
    else:
        right_border = ''.join(get_column(final_grid, (i * 10) + 10)[j * 10:(j * 10) + 10])
        return ANY_VALUE if right_border.isspace() else right_border


def find_left_bound(final_grid: List[str], i: int, j: int) -> str:
    if i == 0:
        return UNIQUE_VALUE
    else:
        left_border = ''.join(get_column(final_grid, (i * 10) - 1)[(j * 10):(j * 10) + 10])
        return ANY_VALUE if left_border.isspace() else left_border


def find_top_bound(final_grid: List[str], i: int, j: int) -> str:
    if j == 0:
        return UNIQUE_VALUE
    else:
        top_border = final_grid[(j * 10) - 1][(i * 10):(i * 10) + 10]
        return ANY_VALUE if top_border.isspace() else top_border


def find_bottom_bound(final_grid: List[str], i: int, j: int) -> str:
    if j == puzzle_size_length - 1:
        return UNIQUE_VALUE
    else:
        bottom_border = final_grid[(j * 10) + 10][i * 10:(i * 10) + 10]
        return ANY_VALUE if bottom_border.isspace() else bottom_border


def add_tile_to_grid(tile: List[str], i: int, j: int, final_grid: List[str]) -> List[str]:
    for y in range(10):
        row_to_update = (j * 10) + y
        before = final_grid[(j * 10) + y][:i * 10]
        during = tile[y]
        after = final_grid[(j * 10) + y][(i * 10) + 10:]
        final_grid[row_to_update] = before + during + after
    return final_grid


def find_matching_tiles(sides_to_fit: Dict[str, str], tiles: Tiles, all_sides: Tiles) -> Tiles:
    matching_tiles = {}
    for tile_id, tile in tiles.items():
        for transposed in transpose_tile(tile):
            if sides_match(sides_to_fit, transposed, tile_id, all_sides):
                matching_tiles[tile_id] = transposed
    return matching_tiles


# All the ways that a tile can be transposed:
# https://forums.ni.com/t5/LabVIEW/mirroring-and-flipping-a-matrix/td-p/833083?profile.language=en
def transpose_tile(tile: List[str]) -> List[List[str]]:
    rotated_90 = rotate_90(tile)
    rotated_180 = rotate_90(rotated_90)
    rotated_270 = rotate_90(rotated_180)
    vertical_flip = [i for i in reversed(tile)]
    transposed = rotate_90(vertical_flip)
    horizontal_flip = rotate_90(transposed)
    diagonal_flip = rotate_90(horizontal_flip)
    return [tile, rotated_90, rotated_180, rotated_270, vertical_flip, horizontal_flip, diagonal_flip, transposed]


def sides_match(sides_to_fit: Dict[str, str], transposed: List[str], tile_id: int, all_sides: Tiles) -> bool:
    if not match_top(all_sides, sides_to_fit, tile_id, transposed):
        return False
    if not match_bottom(all_sides, sides_to_fit, tile_id, transposed):
        return False
    if not match_left(all_sides, sides_to_fit, tile_id, transposed):
        return False
    if not match_right(all_sides, sides_to_fit, tile_id, transposed):
        return False
    return True


def match_top(all_sides: Tiles, sides_to_fit: Dict[str, str], tile_id: int, transposed: List[str]) -> bool:
    if sides_to_fit[TOP] == UNIQUE_VALUE:
        return is_unique_side(transposed[0], tile_id, all_sides)
    elif sides_to_fit[TOP] == ANY_VALUE:
        return True
    else:
        return transposed[0] == sides_to_fit[TOP]


def match_bottom(all_sides: Tiles, sides_to_fit: Dict[str, str], tile_id: int, transposed: List[str]) -> bool:
    if sides_to_fit[BOTTOM] == UNIQUE_VALUE:
        return is_unique_side(transposed[-1], tile_id, all_sides)
    elif sides_to_fit[BOTTOM] == ANY_VALUE:
        return True
    else:
        return transposed[-1] == sides_to_fit[BOTTOM]


def match_left(all_sides: Tiles, sides_to_fit: Dict[str, str], tile_id: int, transposed: List[str]) -> bool:
    left_col = ''.join(get_column(transposed, 0))
    if sides_to_fit[LEFT] == UNIQUE_VALUE:
        return is_unique_side(left_col, tile_id, all_sides)
    elif sides_to_fit[LEFT] == ANY_VALUE:
        return True
    else:
        return left_col == sides_to_fit[LEFT]


def match_right(all_sides: Tiles, sides_to_fit: Dict[str, str], tile_id: int, transposed: List[str]) -> bool:
    right_col = ''.join(get_column(transposed, -1))
    if sides_to_fit[RIGHT] == UNIQUE_VALUE:
        return is_unique_side(right_col, tile_id, all_sides)
    elif sides_to_fit[RIGHT] == ANY_VALUE:
        return True
    else:
        return right_col == sides_to_fit[RIGHT]


def rotate_90(tile: List[str]) -> List[str]:
    return [''.join(row) for row in zip(*reversed(tile))]


def print_grid(final_grid: List[str]):
    print()
    pixel_dimension = len(final_grid)
    for i in range(pixel_dimension):
        print()
        if i % 10 == 0:
            print("-" * (pixel_dimension + (pixel_dimension // 10) + 1))
        for j in range(pixel_dimension):
            if j % 10 == 0:
                print("|", end='')
            print(final_grid[i][j], end='')
            if j == pixel_dimension - 1:
                print("|", end='')
    print()
    print("-" * (pixel_dimension + (pixel_dimension // 10) + 1))
