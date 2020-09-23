class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def get_avg(self):
        num_grades = len(self.grades)
        if num_grades == 0:
            return 0
        sum_grades = 0
        for g in self.grades:
            sum_grades += g
        return sum_grades / num_grades


def highest_avg(stud_lst):
    stud_name = ""
    max_avg = 0
    for s in stud_lst:
        s_avg = s.get_avg()
        if s_avg > max_avg:
            max_avg = s_avg
            stud_name = s.name
        elif s_avg == max_avg:
            if s.name < stud_name:
                stud_name = s.name
    return stud_name
