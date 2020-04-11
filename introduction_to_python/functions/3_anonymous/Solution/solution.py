# Code your solution here
def anomy(*l):
    result=list(filter(lambda x:(x%13==0),l))
    return result 

result=anomy(12,26,39,130,23,56,77)
print(result)