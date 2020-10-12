def test_solution():
    from solution import factorial_recursive

    assert factorial_recursive(5) == 120
    assert factorial_recursive(10) == 3628800
    assert factorial_recursive(1) == 1
    assert factorial_recursive(0) == 1
