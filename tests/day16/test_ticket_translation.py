import math
import os
import re
from enum import Enum
from pathlib import Path

from main.day16.notes import Notes
from main.day16.ticket_translation import solve_find_invalid, solve_match_fields


def test_find_invalid_simple():
    assert solve_find_invalid(read_input("data/part_one_test_input.txt"))[0] == 71


def test_find_invalid_real():
    assert solve_find_invalid(read_input("data/input.txt"))[0] == 23954


def test_find_valid_real():
    notes = read_input("data/input.txt")
    invalid_tickets = solve_find_invalid(notes)[1]
    valid_tickets = [notes.nearby_tickets[i] for i in range(len(notes.nearby_tickets)) if i not in invalid_tickets]
    matched_fields = solve_match_fields(notes, valid_tickets)
    your_departure_values = [notes.your_ticket[i] for i in range(len(matched_fields)) if
                             matched_fields[i].startswith("departure")]
    assert math.prod(your_departure_values) == 453459307723


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        current_section = NotesSection.FIELD_RULES
        field_rules = {}
        your_ticket = []
        nearby_tickets = []
        for line in f:
            stripped_line = line.strip("\n")
            if stripped_line.startswith("your ticket:"):
                current_section = NotesSection.YOUR_TICKET
                continue
            elif stripped_line.startswith("nearby tickets:"):
                current_section = NotesSection.NEARBY_TICKETS
                continue
            elif not stripped_line:
                continue

            if current_section == NotesSection.FIELD_RULES:
                regex = re.search(r"^([a-z ]+): (\d*)-(\d*) or (\d*)-(\d*)$", stripped_line)
                field_rules[regex.group(1)] = ((range(int(regex.group(2)), int(regex.group(3)) + 1),
                                                range(int(regex.group(4)), int(regex.group(5)) + 1)))
            elif current_section == NotesSection.YOUR_TICKET:
                your_ticket = [int(x) for x in stripped_line.split(",")]
            elif current_section == NotesSection.NEARBY_TICKETS:
                nearby_tickets.append([int(x) for x in stripped_line.split(",")])

        return Notes(field_rules, your_ticket, nearby_tickets)


class NotesSection(Enum):
    FIELD_RULES = 1
    YOUR_TICKET = 2
    NEARBY_TICKETS = 3
