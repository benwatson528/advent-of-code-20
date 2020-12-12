import os
import re
from pathlib import Path

from main.day12.instruction import Instruction
from main.day12.rain_risk import solve_ship_movement, solve_waypoint_movement


def test_ship_simple():
    assert solve_ship_movement(read_input("data/test_input.txt")) == 25


def test_part_1_real():
    assert solve_ship_movement(read_input("data/input.txt")) == 1441


def test_waypoint_simple():
    assert solve_waypoint_movement(read_input("data/test_input.txt")) == 286


def test_part_2_real():
    assert solve_waypoint_movement(read_input("data/input.txt")) == 61616

def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f:
            regex = re.search(r"^([A-Z])(\d*)$", line)
            lines.append(Instruction(regex.group(1), int(regex.group(2))))
        return lines
