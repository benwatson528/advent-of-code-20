from typing import List, Dict


def solve(cups: List[int], num_turns: int) -> Dict[int, int]:
    cups_map = dict(zip(cups, cups[1:]))
    cups_map[cups[-1]] = cups[0]
    return take_turn(cups_map, cups[0], num_turns)


def take_turn(cups: Dict[int, int], current_cup: int, num_turns: int) -> Dict[int, int]:
    num_cups = len(cups)
    for _ in range(num_turns):
        cups_to_move = [cups[current_cup], cups[cups[current_cup]], cups[cups[cups[current_cup]]]]
        destination_cup = find_destination_cup(current_cup, cups_to_move, num_cups)
        cups[current_cup] = cups[cups_to_move[-1]]
        cups[cups_to_move[-1]] = cups[destination_cup]
        cups[destination_cup] = cups_to_move[0]
        current_cup = cups[current_cup]
    return cups


def find_destination_cup(current_cup: int, moved_cups: List[int], num_cups: int) -> int:
    destination_cup = current_cup - 1
    if destination_cup == 0:
        destination_cup = num_cups
    while destination_cup in moved_cups:
        destination_cup -= 1
        if destination_cup < 1:
            destination_cup = num_cups
    return destination_cup
