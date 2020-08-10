def test_solution(monkeypatch):
    import solution
    from array import array

    assert solution.square_keys(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
