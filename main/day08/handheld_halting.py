import copy
from typing import List

from main.day08.instruction import Instruction
from main.day08.operation import Operation


def solve(instructions: List[Instruction]) -> (int, bool):
    seen = set()
    accumulator = 0
    idx = 0

    while True:
        instruction = instructions[idx]
        if idx in seen:
            return accumulator, False
        else:
            seen.add(idx)

        if instruction.operation == Operation.acc:
            accumulator += instruction.argument

        jump = instruction.argument if instruction.operation == Operation.jmp else 1
        if idx + jump == len(instructions):
            return accumulator, True

        idx = (idx + jump) % len(instructions)


def fix(instructions: List[Instruction]) -> (int, bool):
    for i in range(len(instructions)):
        instruction = instructions[i]
        if instruction.operation == Operation.jmp:
            output = run_with_updated_command(i, Operation.nop, instructions)
        elif instruction.operation == Operation.nop:
            output = run_with_updated_command(i, Operation.jmp, instructions)
        else:
            continue

        if output[1]:
            return output


def run_with_updated_command(idx, new_op, instructions):
    instruction = instructions[idx]
    updated_instructions = copy.deepcopy(instructions)
    updated_instructions[idx] = Instruction(new_op, instruction.argument)
    return solve(updated_instructions)
