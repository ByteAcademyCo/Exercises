def test_solution():
    import solution
    
    assert solution.longest_palindrome_substr("abaccad") == 4
    assert solution.longest_palindrome_substr("abcadefb") == 1
    assert solution.longest_palindrome_substr("") == 0
    assert solution.longest_palindrome_substr("a") == 1
    assert solution.longest_palindrome_substr("abcadefbbfcfbbfeads") == 11