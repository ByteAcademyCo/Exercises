def test_solution():
    from solution import remove_ages

    pdict = {"Nell": 26, "Sue": 30, "Billy": 4}
    
    assert remove_ages(pdict, 10, 30) == {"Nell": 26, "Sue": 30}
    assert remove_ages({}, 10, 30) == {}
    assert remove_ages({"b": 10}, 12, 40) == {}
    assert remove_ages({"b": 10}, 10, 10) == {"b": 10}