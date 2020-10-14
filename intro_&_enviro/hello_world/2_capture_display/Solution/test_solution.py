
def test_solution(monkeypatch):
    x=['Charlie','100']
    index=-1
    ret_val1=None
    ret_val2=None

    def f():
        nonlocal index
        nonlocal x
        index += 1
        return x[index]
    
    def g(num1,num2):
        nonlocal ret_val1
        nonlocal ret_val2
        ret_val1=num1
        ret_val2=num2
    
    monkeypatch.setattr('builtins.input',f)
    monkeypatch.setattr('builtins.print',g)
    import solution 
    assert solution.name=='Charlie'
    assert solution.age=='100'
