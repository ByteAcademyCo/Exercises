def test_solution(monkeypatch):
    numbers = [10, 20]
    ret_val1 = None
    index = -1

    def f(a):
        nonlocal index
        nonlocal numbers
        index += 1
        return numbers[index]

    def g(num1):
        nonlocal ret_val1
        ret_val1 = num1

    monkeypatch.setattr("builtins.input", f)
    monkeypatch.setattr("builtins.print", g)

    from app_solution import result

    # assert app_solution.number_1==10
    # assert app_solution.number_2==10
    assert result == 30

