def test_solution():
    import solution

    adjacency_list = {
        0: [1,3,6],
        1: [0,1,3,6],
        2: [],
        3: [0,3],
        4: [],
        5: [],
        6: [3],
        7: []
    }
    assert solution.count_islands(adjacency_list) == 4
    
