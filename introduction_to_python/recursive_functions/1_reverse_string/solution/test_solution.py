def test_solution():
    import solution
    assert solution.reverse('hello') == 'olleh'
    assert solution.reverse('') == ''
    assert solution.reverse('h') == 'h'
    assert solution.reverse('yes') == 'sey'
