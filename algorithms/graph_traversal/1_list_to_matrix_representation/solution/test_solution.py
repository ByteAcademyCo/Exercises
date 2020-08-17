import solution

adjacency_matrix = [
    [1, 1, 0, 1, 0],
    [0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
]

def test_solution():
    assert solution.adjacency_matrix == adjacency_matrix
    
