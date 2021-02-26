def test_solution(monkeypatch):
    x=[6,4]
    index=-1

    def f():
        nonlocal index
        nonlocal x
        index+=1
        return x[index]

    monkeypatch.setattr('builtins.input', f)

    import solution
    assert solution.length == 6
    assert solution.width == 4
    assert solution.area == 24



