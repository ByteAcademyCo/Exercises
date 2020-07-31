# Code your solution here
def grade(mark):
    if mark >= 90:
        return 'A+ GRADE'
    elif mark >= 70:
        return 'B GRADE'
    elif mark >= 50:
        return 'C GRADE'
    elif mark >= 35:
        return 'D GRADE'
    else:
        return 'FAIL'
# score = int(input("Enter your grade here:"))
mark = 80
print(grade(mark))
# grade(score)