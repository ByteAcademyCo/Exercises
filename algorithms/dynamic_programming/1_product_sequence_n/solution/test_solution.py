def test_solution():
    import solution
    
    assert solution.product_sequence_n(2) == 2
    assert solution.product_sequence_n(5) == 15
    assert solution.product_sequence_n(1) == 1
    assert solution.product_sequence_n(8) == 384
    assert solution.product_sequence_n(9) == 945
    
