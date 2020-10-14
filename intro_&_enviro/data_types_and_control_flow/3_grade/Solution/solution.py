# Code your solution here
mark=int(input())
if mark >90 and mark <=100:
    grade='A'
elif mark>70 and mark <=90:
    grade='B'
elif mark>50 and mark<=70:
    grade='C'
elif mark>35 and mark<=50:
    grade='D'
else:
    grade='F'

print(grade)