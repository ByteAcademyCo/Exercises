def test_solution():
    import solution
    
    assert solution.merge_sorted([],[]) == []
    assert solution.merge_sorted([1],[]) == [1]
    assert solution.merge_sorted([],[1]) == [1]
    assert solution.merge_sorted([2],[1]) == [1, 2]
    assert solution.merge_sorted([1, 2],[3]) == [1, 2, 3]
    assert solution.merge_sorted([1, 2, 4, 6], [3, 4, 5, 7, 8]) == [1, 2, 3, 4, 4, 5, 6, 7, 8]
    
