# Code your solution here
line = input('Enter any string value:')

if line == line[::-1]:
    is_palindrome = True
else:
    is_palindrome = False

print(is_palindrome)