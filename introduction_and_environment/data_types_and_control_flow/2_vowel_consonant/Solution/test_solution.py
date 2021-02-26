def test_solution(monkeypatch):
    monkeypatch.setattr('builtins.input',lambda: "E")

    from solution import letter, result
    assert letter == "E"
    assert result == "vowel"



