# Divide and Conquer Algorithm - Binary Search

## Motivation
Divide and Conquer Algorithms breaks up a problem into smaller subproblems, solves the subproblems recursively and finally combines the results of the subproblems to find the answer the the main problem.
Often if we can come up with a divide and conquer approach to a problem, this will be much faster than a naive recursive solution.


## Problem Description
In the *solution.py* file, define a function `binary_search` that takes in a sorted list of numbers `lst`, and a target, `x`. Using the divide and conquer Binary Search algorithm, return the index of `x`,  if `x` exists in `lst`, otherwise return `-1`.

## Example
```
lst = [1, 2, 4, 5, 9, 10, 11]
binary_search(lst, 2) == 1
binary_search(lst, 7) == -1
```


## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solution* subdirectory within this directory
