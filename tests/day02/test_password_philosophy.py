import os
from pathlib import Path

from main.day02.password_philosophy import validate_occurrences, validate_positions
from main.day02.policy import Policy


def test_occurrences_simple():
    password_db = read_input("data/test_input.txt")
    assert validate_occurrences(password_db) == 2


def test_occurrences_real():
    password_db = read_input("data/input.txt")
    assert validate_occurrences(password_db) == 548


def test_positions_simple():
    password_db = read_input("data/test_input.txt")
    assert validate_positions(password_db) == 1


def test_positions_real():
    password_db = read_input("data/input.txt")
    assert validate_positions(password_db) == 502


def read_input(file_name):
    f = open(os.path.join(Path(__file__).parent.absolute(), file_name))
    password_db = []
    for line in f:
        split_line = line.strip('\n').split(' ')
        policy_bounds = split_line[0].split('-')
        policy_letter = split_line[1][0]
        password = split_line[2]
        password_db.append((Policy(int(policy_bounds[0]), int(policy_bounds[1]), policy_letter), password))
    return password_db
