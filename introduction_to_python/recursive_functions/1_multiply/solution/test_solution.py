def test_solution():
    from solution import multiply

    assert multiply(2, 3) == 6
    assert multiply(6, 5) == 30
    assert multiply(0, 1) == 0
    assert multiply(5, 0) == 0
