# Code your solution here
# x = bool(input('Enter a boolean value: '))
x = 'false'
def data(x):
    if x == True:
        return 'SHUTDOWN'
    elif x == False:
        return 'SHUTDOWN ABORTED'
    else:
        return 'This is not a boolean value.'
result = data(x)
print(result)