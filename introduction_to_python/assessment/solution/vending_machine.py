class VendingMachine:
    def __init__(self):
        self.sodas = {  'Coca-Cola': {'cost':2, 'quantity':5},
                        'Sprite': {'cost':2, 'quantity':5},
                        'Mountain-Dew': {'cost':2, 'quantity':5},
                        }


class SodaShop:
    def __init__(self):
        self.sodas = {  'Coca-Cola': {'cost':1, 'quantity':10},
                        'Sprite': {'cost':1, 'quantity':10},
                        'Mountain-Dew': {'cost':1, 'quantity':10},
                        }
    
    def create_soda(self, soda, quantity):
        self[soda]['quantity'] += quantity

    def set_cost(self, soda, cost):
        self[soda]['cost'] = cost


class Student:
    def __init__(self, name):
        self.name = name
        self.funds = 10

    def add_funds(self, funds):
        self.funds += funds

    def buy_sodas(self, funds):
        self.funds -= funds

class University:
    def __init__(self):
        self.funds = 100
        self.students = {}
        self.num_students = 0

    def enroll_student(self, student):
        self.students[self.num_students] = student
        self.num_students += 1
        
    def refill_vending_machine(self, soda_info):
        pass

    def change_soda_cost(self, soda_info):
        pass

class VendingMachineError(Exception):
    def __init__(self):
        pass


if __name__ == '__main__':
    from sys import argv
    if len(argv) == 2 and argv[1] == 'input.txt':
        input_file = open('input.txt')
        while command := input_file.readline():
            print(command)
    elif len(argv) == 1:
        while (command := input()) != 'quit':
            print(command)
    else:
        print('Must call with no arguments or "input.txt"')

