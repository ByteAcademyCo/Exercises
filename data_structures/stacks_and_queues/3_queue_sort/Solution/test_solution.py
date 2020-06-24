def test_solution(monkeypatch):
    ret_val1= None
    space=" "

    def g(num1,num2):
        nonlocal ret_val1
        nonlocal space
        ret_val1=num1
        space=num2

    monkeypatch.setattr('builtins.print',g)

    import solution



