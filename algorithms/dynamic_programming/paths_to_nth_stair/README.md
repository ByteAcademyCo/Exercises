# Dynamic Programming Recursion - Paths to nth Stair

## Motivation
We use Dynamic Programming algorithms when we have overlapping subproblems. If we have a naive recursive solution that has repeated calls for same inputs, we can optimize it using Dynamic Programming. We can store the results of the subproblems, so that we do not have to re-compute them when needed later.
Dynamic programing can optimize the time complexity of a problem from exponential `O(2^n)` to polynomial `O(n^c)`, for some constant `c`.

## Problem Description
You are given a flight of stairs where you can either climb up by one or two stairs at each step. In the *solution.py* file, define a recursive function `paths_nth_stair` that consumes a positive integer `n` and returns the total number of ways to get to the `nth` stair. 

## Example
```
paths_nth_stair(3) == 3
```
We can go up the stairs one at a time, or we can take the first two stairs at once and then take the final stair, or we can take the first stair and finish by taking the last two stairs in our final step.

## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solution* subdirectory within this directory
