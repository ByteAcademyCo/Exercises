import solution
def test_solution():
    assert solution.py_solution().reverse_words("") == ""
    assert solution.py_solution().reverse_words("Hello World") == "World Hello"
    assert solution.py_solution().reverse_words("hi there bob") == "bob there hi"
    assert solution.py_solution().reverse_words("l o w") == "w o l"