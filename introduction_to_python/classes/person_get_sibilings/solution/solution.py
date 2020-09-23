from operator import attrgetter


class Person:
    def __init__(self, name, age, spouse=None, children=[]):
        self.name = name
        self.age = age
        self.spouse = spouse
        self.children = children


class Child(Person):
    def __init__(self, name, age, spouse, children, parents):
        Person.__init__(self, name, age, spouse, children)
        self.parents = parents

    def get_siblings(self):
        sib_lst = []
        for parent in self.parents:
            sib_lst = list(set(sib_lst) | set(parent.children))
        sib_lst.remove(self)
        sib_lst = sorted(sib_lst, key=attrgetter("age"))
        sib_names = [sib.name for sib in sib_lst]
        return sib_names


Jonny = Person("Jonny", 32, None, [])
Beth = Person("Beth", 28, Jonny, [])
Jonny.spouse = Beth
Max = Child("Max", 5, None, [], [Jonny])
Annie = Child("Annie", 10, None, [], [Beth])
Ron = Child("Ron", 7, None, [], [Beth, Jonny])
Jonny.children.extend([Max, Ron])
Beth.children.extend([Annie, Ron])
print(Ron.get_siblings())
