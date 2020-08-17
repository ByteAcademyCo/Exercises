import solution

matrix = [
    [0, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 1]
]


def test_solution():
    assert solution.count_edges(matrix) == 14
    
