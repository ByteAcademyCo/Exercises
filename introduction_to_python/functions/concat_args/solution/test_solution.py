import solution


def test_solution():
    assert solution.concat_input("hello ", "world") == "hello world"
    assert solution.concat_input("hello", "") == "hello"
