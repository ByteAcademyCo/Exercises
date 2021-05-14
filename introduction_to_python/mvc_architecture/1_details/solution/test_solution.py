def test_solution(monkeypatch):
    info = ["John", "100"]
    ret_val1 = None
    index = -1

    def f(a):
        nonlocal index
        nonlocal info
        index += 1
        return info[index]

    def g(num1):
        nonlocal ret_val1
        ret_val1 = num1

    monkeypatch.setattr("builtins.input", f)
    monkeypatch.setattr("builtins.print", g)

    from app_solution import name, age, info

    assert name == "John"
    assert age == "100"
    assert info == ret_val1
