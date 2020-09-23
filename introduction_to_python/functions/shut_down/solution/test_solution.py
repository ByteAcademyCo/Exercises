from solution import shut_down


def test_solution():
    assert shut_down(True) == "SHUTDOWN"
    assert shut_down(False) == "SHUTDOWN ABORTED"
