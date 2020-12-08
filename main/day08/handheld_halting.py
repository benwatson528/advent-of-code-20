from typing import List

from main.day08.instruction import Instruction
from main.day08.operation import Operation


def solve(instructions: List[Instruction]) -> int:
    seen = set()
    accumulator = 0
    idx = 0

    while True:
        instruction = instructions[idx]
        if idx in seen:
            return accumulator
        else:
            seen.add(idx)

        if instruction.operation == Operation.acc:
            accumulator += instruction.argument

        jump = instruction.argument if instruction.operation == Operation.jmp else 1
        idx = (idx + jump) % len(instructions)
