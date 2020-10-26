def test_solution():
    import solution

    adjacency_matrix = [
        [1, 1, 0, 1, 0],
        [0, 0, 0, 1, 1],
        [0, 1, 0, 0, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    assert solution.adjacency_matrix == adjacency_matrix
    
