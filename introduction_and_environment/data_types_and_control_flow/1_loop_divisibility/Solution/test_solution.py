def test_solution():
    import solution
    assert solution.x == 50
    assert solution.data == [x for x in range(51) if x%5 == 0 or x%7 == 0]
    


