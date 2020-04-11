def test_solution(monkeypatch):
    x=[1,2,3]
    index=-1
    ret_val1= None

    def f():
        nonlocal x
        nonlocal index
        index+=1
        return x[index]

    def g(num1):
        nonlocal ret_val1
        ret_val1=num1

    monkeypatch.setattr('builtins.input',f)
    monkeypatch.setattr('builtins.print',g)

    import solution
    assert solution.a==1
    assert solution.b==2
    assert solution.c==3
    



