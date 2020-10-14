

def test_solution(monkeypatch):
    ret_val1=None
    def g(num1):
        nonlocal ret_val1
        ret_val1=num1

    monkeypatch.setattr('builtins.print',g)

    import solution
    assert solution.string_value=="Hello Universe"
    assert solution.data=="Hello"