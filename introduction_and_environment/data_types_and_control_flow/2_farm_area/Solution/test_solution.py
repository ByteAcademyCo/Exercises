def test_solution(monkeypatch):
    x=[6,4]
    index=-1
    ret_val1= None

    def f():
        nonlocal index
        nonlocal x
        index+=1
        return x[index]

    def g(num1):
        nonlocal ret_val1
        ret_val1=num1

    monkeypatch.setattr('builtins.input',f)
    monkeypatch.setattr('builtins.print',g)

    import solution
    assert solution.length==6
    assert solution.breadth==4



