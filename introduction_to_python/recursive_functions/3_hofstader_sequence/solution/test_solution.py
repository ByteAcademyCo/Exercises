def test_solution():
    from solution import hofstaderA, hofstaderB

    assert hofstaderA(4) == 3
    assert hofstaderB(4) == 2
    assert hofstaderA(0) == 1
    assert hofstaderB(0) == 0
    assert hofstaderA(6) == 4
    assert hofstaderB(6) == 4