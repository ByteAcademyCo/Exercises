def is_3_by_3_matrix(matrix):
    return len(matrix) == 3 and len(matrix[0]) == 3

def count_edges(matrix):
    edges = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                edges += 1
    return edges

def test_solution():
    import solution
    assert is_3_by_3_matrix(solution.adjacency_matrix)
    assert count_edges(solution.adjacency_matrix) == 4
    
