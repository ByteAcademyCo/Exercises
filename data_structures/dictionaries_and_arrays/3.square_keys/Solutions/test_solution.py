def test_solution(monkeypatch):
    x=5
    ret_val= None
    

    def f(str):
        nonlocal x
        return x

    def g(num):
        nonlocal ret_val
        ret_val=num

    monkeypatch.setattr('builtins.input',f)
    monkeypatch.setattr('builtins.print',g)
    

    import solution
    assert solution.num==x