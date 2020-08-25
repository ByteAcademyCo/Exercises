class VendingMachine:
    max_cap = 10
    def __init__(self):
        self._sodas = {"Coca-Cola": 5,
                        "Sprite": 5,
                        "Mountain-Dew": 5}
        self._soda_costs = {"Coca-Cola": 2.0,
                            "Sprite": 2.0,
                            "Mountain-Dew": 2.0}

    def set_machine_cost(self, soda, cost):
        self._soda_costs[soda] = cost
        return f'Vending Machine cost for {soda} is ${cost}.'

    def get_vending_machine_stock(self):
        Coca_Cola_amt = self._sodas["Coca-Cola"]
        Sprite_amt = self._sodas["Sprite"]
        Mountain_Dew_amt = self._sodas["Mountain-Dew"]
        return f'Vending Machine has {Coca_Cola_amt} Coca-Cola, {Sprite_amt} Sprite, and {Mountain_Dew_amt} Mountain-Dew.'

    

class SodaShop:
    def __init__(self):
        self._inventory = {"Coca-Cola": 10,
                        "Sprite": 10,
                        "Mountain-Dew": 10}
        self._inventory_costs = {"Coca-Cola": 1.0,
                                 "Sprite": 1.0,
                                 "Mountain-Dew": 1.0}

    def set_shop_cost(self, soda, cost):
        self._inventory_costs[soda] = cost
        return f'Soda Shop cost for {soda} is ${cost}.'
    
    def create_soda(self, soda, amount):
        self._inventory[soda] += amount
        return f'{amount} {soda} Created.'

    def get_shop_stock(self):
        Coca_Cola_amt = self._inventory["Coca-Cola"]
        Sprite_amt = self._inventory["Sprite"]
        Mountain_Dew_amt = self._inventory["Mountain-Dew"]
        return f'Soda Shop has {Coca_Cola_amt} Coca-Cola, {Sprite_amt} Sprite, and {Mountain_Dew_amt} Mountain-Dew.'
        
class Student:
    def __init__(self, name="", id=None):
        self._name = name
        self._id = id
        self._id_card_funds = 10
    
    def __str__(self):
        return self._name

class UniversityAdministrator:
    def __init__(self, institution_name=""):
        self._institution_name = institution_name
        self._funds = 100.0
        self._students = {}
        self._student_count = 0
        self._vending_machine = VendingMachine()
    
    def enroll_student(self, student):
        namelst = [s._name for s in self._students.values()]
        if student in namelst:
            return f'Error: {student} Already Enrolled.'
        else:
            self._student_count += 1
            new_student = Student(student, self._student_count)
            self._students[self._student_count] = new_student
            return f'{student} Enrolled.'

    def add_funds(self, student, funds):
        for s in self._students.values():
            if s._name == student:
                s._id_card_funds += funds
                return f'${funds} Added to {student}.'
        return f'Error: {student} Not Enrolled.'

    def buy_soda(self, student, soda):
        for s in self._students.values():
            if s._name == student:
                if s._id_card_funds >= self._vending_machine._soda_costs[soda]:
                    s._id_card_funds -= self._vending_machine._soda_costs[soda]
                    self._vending_machine._sodas[soda] -= 1
                    self._funds += self._vending_machine._soda_costs[soda]
                    return f'{student} Bought {soda}.'
                return f'Error: Insufficient Funds.'
        return f'Error: {student} Not Enrolled.'

    def get_student_funds(self, student):
        for s in self._students.values():
            if s._name == student:
                funds = s._id_card_funds
                return f'{student} has ${funds}.'
        return f'Error: {student} Not Enrolled.'
    
    def get_university_funds(self):
        funds = self._funds
        return f'University has ${funds}.'

    def refill_vm(self, soda1, amount1, soda2, amount2, soda3, amount3, shop):
        num_soda1 = self._vending_machine._sodas[soda1] + amount1
        num_soda2 = self._vending_machine._sodas[soda2] + amount2
        num_soda3 = self._vending_machine._sodas[soda3] + amount3
        cost = amount1 * shop._inventory_costs[soda1]
        cost += amount2 * shop._inventory_costs[soda2]
        cost += amount3 * shop._inventory_costs[soda3]
        if shop._inventory[soda1] < amount1 or shop._inventory[soda2] < amount2 or shop._inventory[soda3] < amount3:
            return f'Error: Shop out of soda.'
        elif self._funds < cost:
            return f'Error: Insufficient Funds.'
        elif num_soda1 > self._vending_machine.max_cap or num_soda2 > self._vending_machine.max_cap or num_soda3 > self._vending_machine.max_cap:
            return f'Error: Over Max Quantity.'
        else:
            self._vending_machine._sodas[soda1] = num_soda1
            self._vending_machine._sodas[soda2] = num_soda2
            self._vending_machine._sodas[soda3] = num_soda3

            shop._inventory[soda1] -= amount1
            shop._inventory[soda2] -= amount2
            shop._inventory[soda3] -= amount3

            self._funds -= cost
            return f'Refilled Machine with {amount1} {soda1}, {amount2} {soda2}, {amount3} {soda3}.'

# To test your code: navigate to the solution folder in your terminal
# and type 'python3 vending_machine.py ../testing/test_n/input.txt'
# where n is replaced by the number of the test.

# You may also test your code using the command line by navigating to the 
# solution folder in your terminal and typing 'python3 vending_machine.py'.

