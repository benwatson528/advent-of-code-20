from collections import defaultdict
from typing import List


def solve_diffs(adapters: List[int]) -> (int, int):
    sorted_adapters = sorted(adapters)
    one_diffs = 0
    three_diffs = 1
    last_val = 0
    for adapter in sorted_adapters:
        diff = adapter - last_val
        if diff == 1:
            one_diffs += 1
        if diff == 3:
            three_diffs += 1
        last_val = adapter
    return one_diffs, three_diffs


def solve_combinations(adapters: List[int]) -> int:
    sorted_adapters = sorted(adapters)
    combinations = defaultdict(int)
    combinations[0] = 1
    for adapter in sorted_adapters:
        combinations[adapter] = combinations[adapter - 1] + combinations[adapter - 2] + combinations[adapter - 3]
    return combinations[sorted_adapters.pop()]
