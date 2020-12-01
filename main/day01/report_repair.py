from collections import defaultdict
from typing import List


def solve_two(nums: List[int], target: int):
    counts = defaultdict(int)
    for n in nums:
        counts[target - n] += 1

    for n in nums:
        if n in counts:
            if n * 2 == target and counts[n] < 2:
                continue
            return n * (target - n)


def solve_three(nums: List[int], target: int):
    counts = {}
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            counts[target - nums[i] - nums[j]] = (nums[i], nums[j])

    for n in nums:
        if n in counts:
            return n * counts.get(n)[0] * counts.get(n)[1]
