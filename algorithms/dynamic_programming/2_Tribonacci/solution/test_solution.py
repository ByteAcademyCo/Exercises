def test_solution():
    import solution
    
    assert solution.tribonacci(0) == 0
    assert solution.tribonacci(1) == 0
    assert solution.tribonacci(2) == 1
    assert solution.tribonacci(3) == 1
    assert solution.tribonacci(4) == 2
    assert solution.tribonacci(5) == 4
    assert solution.tribonacci(10) == 81
    assert solution.tribonacci(15) == 1705
    assert solution.tribonacci(19) == 19513