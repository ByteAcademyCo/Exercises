from solution import concat_args


def test_solution():
    assert concat_args("Hello ", "There") == "Hello There"
    assert concat_args() == ""
    assert concat_args("COZY") == "COZY"
