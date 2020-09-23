def test_solution():
    import solution

    assert solution.min_hops(3, 7, [1, 0, 0, 1, 1, 0, 0, 1]) == 3
    assert solution.min_hops(3, 4, [1, 0, 0, 0, 1]) == -1
    assert solution.min_hops(1, 3, [1, 1, 1, 1]) == 3
    assert solution.min_hops(2, 6, [1, 1, 0, 1, 1, 0, 1]) == 4