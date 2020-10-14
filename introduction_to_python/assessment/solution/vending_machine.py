class VendingMachine:
    def __init__(self):
        pass

    def set_machine_cost(self, soda, cost):
        pass

    def get_vending_machine_stock(self):
        pass
    

class SodaShop:
    def __init__(self):
        pass

    def set_shop_cost(self, soda, cost):
        pass
    
    def create_soda(self, soda, amount):
        pass

    def get_shop_stock(self):
        pass

class Student:
    def __init__(self, name="", id=None):
        pass
    
    def __str__(self):
        pass

class UniversityAdministrator:
    def __init__(self, institution_name=""):
        pass
    
    def enroll_student(self, student):
        pass

    def add_funds(self, student, funds):
        pass

    def buy_soda(self, student, soda):
        pass

    def get_student_funds(self, student):
        pass
    
    def get_university_funds(self):
        pass

    def refill_vm(self, soda1, amount1, soda2, amount2, soda3, amount3, shop):
        pass


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
