from typing import List

from main.day12.instruction import Instruction


def move_north(instruction, position):
    return position[0], position[1] + instruction.value


def move_south(instruction, position):
    return position[0], position[1] - instruction.value


def move_east(instruction, position):
    return position[0] + instruction.value, position[1]


def move_west(instruction, position):
    return position[0] - instruction.value, position[1]


def manhattan_distance(x: int, y: int) -> int:
    return abs(x) + abs(y)


def solve(instructions: List[Instruction]) -> int:
    position = (0, 0)
    direction = 1
    for instruction in instructions:
        if instruction.action == 'N':
            position = move_north(instruction, position)
        elif instruction.action == 'S':
            position = move_south(instruction, position)
        elif instruction.action == 'E':
            position = move_east(instruction, position)
        elif instruction.action == 'W':
            position = move_west(instruction, position)
        elif instruction.action == 'L':
            direction = (direction - (instruction.value // 90)) % 4
        elif instruction.action == 'R':
            direction = (direction + (instruction.value // 90)) % 4
        elif instruction.action == 'F':
            if direction == 0:
                position = move_north(instruction, position)
            elif direction == 1:
                position = move_east(instruction, position)
            elif direction == 2:
                position = move_south(instruction, position)
            elif direction == 3:
                position = move_west(instruction, position)
    return manhattan_distance(position[0], position[1])
