from collections import defaultdict
from typing import List


def solve(nums: List[int], end_turn: int) -> int:
    tracker = defaultdict(list)
    for turn in range(len(nums)):
        tracker[nums[turn]].append(turn + 1)

    last_num = nums[-1]

    for turn in range(len(nums) + 1, end_turn + 1):
        if len(tracker[last_num]) == 1:
            last_num = 0
        else:
            last_num = tracker[last_num][-1] - tracker[last_num][-2]
        tracker[last_num].append(turn)

    return last_num
