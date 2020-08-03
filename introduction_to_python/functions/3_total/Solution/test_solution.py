import solution

def test_solution():
    assert solution.sum_data([]) == 0
    assert solution.sum_data([1]) == 1
    assert solution.sum_data([1, 2, 3]) == 6
    assert solution.sum_data([2, 4, 6, 8]) == 20
