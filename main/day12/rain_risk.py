from typing import List

from main.day12.instruction import Instruction


def manhattan_distance(x: int, y: int) -> int:
    return abs(x) + abs(y)


def solve_ship_movement(instructions: List[Instruction]) -> int:
    position = (0, 0)
    direction = 1
    for instruction in instructions:
        if instruction.action == 'N':
            position = position[0], position[1] + instruction.value
        elif instruction.action == 'S':
            position = position[0], position[1] - instruction.value
        elif instruction.action == 'E':
            position = position[0] + instruction.value, position[1]
        elif instruction.action == 'W':
            position = position[0] - instruction.value, position[1]
        elif instruction.action == 'L':
            direction = (direction - (instruction.value // 90)) % 4
        elif instruction.action == 'R':
            direction = (direction + (instruction.value // 90)) % 4
        elif instruction.action == 'F':
            if direction == 0:  # North
                position = position[0], position[1] + instruction.value
            elif direction == 1:  # East
                position = position[0] + instruction.value, position[1]
            elif direction == 2:  # South
                position = position[0], position[1] - instruction.value
            elif direction == 3:  # West
                position = position[0] - instruction.value, position[1]
    return manhattan_distance(position[0], position[1])


def solve_waypoint_movement(instructions: List[Instruction]) -> int:
    ship = (0, 0)
    waypoint = (10, 1)
    for instruction in instructions:
        if instruction.action == 'N':
            waypoint = waypoint[0], waypoint[1] + instruction.value
        elif instruction.action == 'S':
            waypoint = waypoint[0], waypoint[1] - instruction.value
        elif instruction.action == 'E':
            waypoint = waypoint[0] + instruction.value, waypoint[1]
        elif instruction.action == 'W':
            waypoint = waypoint[0] - instruction.value, waypoint[1]
        elif instruction.action == 'L':
            for _ in range((instruction.value // 90) % 4):
                waypoint = -waypoint[1], waypoint[0]
        elif instruction.action == 'R':
            for _ in range((instruction.value // 90) % 4):
                waypoint = waypoint[1], -waypoint[0]
        elif instruction.action == 'F':
            ship = ship[0] + (instruction.value * waypoint[0]), ship[1] + (instruction.value * waypoint[1])
    return manhattan_distance(ship[0], ship[1])
