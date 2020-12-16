def test_solution():
    from solution import postfix_eval

    assert postfix_eval("123+*") == 9
    assert postfix_eval("") == 0
    assert postfix_eval("2") == 2
    assert postfix_eval("3134-*/") == 1.5
    assert postfix_eval("142-*") == -6
