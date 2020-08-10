def test_solution(monkeypatch):
    ret_val = []

    def g(num):
        ret_val.append(num)

    monkeypatch.setattr("builtins.print", g)

    import solution
    from array import array

    solution.print_array(array("i", [10, 20, 30]))

    assert ret_val[0] == 10
    assert ret_val[1] == 20
    assert ret_val[2] == 30
