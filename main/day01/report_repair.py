from collections import defaultdict
from typing import List


def solve(nums: List[int], target: int):
    counts = defaultdict(int)
    for n in nums:
        counts[target - n] += 1

    for n in nums:
        if n in counts:
            if n * 2 == target and counts[n] < 2:
                continue
            return n * (target - n)
