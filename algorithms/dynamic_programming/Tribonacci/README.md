# Dynamic Programming Recursion - Tribonacci Sequence

## Motivation
We use Dynamic Programming algorithms when we have overlapping subproblems. If we have a naive recursive solution that has repeated calls for same inputs, we can optimize it using Dynamic Programming. We can store the results of the subproblems, so that we do not have to re-compute them when needed later.
Dynamic programing can optimize the time complexity of a problem from exponential `O(2^n)` to polynomial `O(n^c)`, for some constant `c`.

## Problem Description
The Tribonacci sequence is defined as `T(0) = 0`, `T(1) = 0`, `T(2) = 1`, and `T(n) = T(n-1) + T(n-2) + T(n-3)` for `n>=3`. In the *solution.py* file, using dynamic programming, define a recursive function `tribonacci` that consumes a positive integer `n` and returns the `nth` tribonacci number. 

## Example
```
tribonacci(3) == 1
tribonacci(6) == 7
tribonacci(10) == 81
```

## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solution* subdirectory within this directory