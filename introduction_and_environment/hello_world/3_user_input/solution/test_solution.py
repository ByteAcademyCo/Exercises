
def test_solution(monkeypatch):
    x = [4, 5, 6]
    i = -1
    def f(string):
        nonlocal x
        nonlocal i
        i+=1
        return x[i]
    monkeypatch.setattr('builtins.input', f)

    from solution import num1, num2, num3, avg
    assert (sum([num1,num2,num3])/3) == avg

