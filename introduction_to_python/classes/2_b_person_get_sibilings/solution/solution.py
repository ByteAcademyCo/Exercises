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

    def get_siblings(self, children):
        self.child_by_age = []
        children.sort(key=self.child_by_age)
        for self.child in children:
            return self.children.age
