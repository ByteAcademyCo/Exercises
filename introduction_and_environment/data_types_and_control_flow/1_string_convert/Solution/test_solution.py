def test_solution(monkeypatch):
    x=['hi']
    index=-1

    def f(string):
        nonlocal x
        nonlocal index
        index+=1
        return x[index]

    monkeypatch.setattr('builtins.input',f)

    from solution import string, data
    if string.isupper():
        assert data == string.lower()
    else:
        assert data == string.upper()

