import re
from typing import Dict, List, Set

rules = {}


def solve(r: Dict[str, str], part_2: bool) -> Set[str]:
    global rules
    rules = r
    if part_2:
        rules['8'] = "42 | 42 8"
        rules['11'] = "42 31 | 42 11 31"
    return set(build_possible_messages(rules['0'], ['']))


def build_possible_messages(rule_value: str, suffixes: List[str]) -> List[str]:
    regex = re.findall(r'\d+', rule_value)
    if '"' in rule_value:
        updated_suffixes = []
        for suffix in suffixes:
            updated_suffixes.append(suffix + rule_value[1])
        return updated_suffixes
    elif '|' in rule_value:
        updated_suffixes = []
        lhs_suffixes = build_possible_messages(' '.join(re.findall(r'\d+', rule_value.split('|')[0])), suffixes)
        rhs_suffixes = build_possible_messages(' '.join(re.findall(r'\d+', rule_value.split('|')[1])), suffixes)
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
