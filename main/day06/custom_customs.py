from typing import List


def solve(groups: List[List[str]]):
    return sum(map(lambda x: len(''.join(set(''.join(x)))), groups))
