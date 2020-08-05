import solution

def test_solution():
    assert solution.py_solution().int_to_Roman(5) == "V"
    assert solution.py_solution().int_to_Roman(6) == "VI"
    assert solution.py_solution().int_to_Roman(10) == "X"
    assert solution.py_solution().int_to_Roman(150) == "CL"