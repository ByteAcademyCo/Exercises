def test_solution(monkeypatch):
    x=['1','2','3','4','5','6','7']
    ret_val1= None

    def g(num1):
        nonlocal ret_val1
        ret_val1=num1

    monkeypatch.setattr('builtins.print',g)

    import solution
    assert solution.stack_planets==x


