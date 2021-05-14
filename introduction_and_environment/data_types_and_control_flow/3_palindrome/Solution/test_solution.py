def test_solution(monkeypatch):
    x=["civic"]
    index=-1

    def f(string):
        nonlocal index
        nonlocal x
        index+=1
        return x[index]

    monkeypatch.setattr('builtins.input', f)

    from solution import word, is_palindrome
    if word == word[::-1]:
        assert is_palindrome == True
    else:
        assert is_palindrome == False



