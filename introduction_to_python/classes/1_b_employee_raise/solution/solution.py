class Employee:

    def __init__(self, name, employee_id, salary, years_at_company):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self.years_at_company = years_at_company


def give_raises(employee_lst):
    for emp in employee_lst:
        if emp.years_at_company <= 5:
            emp.salary = emp.salary + 5000
        elif emp.years_at_company > 5 and emp.years_at_company < 10:
            emp.salary = emp.salary + 8000
        else:
            emp.years_at_company >= 10
            emp.salary = emp.salary + 10000
