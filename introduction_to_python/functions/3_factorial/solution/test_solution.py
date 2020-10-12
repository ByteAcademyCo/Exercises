from solution import factorial


def test_solution():
    assert factorial(1) == 1
    assert factorial(0) == 1
    assert factorial(10) == 3628800
    assert factorial(3) == 6
    assert factorial(2) == 2
