def test_solution(monkeypatch):
    x= None

    def g(num1):
        nonlocal x
        x=num1

    monkeypatch.setattr('builtins.print',g)
    

    import solution