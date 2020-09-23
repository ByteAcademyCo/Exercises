def test_solution():
    import solution

    assert solution.backspace_compare("ab#c", "ad#c") == True
    assert solution.backspace_compare("a##c", "#a#c") == True
    assert solution.backspace_compare("a#c", "c#d") == False
