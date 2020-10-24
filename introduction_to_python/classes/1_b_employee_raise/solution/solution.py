class Employee:
    def __init__(self, name, employee_id, salary, years_at_company):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self.years_at_company = years_at_company

    def give_raise(self):
        if self.years_at_company <= 5:
            self.salary += 5000
        elif self.years_at_company >= 10:
            self.salary += 10000
        else:
            self.salary += 8000


def give_raises(employee_lst):
    for emp in employee_lst:
        emp.give_raise()
        
        