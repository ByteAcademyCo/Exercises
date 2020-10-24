from operator import attrgetter
class Employee():
    def __init__(self, name, employee_id, salary, years_at_company):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self.years_at_company = years_at_company

def sort_employees(employee_lst):
    emp_lst = sorted(employee_lst, key=attrgetter("name"))
    return [emp.name for emp in emp_lst]