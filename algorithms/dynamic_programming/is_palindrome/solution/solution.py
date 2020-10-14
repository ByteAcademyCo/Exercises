def is_palindrome(string):
    # a string of len 1 is by defnition a palindrome so we return True
    if len(string) <= 1:
        return True
    else:
        # if the first and last charaters are equal
        # we recurse in the rest of the string removing the
        # first and last character to check if the rest of
        # the string is a palindrome.
        return string[0] == string[-1] and is_palindrome(string[1:-1])