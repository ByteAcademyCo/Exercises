class Student:
    def __init__(self, name=None, avg=None, grade=None):
        self.name = name
        self.avg = avg
        self.grade = grade
    
    def __lt__(self, other):
        if self.grade < other.grade:
            return True
        if self.grade == other.grade:
            if self.avg < other.avg:
                return True
            if self.avg == other.avg:
                return self.name < other.name
        return False

    def __repr__(self):
        return f'name: {self.name} avg: {self.avg} grade: {self.grade}'

def sort_students(slst):
    return sorted(slst)

student1 = Student("Bob", 75, 10)
student2 = Student("Annie", 90, 8)
student3 = Student("Carrie", 82, 8)
student4 = Student("Harry", 75, 10)

slst = [student1, student2, student3, student4]
print(sort_students(slst))