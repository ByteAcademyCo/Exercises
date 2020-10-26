def test_solution():
    import solution
    
    assert ((solution.min_or_max_heap([]) == "min") or (solution.min_or_max_heap([]) == "max"))
    assert solution.min_or_max_heap([1, 3, 5, 7, 4, 8]) == "min"
    assert solution.min_or_max_heap([10, 5, 9, 4, 2, 8]) == "max"
    assert solution.min_or_max_heap([10, 5, 8, 4, 2, 9]) == "neither"
    assert ((solution.min_or_max_heap([5]) == "min") or (solution.min_or_max_heap([5]) == "max"))
    
