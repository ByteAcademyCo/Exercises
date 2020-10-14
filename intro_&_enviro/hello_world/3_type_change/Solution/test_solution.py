
def test_solution(monkeypatch):
    ret_val1= None
    ret_val2=None

    def g(num1,num2):
        nonlocal ret_val1
        nonlocal ret_val2
        ret_val1=num1
        ret_val2=num2
    
    monkeypatch.setattr('builtins.print',g)

    import solution
    assert solution.object_1==100.0
    assert solution.object_2=="99"