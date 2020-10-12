class Person:
    def __init__(self, name, age, spouse=None, children=[]):
        self.name = name
        self.age = age
        self.spouse = spouse
        self.children = children

    def get_married(self, other):
        self.spouse = other
        other.spouse = self


class Child(Person):
    def __init__(self, name, age, spouse, children, parents):
        Person.__init__(self, name, age, spouse, children)
        self.parents = parents


Anton = Person("Anton", 29, None, [])
Nell = Person("Nell", 26, None, [])
Anton.get_married(Nell)
print(Anton.spouse.name)
print(Nell.spouse.name)
