# Person and Child Class Definitions

## Problem Description
Define a Python class Person. The constructor function should take in the following attributes:
* `name` - a string
* `age` - a non-negative integer
* `spouse` - either `None` or a `Person` object.
* `children` - a list of `Child` objects.
Define a Python class Child which inherits from the `Person` class. The constructor function should take in the following attributes:
* `name` - a string
* `age` - a non-negative integer
* `spouse` - either `None` or a `Person` object.
* `children` - a list of `Child` objects.
* `parents` - a list of `Person` objects.

Define two person objects assigned to variables `jim` and `suzy` respectively, where `jim` has the name `Jim Brown`, an age of `45`, with `suzy` as his spouse and one child `martha`. `suzy` has the name `Suzy Brown`, an age of `42`, with `jim` as her spouse, and one child `martha`.
Define a child object assined to the variable `martha` with the name `Martha Brown`, aged `18`, having no spouse and no children, and having parents `jim` and `suzy`.


## Testing
* To test your solution, type 'pytest' within the solution subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory