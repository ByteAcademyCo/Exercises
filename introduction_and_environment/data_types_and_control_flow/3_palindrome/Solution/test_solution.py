def test_solution(monkeypatch):
    monkeypatch.setattr('builtins.input',lambda: "racecar")

    import solution
    assert solution.is_palindrome == True



