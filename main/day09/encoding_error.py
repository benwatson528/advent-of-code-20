import itertools
from typing import List, Optional, Callable


def solve_any_two(nums: List[int], preamble_size: int) -> Optional[int]:
    return solve(nums, preamble_size, find_any_two)[0]


def solve_contiguous(nums: List[int], target: int) -> Optional[List[int]]:
    for i in range(len(nums)):
        contiguous_sum = set()
        for j in range(i, len(nums)):
            contiguous_sum.add(nums[j])
            if sum(contiguous_sum) == target:
                return [min(contiguous_sum), max(contiguous_sum)]
            elif sum(contiguous_sum) > target:
                break
    return None


def find_any_two(preamble: List[int], target: int) -> Optional[List[int]]:
    combinations = itertools.combinations(preamble, 2)
    valid_combination = next((x for x in combinations if x[0] + x[1] == target), None)
    if not valid_combination:
        return [target]
    else:
        return None


def solve(nums: List[int], preamble_size: int,
          combination_evaluator: Callable[[List[int], int], Optional[List[int]]]) -> Optional[List[int]]:
    preamble = nums[:preamble_size]
    codes = nums[preamble_size:]
    for num in codes:
        combination = combination_evaluator(preamble, num)
        if combination:
            return combination
        preamble.pop(0)
        preamble.append(num)
    return None
