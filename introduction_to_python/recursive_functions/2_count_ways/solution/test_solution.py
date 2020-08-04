def test_solution():
    import solution
    assert solution.count_ways(steps=2) == 2
    assert solution.count_ways(steps=10) == 89
    assert solution.count_ways(steps=20) == 10946
    assert solution.count_ways(steps=0) == 1
    assert solution.count_ways(steps=1) == 1
