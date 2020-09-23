# Counting Sort - Frequency Array

## Motivation
Sorting is one of the most studied type of algorithms in computer science. There are many different sorting algorithms which may have different benifits and drawbacks given the problem you are trying to solve and your data. You must consider your time contraints and space constraints when choosing the appropriate sorting algorithm for your problem.
Sorting is important because it allows us to optimize data searching to a very high level, when data is stored in a sorted manner. Sorting also allows us to represent data in more readable formats.

## Problem Description
In the *solution.py* file, define a function `frequency_array` that consumes a lists of non-negative integers `lst` and returns a new list where the length of the new list is one more than the value of the largest element in the original list `lst`, and the values at each index `i` in the new list is the frequency, the number of times `i` apprears in the list `lst`.

## Example
```
lst = [1, 1, 3, 4, 4, 5, 6, 8, 8, 8, 9]
frequency_array(lst) == [0, 2, 0, 1, 2, 1, 1, 0, 3, 1]
```
The largest element in `lst` is `9`, so our returned list has length `10`. In the returned list we can see there are no `0`s in `lst`, two `1`s in `lst`, no `2`s in `lst` and so on.


## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solution* subdirectory within this directory
