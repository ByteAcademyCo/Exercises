def test_solution():
    import solution
    
    assert solution.longest_common_subseq("abcdabcf", "ecfdacagb") == 4
    assert solution.longest_common_subseq("", "") == 0
    assert solution.longest_common_subseq("abc", "") == 0
    assert solution.longest_common_subseq("", "a") == 0
    assert solution.longest_common_subseq("a", "bc") == 0
    assert solution.longest_common_subseq("a", "ba") == 1
    assert solution.longest_common_subseq("abcdefg", "hijklmn") == 0
    assert solution.longest_common_subseq("abcda", "fgafbhadce") == 3