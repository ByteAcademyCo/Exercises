import solution

def test_solution():
    assert solution.concat_args("Hello ", "There") == "Hello There"
    assert solution.concat_args() == ''
    assert solution.concat_args("COZY") == "COZY"

