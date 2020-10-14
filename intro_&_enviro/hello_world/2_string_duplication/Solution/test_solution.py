

def test_solution(monkeypatch):
    x=['Charlie',5]
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
    assert solution.string_1=='Charlie'
    assert solution.dup_val==5

