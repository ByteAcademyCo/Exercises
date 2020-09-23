def test_solution():
    import solution

    jewels1 = [(1, 4), (2, 8), (3, 15), (9, 50)]
    jewels2 = [(1, 1)]
    jewels3 = [(1, 1), (2, 8), (3, 15), (4,24)]
    
    assert solution.steal_jewels(10, jewels1) == 55
    assert solution.steal_jewels(10, []) == 0
    assert solution.steal_jewels(1, jewels2) == 1
    assert solution.steal_jewels(3, jewels2) == 1
    assert solution.steal_jewels(3, jewels3) == 18