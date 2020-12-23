from typing import List


def solve(player1: List[int], player2: List[int]) -> int:
    winning_deck = take_turn(player1, player2)
    return sum((a + 1) * b for a, b in enumerate(reversed(winning_deck)))


def take_turn(player1: List[int], player2: List[int], ) -> List[int]:
    if len(player1) == 0:
        return player2
    elif len(player2) == 0:
        return player1
    else:
        p1_head, *p1_tail = player1
        p2_head, *p2_tail = player2
        if p1_head > p2_head:
            p1_tail.extend([p1_head, p2_head])
            return take_turn(p1_tail, p2_tail)
        else:
            p2_tail.extend([p2_head, p1_head])
            return take_turn(p1_tail, p2_tail)
