def test_solution():
    import solution
    
    assert solution.frequency_array([]) == []
    assert solution.frequency_array([0]) == [1]
    assert solution.frequency_array([1]) == [0, 1]
    assert solution.frequency_array([3]) == [0, 0, 0, 1]
    assert solution.frequency_array([1, 1, 2, 3, 3, 3, 5, 8, 8]) == [0, 2, 1, 3, 0, 1, 0, 0, 2]
    assert solution.frequency_array([1, 1, 4, 3, 8, 5, 9, 8, 8, 4, 6]) == [0, 2, 0, 1, 2, 1, 1, 0, 3, 1]
