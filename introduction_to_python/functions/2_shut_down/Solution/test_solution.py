import solution

def test_solution():
    assert solution.shut_down(True) == "SHUTDOWN"
    assert solution.shut_down(False) == "SHUTDOWN ABORTED"


