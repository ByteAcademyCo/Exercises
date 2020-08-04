def test_solution():
    import solution
    assert solution.factorial_recursive(5) == 120
    assert solution.factorial_recursive(10) == 3628800
    assert solution.factorial_recursive(1) == 1
    assert solution.factorial_recursive(0) == 1