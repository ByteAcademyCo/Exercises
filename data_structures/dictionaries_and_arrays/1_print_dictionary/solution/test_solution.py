def test_solution(monkeypatch):
    ret_val = []

    def g(num):
        ret_val.append(num)

    monkeypatch.setattr("builtins.print", g)

    import solution

    solution.print_dict({1: 10, 2: 20, 3: 30})

    assert ret_val[0] == 10
    assert ret_val[1] == 20
    assert ret_val[2] == 30
