# Code your solution here
def grade(mark):
    if mark >= 90:
<<<<<<< HEAD
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
=======
        # return 'A+ GRADE'
        print('A+ GRADE')
    elif mark >= 70:
        # return 'B GRADE'
        print('B GRADE')
    elif mark >= 50:
        # return 'C GRADE'
        print('C GRADE')
    elif mark >= 35:
        # return 'D GRADE'
        print('D GRADE')
    else:
        # return 'FAIL'
        print('FAIL')
score = int(input("Enter your grade here:"))
print(grade(score))
>>>>>>> d536594... Pushing exercises
# grade(score)