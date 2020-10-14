import pytest

ret_val_1= None
ret_val_2= None
ret_val_3= None

def g(x,x1,x2):
    global ret_val_1
    global ret_val_2
    global ret_val_3
    ret_val_1 = x
    ret_val_2 = x1
    ret_val_3 = x2

def test_solution(monkeypatch):
    monkeypatch.setattr('builtins.print',g)
    
    import solution as s

    assert ret_val_1 == bin(0b1110)
    assert ret_val_2 == bin(0b11)
    assert ret_val_3 == bin(0b1100)
    

    

