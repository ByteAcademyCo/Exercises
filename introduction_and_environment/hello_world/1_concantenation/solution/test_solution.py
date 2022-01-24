def test_solution(monkeypatch):
    x = ["Good Morning ", "Universe"]
    i = -1

    def f():
        nonlocal x
        nonlocal i
        i+=1
        return x[i]

    monkeypatch.setattr('builtins.input',f)

    from solution import string_1, string_2, result
    assert result == string_1 + string_2
