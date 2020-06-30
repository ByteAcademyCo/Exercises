def test_solution():
    import solution
    assert solution.custom_sort([1,7,4,2]) == [1,2,4,7]
    assert solution.custom_sort([2,1]) == [1,2]
