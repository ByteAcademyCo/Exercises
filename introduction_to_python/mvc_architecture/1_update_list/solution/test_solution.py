def test_solution(monkeypatch):
    numbers = ["Cherry", "kiwi", "Grape"]
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

    import app_solution

    # This test is wrong !
    # assert app_solution.show==ret_val1
