def reverse(string):
    return '' if string == '' else reverse(string[1:]) + string[0]

