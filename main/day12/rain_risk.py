from typing import List

from main.day12.instruction import Instruction


def manhattan_distance(x: int, y: int) -> int:
    return abs(x) + abs(y)


def solve_ship_movement(instructions: List[Instruction]) -> int:
    (x, y) = (0, 0)
    direction = 1
    for instruction in instructions:
        if instruction.action == 'N':
            y += instruction.value
        elif instruction.action == 'S':
            y -= instruction.value
        elif instruction.action == 'E':
            x += instruction.value
        elif instruction.action == 'W':
            x -= instruction.value
        elif instruction.action == 'L':
            direction = (direction - (instruction.value // 90)) % 4
        elif instruction.action == 'R':
            direction = (direction + (instruction.value // 90)) % 4
        elif instruction.action == 'F':
            if direction == 0:  # North
                y += instruction.value
            elif direction == 1:  # East
                x += instruction.value
            elif direction == 2:  # South
                y -= instruction.value
            elif direction == 3:  # West
                x -= instruction.value
    return manhattan_distance(x, y)


def solve_waypoint_movement(instructions: List[Instruction]) -> int:
    (ship_x, ship_y) = (0, 0)
    (waypoint_x, waypoint_y) = (10, 1)
    for instruction in instructions:
        if instruction.action == 'N':
            waypoint_y += instruction.value
        elif instruction.action == 'S':
            waypoint_y -= instruction.value
        elif instruction.action == 'E':
            waypoint_x += instruction.value
        elif instruction.action == 'W':
            waypoint_x -= instruction.value
        elif instruction.action == 'L':
            for _ in range((instruction.value // 90) % 4):
                (waypoint_x, waypoint_y) = -waypoint_y, waypoint_x
        elif instruction.action == 'R':
            for _ in range((instruction.value // 90) % 4):
                (waypoint_x, waypoint_y) = waypoint_y, -waypoint_x
        elif instruction.action == 'F':
            ship_x += instruction.value * waypoint_x
            ship_y += instruction.value * waypoint_y
    return manhattan_distance(ship_x, ship_y)
