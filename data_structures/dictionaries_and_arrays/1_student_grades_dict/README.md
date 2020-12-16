# Student Grades Dictionary 

# Motivation
Dictionaries are Python’s implementation of a data structure that is more generally known as an associative array. A dictionary consists of a collection of key-value pairs.

You can define a dictionary by enclosing a comma-separated list of key-value pairs in curly braces ({}). A colon (:) separates each key from its associated value:

## Problem Description 
Define a Python function `student_grades`, that consumes two dictionaries, `sgrades`, and `letter_grades`. `sgrades` will have strings representing the names of students as its keys and non-empty lists of integers between `1` and `100` representing the grades for that student in all their classes. `letter_grades` will be a dictionary with the key being a string, `A` to `F` and the value for each key being a tuple representing the range of values corresponding to that letter grade. Output a dictionary where the names of each student are the keys and the values in your new dictionary will be a tuple `(letter_grade, average)` where average is rounded to the nearest integer, for each student.


## Examples
```
sgrades = {"Anton": [62, 55, 82], "Wasif": [100, 72, 94, 50], "Nell": [99, 100]}

letter_grades = {"A": (90, 100), "B": (75, 89), "C": (60, 74), "D": (45, 59), "E": (30, 44), "F": (1, 29)}

student_grades(sgrades, letter_grades) == 
{"Anton": ("C", 66), "Wasif": ("B", 79), "Nell": ("A", 99)}
```

## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory
