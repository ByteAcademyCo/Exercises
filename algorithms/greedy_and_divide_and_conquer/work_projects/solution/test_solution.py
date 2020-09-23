def test_solution():
    import solution
    
    projects1 = [(1, 100), (2, 150), (2, 300), (4, 200), (3, 100)]
    projects2 = [(2, 300), (2, 100), (2, 200)]
    projects3 = [(2, 300), (2, 100), (2, 200), (4, 50), (3, 200), (4, 100)]

    assert solution.max_profits(projects1) == 750
    assert solution.max_profits([]) == 0
    assert solution.max_profits([(4, 200)]) == 200
    assert solution.max_profits(projects2) == 500
    assert solution.max_profits(projects3) == 800
