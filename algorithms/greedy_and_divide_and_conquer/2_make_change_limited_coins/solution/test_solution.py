def test_solution():
    import solution

    denominations1 = {1: 5, 2: 1, 10: 5, 50: 3, 100: 1, 200: 1}
    denominations2 = {1: 5, 2: 1, 50: 3, 100: 1, 200: 1}
    denominations3 = {1: 5, 2: 1, 5: 1, 10: 1, 20: 1, 50: 3}
    denominations4 = {1: 5, 2: 1, 50: 3, 100: 1, 200: 1}
    
    assert solution.make_change(450, denominations1) == 5
    assert solution.make_change(10, denominations2) == -1
    assert solution.make_change(10, {}) == -1
    assert solution.make_change(305, denominations4) == 6
    assert solution.make_change(43, denominations3) == -1
