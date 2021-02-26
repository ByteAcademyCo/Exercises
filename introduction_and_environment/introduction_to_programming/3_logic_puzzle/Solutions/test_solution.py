from solution import a, b, c, d


def test_solution():
    assert type(a) == list
    assert type(c) == float
    assert type(a or b) == str
    assert (d and b) == "rocketship"
    assert (b or d) == "rocketship"
    assert (c and d) == 0.0
    assert type(c or d) == int
    assert c + d == 5.0
    

