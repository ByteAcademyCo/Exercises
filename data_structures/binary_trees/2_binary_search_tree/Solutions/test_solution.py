def test_solution(monkeypatch):
    ret_val= None
    
    def g(result):
        nonlocal ret_val
        ret_val = result 

    monkeypatch.setattr('builtins.print',g)
    

    