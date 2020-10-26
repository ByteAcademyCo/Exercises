# Merge Sort - Merge two Sorted List

## Motivation
Sorting is one of the most studied type of algorithms in computer science. There are many different sorting algorithms which may have different benifits and drawbacks given the problem you are trying to solve and your data. You must consider your time contraints and space constraints when choosing the appropriate sorting algorithm for your problem.
Sorting is important because it allows us to optimize data searching to a very high level, when data is stored in a sorted manner. Sorting also allows us to represent data in more readable formats.

## Problem Description
In the *solution.py* file, define a function `merge_sorted` that consumes two sorted lists of integers in increasing order, `lst1` and `lst2`, and returns a new list containing all the elements from `lst1` and `lst2` in increasing sorted order.

## Example
```
lst1 = [-1, 1, 4, 6]
lst2 = [0, 1, 2, 5, 7]
merge_sorted(lst1, lst2) == [-1, 0, 1, 1, 2, 4, 5, 6, 7]
```


## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solution* subdirectory within this directory
