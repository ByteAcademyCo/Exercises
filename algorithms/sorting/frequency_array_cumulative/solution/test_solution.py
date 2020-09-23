def test_solution():
    import solution
    
    assert solution.frequency_array_cumulative([]) == []
    assert solution.frequency_array_cumulative([0]) == [1]
    assert solution.frequency_array_cumulative([1]) == [0, 1]
    assert solution.frequency_array_cumulative([3]) == [0, 0, 0, 1]
    assert solution.frequency_array_cumulative([1, 1, 2, 3, 3, 3, 5, 8, 8]) == [0, 2, 3, 6, 6, 7, 7, 7, 9]
    assert solution.frequency_array_cumulative([1, 1, 4, 3, 8, 5, 9, 8, 8, 4, 6]) == [0, 2, 2, 3, 5, 6, 7, 7, 10, 11]
