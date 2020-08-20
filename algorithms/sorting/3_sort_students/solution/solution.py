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
        return f'Name: {self.name}, Avg: {self.avg}, Grade: {self.grade}'
    
def sort_students(slst):
    return sorted(slst)
