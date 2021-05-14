

def test_solution(monkeypatch):
    x=['hi',3]
    index=-1

    def f(string):
        nonlocal x
        nonlocal index
        index+=1
        return x[index]

    monkeypatch.setattr('builtins.input',f)

    from solution import result, str1, mult
    assert type(str1) == str and type(mult) == int
    assert result == str1 * mult

