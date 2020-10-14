# Code your solution here
line=input()
is_palindrome=bool
for i in range(0,len(line)//2):
    if line[i]!=line[len(line)-i-1]:
        is_palindrome=False
    else:
        is_palindrome=True 
print(is_palindrome)