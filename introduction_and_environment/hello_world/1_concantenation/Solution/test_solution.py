

def test_solution(monkeypatch):
    # x="Good Morning "
    # y="Universe"
    # ret_val1=None

    # def g(num1):
    #     nonlocal ret_val1
    #     ret_val1=num1

    # monkeypatch.setattr('builtins.print',g)

    import solution
    assert solution.result == solution.string_1 + solution.string_2
    # assert solution.string_2==y
