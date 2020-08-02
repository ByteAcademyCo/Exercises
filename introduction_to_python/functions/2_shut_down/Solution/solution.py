def shut_down(x):
    if x == True:
        return 'SHUTDOWN'
    elif x == False:
        return 'SHUTDOWN ABORTED'
    else:
        return 'This is not a boolean value.'