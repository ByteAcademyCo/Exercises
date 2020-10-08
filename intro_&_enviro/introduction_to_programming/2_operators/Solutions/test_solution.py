import pytest

ret_val= None

def g(result):
    global ret_val
    ret_val = result

def test_solution(monkeypatch):
    monkeypatch.setattr('builtins.print',g)
    
    import solution
    
    assert ret_val == "Hexadecimal"
    

