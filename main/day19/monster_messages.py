import re
from typing import Dict, List

rules = {}


def solve(r: Dict[str, str]) -> List[str]:
    global rules
    rules = r
    possible_messages = build_possible_messages(rules['0'], [])
    return possible_messages


# Do we need a concept of finished messages vs in-progress messages? Not sure, what about ORs?
def build_possible_messages(rule_value: str, messages: List[str]) -> List[str]:
    regex = re.findall(r'\d+', rule_value)
    if "\"" in rule_value:
        # Just return a single value (as a singleton list)
        value_ = [rule_value[1]]
        return value_
    elif "|" in rule_value:
        # Go down the left - this gives us numerous new endings
        lhs = build_possible_messages(regex[0] + " " + regex[1], messages)
        # Go down the right - this gives us numerous new endings
        rhs = build_possible_messages(regex[2] + " " + regex[3], messages)
        # We should end up returning 2 new messages here - our existing prefix + LHS, our existing prefix + RHS
        combined = messages + lhs + rhs
        return combined
    else:
        # We
        ans = []
        for r in regex:
            ans += build_possible_messages(rules[r], messages)
            # Get a lot of suffixes and slap them onto our existing message. But what if multiple ORs inside...
        joined = ''.join(ans)
        return [joined]
