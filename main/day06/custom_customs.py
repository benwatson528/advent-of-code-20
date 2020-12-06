from collections import Counter
from typing import List


def find_anyone_response(groups: List[List[str]]):
    return sum(map(lambda x: len(''.join(set(''.join(x)))), groups))


def find_everyone_response(groups: List[List[str]]):
    everyone_responses = 0
    for group in groups:
        num_respondents = len(group)
        counted = map(lambda x: Counter(x), group)
        combined = sum(counted, Counter())
        everyone_responses += len({x: count for x, count in combined.items() if count == num_respondents})
    return everyone_responses
