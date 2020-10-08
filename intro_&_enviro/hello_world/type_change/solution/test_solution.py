
def test_solution(monkeypatch):
    ret_val1 = None
    ret_val2 = None

    def g(num1, num2):
        nonlocal ret_val1
        nonlocal ret_val2
        ret_val1 = num1
        ret_val2 = num2
    
    monkeypatch.setattr('builtins.print',g)

    import solution
    assert type(solution.object_1) == float and type(solution.object_2) == str
    assert type(ret_val1) == str and type(ret_val2) == int