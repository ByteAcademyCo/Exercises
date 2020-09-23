def test_solution():
    import solution

    adjacency_list = {
        0: [1,4,5],
        1: [0,2,3,6],
        2: [0],
        3: [],
        4: [1,5],
        5: [6],
        6: [3,5]
    }
    assert sorted(solution.hops_away(adjacency_list, 0, 2)) == [0,1,2,3,5,6]
    assert sorted(solution.hops_away(adjacency_list, 2, 0)) == [2]
    assert sorted(solution.hops_away(adjacency_list, 5, 3)) == [6]
    assert sorted(solution.hops_away(adjacency_list, 7, 2)) == []
    assert sorted(solution.hops_away(adjacency_list, 3, 4)) == []
    
