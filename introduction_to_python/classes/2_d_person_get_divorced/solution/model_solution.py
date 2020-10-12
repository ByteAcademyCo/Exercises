class Person:
    def __init__(self, name, age, spouse=None, children=[]):
        self.name = name
        self.age = age
        self.spouse = spouse
        self.children = children

    def get_divorced(self):
        if self.spouse:
            spouse = self.spouse
            spouse.spouse = None
            self.spouse = None


class Child(Person):
    def __init__(self, name, age, spouse, children, parents):
        Person.__init__(self, name, age, spouse, children)
        self.parents = parents


jim = Person("Jim Brown", 45)
suzy = Person("Suzy Brown", 42, jim)
jim.spouse = suzy
martha = Child("Martha Brown", 18, None, [], [jim, suzy])
jim.children.append(martha)
suzy.children.append(martha)

jim.get_divorced()
print(jim.spouse)
print(suzy.spouse)

John = Person("John", 31, None, [])
Kathy = Person("Kathy", 29, John, [])
John.spouse = Kathy
John.get_divorced()
print(John.spouse)
print(Kathy.spouse)
