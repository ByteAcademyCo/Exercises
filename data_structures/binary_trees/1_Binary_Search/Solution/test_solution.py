def test_solution(monkeypatch):
    a = None
    x = 2

    def g(num1):
        nonlocal a 
        a = num1 
    
    def f():

        nonlocal x
        return x
    
    monkeypatch.setattr('builtins.print',g)
    
    monkeypatch.setattr('builtins.input',f)

    import solution
    assert solution.ele==x


