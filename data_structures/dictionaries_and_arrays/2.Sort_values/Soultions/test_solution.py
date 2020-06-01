def test_solution(monkeypatch):
    x= None
    y= None 

    def g(num1,num2):
        nonlocal x
        nonlocal y
        x=num1
        y=num2

    monkeypatch.setattr('builtins.print',g)
    

    import solution