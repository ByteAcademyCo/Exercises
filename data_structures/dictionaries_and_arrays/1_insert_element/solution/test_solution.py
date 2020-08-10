def test_solution(monkeypatch):
    import solution
    from array import array

    assert solution.insert_element(array("i", [1, 2, 3, 4, 5]),3, 10) == array("i", [1, 2, 3, 10, 4, 5])
