def test_solution(monkeypatch):
    numbers = ["1", "2", "3", "4", "5"]
    # list_a={'1':'World War Z','2':'Inception','3':'Black Mirror','4':'Once Upon A Time In Hollywood','5':'Birdman'}
    ret_val1 = None
    index = -1

    def f(a):
        nonlocal index
        nonlocal numbers
        index += 1
        return numbers[index]

    def g(num1):
        nonlocal ret_val1
        ret_val1 = num1

    monkeypatch.setattr("builtins.input", f)
    monkeypatch.setattr("builtins.print", g)

    import app_solution

    # assert app_solution.number_1==10
    # assert app_solution.number_2==10
    assert app_solution.final_list == ret_val1
