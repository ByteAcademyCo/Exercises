def test_solution(monkeypatch):
    from solution import squares_dict

    assert squares_dict(3) == {1:1, 2: 4, 3: 9}
    assert squares_dict(1) == {1:1}
    assert squares_dict(4) == {1:1, 2: 4, 3: 9, 4: 16}