def test_solution():
    import solution
    
    assert solution.median_of_medians([9, 1, 0, 2, 3, 4, 6, 8, 7, 10, 5]) == 5
    assert solution.median_of_medians([1]) == 1
    assert solution.median_of_medians([1, 2, 3]) == 2
    assert solution.median_of_medians([1, 2, 2, 3]) == 2
    
