from provided_code import grades
letter_grades = []

for grade in grades:
    if grade < 35:
        letter_grades.append("F")
    elif grade < 50:
        letter_grades.append("D")
    elif grade < 70:
        letter_grades.append("C")
    elif grade < 90:
        letter_grades.append("B")
    else:
        letter_grades.append("A")