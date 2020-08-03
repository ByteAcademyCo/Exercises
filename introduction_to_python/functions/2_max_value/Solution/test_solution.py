import solution

def test_solution():
    assert solution.max_val(5, 3, 1) == 5
    assert solution.max_val(5, 5, 5) == 5
    assert solution.max_val(1, 3, 1) == 3
    assert solution.max_val(2, 1, 6) == 6



