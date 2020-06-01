def test_solution(monkeypatch):
    ret_val= None

    def g(num):
        nonlocal ret_val
        ret_val=num

    monkeypatch.setattr('builtins.print',g)

    import solution