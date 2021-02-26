
def test_solution(monkeypatch):
    x = ['Charlie','100']
    index = -1

    def f():
        nonlocal index
        nonlocal x
        index += 1
        return x[index]

    
    monkeypatch.setattr('builtins.input',f)
    import solution 
    assert solution.name == 'Charlie'
    assert solution.age == '100'
