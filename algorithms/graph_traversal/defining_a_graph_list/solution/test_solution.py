def count_edges(alist):
    edges = 0
    for i in range(len(alist)):
        edges += len(alist[i])
    return edges

def test_solution():
    import solution
    assert len(solution.adjacency_list) == 4
    assert count_edges(solution.adjacency_list) == 4
    assert len(solution.adjacency_list[0]) == 0
    
