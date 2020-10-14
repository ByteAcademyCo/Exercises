def test_solution(monkeypatch):
    y=50
    ret_val1= None

    def g(num1):
        nonlocal ret_val1
        ret_val1=num1
    monkeypatch.setattr('builtins.print',g)

    import solution
    assert solution.x==y



