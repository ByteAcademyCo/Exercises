# Code your solution here
def shut_down(x):
    if x=="true"or x=="True":
        data="SHUTTING DOWN"
    elif x=="false" or x=="False":
        data="SHUTDOWN ABORTED"
    else:
        data="SORRY"
    return data 
x=str(input())
result=shut_down(x)
print(result)