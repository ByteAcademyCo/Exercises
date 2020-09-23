def test_solution():
    import solution

    student1 = solution.Student("Bob", 75, 10)
    student2 = solution.Student("Annie", 90, 8)
    student3 = solution.Student("Carrie", 82, 8)
    student4 = solution.Student("Harry", 75, 10)

    slst = [student1, student2, student3, student4]
    assert solution.sort_students(slst) == [student3, student2, student1, student4]
    assert solution.sort_students([]) == []
    assert solution.sort_students([student1]) == [student1]
    assert solution.sort_students([student2, student3]) == [student3, student2]
    assert solution.sort_students([student4, student1]) == [student1, student4]
