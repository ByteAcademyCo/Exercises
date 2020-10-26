def test_solution():
    import solution

    matrix = [
    [0, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 1]
    ]

    assert solution.count_edges(matrix) == 14
    
