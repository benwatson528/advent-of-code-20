import os
from pathlib import Path

from main.day05.seat import Seat
from main.day05.binary_boarding import solve


def test_simple():
    assert solve("FBFBBFFRLR") == Seat(44, 5, 357)
    assert solve("BFFFBBFRRR") == Seat(70, 7, 567)
    assert solve("FFFBBBFRRR") == Seat(14, 7, 119)
    assert solve("BBFFBBFRLL") == Seat(102, 4, 820)


def test_real():
    assert max(map(lambda x: solve(x).seat_id, read_input("data/input.txt"))) == 915


def test_find_missing_seat():
    seats = map(lambda x: solve(x), read_input("data/input.txt"))
    seats = {(x.row, x.column): x.seat_id for x in seats}
    assert find_missing_seat_id(seats) == 699


def find_missing_seat_id(seats):
    seat_ids = seats.values()
    for i in range(128):
        for j in range(8):
            if not (i, j) in seats:
                seat_id = (i * 8) + j
                if seat_id - 1 in seat_ids and seat_id + 1 in seat_ids:
                    return seat_id
    return None


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f:
            lines.append(line.strip('\n'))
        return lines
