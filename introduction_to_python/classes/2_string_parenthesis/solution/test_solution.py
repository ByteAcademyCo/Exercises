import solution

def test_solution():
    assert solution.py_solution().is_valid_parenthese("") == True
    assert solution.py_solution().is_valid_parenthese("{}") == True
    assert solution.py_solution().is_valid_parenthese("(") == False
    assert solution.py_solution().is_valid_parenthese("{]") == False
    assert solution.py_solution().is_valid_parenthese("({[]})") == True
    assert solution.py_solution().is_valid_parenthese("{}[]()") == True