import copy
import itertools
from typing import List

from main.day14.instruction import Instruction

EMPTY_BITS = "000000000000000000000000000000000000"


def solve_static(instructions: List[Instruction]) -> int:
    memories = {}
    for instruction in instructions:
        memory = list(memories.get(instruction.address, EMPTY_BITS))
        instruction_bytes = format(instruction.value, 'b').zfill(36)
        memories[instruction.address] = apply_static_mask(instruction_bytes, instruction.mask, memory)
    return sum([int(''.join(v), 2) for v in memories.values()])


def apply_static_mask(instruction_bytes: str, mask: str, memory: List[str]) -> List[str]:
    for i in range(36):
        memory[i] = mask[i] if mask[i] != "X" else instruction_bytes[i]
    return memory


def solve_floating(instructions: List[Instruction]) -> int:
    memories = {}
    for instruction in instructions:
        mask = instruction.mask
        instruction_address_bytes = list(format(instruction.address, 'b').zfill(36))
        floaters = []
        for i in range(36):
            if mask[i] == "1":
                instruction_address_bytes[i] = "1"
            elif mask[i] == "X":
                floaters.append(i)
        instruction_value_bytes = format(instruction.value, 'b').zfill(36)
        resolve_floaters(floaters, instruction_address_bytes, instruction_value_bytes, memories)

    output_numbers = []
    for _, value in memories.items():
        output_numbers.append(int(''.join(value), 2))
    return sum(output_numbers)


def resolve_floaters(floaters, instruction_address_bytes, instruction_value_bytes, memories):
    products = list(itertools.product(["0", "1"], repeat=len(floaters)))
    for product in products:
        updated_memory = copy.deepcopy(instruction_address_bytes)
        for i in range(len(floaters)):
            updated_memory[floaters[i]] = product[i]
        updated_memory_int = int(''.join(updated_memory), 2)
        memories[updated_memory_int] = instruction_value_bytes
