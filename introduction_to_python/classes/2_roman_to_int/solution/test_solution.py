import solution

def test_solution():
    assert solution.py_solution().roman_to_int("V") == 5
    assert solution.py_solution().roman_to_int("VI") == 6
    assert solution.py_solution().roman_to_int("X") == 10
    assert solution.py_solution().roman_to_int("CL") == 150