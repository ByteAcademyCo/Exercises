def test_solution(monkeypatch):
    import solution

    assert (
        solution.convert({"students": [{"firstName": "Nikki", "lastName": "Roysden"}]})
        == '{"students": [{"firstName": "Nikki", "lastName": "Roysden"}]}'
    )
