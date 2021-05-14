def test_solution(monkeypatch):
    x=[6,4]
    index=-1

    def f(string):
        nonlocal index
        nonlocal x
        index+=1
        return x[index]

    monkeypatch.setattr('builtins.input', f)

    from solution import length, width, area
    assert area == length * width 



