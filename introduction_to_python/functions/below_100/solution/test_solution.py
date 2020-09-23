import solution


def test_solution():
    assert solution.below_100(100) == "greater than 100"
    assert solution.below_100(200) == "greater than 100"
    assert solution.below_100(55) == "less than 100"
