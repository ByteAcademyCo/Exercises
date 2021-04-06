

def test_solution(monkeypatch):
    x=['hi',3]
    index=-1

    def f():
        nonlocal x
        nonlocal index
        index+=1
        return x[index]

    monkeypatch.setattr('builtins.input',f)

    from solution import result
    assert result == "hihihi"

