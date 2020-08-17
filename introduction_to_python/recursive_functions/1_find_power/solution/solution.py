# Write your solution here
def power(a, b):
    if a == 0:
        return 0
    elif b == 0:
        return 1
    else:
        return a*power(a,b-1)