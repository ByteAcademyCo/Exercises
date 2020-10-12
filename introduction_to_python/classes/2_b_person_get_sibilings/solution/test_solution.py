def test_solution():
    from solution import Person, Child

    Jonny = Person("Jonny", 32, None, [])
    Beth = Person("Beth", 28, Jonny, [])
    Jonny.spouse = Beth
    Max = Child("Max", 5, None, [], [Jonny])
    Annie = Child("Annie", 10, None, [], [Beth])
    Ron = Child("Ron", 7, None, [], [Beth, Jonny])
    Jonny.children.extend([Max, Ron])
    Beth.children.extend([Annie, Ron])

    Jack = Person("Jack", 32, None, [])
    Donna = Person("Donna", 28, Jack, [])
    Jack.spouse = Donna
    Alex = Child("Alex", 10, None, [], [Jack, Donna])
    Bob = Child("Bob", 12, None, [], [Jack, Donna])
    Emily = Child("Emily", 1, None, [], [Jack, Donna])
    Jack.children.extend([Alex, Bob, Emily])
    Donna.children.extend([Alex, Bob, Emily])

    Ken = Person("Ken", 32, None, [])
    Chloe = Child("Chloe", 5, None, [], [Ken])
    Ken.children.append(Chloe)

    assert Ron.get_siblings() == ["Max", "Annie"]
    assert Alex.get_siblings() == ["Emily", "Bob"]
    assert Chloe.get_siblings() == []
