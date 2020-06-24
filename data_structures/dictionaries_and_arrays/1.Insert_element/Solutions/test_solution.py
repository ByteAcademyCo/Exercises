def test_solution(monkeypatch):
    x=[2,5]
    index=-1
    ret_val= None

    def f():
        nonlocal x
        nonlocal index
        index+=1
        return x[index]

    def g(num):
        nonlocal ret_val
        ret_val=num

    monkeypatch.setattr('builtins.input',f)
    monkeypatch.setattr('builtins.print',g)

    import solution
    assert solution.ins_pos==2
    assert solution.ins_val==5