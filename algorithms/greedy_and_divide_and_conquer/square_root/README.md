# Divide and Conquer Algorithm - Square Root Using Binary Search

## Motivation
Divide and Conquer Algorithms breaks up a problem into smaller subproblems, solves the subproblems recursively and finally combines the results of the subproblems to find the answer the the main problem.
Often if we can come up with a divide and conquer approach to a problem, this will be much faster than a naive recursive solution.

## Problem Description
In the *solution.py* file, define a function `bin_sqrt` that takes in a positive integer `n`, and using a binary search technique outputs the closest integer which is less than or equal to the square root of `n`. Hint: At each step compare the square of the middle of a given interval with `n`.

## Example
```
bin_sqrt(9) == 3
bin_sqrt(26) == 5
```

## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solution* subdirectory within this directory
