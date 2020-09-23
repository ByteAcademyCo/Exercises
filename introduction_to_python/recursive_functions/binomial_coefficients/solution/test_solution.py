def test_solution():
    from solution import binomial_coefficient

    assert binomial_coefficient(6, 2) == 15
    assert binomial_coefficient(5, 0) == 1
    assert binomial_coefficient(4, 3) == 4
    assert binomial_coefficient(0, 0) == 1
    assert binomial_coefficient(18, 1) == 18
    assert binomial_coefficient(20, 5) == 15504
