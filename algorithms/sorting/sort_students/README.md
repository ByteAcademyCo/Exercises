# Linked Lists - Sort a Linked List

## Motivation
Sorting is one of the most studied type of algorithms in computer science. There are many different sorting algorithms which may have different benifits and drawbacks given the problem you are trying to solve and your data. You must consider your time contraints and space constraints when choosing the appropriate sorting algorithm for your problem.
Sorting is important because it allows us to optimize data searching to a very high level, when data is stored in a sorted manner. Sorting also allows us to represent data in more readable formats.

## Problem Description
You are given a class Student, where Students have a name (a string), average (an integer value between 0-100), and grade (an integer value between 1-12). In the *solution.py* file, define a function `sort_students` that consumes a list of Students `slst` and returns a sorted list of Students in increasing order, where the students are sorted first by grade, then by average, then by name. You may use the magic method `__lt__`, and you may use any sorting algorithm from class or Python's built in sorting method.
```
class Student:
    def __init__(self, name=None, avg=None, grade=None):
        self.name = name
        self.avg = avg
        self.grade = grade
```

## Example
```
student1 = Student("Bob", 75, 10)
student2 = Student("Annie", 90, 8)
student3 = Student("Carrie", 82, 8)
student4 = Student("Harry", 75, 10)

slst = [student1, student2, student3, student4]

sort_students(slst) == [student3, student2, student1, student4]
```


## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solution* subdirectory within this directory
