import re
from typing import Dict, List, Set

rules = {}


def solve(r: Dict[str, str]) -> Set[str]:
    global rules
    rules = r
    return set(build_possible_messages(rules['0'], ['']))


def build_regex(start_rule_value: str, messages: List[str]) -> str:
    return ""


# Do we need a concept of finished messages vs in-progress messages? Not sure, what about ORs?
def build_possible_messages(rule_value: str, suffixes: List[str]) -> List[str]:
    regex = re.findall(r'\d+', rule_value)
    if '"' in rule_value:
        updated_suffixes = []
        for suffix in suffixes:
            updated_suffixes.append(suffix + rule_value[1])
        return updated_suffixes
    elif '|' in rule_value:
        updated_suffixes = []
        if len(regex) == 4:
            lhs_suffixes = build_possible_messages(regex[0] + " " + regex[1], suffixes)
            rhs_suffixes = build_possible_messages(regex[2] + " " + regex[3], suffixes)
        else:
            lhs_suffixes = build_possible_messages(regex[0], suffixes)
            rhs_suffixes = build_possible_messages(regex[1], suffixes)
        for lhs in lhs_suffixes:
            updated_suffixes.append(lhs)
        for rhs in rhs_suffixes:
            updated_suffixes.append(rhs)
        return updated_suffixes
    else:
        updated_suffixes = suffixes.copy()
        for r in regex:
            updated_suffixes = [s for s in build_possible_messages(rules[r], updated_suffixes)]
    return updated_suffixes
