# Code your solution here
# n = int(input(Enter any integer: ))
n = 4

def numbers(n):
    factorial = 1
    if int(n) >= 1:
        for i in range(1, int(n) + 1):
            factorial = factorial * i

result = numbers(n)
print(result)