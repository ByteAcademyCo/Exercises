
def test_solution():


    from solution import x, y, X,Y
    assert type(x) == float and type(X) == str and X == str(x)
    assert type(y) == str and type(Y) == int and Y == int(y)