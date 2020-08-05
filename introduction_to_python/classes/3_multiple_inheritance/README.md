# Multiple Inheritance Implementation

# Problem Description
 Write a Python program to implement Multiple Inheritance. Write two base classes `Clock` and `Calendar` and a derived class `CalendarClock` which derives from the base classes `Clock` and `Calendar`.
 In the `Clock` class:
 * The constructor function should take in `hrs` an integer between `0-23`, `mins` and integer between `0-59`, and `secs` an integer between `0-59` and set the values in the constructor.
 * Use the `__str__` magic method to create a string representation for the clock in the format `hrs:mins:secs`. Hint: Use `"{0:02d}:{1:02d}:{2:02d}".format()` 

 In the `Calendar` class:
 * The constructor function should take in `day` an integer between `1-31`, `month` and integer between `1-12`, and `year` an integer between `1900-2020` and set the values in the constructor. For the sake of this question, we will not worry about checking if the day is a valid day for a given month.
 * Use the `__str__` magic method to create a string representation for the calendar in the format `day/month/year`. Hint: Use `"{0:02d}/{1:02d}/{2:4d}".format()` 

 In the `CalendarClock` derived class:
 * The constructor function should take in `day`, `month`, `year`, `hrs`, `mins`, `secs` and set the values using the base class constructors in its constructor.
 * Use the `__str__` magic method to create a string representation for the calendar in the format `day/month/year hrs:mins:secs`.

 For Example:
 ```
 str(Clock(10, 30, 5)) => "10:30:05"
 str(Calendar(20, 10, 2020)) => "20/10/2020"
 str(CalendarClock(20, 10, 2020, 10, 30, 5)) => "20/10/2020, 10:30:05"
 ```

## Testing
* To test your solution, type 'pytest' within the solution subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory