class Employee():
    def __init__(self, name, employee_id = 0, salary = 0, years_at_company = 0):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self.years_at_company = years_at_company
    
cosette = Employee("Cosette Rodger", 1, 100000, 4)