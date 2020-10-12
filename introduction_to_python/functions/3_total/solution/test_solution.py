from solution import sum_data


def test_solution():
    assert sum_data([]) == 0
    assert sum_data([1]) == 1
    assert sum_data([1, 2, 3]) == 6
    assert sum_data([2, 4, 6, 8]) == 20
