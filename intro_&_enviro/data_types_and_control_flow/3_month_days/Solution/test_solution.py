def test_solution(monkeypatch):
    x='august'
    ret_val1= None

    def f():
        nonlocal x
        return x

    def g(num1):
        nonlocal ret_val1
        ret_val1=num1

    monkeypatch.setattr('builtins.input',f)
    monkeypatch.setattr('builtins.print',g)

    import solution
    assert solution.month==x



