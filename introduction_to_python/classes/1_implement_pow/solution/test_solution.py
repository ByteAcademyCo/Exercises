import solution

def test_solution():
    assert solution.py_solution().pow(2, -3) == 0.125
    assert solution.py_solution().pow(2, 2) == 4
    assert solution.py_solution().pow(0, 1) == 0
    assert solution.py_solution().pow(-1, 3) == -1
    assert solution.py_solution().pow(-2, 3) == -8
    assert solution.py_solution().pow(2, 0) == 1