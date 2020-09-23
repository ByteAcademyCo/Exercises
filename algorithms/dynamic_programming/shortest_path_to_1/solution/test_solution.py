def test_solution():
    import solution
    
    assert solution.shortest_path_to_1(1) == 0
    assert solution.shortest_path_to_1(2) == 1
    assert solution.shortest_path_to_1(3) == 1
    assert solution.shortest_path_to_1(4) == 2
    assert solution.shortest_path_to_1(10) == 3
    assert solution.shortest_path_to_1(16) == 4
    assert solution.shortest_path_to_1(22) == 5