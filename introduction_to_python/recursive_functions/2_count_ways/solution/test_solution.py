def test_solution():
    from solution import count_ways

    assert count_ways(steps=2) == 2
    assert count_ways(steps=10) == 89
    assert count_ways(steps=20) == 10946
    assert count_ways(steps=0) == 1
    assert count_ways(steps=1) == 1
