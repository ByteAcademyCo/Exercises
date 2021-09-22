class Person:

    def __init__(self, name, age, spouse, children):
        self.name = name
        self.age = age
        self.spouse = spouse
        self.children = children


class Child(Person):
    def __init__(self, name, age, spouse, children, parents):
        Person.__init__(self, name, age, spouse, children)
        self.parents = parents


jim = Person('Jim Brown', 45, None, [])
suzy = Person('Suzy Brown', 42, None, [])
martha = Child('Martha Brown', 18, None, [], [])

jim.spouse = suzy
suzy.spouse = jim
jim.children.append(martha)
suzy.children.append(martha)
martha.parents.append(jim)
martha.parents.append(suzy)
