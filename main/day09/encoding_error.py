import itertools
from typing import List


def solve(nums: List[int], preamble_size: int) -> int:
    queue = nums[:preamble_size]
    codes = nums[preamble_size:]
    for num in codes:
        combinations = list(itertools.combinations(queue, 2))
        valid_combination = next((x for x in combinations if x[0] + x[1] == num), None)
        if not valid_combination:
            return num
        queue.pop(0)
        queue.append(num)
