from functools import reduce
from typing import List


def solve_first_bus(time: int, bus_ids: List[int]) -> int:
    min_time, min_bus_id = min(map(lambda x: (x - (time % x), x), bus_ids), key=lambda x: x[0])
    return min_time * min_bus_id


def solve_consecutive_bus(bus_ids: List[int]) -> int:
    valid_buses = []
    indices = []
    for i in range(len(bus_ids)):
        if bus_ids[i] != "x":
            valid_buses.append(int(bus_ids[i]))
            indices.append(-i)
    return chinese_remainder(valid_buses, indices)


#  https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
def chinese_remainder(n, a):
    remainder_sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        remainder_sum += a_i * mul_inv(p, n_i) * p
    return remainder_sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1
