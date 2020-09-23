def test_solution():
    from solution import is_leaf
    assert is_leaf([1, 2, 3, 4, 5, 6], 3) == True
    assert is_leaf([1, 2, 3, 4, 5, 6], 5) == True
    assert is_leaf([1, 2, 3, 4, 5, 6], 1) == False
    assert is_leaf([], 1) == False
    assert is_leaf([1, 2, 3], 3) == False