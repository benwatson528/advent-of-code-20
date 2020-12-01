from typing import List


def solve(nums: List[int], target: int):
    for i in range(len(nums)):
        first_elem = nums[i]
        for j in range(i, len(nums)):
            if first_elem + nums[j] == target:
                return first_elem * nums[j]
