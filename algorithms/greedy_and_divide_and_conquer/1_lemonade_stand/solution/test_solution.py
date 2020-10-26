def test_solution():
    import solution
    
    assert solution.lemonade_change([5, 10, 5, 20]) == True
    assert solution.lemonade_change([]) == True
    assert solution.lemonade_change([5, 20, 5, 20]) == False
    assert solution.lemonade_change([5]) == True
    assert solution.lemonade_change([10]) == False
    assert solution.lemonade_change([5, 10, 10, 20]) == False
