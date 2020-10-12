class Person:
    def __init__(self, name, age, spouse=None, children=[]):
        self.name = name
        self.age = age
        self.spouse = spouse
        self.children = children

    def give_birth(self, name):
        baby = Child(name, 0, None, [], [self])
        self.children.append(baby)
        if self.spouse:
            self.spouse.children.append(baby)
            baby.parents.append(self.spouse)


class Child(Person):
    def __init__(self, name, age, spouse, children, parents):
        Person.__init__(self, name, age, spouse, children)
        self.parents = parents


Jonny = Person("Jonny", 32, None, [])
Beth = Person("Beth", 28, Jonny, [])
Jonny.spouse = Beth
Beth.give_birth("Sam")
print(Beth.children[0].name)
print(Jonny.children[0].name)
print(Beth.children[0].parents[0].name)
print(Beth.children[0].parents[1].name)
