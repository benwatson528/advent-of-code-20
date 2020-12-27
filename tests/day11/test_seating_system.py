import operator
import os
from pathlib import Path
from typing import Set

from main.day11.seating_system import solve_adjacent, solve_visible, count_visible_tiles


def test_adjacent_simple():
    empty_seats, occupied_seats = read_input("data/test_input.txt")
    assert solve_adjacent(empty_seats, occupied_seats) == 37


def test_adjacent_real():
    empty_seats, occupied_seats = read_input("data/input.txt")
    assert solve_adjacent(empty_seats, occupied_seats) == 2468


def test_visible_diagonal():
    empty_seats, occupied_seats = read_input("data/small_diagonal.txt")
    assert count_visible_tiles(empty_seats, occupied_seats, (3, 4), operator.eq, 8)


def test_visible_no_occupied():
    empty_seats, occupied_seats = read_input("data/small_no_occupied.txt")
    assert count_visible_tiles(empty_seats, occupied_seats, (3, 3), operator.eq, 0)


def test_visible_one_empty():
    empty_seats, occupied_seats = read_input("data/small_one_empty.txt")
    assert count_visible_tiles(empty_seats, occupied_seats, (1, 1), operator.eq, 0)


def test_visible_simple():
    empty_seats, occupied_seats = read_input("data/test_input.txt")
    assert solve_visible(empty_seats, occupied_seats) == 26


def test_visible_real():
    empty_seats, occupied_seats = read_input("data/input.txt")
    assert solve_visible(empty_seats, occupied_seats) == 2214


def read_input(file_name) -> (Set, Set):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f:
            lines.append(line.strip('\n'))

    empty = set()
    occupied = set()
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == 'L':
                empty.add((j, i))
            elif lines[i][j] == '#':
                occupied.add((j, i))
    return empty, occupied
