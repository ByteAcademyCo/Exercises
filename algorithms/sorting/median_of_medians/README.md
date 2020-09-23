# Pivot Selection - Median of Medians

## Motivation
Sorting is one of the most studied type of algorithms in computer science. There are many different sorting algorithms which may have different benifits and drawbacks given the problem you are trying to solve and your data. You must consider your time contraints and space constraints when choosing the appropriate sorting algorithm for your problem.
Sorting is important because it allows us to optimize data searching to a very high level, when data is stored in a sorted manner. Sorting also allows us to represent data in more readable formats.

## Problem Description
In the *solution.py* file, define a function `median_of_medians` that consumes a lists of integers `lst` and uses the median of medians algorithm to recursively find and return the approximate median value of `lst`. You may assume `lst` is never empty.

## Example
```
lst = [9, 1, 0, 2, 3, 4, 6, 8, 7, 10, 5]
median_of_medians(lst) == 5
```

## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solution* subdirectory within this directory
