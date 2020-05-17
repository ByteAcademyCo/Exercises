def test_solution(monkeypatch):
    y='true'
    x='false'
    ret_val1= None

    def f():
        nonlocal y
        return y

    def g(num1):
        nonlocal ret_val1
        ret_val1=num1

    monkeypatch.setattr('builtins.input',f)
    monkeypatch.setattr('builtins.print',g)

    import solution
    assert solution.x==y or solution.x==x


