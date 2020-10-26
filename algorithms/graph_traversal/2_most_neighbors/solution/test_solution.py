def test_solution():
    import solution

    adj_list1 = {
        0: [1,4,5],
        1: [0,2,3,6],
        2: [0],
        3: [],
        4: [1,5],
        5: [6],
        6: [3,5]
    }
             
    adj_list2 = {
        0: [1,2],
        1: [0,2],
        2: [0]
    }

    adj_list3 = {
        0: [],
        1: [],
        2: []
    }
    assert solution.most_neighbours(adj_list1) == 1
    assert solution.most_neighbours(adj_list2) == 0
    assert solution.most_neighbours(adj_list3) == 0
