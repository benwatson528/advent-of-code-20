import re
import sys
import urllib.request
from urllib.error import URLError

from setup import file_creator

BASE_URL = "https://adventofcode.com/2020/day/"


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


def read_template_file(template_file_name):
    return open(f"templates/{template_file_name}_template.txt").read()


day = int(input("Please enter a day to be setup: "))
puzzle_name = get_puzzle_name(f"{BASE_URL}{day}")
print(f"Puzzle name: {puzzle_name}")

file_creator.create_python_file(f"{puzzle_name}.py", day, "main", read_template_file("main"))
file_creator.create_python_file(f"test_{puzzle_name}.py", day, "tests",
                                read_template_file("test").format(day=day, puzzle_name=puzzle_name))
file_creator.create_test_data_file(day, "test_input.txt")
file_creator.create_test_data_file(day, "input.txt")
