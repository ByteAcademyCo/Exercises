from operator import attrgetter


class Employee:
    def __init__(self, name, employee_id, salary, years_at_company):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self.years_at_company = years_at_company


def sort_employees(employee_lst):
    emp_lst = sorted(employee_lst, key=attrgetter("name"))
    return [emp.name for emp in emp_lst]


emp1 = Employee("John", 1, 45000, 8)
emp2 = Employee("Jane", 2, 22000, 1)
emp3 = Employee("Marie", 3, 90000, 10)
emp4 = Employee("Mark", 3, 90000, 5)

print(sort_employees([emp1, emp2, emp3, emp4]))
