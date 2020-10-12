def test_solution(monkeypatch):
    books = ["book_a", "book_b", "book_c"]
    ret_val1 = None
    index = -1

    def f(a):
        nonlocal index
        nonlocal books
        index += 1
        return books[index]

    def g(num1):
        nonlocal ret_val1
        ret_val1 = num1

    monkeypatch.setattr("builtins.input", f)
    monkeypatch.setattr("builtins.print", g)

    import app_solution

    assert app_solution.data == ret_val1
