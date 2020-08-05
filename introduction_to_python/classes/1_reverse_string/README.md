# reverse a string word by word
## Motivation
brackets must be close in the correct order,
for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.


# Problem Description
Write a Python class `py_solution` to implement the method `reverse_words`, which takes in a string `str`, which can contain multiple words seperated by spaces, and returns a string where the order of words in `str` is reversed.

 For Example:
 ```
 py_solution.reverse_words("Hello World") => "World Hello"
 ```

## Testing
* To test your solution, type 'pytest' within the solution subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory