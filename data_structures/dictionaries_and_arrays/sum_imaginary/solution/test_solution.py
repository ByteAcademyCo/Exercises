def test_solution():
    from solution import sum_imaginary

    assert sum_imaginary([(1,2), (4,-1), (0, 0), (-2, -2)]) == (3,-1)
    assert sum_imaginary([(1,2)]) == (1,2)
    assert sum_imaginary([]) == (0,0)