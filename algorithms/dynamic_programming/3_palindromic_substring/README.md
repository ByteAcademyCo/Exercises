# Dynamic Programming Recursion - Longest Palindromic Substring

## Motivation
We use Dynamic Programming algorithms when we have overlapping subproblems. If we have a naive recursive solution that has repeated calls for same inputs, we can optimize it using Dynamic Programming. We can store the results of the subproblems, so that we do not have to re-compute them when needed later.
Dynamic programing can optimize the time complexity of a problem from exponential `O(2^n)` to polynomial `O(n^c)`, for some constant `c`.

## Problem Description
In the *solution.py* file, using dynamic programming, define a function `longest_palindrome_substr` that consumes a string `str` and returns the length of the longest palindromic substring contained in the string.  

## Example
```
longest_palindrome_substr("abaccad") == 4
longest_palindrome_substr("abcadefb") == 1
```

## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solution* subdirectory within this directory