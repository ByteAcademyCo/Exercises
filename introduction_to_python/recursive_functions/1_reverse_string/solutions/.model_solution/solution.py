def reverse(string):
    return '' if string is '' else reverse(string[1:]) + string[0]

