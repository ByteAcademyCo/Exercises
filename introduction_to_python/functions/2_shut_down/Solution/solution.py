# x = bool(input('Enter a boolean value: '))
x = 'false'
def shut_down(x):
    if x == True:
        return 'SHUTDOWN'
    elif x == False:
        return 'SHUTDOWN ABORTED'
    else:
        return '.'