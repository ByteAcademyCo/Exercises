# Code your solution here
def ranger(number):
    if number >=0 and number <=100:
        data="GREATNESS"
    else:
        data="OOPS"
    return data
number=int(input())
result=ranger(number)
print(result)