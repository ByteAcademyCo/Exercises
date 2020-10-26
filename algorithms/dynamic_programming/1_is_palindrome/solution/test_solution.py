def test_solution():
    import solution
    
    assert solution.is_palindrome("racecar") == True
    assert solution.is_palindrome("a") == True
    assert solution.is_palindrome("racecars") == False
    assert solution.is_palindrome("lol") == True
    assert solution.is_palindrome("noon") == True
    assert solution.is_palindrome("at") == False
    assert solution.is_palindrome("shrek") == False
    
