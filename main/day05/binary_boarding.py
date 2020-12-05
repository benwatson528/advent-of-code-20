from math import ceil

from main.day05.seat import Seat


def solve(command: str) -> Seat:
    row_range = [0, 127]
    column_range = [0, 7]
    for c in command:
        if c == 'F':
            row_range[1] = ((row_range[1] - row_range[0]) // 2) + row_range[0]
        elif c == 'B':
            row_range[0] = ceil((row_range[1] - row_range[0]) / 2) + row_range[0]
        elif c == 'L':
            column_range[1] = ((column_range[1] - column_range[0]) // 2) + column_range[0]
        elif c == 'R':
            column_range[0] = ceil((column_range[1] - column_range[0]) / 2) + column_range[0]

    return Seat(row_range[0], column_range[0], (row_range[0] * 8) + column_range[0])
