def test_solution_upper(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda: "UNIVERSE")
    import solution
    assert solution.data == "universe"

