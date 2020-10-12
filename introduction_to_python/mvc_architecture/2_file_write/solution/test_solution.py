def test_solution(monkeypatch):
    filename = ["filename_x", "filename_y", "filename_z"]
    ret_val1 = None
    index = -1

    def f(a):
        nonlocal index
        nonlocal filename
        index += 1
        return filename[index]

    def g(num1):
        nonlocal ret_val1
        ret_val1 = num1

    monkeypatch.setattr("builtins.input", f)
    monkeypatch.setattr("builtins.print", g)

    import app_solution

    assert app_solution.result == ret_val1
