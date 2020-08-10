def test_solution(monkeypatch):
    import solution

    assert solution.update_dict(1,"Bob") == {1: "Bob"}
