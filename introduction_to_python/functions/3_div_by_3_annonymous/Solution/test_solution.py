import solution

def test_solution():
    assert solution.div_by_3(2, 3, 5, 6, 9) == [3, 6, 9]
    assert solution.div_by_3(1, 2, 4) == []
    assert solution.div_by_3(9) == [9]
    assert solution.div_by_3() == []



