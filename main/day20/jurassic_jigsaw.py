from typing import Dict, List, Set


def solve(raw_tiles: Dict[int, List[str]]) -> Set[int]:
    all_sides = get_all_sides(raw_tiles)
    corner_tiles = find_corner_tiles(all_sides)
    return corner_tiles


def find_corner_tiles(tiles: Dict[int, List[str]]) -> Set[int]:
    corner_tiles = set()
    for tile_id, sides in tiles.items():
        # Only compare against the original 4 sides - the flipped sides are accounted for in the main tiles list
        num_unique_sides = sum(1 for i in range(4) if is_unique_side(sides[i], tile_id, tiles))
        if num_unique_sides == 2:
            corner_tiles.add(tile_id)
    return corner_tiles


def get_column(tile: List[str], idx: int) -> List[str]:
    return [row[idx] for row in tile]


def is_unique_side(side: str, tile_id: int, tiles: Dict[int, List[str]]) -> bool:
    for iter_tile_id, iter_sides in tiles.items():
        if iter_tile_id == tile_id:
            continue
        for iter_side in iter_sides:
            if side == iter_side:
                return False
    return True


def get_all_sides(tiles: Dict[int, List[str]]) -> Dict[int, List[str]]:
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
