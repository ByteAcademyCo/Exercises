def test_solution():
    import solution
    
    assert solution.binary_search([1, 2, 4, 5, 9, 10, 11], 2) == 1
    assert solution.binary_search([1, 2, 4, 5, 9, 10, 11], 7) == -1
    assert solution.binary_search([], 2) == -1
    assert solution.binary_search([1, 10], 5) == -1
    assert solution.binary_search([1, 2, 4, 5, 6, 9, 10, 11], 6) == 4
    assert solution.binary_search([1, 2, 4, 5, 6, 9, 10, 11], 11) == 7
