def test_solution(monkeypatch):
    x=["E"]
    index=-1

    def f(string):
        nonlocal index
        nonlocal x
        index+=1
        return x[index]

    monkeypatch.setattr('builtins.input', f)

    from solution import letter, result
    if letter in ['a','e','i','o','u','A','E','I','O','U']:
          assert result == 'vowel'
    else:
        assert result == 'consonant'  



