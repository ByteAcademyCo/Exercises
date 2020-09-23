# Dynamic Programming Recursion - Longest Common Subsequence

## Motivation
We use Dynamic Programming algorithms when we have overlapping subproblems. If we have a naive recursive solution that has repeated calls for same inputs, we can optimize it using Dynamic Programming. We can store the results of the subproblems, so that we do not have to re-compute them when needed later.
Dynamic programing can optimize the time complexity of a problem from exponential `O(2^n)` to polynomial `O(n^c)`, for some constant `c`.

## Problem Description
In the *solution.py* file, using dynamic programming, define a function `longest_common_subseq` that consumes two strings `str1` and `str2` and returns the length of the longest common subsequence between the two strings. Note that the characters do not need to be in contiguous order within the strings to be considered a subsequence.

## Example
```
str1 = "abcdabcf"
str2 = "ecfdacagb"
longest_common_subseq(str1, str2) == 4
```
The longest common subsquence between str1 and str2 is either "cdac" or "cdab" both which have length 4.

## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solution* subdirectory within this directory