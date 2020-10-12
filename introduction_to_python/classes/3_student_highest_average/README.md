# Student Class - Highest Average

# Problem Description
Define a class `Student` with attributes `name` - a string, `age` - a non-negative integer, and `grades` - a list of integers between 0-100.
Define a function, `highest_avg`, that consumes a non-empty list of student objects `stud_lst`, and returns the name of the sudent with the highest average. If two students have the same average, return the name of the student who's name comes first alphabetically.

 ## Example
 ```
 Anton = Student("Anton", 29, [75, 82, 96, 100, 50])
 Nell = Student("Nell", 26, [98, 95, 89, 92, 100, 90])
 Cosette = Student("Cosette", 20, [85, 72, 96, 99, 92])
 highest_avg([Anton, Nell, Cosette]) == "Nell"
 ```

## Testing
* To test your solution, type 'pytest' within the solution subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory