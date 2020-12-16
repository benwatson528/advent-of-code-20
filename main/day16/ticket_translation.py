from collections import defaultdict
from typing import Set, Dict, List

from main.day16.notes import Notes


def solve_find_invalid(notes: Notes) -> (int, Set[int]):
    invalid_fields = []
    invalid_tickets = set()
    for i in range(len(notes.nearby_tickets)):
        nearby_ticket = notes.nearby_tickets[i]
        for nearby_ticket_value in nearby_ticket:
            valid_value = False
            for field_rule in notes.field_rules.values():
                if nearby_ticket_value in field_rule[0] or nearby_ticket_value in field_rule[1]:
                    valid_value = True
                    break
            if not valid_value:
                invalid_fields.append(nearby_ticket_value)
                invalid_tickets.add(i)
    return sum(invalid_fields), invalid_tickets


def solve_match_fields(notes: Notes, valid_tickets: List[List[int]]) -> List[str]:
    possible_answers = defaultdict(set)
    num_fields = len(notes.field_rules)
    columns = build_columns(num_fields, valid_tickets)

    for i in range(len(columns)):
        column = columns[i]
        for rule_name, rule_ranges in notes.field_rules.items():
            valid_rule = True
            for value in column:
                if value not in rule_ranges[0] and value not in rule_ranges[1]:
                    valid_rule = False
                    break
            if valid_rule:
                possible_answers[i].add(rule_name)
    return deduce_fields(possible_answers)


def build_columns(num_fields: int, valid_tickets: List[List[int]]) -> List[List[int]]:
    columns = []
    for j in range(num_fields):
        column = []
        for i in range(len(valid_tickets)):
            column.append(valid_tickets[i][j])
        columns.append(column)
    return columns


def deduce_fields(possible_answers: Dict[int, Set[str]]) -> List[str]:
    answers = [""] * len(possible_answers)
    num_assigned_fields = 0
    while num_assigned_fields < len(possible_answers):
        for col_idx, field_names in possible_answers.items():
            difference = field_names.difference(answers)
            if len(difference) == 1:
                field_name = difference.pop()
                answers[col_idx] = field_name
                num_assigned_fields += 1
                break
    return answers
