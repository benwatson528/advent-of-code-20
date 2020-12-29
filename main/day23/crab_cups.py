from typing import List, Dict

num_cups = 0
num_turns = 0


def solve(cups: str, turns: int) -> Dict[int, int]:
    global num_cups
    num_cups = len(cups)
    global num_turns
    num_turns = turns
    cup_ints = [int(c) for c in cups]
    cups_map = dict(zip(cup_ints, cup_ints[1:]))
    cups_map[cup_ints[-1]] = cup_ints[0]
    return take_turn(cups_map, cup_ints[0], 1)


def take_turn(cups: Dict[int, int], current_cup: int, current_turn: int) -> Dict[int, int]:
    # print_cups(cups, current_cup, current_turn)
    if current_turn > num_turns:
        return cups
    else:
        cups_to_move = [cups[current_cup], cups[cups[current_cup]], cups[cups[cups[current_cup]]]]
        destination_cup = find_destination_cup(current_cup, cups_to_move)
        cups[current_cup] = cups[cups_to_move[-1]]
        cups[cups_to_move[-1]] = cups[destination_cup]
        cups[destination_cup] = cups_to_move[0]
        next_cup = cups[current_cup]
        return take_turn(cups, next_cup, current_turn + 1)


def find_destination_cup(current_cup: int, moved_cups: List[int]) -> int:
    destination_cup = current_cup - 1
    if destination_cup == 0:
        destination_cup = 9
    while destination_cup in moved_cups:
        destination_cup -= 1
        if destination_cup < 1:
            destination_cup = 9
    return destination_cup


def follow_n_cups(current_cup: int, cups: Dict[int, int], n: int) -> int:
    next_cup = current_cup
    for _ in range(n - 1):
        next_cup = cups[next_cup]
    return cups[next_cup]


def print_cups(cups: Dict[int, int], current_cup: int, turn: int):
    print(f"\nTurn {turn}")
    next_cup = 1
    for _ in range(1, 10):
        if next_cup == current_cup:
            print(f"({next_cup})", end=' ')
        else:
            print(f"{next_cup}", end=' ')
        next_cup = cups[next_cup]
