def test_solution():
    from solution import jim, suzy, martha

    assert jim.name == "Jim Brown"
    assert jim.age == 45
    assert jim.spouse == suzy
    assert jim.children[0] == martha

    assert suzy.name == "Suzy Brown"
    assert suzy.age == 42
    assert suzy.spouse == jim
    assert suzy.children[0] == martha

    assert martha.name == "Martha Brown"
    assert martha.age == 18
    assert martha.spouse == None
    assert martha.children == []
    assert martha.parents[0] == jim
    assert martha.parents[1] == suzy
