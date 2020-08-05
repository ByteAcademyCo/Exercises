class Person(object): 
      
    # Constructor 
    def __init__(self, name): 
        self.name = name 
  
    # To get name 
    def getName(self): 
        return self.name 
  
    # To check if this person is employee 
    def isEmployee(self): 
        return False
    
    def __str__(self):
        return 'Person(name='+self.name+')'
  
  
# Inherited or Sub class (Note Person in bracket) 
class Employee(Person): 
  
    # Here we return true 
    def isEmployee(self): 
        return True

    def __str__(self):
        return 'Employee(name='+self.name+')'