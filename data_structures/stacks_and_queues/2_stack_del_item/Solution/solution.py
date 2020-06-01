# Code your solution here
def delete(stack_continents):
    del stack_continents[5] # indexing value of the 6th element from the stack 
    return stack_continents

stack_continents=['North America','Europe','Asia','South America','Antartica','Australia','Africa']
result=delete(stack_continents)
print(result)