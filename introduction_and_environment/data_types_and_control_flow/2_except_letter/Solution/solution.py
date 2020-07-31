# Code your solution here
string = 'BYTE ACADEMY'
vowels = ['A', 'E', 'I', 'O', 'U']
def data(x):
    ans = False
    for characters in string:
        if characters != vowels:
            ans = True
    return ans
print(data)
        