import os
from pathlib import Path
import re
import sys
import urllib.request
from urllib.error import URLError

BASE_URL = "https://adventofcode.com/2019/day/"


def get_puzzle_name(puzzle_url):
    """
    Finds the name of the given day's puzzle and formats it into a string that can be used for a Python class by
    lower-casing and replacing spaces with underscores. If the resulting string starts with a number, "a_" is added as a
    prefix.
    :param puzzle_url: the URL of the given day"s puzzle
    :return: the puzzle name
    """
    try:
        with urllib.request.urlopen(puzzle_url) as f:
            print(f"Retrieving contents of {puzzle_url}")
            entirePage = f.read().decode("utf-8")
            raw_puzzle_name = re.search("--- (.*) ---", entirePage).group(1).split(": ")[1]
            parsed_puzzle_name = "a_" + raw_puzzle_name if raw_puzzle_name[0].isnumeric() else raw_puzzle_name
            return parsed_puzzle_name.lower().replace(" ", "_")
    except URLError as e:
        sys.exit(e.reason)


def create_file(file_name, day_number, file_type, contents=None):
    script_dir = os.path.dirname(__file__)
    file_dir = os.path.join(script_dir, "..", file_type, f"day{day_number:02d}")
    os.makedirs(file_dir, exist_ok=True)
    file_path = os.path.join(script_dir, file_dir, file_name)
    print(f"Creating file {file_path}")
    with open(file_path, "w") as f:
        if contents:
            f.write(contents)


day = int(input("Please enter a day to be setup: "))
puzzle_name = get_puzzle_name(f"{BASE_URL}{day}")
print(f"Puzzle name: {puzzle_name}")
create_file(f"{puzzle_name}.py", day, "main")
create_file(f"test_{puzzle_name}.py", day, "test", f"from main.day{day:02d}.{puzzle_name} import solve")
