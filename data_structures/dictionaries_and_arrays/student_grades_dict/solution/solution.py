def average(glst):
    avg = 0
    for g in glst:
        avg += g
    return int(avg/len(glst))

def get_letter(avg, letter_grades):
    for letter, grade_range in letter_grades.items():
        if avg in range(grade_range[0], grade_range[1]+1):
            return letter

def student_grades(sgrades, letter_grades):
    ret_dict = {}
    for name, grades in sgrades.items():
        avg = average(grades)
        letter = get_letter(avg, letter_grades)
        ret_dict[name] = (letter, avg)
    return ret_dict
    