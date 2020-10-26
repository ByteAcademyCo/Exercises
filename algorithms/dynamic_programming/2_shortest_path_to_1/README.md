# Dynamic Programming Recursion - Shortest Path to 1

## Motivation
We use Dynamic Programming algorithms when we have overlapping subproblems. If we have a naive recursive solution that has repeated calls for same inputs, we can optimize it using Dynamic Programming. We can store the results of the subproblems, so that we do not have to re-compute them when needed later.
Dynamic programing can optimize the time complexity of a problem from exponential `O(2^n)` to polynomial `O(n^c)`, for some constant `c`.

## Problem Description
You are given three mathematical operations: `-1`, `/2`, and `/3`. In the *solution.py* file, define a function `shortest_path_to_1` that consumes a positive integer `n` and returns the lowest number of operations you can perform to get to 1. You may solve this using breath first search or dynamic programming.

## Example
```
shortest_path_to_1(10) == 3
```
In the example, with `n=10`, we can naivly assume since `10` is divisible by `2`, we could do `10/2 = 5`, `5-1 = 4`, `4/2 = 2`, `2/2 = 1`. But this is not the shortest path we can take. The shortest path of operations we can take is `10-1 = 9`, `9/3 = 3`, `3/3 = 1`.

## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solution* subdirectory within this directory
