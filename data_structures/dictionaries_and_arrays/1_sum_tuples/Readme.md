# Sum Tuple Components

# Motivation
A list is a container which can hold a collection of elements.

Element − Each item stored in an array is called an element.

Index − Each location of an element in an array has a numerical index, which is used to identify the element.

A Tuple is an element of the form (x, y) which can be indexed like a list.

## Problem Description 
Define a Python function `sum_tuples` which consumes a list of tuples `tlst`, where the tuples are of the form `(x, y)` where `x` and `y` integers. The functions should returns a list of integers, where each integer is the sum of the `x` and `y` components in each tuple.

## Examples
```
tlst = [(4, 2), (5, 5), (-1, 2)]
sum_tuples(tlst) == [6, 10, 1]
```

## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory