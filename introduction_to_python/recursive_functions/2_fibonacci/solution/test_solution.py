def test_solution():
    from solution import fibonacci

    assert fibonacci(n=5) == 5
    assert fibonacci(n=10) == 55
    assert fibonacci(n=15) == 610
    assert fibonacci(n=1) == 1
