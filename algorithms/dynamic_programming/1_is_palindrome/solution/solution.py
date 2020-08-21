def is_palindrome(string):
    if len(string) <= 1:
        return True
    else:
        return string[0] == string[-1] 
        is_palindrome(string[1:-1])