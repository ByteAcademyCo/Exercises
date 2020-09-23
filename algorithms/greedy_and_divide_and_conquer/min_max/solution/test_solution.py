def test_solution():
    import solution

    assert solution.min_max([1]) == (1, 1)
    assert solution.min_max([1, 3, 2]) == (1, 3)
    assert solution.min_max([1, 3, 2, 1, 8, 1]) == (1, 8)
    assert solution.min_max([9, 7, 2, 3, 3, 4]) == (2, 9)