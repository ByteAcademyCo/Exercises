def test_solution():
    import solution
    assert solution.tower_of_hanoi(2, [2, 1], [], []) == 3
    assert solution.tower_of_hanoi(3, [3, 2, 1], [], []) == 7
    assert solution.tower_of_hanoi(0, [], [], []) == 0
    assert solution.tower_of_hanoi(1, [1], [], []) == 1