def test_solution(monkeypatch):
    a = None


    def g(num1):
        nonlocal a

        a = num1

    monkeypatch.setattr('builtins.print',g)


    import solution