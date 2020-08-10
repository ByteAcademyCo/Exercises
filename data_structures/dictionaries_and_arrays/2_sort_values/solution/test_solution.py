def test_solution(monkeypatch):
    import solution

    assert solution.sort_dict({1: 2, 3: 4, 4: 3, 2: 1, 0: 0}) == {
        0: 0,
        2: 1,
        1: 2,
        4: 3,
        3: 4
    }
