
def test_solution(monkeypatch):
    print_val = 0
    def f(x):
        nonlocal print_val
        print_val = x
    monkeypatch.setattr('builtins.input', lambda: 100)
    monkeypatch.setattr('builtins.print', f)
    import solution
    assert solution.first_num == solution.second_num == solution.third_num == print_val == 100
