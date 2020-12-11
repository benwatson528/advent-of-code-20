import operator
from typing import Callable, Set

AdjacencyFunction = Callable


def solve_adjacent(empty_seats: Set, occupied_seats: Set) -> int:
    return solve(empty_seats, occupied_seats, count_adjacent_tiles, 4)


def solve_visible(empty_seats: Set, occupied_seats: Set) -> int:
    return solve(empty_seats, occupied_seats, count_visible_tiles, 5)


def solve(empty_seats: Set, occupied_seats: Set, adjacency_function: AdjacencyFunction,
          empty_threshold: int) -> int:
    updated_empty_seats, updated_occupied_seats = update_grid(empty_seats, occupied_seats, adjacency_function,
                                                              empty_threshold)
    if updated_empty_seats == empty_seats and updated_occupied_seats == occupied_seats:
        return len(updated_occupied_seats)
    else:
        return solve(updated_empty_seats, updated_occupied_seats, adjacency_function, empty_threshold)


def update_grid(empty_seats: Set, occupied_seats: Set, adjacency_function: AdjacencyFunction,
                empty_threshold: int) -> (Set, Set):
    updated_empty_seats = set()
    updated_occupied_seats = set()
    for empty_seat in empty_seats:
        if adjacency_function(empty_seats, occupied_seats, empty_seat, operator.eq, 0):
            updated_occupied_seats.add(empty_seat)
        else:
            updated_empty_seats.add(empty_seat)

    for occupied_seat in occupied_seats:
        if adjacency_function(empty_seats, occupied_seats, occupied_seat, operator.ge, empty_threshold):
            updated_empty_seats.add(occupied_seat)
        else:
            updated_occupied_seats.add(occupied_seat)
    return updated_empty_seats, updated_occupied_seats


def count_adjacent_tiles(empty_seats: Set, occupied_seats: Set, coords: (int, int), equality_operator: operator,
                         threshold: int) -> bool:
    x, y = coords
    num_tiles = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if not (i == x and j == y) and (i, j) in occupied_seats:
                num_tiles += 1
    return equality_operator(num_tiles, threshold)


def count_visible_tiles(empty_seats: Set, occupied_seats: Set, coords: (int, int), equality_operator: operator,
                        threshold: int) -> bool:
    x, y = coords
    num_tiles = 0
    max_x, max_y = get_grid_bounds(empty_seats, occupied_seats)
    num_tiles += walk_right(empty_seats, occupied_seats, max_x, x, y)
    num_tiles += walk_left(empty_seats, occupied_seats, x, y)
    num_tiles += walk_down(empty_seats, occupied_seats, x, y)
    num_tiles += walk_up(empty_seats, occupied_seats, max_y, x, y)
    num_tiles += walk_diagonally_down_left(empty_seats, occupied_seats, max_x, max_y, x, y)
    num_tiles += walk_diagonally_down_right(empty_seats, occupied_seats, max_x, x, y)
    num_tiles += walk_diagonally_up_left(empty_seats, occupied_seats, max_y, x, y)
    num_tiles += walk_diagonally_up_right(empty_seats, occupied_seats, x, y)
    return equality_operator(num_tiles, threshold)


def walk_right(empty_seats, occupied_seats, max_x, x, y):
    for i in range(x + 1, max_x + 1):
        if (i, y) in empty_seats:
            break
        elif (i, y) in occupied_seats:
            return 1
    return 0


def walk_left(empty_seats, occupied_seats, x, y):
    for i in reversed(range(0, x)):
        if (i, y) in empty_seats:
            return 0
        elif (i, y) in occupied_seats:
            return 1
    return 0


def walk_down(empty_seats, occupied_seats, x, y):
    for j in reversed(range(0, y)):
        if (x, j) in empty_seats:
            return 0
        elif (x, j) in occupied_seats:
            return 1
    return 0


def walk_up(empty_seats, occupied_seats, max_y, x, y):
    for j in range(y + 1, max_y + 1):
        if (x, j) in empty_seats:
            return 0
        elif (x, j) in occupied_seats:
            return 1
    return 0


def walk_diagonally_down_left(empty_seats, occupied_seats, max_x, max_y, x, y):
    i = x + 1
    j = y + 1
    while i < max_x + 1 and j < max_y + 1:
        if (i, j) in empty_seats:
            return 0
        elif (i, j) in occupied_seats:
            return 1
        i += 1
        j += 1
    return 0


def walk_diagonally_down_right(empty_seats, occupied_seats, max_x, x, y):
    i = x + 1
    j = y - 1
    while i < max_x + 1 and j >= 0:
        if (i, j) in empty_seats:
            return 0
        elif (i, j) in occupied_seats:
            return 1
        i += 1
        j -= 1
    return 0


def walk_diagonally_up_left(empty_seats, occupied_seats, max_y, x, y):
    i = x - 1
    j = y + 1
    while i >= 0 and j < max_y + 1:
        if (i, j) in empty_seats:
            return 0
        elif (i, j) in occupied_seats:
            return 1
        i -= 1
        j += 1
    return 0


def walk_diagonally_up_right(empty_seats, occupied_seats, x, y):
    i = x - 1
    j = y - 1
    while i >= 0 and j >= 0:
        if (i, j) in empty_seats:
            return 0
        elif (i, j) in occupied_seats:
            return 1
        i -= 1
        j -= 1
    return 0


def get_grid_bounds(empty_seats: Set, occupied_seats: Set):
    max_x = max(set(map(lambda x: x[0], empty_seats)).union(set(map(lambda x: x[0], occupied_seats))))
    max_y = max(set(map(lambda x: x[1], empty_seats)).union(set(map(lambda x: x[1], occupied_seats))))
    return max_x, max_y
