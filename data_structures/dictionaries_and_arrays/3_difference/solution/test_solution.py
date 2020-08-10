def test_solution(monkeypatch):
    import solution
    from array import array

    assert solution.difference(array("i", [5, 8, 12, 15, 10, 7])) == 10
