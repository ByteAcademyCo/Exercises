def test_solution(monkeypatch):
    x=['ByteAcademy']
    index=-1

    def f(string):
        nonlocal x
        nonlocal index
        index+=1
        return x[index]

    monkeypatch.setattr('builtins.input',f)

    from solution import string, strlen
    assert type(string) == str
    assert strlen == len(string)
  

    