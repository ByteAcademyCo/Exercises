class Clock(object): 
    def __init__(self, hrs=0, mins=0, secs=0): 
        self.hrs = hrs
        self.mins = mins
        self.secs = secs

    def __str__(self):
        return "{0:02d}:{1:02d}:{2:02d}".format(self.hrs, self.mins, self.secs)
  
class Calendar(object): 
    def __init__(self, day=1, month=1, year=2020):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return "{0:02d}/{1:02d}/{2:4d}".format(self.day, self.month, self.year)
        
  
class CalendarClock(Clock, Calendar): 
    def __init__(self, day, month, year, hrs, mins, secs):
        self.day = day
        self.month = month
        self.year = year
        self.hrs = hrs
        self.mins = mins
        self.secs = secs
  
    def __str__(self):
        return "{0:02d}/{1:02d}/{2:4d}".format(self.day, self.month, self.year) + ', ' + "{0:02d}:{1:02d}:{2:02d}".format(self.hrs, self.mins, self.secs)