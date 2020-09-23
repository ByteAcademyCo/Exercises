def test_solution():
    import solution
    
    assert solution.sum_first_n(5) == 15
    assert solution.sum_first_n(1) == 1
    assert solution.sum_first_n(15) == 120
    assert solution.sum_first_n(20) == 210
    
