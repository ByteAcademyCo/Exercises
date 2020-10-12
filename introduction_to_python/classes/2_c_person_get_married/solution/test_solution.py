def test_solution():
    from solution import Person, Child

    Anton = Person("Anton", 29, None, [])
    Nell = Person("Nell", 26, None, [])
    Anton.get_married(Nell)

    assert Anton.spouse.name == "Nell"
    assert Nell.spouse.name == "Anton"
