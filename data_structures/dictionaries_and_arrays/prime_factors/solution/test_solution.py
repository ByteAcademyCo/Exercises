def test_solution():
    from solution import prime_factors

    assert prime_factors(1) == [1]
    assert prime_factors(13) == [1, 13]
    assert prime_factors(4) == [1, 2]
    assert prime_factors(10) == [1, 2, 5]
    assert prime_factors(12) == [1, 2, 3]