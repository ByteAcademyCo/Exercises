def test_solution():
    import solution
    
    assert solution.quick_sort([9, 1, 0, 2, 3, 4, 6, 8, 7, 10, 5]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert solution.quick_sort([]) == []
    assert solution.quick_sort([5]) == [5]
    assert solution.quick_sort([1, 2, 1]) == [1, 1, 2]
    assert solution.quick_sort([3, 2, 1, 0]) == [0, 1, 2, 3]
    