# Do not modify this code.
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 2 and 'input.txt' in argv[1]:
        file_path = argv[1]
        test_num = argv[1][-11]
        input_file = open(f'{file_path}', "r")
        output_file = open(f'../testing/test_{test_num}/output.txt', "w")
        university = UniversityAdministrator()
        shop = SodaShop()
        output_lines = []
        try:
            while (line := input_file.readline()) != 'quit':
                words = line.split()
                function = words[0]
                if function == "enroll_student":
                    output_lines.append(university.enroll_student(words[1]))
                elif function == "add_funds":
                    output_lines.append(university.add_funds(words[1], float(words[2])))
                elif function == "buy_soda":
                    output_lines.append(university.buy_soda(words[1], words[2]))
                elif function == "create_soda":
                    output_lines.append(shop.create_soda(words[1], int(words[2])))
                elif function == "set_machine_cost":
                    output_lines.append(university._vending_machine.set_machine_cost(words[1], float(words[2])))
                elif function == "set_shop_cost":
                    output_lines.append(shop.set_shop_cost(words[1], float(words[2])))
                elif function == "get_student_funds":
                    output_lines.append(university.get_student_funds(words[1]))
                elif function == "get_university_funds":
                    output_lines.append(university.get_university_funds())
                elif function == "get_vending_machine_stock":
                    output_lines.append(university._vending_machine.get_vending_machine_stock())
                elif function == "get_shop_stock":
                    output_lines.append(shop.get_shop_stock())
                elif function == "refill_vm":
                    output_lines.append(university.refill_vm(words[1], int(words[2]), words[3], int(words[4]), words[5], int(words[6]), shop))
                output_lines.append("\n")
            output_file.writelines(output_lines[:-1])
        except:
            output_lines.append("Something went wrong!")
            output_file.writelines(output_lines)

    elif len(argv) == 1:
        output_file = open(f'output_command_line.txt', "w")
        university = UniversityAdministrator()
        shop = SodaShop()
        output_lines = []

        while (function := input("Enter a command: ")) != 'quit':
            try:
                if function == "enroll_student":
                    student = input("Enter the name of the student to be enrolled: ")
                    ret_string = university.enroll_student(student)
                    output_lines.append(ret_string)
                    print(ret_string)
                elif function == "add_funds":
                    student = input("Enter the name of the student to add funds to: ")
                    amount = input("Enter the amount of funds to add: ")
                    ret_string = university.add_funds(student, float(amount))
                    output_lines.append(ret_string)
                    print(ret_string)
                elif function == "buy_soda":
                    student = input("Enter the name of the student who wishes to buy a soda: ")
                    amount = input(f'Enter the type of soda {student} wishes to buy: ')
                    ret_string = university.buy_soda(student, amount)
                    output_lines.append(ret_string)
                    print(ret_string)
                elif function == "create_soda":
                    soda = input("Enter the type of soda to be created: ")
                    amount = input(f'Enter the amount of {soda} to be created: ')
                    ret_string = shop.create_soda(soda, int(amount))
                    output_lines.append(ret_string)
                    print(ret_string)
                elif function == "set_machine_cost":
                    soda = input("Enter the type of soda: ")
                    cost = input(f'Enter the new cost for {soda}: ')
                    ret_string = university._vending_machine.set_machine_cost(soda, float(cost))
                    output_lines.append(ret_string)
                    print(ret_string)
                elif function == "set_shop_cost":
                    soda = input("Enter the type of soda: ")
                    cost = input(f'Enter the new cost for {soda}: ')
                    ret_string = shop.set_shop_cost(soda, float(cost))
                    output_lines.append(ret_string)
                    print(ret_string)
                elif function == "get_student_funds":
                    student = input("Enter the name of the student: ")
                    ret_string = university.get_student_funds(student)
                    output_lines.append(ret_string)
                    print(ret_string)
                elif function == "get_university_funds":
                    ret_string = university.get_university_funds()
                    output_lines.append(ret_string)
                    print(ret_string)
                elif function == "get_vending_machine_stock":
                    ret_string = university._vending_machine.get_vending_machine_stock()
                    output_lines.append(ret_string)
                    print(ret_string)
                elif function == "get_shop_stock":
                    ret_string = shop.get_shop_stock()
                    output_lines.append(ret_string)
                    print(ret_string)
                elif function == "refill_vm":
                    soda1 = input("Enter the first type of soda: ")
                    amount1 = input(f"Enter the amount of {soda1} you wish to refill: ")
                    soda2 = input("Enter the second type of soda: ")
                    amount2 = input(f"Enter the amount of {soda2} you wish to refill: ")
                    soda3 = input("Enter the third type of soda: ")
                    amount3 = input(f"Enter the amount of {soda3} you wish to refill: ")
                    if (sodas := sorted([soda1, soda2, soda3])) != ["Coca-Cola", "Mountain-Dew", "Sprite"]:
                        print("The given sodas are not valid. Sodas must be one of Coca-Cola, Sprite, and Mountain-Dew. Please try again!")
                    else:
                        ret_string = university.refill_vm(soda1, int(amount1), soda2, int(amount2), soda3, int(amount3), shop)
                        output_lines.append(ret_string)
                        print(ret_string)
                else:
                    print(f'{function} is not a valid command. Please try again!')
                    continue
                output_lines.append("\n")
            except:
                print("Something went wront! Please try again!")
        output_file.writelines(output_lines[:-1])
    else:
        print('Must call with valid path to "input.txt"')