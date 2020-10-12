def test_solution():
    from solution import divisible_by_3

    assert divisible_by_3(2, 3, 5, 6, 9) == [3, 6, 9]
    assert divisible_by_3(1, 2, 4) == []
    assert divisible_by_3(9) == [9]
    assert divisible_by_3() == []
