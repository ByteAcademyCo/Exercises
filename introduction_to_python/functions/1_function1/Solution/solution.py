# Code your solution heree
def ranger(number):
    if number >=0 and number <=100:
        data="Hooray, Falls in my range"
    else:
        data="Oops,outside range"
    return data
number=int(input())
result=ranger(number)
print(result)
