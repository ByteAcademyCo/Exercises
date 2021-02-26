def test_solution():
    import solution
    assert(type(solution.num) == int)
    if solution.num%2 == 0:
        assert solution.result == 'even'
    else:
        assert solution.result == 'odd'



