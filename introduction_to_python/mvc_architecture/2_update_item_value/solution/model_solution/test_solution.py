def test_solution(monkeypatch):
    program_list = ["1", "2", "3", "4", "5"]
    ret_val1 = None
    index = -1

    def f(a):
        nonlocal index
        nonlocal program_list
        index += 1
        return program_list[index]

    def g(num1):
        nonlocal ret_val1
        ret_val1 = num1

    monkeypatch.setattr("builtins.input", f)
    monkeypatch.setattr("builtins.print", g)

    import app_solution

    assert app_solution.result == ret_val1
