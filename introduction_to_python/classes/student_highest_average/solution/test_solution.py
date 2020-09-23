def test_solution():
    from solution import Student, highest_avg

    Anton = Student("Anton", 29, [75, 82, 96, 100, 50])
    Nell = Student("Nell", 26, [98, 95, 89, 92, 100, 90])
    Cosette = Student("Cosette", 20, [85, 72, 96, 99, 92])
    Cam = Student("Cam", 25, [85, 72, 96, 99, 92])

    assert highest_avg([Anton, Nell, Cosette]) == "Nell"
    assert highest_avg([Cam, Anton, Cosette]) == "Cam"
    assert highest_avg([Anton]) == "Anton"
