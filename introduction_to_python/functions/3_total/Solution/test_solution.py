def test_solution(monkeypatch):
    x=[10,20,30,40,50,60]
    ret_val1= None

    def g(num1):
        nonlocal ret_val1
        ret_val1=num1

    monkeypatch.setattr('builtins.print',g)

    import solution
    assert solution.l==x


