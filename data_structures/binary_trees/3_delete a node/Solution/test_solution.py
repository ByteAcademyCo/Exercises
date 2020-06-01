def test_solution(monkeypatch):
    a = None
    b = None

    def g(num1,num2):
        nonlocal a
        nonlocal b
        a = num1
        b = num2
    monkeypatch.setattr('builtins.print',g)


    import solution