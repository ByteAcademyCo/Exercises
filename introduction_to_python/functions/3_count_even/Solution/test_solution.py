import solution

def test_solution():
    assert solution.count_even(1, 2, 3, 4) == 2
    assert solution.count_even(1, 3, 5) == 0
    assert solution.count_even() == 0
    assert solution.count_even(2, 4, 6, 8, 10) == 5
    



