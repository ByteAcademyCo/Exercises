def test_solution():
    from solution import Clock, Calendar, CalendarClock

    assert str(Clock(10, 30, 5)) == "10:30:05"
    assert str(Calendar(20, 10, 2020)) == "20/10/2020"
    assert str(CalendarClock(20, 10, 2020, 10, 30, 5)) == "20/10/2020, 10:30:05"
