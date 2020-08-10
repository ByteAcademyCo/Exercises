def test_solution(monkeypatch):
    import solution
    from array import array

    assert solution.occurances(array("i", [1, 3, 5, 3, 7, 9]), 3) == 2
