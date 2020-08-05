def test_solution():
    import solution
    test_str = solution.MyString()
    assert test_str.upper_string() == 'undefined'
    
    test_str.set_string('hello')
    assert test_str.upper_string() == 'HELLO'
