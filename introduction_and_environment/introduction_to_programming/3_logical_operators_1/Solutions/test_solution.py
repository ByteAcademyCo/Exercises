import pytest

ret_val_1= None

def g(x):
    global ret_val_1
    ret_val_1 = x

def test_solution(monkeypatch):
    monkeypatch.setattr('builtins.print',g)
    
    import solution as s

    assert ret_val_1 == False
    

    

