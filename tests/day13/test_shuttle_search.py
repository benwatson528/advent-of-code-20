import os
import re
from pathlib import Path

from main.day13.shuttle_search import solve


def test_simple():
    time, bus_ids = read_input("data/test_input.txt")
    assert solve(time, bus_ids) == 295


def test_real():
    time, bus_ids = read_input("data/input.txt")
    assert solve(time, bus_ids) == 370


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        time = int(f.readline().strip("\n"))
        bus_ids = [int(s) for s in re.findall(r'\d+', f.readline().strip("\n"))]
        return time, bus_ids
