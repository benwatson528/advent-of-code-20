import os
import re
from pathlib import Path

from main.day13.shuttle_search import solve_first_bus, solve_consecutive_bus


def test_first_bus_simple():
    time, bus_ids = read_part_one_input("data/test_input.txt")
    assert solve_first_bus(time, bus_ids) == 295


def test_first_bus_real():
    time, bus_ids = read_part_one_input("data/input.txt")
    assert solve_first_bus(time, bus_ids) == 370


def test_consecutive_bus_simple_one():
    assert solve_consecutive_bus(parse_whole_line("7,13,x,x,59,x,31,19")) == 1068781


def test_consecutive_bus_simple_two():
    assert solve_consecutive_bus(parse_whole_line("17,x,13,19")) == 3417


def test_consecutive_bus_simple_three():
    assert solve_consecutive_bus(parse_whole_line("67,7,59,61")) == 754018


def test_consecutive_bus_simple_four():
    assert solve_consecutive_bus(parse_whole_line("67,x,7,59,61")) == 779210


def test_consecutive_bus_simple_five():
    assert solve_consecutive_bus(parse_whole_line("67,7,x,59,61")) == 1261476


def test_consecutive_bus_simple_six():
    assert solve_consecutive_bus(parse_whole_line("1789,37,47,1889")) == 1202161486


def test_consecutive_bus_real():
    bus_ids = read_part_two_input("data/input.txt")
    assert solve_consecutive_bus(bus_ids) == 894954360381385


def read_part_one_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        time = int(f.readline().strip("\n"))
        bus_ids = [int(s) for s in re.findall(r'\d+', f.readline().strip("\n"))]
        return time, bus_ids


def read_part_two_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        f.readline()
        return parse_whole_line(f.readline())


def parse_whole_line(line):
    return [s for s in line.strip("\n").split(",")]
