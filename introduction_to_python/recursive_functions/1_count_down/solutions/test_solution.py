def test_solution(monkeypatch):
    ret_val= []
    def g(num):
        ret_val.append(num)
        
    monkeypatch.setattr('builtins.print',g)

    import solution
    solution.count_down_from(3)
    
    assert ret_val[0] == 3
    assert ret_val[1] == 2
    assert ret_val[2] == 1
    assert len(ret_val) == 3
    
    
