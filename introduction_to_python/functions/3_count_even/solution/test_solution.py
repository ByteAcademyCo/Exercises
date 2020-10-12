from solution import count_even


def test_solution():
    assert count_even(1, 2, 3, 4) == 2
    assert count_even(1, 3, 5) == 0
    assert count_even() == 0
    assert count_even(2, 4, 6, 8, 10) == 5
