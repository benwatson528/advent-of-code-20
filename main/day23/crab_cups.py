from typing import List

num_cups = 0


def solve(cups: str, num_turns: int) -> List[int]:
    global num_cups
    num_cups = len(cups)
    return take_turn([int(c) for c in cups], 0, 1, num_turns)


def take_turn(cups: List[int], current_cup_idx: int, current_turn: int, num_turns: int) -> List[int]:
    if current_turn > num_turns:
        return cups
    else:
        removed_cups = [cups[c] for c in [(current_cup_idx + 1) % num_cups,
                                          (current_cup_idx + 2) % num_cups,
                                          (current_cup_idx + 3) % num_cups]]
        current_cup = cups[current_cup_idx]
        destination_cup = find_destination_cup(current_cup, removed_cups)
        updated_cups = []
        for idx in range(num_cups):
            if cups[idx] not in removed_cups:
                updated_cups.append(cups[idx])
            if cups[idx] == destination_cup:
                updated_cups.extend(removed_cups)
        next_cup_idx = (updated_cups.index(current_cup) + 1) % num_cups
        return take_turn(updated_cups, next_cup_idx, current_turn + 1, num_turns)


def find_destination_cup(current_cup: int, removed_cups: List[int]) -> int:
    destination_cup = current_cup - 1
    if destination_cup == 0:
        destination_cup = 9
    while destination_cup in removed_cups:
        destination_cup -= 1
        if destination_cup < 1:
            destination_cup = 9
    return destination_cup
