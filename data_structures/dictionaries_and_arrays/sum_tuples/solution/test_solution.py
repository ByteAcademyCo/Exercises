def test_solution(monkeypatch):
    from solution import sum_tuples

    assert sum_tuples([(1,2), (3,4)]) == [3, 7]
    assert sum_tuples([(-1,-2)]) == [-3]
    assert sum_tuples([]) == []
