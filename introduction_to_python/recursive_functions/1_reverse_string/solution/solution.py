# Write your solution here
def reverse(string):
    if string == '':
        return ''
    else:
        return reverse(string[1:]) + string[0]