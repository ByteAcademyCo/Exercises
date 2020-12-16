def test_solution():
    from solution import binary_numbers

    assert binary_numbers(1) == ['1']
    assert binary_numbers(2) == ['1', '10']
    assert binary_numbers(4) == ['1', '10', '11', '100']
    assert binary_numbers(5) == ['1', '10', '11', '100', '101']
