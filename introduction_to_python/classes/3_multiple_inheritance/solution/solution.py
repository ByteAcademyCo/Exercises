class Clock(object): 
    def __init__(self, hrs=0, mins=0, secs=0): 
        pass

    def __str__(self):
        return
  
class Calendar(object): 
    def __init__(self, day=1, month=1, year=2020):
        pass

    def __str__(self):
        return
        
  
class CalendarClock(Clock, Calendar): 
    def __init__(self, day, month, year, hrs, mins, secs):
        pass
  
    def __str__(self):
        return     