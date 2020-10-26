def test_solution():
    import solution

    matrix = [
        [1, 1, 0, 1],
        [0, 0, 1, 1],
        [1, 0, 0, 1],
        [0, 0, 0, 1]
    ]
    assert solution.exists_path(matrix, 0, 2) == True
    assert solution.exists_path(matrix, 1, 0) == True
    assert solution.exists_path(matrix, 4, 2) == False
    assert solution.exists_path(matrix, 0, 4) == False
    assert solution.exists_path(matrix, 3, 1) == False
    
