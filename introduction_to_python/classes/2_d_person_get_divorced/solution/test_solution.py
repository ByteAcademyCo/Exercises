def test_solution():
    from solution import Person
    from solution import Child

    jim = Person("Jim Brown", 45)
    suzy = Person("Suzy Brown", 42, jim)
    jim.spouse = suzy
    martha = Child("Martha Brown", 18, None, [], [jim, suzy])
    jim.children.append(martha)
    suzy.children.append(martha)

    jim.get_divorced()
    martha.get_divorced()

    assert jim.spouse == None
    assert suzy.spouse == None
    assert martha.spouse == None
