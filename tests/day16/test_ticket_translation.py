import os
import re
from enum import Enum
from pathlib import Path

from main.day16.notes import Notes
from main.day16.ticket_translation import solve


def test_simple():
    assert solve(read_input("data/test_input.txt")) == 71


def test_real():
    assert solve(read_input("data/input.txt")) == 23954


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        current_section = NotesSection.FIELD_RULES
        field_rules = []
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
                regex = re.search(r"^[a-z ]+: (\d*)-(\d*) or (\d*)-(\d*)$", stripped_line)
                field_rules.append((range(int(regex.group(1)), int(regex.group(2)) + 1),
                                    range(int(regex.group(3)), int(regex.group(4)) + 1)))
            elif current_section == NotesSection.YOUR_TICKET:
                your_ticket = [int(x) for x in stripped_line.split(",")]
            elif current_section == NotesSection.NEARBY_TICKETS:
                nearby_tickets.append([int(x) for x in stripped_line.split(",")])

        return Notes(field_rules, your_ticket, nearby_tickets)


class NotesSection(Enum):
    FIELD_RULES = 1
    YOUR_TICKET = 2
    NEARBY_TICKETS = 3
