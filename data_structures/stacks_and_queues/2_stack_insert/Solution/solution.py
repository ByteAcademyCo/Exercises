# Code your solution here
def insert(stack_planets):
    stack_planets.insert(2,'Earth') 
    return stack_planets

stack_planets=['Mercury','Venus','Mars','Jupiter','Saturn','Uranus','Neptune']
result=insert(stack_planets)
print(result)