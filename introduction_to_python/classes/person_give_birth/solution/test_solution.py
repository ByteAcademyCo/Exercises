def test_solution():
    from solution import Person, Child

    Jonny = Person("Jonny", 32, None, [])
    Beth = Person("Beth", 28, Jonny, [])
    Jonny.spouse = Beth
    Beth.give_birth("Sam")

    Jane = Person("Jane", 32, None, [])
    Max = Child("Max", 2, None, [], [Jane])
    Jane.children.append(Max)
    Jane.give_birth("Annie")

    assert Beth.children[0].name == "Sam"
    assert Jonny.children[0].name == "Sam"
    assert Beth.children[0].parents[0].name == "Beth"
    assert Jonny.children[0].parents[1].name == "Jonny"

    assert Jane.children[1].name == "Annie"
    assert Jane.children[1].parents[0].name == "Jane"
    assert Jane.children[1].age == 0
    assert Jane.children[1].spouse == None
    assert Jane.children[1].children == []
