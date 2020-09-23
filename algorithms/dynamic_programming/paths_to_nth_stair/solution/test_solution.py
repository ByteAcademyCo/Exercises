def test_solution():
    import solution
    
    assert solution.paths_nth_stair(3) == 3
    assert solution.paths_nth_stair(1) == 1
    assert solution.paths_nth_stair(2) == 2
    assert solution.paths_nth_stair(5) == 8