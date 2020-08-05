def test_solution():
    import solution
    assert str(solution.Clock(10, 30, 5)) == "10:30:05"
    assert str(solution.Calendar(20, 10, 2020)) == "20/10/2020"
    assert str(solution.CalendarClock(20, 10, 2020, 10, 30, 5)) == "20/10/2020, 10:30:05"