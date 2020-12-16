def test_solution(monkeypatch):
    from solution import student_grades
    letter_grades = {"A": (90, 100), "B": (75, 89), "C": (60, 74), "D": (45, 59), "E": (30, 44), "F": (1, 29)}

    sgrades1 = {"Anton": [62, 55, 82], "Wasif": [100, 72, 94, 50], "Nell": [99, 100]}
    ret_val1 = {"Anton": ("C", 66), "Wasif": ("B", 79), "Nell": ("A", 99)}

    sgrades2 = {"Bob": [1, 30], "Sue": [35]}
    ret_val2 = {"Bob": ("F", 15), "Sue": ("E", 35)}

    assert student_grades(sgrades1, letter_grades) == ret_val1
    assert student_grades(sgrades2, letter_grades) == ret_val2
