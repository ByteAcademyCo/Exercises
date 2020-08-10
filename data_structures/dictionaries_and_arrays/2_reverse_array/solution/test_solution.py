def test_solution(monkeypatch):
    import solution
    from array import array

    assert solution.reverse(array("i", [1, 3, 5, 3, 7, 1, 9, 3])) == array(
        "i", [3, 9, 1, 7, 3, 5, 3, 1]
    )
