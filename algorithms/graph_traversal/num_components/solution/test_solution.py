def test_solution():
    import solution

    adj_matrix1 = [
        [0, 1, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 0]
    ]
             
    adj_matrix2 = [
        [0, 1, 1],
        [1, 0, 0],
        [1, 0, 0]
    ]

    adj_matrix3 = [
        [0, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0],
        [0, 1, 0, 0]
    ]

    adj_matrix4 = []
    assert solution.num_components(adj_matrix1) == 2
    assert solution.num_components(adj_matrix2) == 1
    assert solution.num_components(adj_matrix3) == 3
    assert solution.num_components(adj_matrix4) == 0
    
    
