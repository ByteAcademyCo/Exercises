def test_solution(monkeypatch):
    print_val = 0
    def f(x):
        nonlocal print_val
        print_val = x
    monkeypatch.setattr('builtins.input', lambda: 100)
    monkeypatch.setattr('builtins.print', f)
    import solution as S
    assert S.FIRST_NUM == S.SECOND_NUM == S.THIRD_NUM == print_val == 100
