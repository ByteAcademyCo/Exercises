# Code your solution here
def value(a,b,c):
    if a>b and a>c:
        max_value=a
    elif b>a and b>c:
        max_value=b
    elif c>a and c>b:
        max_value=c
    else:
        max_value=None
    return max_value 
a=int(input())
b=int(input())
c=int(input())
result=value(a,b,c)
print(result)