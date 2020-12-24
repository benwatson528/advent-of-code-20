from main.day23.crab_cups import solve


def test_part_one_simple():
    end_cups = solve("389125467", 100)
    assert pivot_answer(end_cups) == 67384529


def test_part_one_real():
    end_cups = solve("219347865", 100)
    assert pivot_answer(end_cups) == 36472598


def test_part_two_simple():
    end_cups = solve("389125467", 100)
    assert pivot_answer(end_cups) == 67384529


def test_part_two_real():
    end_cups = solve("219347865", 100)
    assert pivot_answer(end_cups) == 36472598


def pivot_answer(end_cups):
    pivot_idx = end_cups.index(1)
    pivoted_cups = end_cups[pivot_idx + 1:] + end_cups[:pivot_idx]
    return int(''.join(str(i) for i in pivoted_cups))
