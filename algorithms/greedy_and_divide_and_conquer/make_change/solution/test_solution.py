def test_solution():
    import solution

    denominations1 = [1, 2, 5, 10, 20, 50, 100, 200]
    denominations2 = [1, 2, 5, 100]
    denominations3 = [20, 50, 100, 200]
    denominations4 = [1, 100, 200]
    
    assert solution.make_change(450, denominations1) == 3
    assert solution.make_change(50, denominations1) == 1
    assert solution.make_change(233, denominations2) == 10
    assert solution.make_change(30, denominations3) == -1
    assert solution.make_change(77, denominations4) == 77
