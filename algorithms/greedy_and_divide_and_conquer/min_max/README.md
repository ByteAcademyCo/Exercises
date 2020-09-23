# Divide and Conquer Algorithm - Min and Max of a list

## Motivation
Divide and Conquer Algorithms breaks up a problem into smaller subproblems, solves the subproblems recursively and finally combines the results of the subproblems to find the answer the the main problem.
Often if we can come up with a divide and conquer approach to a problem, this will be much faster than a naive recursive solution.

## Problem Description
In the *solution.py* file, define a function `min_max` that takes in a non-empty list of integers `lst`, and using a binary search technique outputs a tuple `(min, max)`, which contains the the minimum and maximum integers in `lst`. Hint: Recursively divide the list in halves at each step and compare the min and max of the smaller sublists.

## Example
```
min_max([8, 2, 1, 3, 1, 5]) == (1, 8)
```

## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solution* subdirectory within this directory
