import solution

adjacency_list = {
    0: [1,2,3],
    1: [0,3],
    2: [1],
    3: [0,3]
}

def test_solution():
    assert solution.adjacency_list == adjacency_list
