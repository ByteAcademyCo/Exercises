def test_solution():
    import solution
    assert solution.fibonacci(n=5) == 5
    assert solution.fibonacci(n=10) == 55
    assert solution.fibonacci(n=15) == 610
    assert solution.fibonacci(n=1) == 1
