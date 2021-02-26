def test_solution(monkeypatch):
    x=[3, 5, 4, 8, 9, 7, 6, 1]
    i = -1

    def f():
        nonlocal x
        nonlocal i 
        i += 1 
        return x[i]

    monkeypatch.setattr('builtins.input',f)

    import solution
    assert solution.g_lst == ['Triangle', 'Pentagon', 'Quadrilateral', 'Octagon', 'Nonagon', 'Heptagon', 'Hexagon']



