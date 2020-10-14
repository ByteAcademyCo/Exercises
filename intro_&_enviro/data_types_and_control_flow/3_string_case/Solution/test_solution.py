def test_solution(monkeypatch):
    x='Beautiful World'
    ret_val1= None
    ret_val2= None

    def f():
        nonlocal x
        return x

    def g(num1,num2):
        nonlocal ret_val1
        nonlocal ret_val2
        ret_val1=num1
        ret_val2=num2

    monkeypatch.setattr('builtins.input',f)
    monkeypatch.setattr('builtins.print',g)

    import solution
    assert solution.string_val==x



