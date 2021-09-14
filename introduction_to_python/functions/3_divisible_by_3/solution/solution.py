# Write your code here

def divisible_by_3(*args):
    div_3 = []
    for num in args:
        if num % 3 == 0:
            return  div_3.append(num) 

print(divisible_by_3(2,3,5,6,9))
