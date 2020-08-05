# Validity of string of parentheses
## Motivation
Brackets must be closed in the correct order,
for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.


# Problem Description
Write a Python class `py_solution` to implement the method `is_valid_parenthese`, which takes in a string of parentheses, '(', ')', '{', '}', '[' and ']`str`, and returns `True` if the parentheses in `str` are in a valid order, and `False` otherwise.

For Example:
```
py_solution.is_valid_parenthese("") => True
py_solution.is_valid_parenthese("({})[]") => True
py_solution.is_valid_parenthese("({}]") => False
```

## Testing
* To test your solution, type 'pytest' within the solution subdirectory


## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory