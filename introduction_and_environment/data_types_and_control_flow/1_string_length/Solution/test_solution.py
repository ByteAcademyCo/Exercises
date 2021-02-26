def test_solution(monkeypatch):
    x='Hello'
    monkeypatch.setattr('builtins.input', lambda: x)

    import solution
    assert solution.strlen == 5

    