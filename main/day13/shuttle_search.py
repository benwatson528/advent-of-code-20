from typing import List


def solve(time: int, bus_ids: List[int]) -> int:
    min_time, min_bus_id = min(map(lambda x: (x - (time % x), x), bus_ids), key=lambda x: x[0])
    return min_time * min_bus_id
