from typing import List

from main.day14.instruction import Instruction

EMPTY_BITS = "000000000000000000000000000000000000"


def solve(instructions: List[Instruction]) -> int:
    memories = {}
    for instruction in instructions:
        memory = list(memories.get(instruction.address, EMPTY_BITS))
        instruction_bytes = format(instruction.value, 'b').zfill(36)
        memories[instruction.address] = apply_mask(instruction_bytes, instruction.mask, memory)

    output_numbers = []
    for _, value in memories.items():
        output_numbers.append(int(''.join(value), 2))
    return sum(output_numbers)


def apply_mask(instruction_bytes: str, mask: str, memory: List[str]):
    for i in range(36):
        memory[i] = mask[i] if mask[i] != "X" else instruction_bytes[i]
    return memory
