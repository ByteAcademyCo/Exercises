def test_solution():
    from solution import minimum_parentheses

    assert minimum_parentheses("") == 0
    assert minimum_parentheses("(") == 1
    assert minimum_parentheses("()(()())") == 0
    assert minimum_parentheses("()((") == 2
    assert minimum_parentheses("()))((()") == 4
